'''
Created by: Sam Hiken, 10/19
The get_connection() method, in addition to portions of the get_athletes,
get_nocs_by_golds, and get_athletes_by_medals methods were written by Jeff Ondich
Last edited by: Sam Hiken, 10/20
'''

import sys
import psycopg2
import config

def get_connection():
    try:
        return psycopg2.connect(database=config.database,
                                user=config.user)
    except Exception as e:
        print(e, file=sys.stderr)
        exit()

def main():
    if len(sys.argv)<2:
        print('Incorrect command line input. Enter python3 olympics.py --help for usage text.')
    elif sys.argv[1] == '-h' or sys.argv[1] == '--help':
        file = open('usage.txt')
        print(file.read())
        file.close()
    elif sys.argv[1] == 'names':
        if len(sys.argv)>=3:
            print_athlete_names(sys.argv[2])
        else:
            print('Incorrect command line input. Enter python3 olympics.py --help for usage text.')
    elif sys.argv[1] == 'nocs_golds':
        print_nocs_by_golds()
    elif sys.argv[1] == 'athletes_medals':
        print_athletes_by_medals()
    else:
        print('Incorrect command line input. Enter python3 olympics.py --help for usage text.')

def get_athletes(noc):
    ''' Returns a list of the full names of all the athletes
        that have competed for noc'''
    athletes = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        # Execute a query to retrieve athlete names
        query = '''SELECT DISTINCT athletes.name 
                   FROM athletes, nocs, athletes_teams_nocs_games_events_medals 
                   WHERE athletes.id = athletes_teams_nocs_games_events_medals.athlete_id 
                   AND nocs.id = athletes_teams_nocs_games_events_medals.noc_id 
                   AND nocs.region = ''' + "'" + noc + "';"
        cursor.execute(query)

        # Iterate over the query results to produce the list of athlete names.
        for row in cursor:
            name = row[0]
            athletes.append(f'{name}')
    except Exception as e:
        print(e, file=sys.stderr)

    connection.close()
    return athletes

def get_nocs_by_golds():
    ''' Returns a dictionary in which each key is a country that
        has won at least one gold medal and each value is the
        number of medals it has won'''
    nocs = {}
    try:
        connection = get_connection()
        cursor = connection.cursor()
        # Execute a query to retrieve a list of all times countries
        # have won gold medals
        query = '''SELECT nocs.noc 
                   FROM nocs, medals, athletes_teams_nocs_games_events_medals 
                   WHERE nocs.id = athletes_teams_nocs_games_events_medals.noc_id 
                   AND medals.id = athletes_teams_nocs_games_events_medals.medal_id 
                   AND medals.rank = 'Gold';'''
        cursor.execute(query)
        
        # Iterate over the query results to produce the dictionary of nocs.
        for row in cursor:
            noc = row[0]
            if noc in nocs:
                nocs[noc]+=1
            else:
                nocs[noc] = 1
    except Exception as e:
        print(e, file=sys.stderr)

    connection.close()
    return nocs

def get_athletes_by_medals():
    ''' Returns a dictionary in which each key is a athlete that
        has won at least one medal and each value is the
        number of medals they have won'''
    athletes = {}
    try:
        connection = get_connection()
        cursor = connection.cursor()
        # Execute a query to retrieve a list of all instance of athletes
        # winning medals
        query = '''SELECT athletes.name 
                   FROM athletes, medals, athletes_teams_nocs_games_events_medals 
                   WHERE athletes.id = athletes_teams_nocs_games_events_medals.athlete_id 
                   AND medals.id = athletes_teams_nocs_games_events_medals.medal_id 
                   AND medals.rank != 'NA';'''
        cursor.execute(query)
        
        # Iterate over the query results to produce the dictionary of athletes.
        for row in cursor:
            athlete = row[0]
            if athlete in athletes:
                athletes[athlete]+=1
            else:
                athletes[athlete] = 1
    except Exception as e:
        print(e, file=sys.stderr)

    connection.close()
    return athletes

def print_athlete_names(noc):
    for athlete in get_athletes(noc):
        print(athlete)

def print_nocs_by_golds():
    noc_list = []
    noc_dict = get_nocs_by_golds()
    # Turns the dict returned by get_nocs_by_gold()
    # into a list, then sorts and prints it
    for noc in noc_dict:
        noc_and_medal = noc, noc_dict[noc]
        noc_list.append(noc_and_medal)
    noc_list.sort(key = lambda x: x[1], reverse = True)
    for noc in noc_list:
        print(noc[0] + ": " + str(noc[1]) + " golds")

def print_athletes_by_medals():
    athlete_list = []
    athlete_dict = get_athletes_by_medals()
    # Turns the dict returned by get_athletes_by_medal()
    # into a list, then sorts and prints it
    for athlete in athlete_dict:
        athlete_and_medal = athlete, athlete_dict[athlete]
        athlete_list.append(athlete_and_medal)
    athlete_list.sort(key = lambda x: x[1], reverse = True)
    for athlete in athlete_list:
        print(athlete[0] + ": " + str(athlete[1]) + " medal(s)")
    
if __name__ == '__main__':
    main()