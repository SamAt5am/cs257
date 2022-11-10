--
-- PostgreSQL database dump
--

-- Dumped from database version 14.5 (Homebrew)
-- Dumped by pg_dump version 14.5 (Homebrew)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: answers; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.answers (
    id integer NOT NULL,
    answer text
);


--
-- Name: authors; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.authors (
    author_id integer,
    name text
);


--
-- Name: authors_puzzles; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.authors_puzzles (
    author_id integer,
    puzzle_id integer
);


--
-- Name: clues; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.clues (
    id integer NOT NULL,
    clue text
);


--
-- Name: clues_answers_years; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.clues_answers_years (
    clue_id integer,
    answer_id integer,
    year integer,
    times_used_in_year integer
);


--
-- Name: puzzles; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.puzzles (
    puzzle_id integer,
    title text,
    publisher text,
    date text
);


--
-- Data for Name: answers; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.answers (id, answer) FROM stdin;
0	ABA
1	ACTOR
2	ADES
3	ADS
4	AFRO
5	AGATE
6	AMEN
7	AMIR
8	ANISE
9	ANS
10	ARES
11	ARIEL
12	ARTURS
13	BASILICA
14	BASIN
15	BOCA
16	CARDINALOCONNOR
17	CINQUE
18	COCOA
19	CRU
20	DEC
21	DRAPE
22	EELS
23	EENS
24	ELI
25	ESE
26	ESTE
27	ETTU
28	EVADE
29	GOOSEGOSSAGE
30	ICE
31	ILIVE
32	INTRO
33	IPO
34	LAMER
35	LAVE
36	MOLAR
37	MUTUAL
38	NOFEE
39	OCT
40	OMEN
41	OPART
42	OPOSSUMS
43	OVERT
44	PLEA
45	PSI
46	REATA
47	RECOUP
\.


--
-- Data for Name: authors; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.authors (author_id, name) FROM stdin;
\.


--
-- Data for Name: authors_puzzles; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.authors_puzzles (author_id, puzzle_id) FROM stdin;
\.


--
-- Data for Name: clues; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.clues (id, clue) FROM stdin;
0	Litigator's group
1	Thespian
2	Summer coolers
3	Newspaper revenue
4	Head of hair
5	Quartz
6	Famous last word
7	Top Turk
8	Cordial flavoring
9	Part of Q&A
10	He means war
11	Mr. Sharon
12	Rubenstein and Schnabel
13	It has an apse
14	Concavity
15	___ Raton
16	New York prelate
17	One point
18	Designated driver's beverage
19	Grande ___ (wine)
20	Knitting direction
21	Window treatment
22	Shockers
23	Poetic nights
24	Mr. Wallach
25	Vane dir.
26	This
27	You too?
28	Sidestep
29	Yankee pitcher
30	Chill
31	As ___ and breathe
32	Opening remarks
33	Wall St. deal
34	Less convincing
35	Wash
36	Filling station
37	Our ___ Friend
38	Preferred checking account
39	Columbus Day mo.
40	Warning
41	Gallery offering
42	Nocturnal marsupials
43	Above-board
44	Adjuration
45	Greek character
46	Rope
47	Win back
\.


--
-- Data for Name: clues_answers_years; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.clues_answers_years (clue_id, answer_id, year, times_used_in_year) FROM stdin;
0	0	1997	1
1	1	1997	1
2	2	1997	1
3	3	1997	1
4	4	1997	1
5	5	1997	1
6	6	1997	1
7	7	1997	1
8	8	1997	1
9	9	1997	1
10	10	1997	1
11	11	1997	1
12	12	1997	1
13	13	1997	1
14	14	1997	1
15	15	1997	1
16	16	1997	1
17	17	1997	1
18	18	1997	1
19	19	1997	1
20	20	1997	1
21	21	1997	1
22	22	1997	1
23	23	1997	1
24	24	1997	1
25	25	1997	1
26	26	1997	1
27	27	1997	1
28	28	1997	1
29	29	1997	1
30	30	1997	1
31	31	1997	1
32	32	1997	1
33	33	1997	1
34	34	1997	1
35	35	1997	1
36	36	1997	1
37	37	1997	1
38	38	1997	1
39	39	1997	1
40	40	1997	1
41	41	1997	1
42	42	1997	1
43	43	1997	1
44	44	1997	1
45	45	1997	1
46	46	1997	1
47	47	1997	1
\.


--
-- Data for Name: puzzles; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.puzzles (puzzle_id, title, publisher, date) FROM stdin;
\.


--
-- PostgreSQL database dump complete
--

