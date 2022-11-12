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

clues_answers_puzzles_list = list()

# create dictionaries connecting tuples to ids, create linking list
with open('data.csv', newline = '') as csv_input:
    reader = csv.reader(csv_input, delimiter=',')
    next(reader)
    for row in reader:
        clue_text = row[1]
        answer_text = row[2]
        definition = row[3]
        clue_number = row[4]
        date = row[5]
        title = row[6]
        source = row[8]

        clue_id = len(clues_dict)

        clue_info = [clue_id,clue_text,definition,clue_number]
        
        clues_dict[clue_text] = clue_info
        if answer_text not in answers_dict:
            answers_dict[answer_text] = len(answers_dict)
        if title not in puzzles_dict:
            puzzles_dict[title] = [len(puzzles_dict),title,source,date]

        clues_answers_puzzles_list.append([clue_id,
                            answers_dict[answer_text],
                            puzzles_dict[title][0]])

clues_list = []
answers_list = []
puzzles_list = []

# convert dictionaries to lists with ids
for clue in clues_dict:
    clues_list.append(clues_dict[clue])
for answer in answers_dict:
    answers_list.append([answers_dict[answer],answer])
for title in puzzles_dict:
    puzzles_list.append(puzzles_dict[title])

# helper method for writing list to rows of csv
def write_to_csv(file_name, data_list):
    with open(file_name, 'w') as csv_output:
        writer = csv.writer(csv_output)
        for element in data_list:
            writer.writerow(element)

write_to_csv('clues.csv', clues_list)
write_to_csv('answers.csv', answers_list)
write_to_csv('puzzles.csv', puzzles_list)
write_to_csv('clues_answers_puzzles.csv', clues_answers_puzzles_list)