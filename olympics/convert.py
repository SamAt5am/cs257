''' File for converting data from athlete_events.csv file to a database consisting of seven tables:
        athletes
        teams
        nocs
        games
        events
        medals
        athletes_teams_nocs_games_events_medals (linking table)
    For access to original dataset, go here: https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results
    
    Created by: Sam Hiken, 10/11
'''

import csv

# key will be tuple representing data stored in input csv; value will be id
athletes_dict = dict()
teams_dict = dict()
nocs_dict = dict()
games_dict = dict()
events_dict = dict()
medals_dict = dict()

linking_list = list()

# create dictionaries connecting tuples to ids, create linking list
with open('athlete_events.csv', newline = '') as csv_input:
    reader = csv.reader(csv_input, delimiter=',')
    next(reader)
    for row in reader:
        athlete = (row[1],row[2])
        team = (row[6])
        noc = (row[7])
        game = (row[9],row[10],row[11])
        event = row[13]
        medal = (row[14])

        if athlete not in athletes_dict:
            athletes_dict[athlete] = len(athletes_dict)
        if team not in teams_dict:
            teams_dict[team] = len(teams_dict)
        if noc not in nocs_dict:
            nocs_dict[noc] = len(nocs_dict)
        if game not in games_dict:
            games_dict[game] = len(games_dict)
        if event not in events_dict:
            events_dict[event] = len(events_dict)
        if medal not in medals_dict:
            medals_dict[medal] = len(medals_dict)

        linking_list.append([athletes_dict[athlete],
                            teams_dict[team],
                            nocs_dict[noc],
                            games_dict[game],
                            events_dict[event],
                            medals_dict[medal]])

noc_regions_dict = dict()

# create dictionary for noc regions
with open('noc_regions.csv', newline = '') as csv_input:
    reader = csv.reader(csv_input, delimiter=',')
    next(reader)
    for row in reader:
        noc_regions_dict[row[0]] = row[1]

athletes_list = []
teams_list = []
nocs_list = []
games_list = []
events_list = []
medals_list = []

# convert dictionaries to lists with ids
for athlete in athletes_dict:
    athletes_list.append([athletes_dict[athlete],athlete[0],athlete[1]])
for team in teams_dict:
    teams_list.append([teams_dict[team],team])
for noc in nocs_dict:
    if noc in noc_regions_dict:
        nocs_list.append([nocs_dict[noc],noc,noc_regions_dict[noc]])
    else:
        nocs_list.append([nocs_dict[noc],noc,'NA'])
for game in games_dict:
    games_list.append([games_dict[game],game[0],game[1],game[2]])
for event in events_dict:
    events_list.append([events_dict[event],event])
for medal in medals_dict:
    medals_list.append([medals_dict[medal],medal])

# helper method for writing list to rows of csv
def write_to_csv(file_name, data_list):
    with open(file_name, 'w') as csv_output:
        writer = csv.writer(csv_output)
        for element in data_list:
            writer.writerow(element)

write_to_csv('athletes.csv', athletes_list)
write_to_csv('teams.csv', teams_list)
write_to_csv('nocs.csv', nocs_list)
write_to_csv('games.csv', games_list)
write_to_csv('events.csv', events_list)
write_to_csv('medals.csv', medals_list)
write_to_csv('athletes_teams_nocs_games_events_medals.csv', linking_list)