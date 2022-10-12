SELECT noc FROM nocs ORDER BY noc;

SELECT DISTINCT athletes.name 
FROM athletes, nocs, athletes_teams_nocs_games_events_medals
WHERE athletes.id = athletes_teams_nocs_games_events_medals.athlete_id
AND nocs.id = athletes_teams_nocs_games_events_medals.noc_id
AND nocs.region = 'Jamaica';

SELECT games.season, games.year, medals.rank
FROM athletes, games, medals, athletes_teams_nocs_games_events_medals
WHERE athletes.id = athletes_teams_nocs_games_events_medals.athlete_id
AND games.id = athletes_teams_nocs_games_events_medals.game_id
AND medals.id = athletes_teams_nocs_games_events_medals.medal_id
AND athletes.name = 'Gregory Efthimios "Greg" Louganis'
ORDER BY games.year;

SELECT nocs.noc, COUNT(athletes_teams_nocs_games_events_medals.medal_id)
FROM nocs, medals, athletes_teams_nocs_games_events_medals
WHERE nocs.id = athletes_teams_nocs_games_events_medals.noc_id
AND athletes_teams_nocs_games_events_medals.medal_id = 1
GROUP BY nocs.noc;