AUTHORS: James Brink and Sam Hiken

DATA: The database includes clues, answers, and puzzle-specific information (publications, dates) of British-style 'cryptic crossword' puzzles.

CS257 Software Design
Fall 2022
To access the data, go to https://cryptics.georgeho.org/data/clues, click on (advanced), check download file and stream all rows, then click 'Export CSV.'

FEATURES CURRENTLY WORKING:
- search by text for clues
- search by text for answers
- click on clue to get corresponding answer, along with info on puzzle it appeared in
- click on answer to get corresponding clue(s), along with info on puzzle(s) it has appeared in
- search by date for puzzles

FEATURE NOT WORKING:
- We previously indicated we would implement a search feature that would allow a user to get information on the puzzles written by individual crossword authors. We switched datasets midway through the project, so we no longer have access to data on that front.
- We previously considered adding a feature that would allow a user to access all answers that appeared between two dates. In the interest of time, we decided not to implement this feature, although there is still an api endpoint that allows users to access this data.

NOTE:
- We work only with clues that have a date listed in the dataset available online, leaving out those that do not have a date listed. Only a small percentage of the puzzles were missing a date, so the remaining database is still quite large.
- We assume that clues are not repeated in the dataset. In a previous version of this project, we were working with standard American-style crossword puzzles. Currently, we are working with British-style 'cryptic crosswords,' which have far more distinctive clues. Nevertheless, there may be a very small handful of clue instances which are not accounted for in the database. We believe that this set of clue instances is small enough not to substantially impact the user's experience with the web app.