CREATE TABLE athletes (
	id SERIAL,
	name text,
	sex text);

CREATE TABLE teams (
	id SERIAL,
	team text);

CREATE TABLE nocs (
	id SERIAL,
	noc text,
	region text);
	
CREATE TABLE games (
	id SERIAL,
	year integer,
	season text,
	city text);

CREATE TABLE events (
	id SERIAL,
	event text);

CREATE TABLE medals (
	id SERIAL,
	rank text);

CREATE TABLE athletes_teams_nocs_games_events_medals (
	athlete_id integer,
	team_id integer,
	noc_id integer,
	game_id integer,
	event_id integer,
	medal_id integer);