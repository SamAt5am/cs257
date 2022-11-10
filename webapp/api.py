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

@api.route('/clues/') 
def get_clues():
    ''' 
    Returns the list of all clues and their answers
    '''
    query = '''SELECT clues.clue, answers.answer, clues_answers_years.year 
    FROM clues, answers, clues_answers_years
    WHERE clues.id = clues_answers_years.clue_id
    AND answers.id = clues_answers_years.answer_id;
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