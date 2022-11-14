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
    Returns the list of all answers
    '''
    like_clause = '%' + search_text + '%'
    query = '''SELECT clues_answers_puzzles.clue_id, clues.clue, answers.answer
    FROM clues, answers, clues_answers_puzzles
    WHERE clues.clue LIKE CONCAT('%%', %s, '%%')
    AND clues.id = clues_answers_puzzles.clue_id
    AND answers.id = clues_answers_puzzles.answer_id;
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
    Returns the list of all answers
    '''
    like_clause = '%' + search_text.upper() + '%'
    query = '''SELECT clues_answers_puzzles.answer_id, answers.answer, clues.clue
    FROM clues, answers, clues_answers_puzzles
    WHERE answers.answer LIKE CONCAT('%%', %s, '%%')
    AND clues.id = clues_answers_puzzles.clue_id
    AND answers.id = clues_answers_puzzles.answer_id;
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
def get_puzzles(start_date,end_date):
    ''' 
    Returns the list of all puzzles
    '''
    query = '''SELECT puzzles.puzzle_id, puzzles.title, puzzles.source, puzzles.date
    FROM answers;
    '''

    clue_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, tuple())
        for row in cursor:
            clue = {
            'clue':row[0],
            'answer':row[1],
            'clues_answers_year':row[2]
            }
            clue_list.append(clue)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)
        
    return json.dumps(clue_list)
