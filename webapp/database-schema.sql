CREATE TABLE clues (
    id integer NOT NULL,
    clue text);

CREATE TABLE answers (
    id integer NOT NULL,
    answer text);

CREATE TABLE clues_answers_years (
    clue_id integer,
    answer_id integer,
    year integer,
    times_used_in_year integer);

CREATE TABLE authors (
    author_id integer,
    name text);

CREATE TABLE puzzles (
    puzzle_id integer,
    title text,
    publisher text,
    date text);

CREATE TABLE authors_puzzles (
    author_id integer,
    puzzle_id integer);