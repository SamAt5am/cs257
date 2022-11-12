CREATE TABLE clues (
    id integer NOT NULL,
    clue text,
    def text,
    number text);

CREATE TABLE answers (
    id integer NOT NULL,
    answer text);

CREATE TABLE clues_answers_puzzles (
    clue_id integer,
    answer_id integer,
    puzzle_id integer);

CREATE TABLE puzzles (
    puzzle_id integer NOT NULL,
    title text,
    source text,
    date text);