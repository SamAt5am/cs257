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

@api.route('/answers/<search_text>') 
def get_answers(search_text):
    ''' 
    Returns the list of clues matching search_text, along with corresponding answers
    '''
    #like_clause = '%' + search_text + '%'
    query = '''SELECT clues_answers_puzzles.clue_id, clues.clue, answers.answer
    FROM clues, answers, clues_answers_puzzles
    WHERE clues.clue LIKE CONCAT('%%', %s, '%%')
    AND clues.id = clues_answers_puzzles.clue_id
    AND answers.id = clues_answers_puzzles.answer_id;
    '''

    answer_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (search_text,))
        print(cursor.query)
        for row in cursor:
            #answer = {
            clue = row[0],
            answer = row[1]
            #}
            answer_list.append(f'{clue} | {answer}')
        print(answer_list)
        cursor.close()
        connection.close()
    except Exception as e:
        print("hi we got a problem.")
        print(e, file=sys.stderr)
    
        
    #eturn json.dumps(clue_list)
    return answer_list


print(get_answers('b'))



