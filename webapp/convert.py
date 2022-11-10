''' File for converting data from crossword_data_mini.csv file to a database consisting of seven tables:
        clues
        answers
        clues_answers_years
        authors
        puzzles
        authors_puzzles

    Created by: Sam Hiken and James Brink, 11/9
'''

import csv

# key will be tuple representing data stored in input csv; value will be id
clues_dict = dict()
answers_dict = dict()
authors_dict = dict()
puzzles_dict = dict()

clues_answers_years_list = list()

# create dictionaries connecting tuples to ids, create linking list
with open('crossword_data_mini.csv', newline = '') as csv_input:
    reader = csv.reader(csv_input, delimiter=',')
    next(reader)
    for row in reader:
        clue = row[3]
        answer = row[2]
        year = row[1]

        if clue not in clues_dict:
            clues_dict[clue] = len(clues_dict)
        if answer not in answers_dict:
            answers_dict[answer] = len(answers_dict)

        clues_answers_years_list.append([clues_dict[clue],
                            answers_dict[answer],
                            # here, we're assuming that each clue-answer pair appears no more than 
                            # once per year; this is true for our small dataset, but we will fix it in a 
                            # future draft
                            int(year),1])

clues_list = []
answers_list = []

# convert dictionaries to lists with ids
for clue in clues_dict:
    clues_list.append([clues_dict[clue],clue])
for answer in answers_dict:
    answers_list.append([answers_dict[answer],answer])

# helper method for writing list to rows of csv
def write_to_csv(file_name, data_list):
    with open(file_name, 'w') as csv_output:
        writer = csv.writer(csv_output)
        for element in data_list:
            writer.writerow(element)

write_to_csv('clues.csv', clues_list)
write_to_csv('answers.csv', answers_list)
write_to_csv('clues_answers_years.csv', clues_answers_years_list)