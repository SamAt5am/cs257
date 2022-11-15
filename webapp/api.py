'''
    api.py
    Sam Hiken and James Brink
    9 November 2022

    An in-progress API for our webapp
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
    Returns the list of all clues matching search texrt
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
    Returns the list of all answers matching search text
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
    
    #answer_list.append('hello')
    return json.dumps(answer_list)

@api.route('/puzzles/clue/<clue_id>') 
def get_puzzles_by_clue(clue_id):
    ''' 
    Returns the list of all puzzles
    '''
    query = '''SELECT puzzles.puzzle_id, puzzles.title, puzzles.source, puzzles.date
    FROM puzzles, clues_answers_puzzles
    WHERE clues_answers_puzzles.clue_id = %s
    AND clues_answers_puzzles.puzzle_id = puzzles.puzzle_id
    ORDER BY puzzles.title;
    '''

    puzzle_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (int(clue_id),))
        for row in cursor:
            puzzle = {
            'puzzle_id':row[0],
            'title':row[1],
            'source':row[2],
            'date':row[3]
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
    query = '''SELECT puzzles.puzzle_id, puzzles.title, puzzles.source, puzzles.date
    FROM puzzles, clues_answers_puzzles
    WHERE clues_answers_puzzles.answer_id = %s
    AND clues_answers_puzzles.puzzle_id = puzzles.puzzle_id
    ORDER BY puzzles.title;
    '''

    puzzle_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (int(answer_id),))
        for row in cursor:
            puzzle = {
            'puzzle_id':row[0],
            'title':row[1],
            'source':row[2],
            'date':row[3]
            }
            puzzle_list.append(puzzle)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(puzzle_list)


@api.route('/help')
def get_help():
    f = open('help.txt')
    lines = f.readlines()
    help_text = ''
    for line in lines:
        help_text += (line + '\\n')
    return help_text