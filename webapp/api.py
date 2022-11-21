'''
    api.py
    Sam Hiken and James Brink
    9 November 2022

    An API for our crosswords webapp
'''
import sys
import flask
import json
import config
import psycopg2

api = flask.Blueprint('api', __name__)

def get_connection():
    ''' Returns a connection to the database described in the
        config module. May raise an exception as described in the
        documentation for psycopg2.connect. '''
    return psycopg2.connect(database=config.database,
                            user=config.user,
                            password = config.password)

@api.route('/clues/<search_text>') 
def get_clues(search_text):
    ''' 
    Returns the list of all clues containing search_text, sorted alphabetically by clue, then answer
    '''
    like_clause = '%' + search_text + '%'
    query = '''SELECT clues_answers_puzzles.clue_id, clues.clue, answers.answer
    FROM clues, answers, clues_answers_puzzles
    WHERE clues.clue LIKE CONCAT('%%', %s, '%%')
    AND clues.id = clues_answers_puzzles.clue_id
    AND answers.id = clues_answers_puzzles.answer_id
    ORDER BY clues.clue, answers.answer;
    '''

    clue_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (like_clause,))
        for row in cursor:
            clue = {
            'clue_id':row[0],
            'clue':row[1],
            'answer':row[2]
            }
            clue_list.append(clue)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)
    
    return json.dumps(clue_list)

@api.route('/answers/<search_text>') 
def get_answers(search_text):
    ''' 
    Returns the list of all answers containing search_text, sorted alphabetically by answer, then clue
    '''
    like_clause = '%' + search_text.upper() + '%'
    query = '''SELECT clues_answers_puzzles.answer_id, answers.answer, clues.clue
    FROM clues, answers, clues_answers_puzzles
    WHERE answers.answer LIKE CONCAT('%%', %s, '%%')
    AND clues.id = clues_answers_puzzles.clue_id
    AND answers.id = clues_answers_puzzles.answer_id
    ORDER BY answers.answer, clues.clue;
    '''

    answer_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (like_clause,))
        for row in cursor:
            answer = {
            'answer_id':row[0],
            'answer':row[1],
            'clue':row[2]
            }
            answer_list.append(answer)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)
    
    return json.dumps(answer_list)

@api.route('/puzzles/clue/<clue_id>') 
def get_puzzles_by_clue(clue_id):
    ''' 
    Returns the list of all puzzles containing the clue 
    '''
    query = '''SELECT puzzles.id, puzzles.title, puzzles.source, puzzles.publication_date
    FROM puzzles, clues_answers_puzzles
    WHERE clues_answers_puzzles.clue_id = %s
    AND clues_answers_puzzles.puzzle_id = puzzles.id
    ORDER BY puzzles.title;
    '''

    puzzle_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (int(clue_id),))
        for row in cursor:
            puzzle = {
            'id':row[0],
            'title':row[1],
            'source':row[2],
            'publication_date':str(row[3])
            }
            puzzle_list.append(puzzle)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(puzzle_list)

@api.route('/puzzles/answer/<answer_id>') 
def get_puzzles_by_answer(answer_id):
    ''' 
    Returns the list of all puzzles
    '''
    query = '''SELECT puzzles.id, puzzles.title, puzzles.source, puzzles.publication_date, clues.clue
    FROM puzzles, clues_answers_puzzles, clues
    WHERE clues_answers_puzzles.answer_id = %s
    AND clues_answers_puzzles.puzzle_id = puzzles.id
    AND clues_answers_puzzles.clue_id = clues.id
    ORDER BY puzzles.title;
    '''

    puzzle_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (int(answer_id),))
        for row in cursor:
            puzzle = {
            'id':row[0],
            'title':row[1],
            'source':row[2],
            'publication_date':str(row[3]),
            'clue':row[4]
            }
            puzzle_list.append(puzzle)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(puzzle_list)

@api.route('/puzzles/dates/<start_date>/<end_date>') 
def get_puzzles_by_dates(start_date,end_date):
    ''' 
    Returns the list of all puzzles between start and end dates
    '''
    query = '''SELECT puzzles.id, puzzles.title, puzzles.source, puzzles.publication_date
    FROM puzzles
    WHERE puzzles.publication_date >= CAST(%s AS DATE) 
    AND puzzles.publication_date <= CAST(%s AS DATE)
    ORDER BY puzzles.publication_date;
    '''
    puzzle_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (str(start_date),str(end_date),))
        for row in cursor:
            puzzle = {
            'id':row[0],
            'title':row[1],
            'source':row[2],
            'publication_date':str(row[3])
            }
            puzzle_list.append(puzzle)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(puzzle_list)

@api.route('/clues_answers/puzzle/<puzzle_id>') 
def get_clues_answers_by_puzzle(puzzle_id):
    ''' 
    Returns the list of all entries in a puzzle with puzzle_id
    '''
    query = '''SELECT clues.clue_number, clues.id, clues.clue, answers.id, answers.answer
    FROM clues, answers, clues_answers_puzzles
    WHERE clues_answers_puzzles.puzzle_id = %s
    AND clues_answers_puzzles.clue_id = clues.id
    AND clues_answers_puzzles.answer_id = answers.id
    ORDER BY clues.clue_number;
    '''

    entry_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (int(puzzle_id),))
        for row in cursor:
            entry = {
            'clue_number':row[0],
            'clue_id':row[1],
            'clue':row[2],
            'answer_id':row[3],
            'answer':row[4]
            }
            entry_list.append(entry)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(entry_list)

@api.route('/answers/dates/<start_date>/<end_date>') 
def get_answer_by_date(start_date,end_date):
    ''' 
    Returns the list of all answers between start and end dates
    '''
    query = '''SELECT answers.id, answers.answer, COUNT(answers.id)
            FROM answers, puzzles, clues_answers_puzzles
            WHERE puzzles.publication_date >= CAST(%s AS DATE) 
            AND puzzles.publication_date <= CAST(%s AS DATE) 
            AND answers.id = clues_answers_puzzles.answer_id
            AND puzzles.id = clues_answers_puzzles.puzzle_id
            GROUP BY answers.id, answers.answer
            ORDER BY COUNT(answers.id) DESC;
    '''

    entry_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (str(start_date),str(end_date)))
        for row in cursor:
            entry = {
            'id':row[0],
            'answer':row[1],
            'frequency':row[2]
            }
            entry_list.append(entry)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(entry_list)


@api.route('/help')
def get_help():
    f = open('help.txt')
    lines = f.readlines()
    help_text = ''
    for line in lines:
        help_text += (line + '\\n')
    return help_text