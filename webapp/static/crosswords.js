/*
 * crosswords.js
 * Sam Hiken and James Brink
 * For assignment due 9 Nov 2022
 */

window.onload = initialize;

function initialize() {
    var button = document.getElementById('search-button');
    button.onclick = onSearchButtonClick;
}

// Returns the base URL of the API, onto which endpoint
// components can be appended.
function getAPIBaseURL() {
    let baseURL = window.location.protocol
                    + '//' + window.location.hostname
                    + ':' + window.location.port
                    + '/api';
    return baseURL;
}

function onSearchButtonClick() {
    console.log('Search Button clicked!')
    var searchElement = document.getElementById('search-box');
    var searchSelect = document.getElementById('search-select');
    console.log(searchElement.value)
    console.log(searchSelect.value)

    if (searchSelect.value == "answer") {
        onAnswersSearch(searchElement.value)
    }
    else if (searchSelect.value == "clue") {
        onCluesSearch(searchElement.value)
    }
    
}
function onAnswersSearch(searchText) {

    var url = getAPIBaseURL() + '/answers/' + searchText;

    // Send the request to the Crosswords API /authors/ endpoint
    fetch(url, {method: 'get'})

    // When the results come back, transform them from a JSON string into
    // a Javascript object (in this case, a list of author dictionaries).
    .then((response) => response.json())

    // Once you have your list of author dictionaries, use it to build
    // an HTML table displaying the author names and lifespan.
    .then(function(answerList) {

        // Initialize table html string
        var tableBody = '';

        // Initialize search result text
        var searchResult = document.getElementById('search-result');
        
        // No search results found.
        if(answerList == 0) {
            searchResult.innerHTML = "No results found for:" + '"' + searchText + '"' + ' Try a different search!';
        }
        else {
            searchResult.innerHTML = "Showing results for: " + '"' + searchText + '"';

            const answersCheck = [];
            for (var k = 0; k < answerList.length; k++) {
                
                // Checking to see if answer is already in table
                if(answersCheck.includes(answerList[k]['answer']) == false) {
                    tableBody += '<tr>'
                    tableBody += '<td><a onclick="getPuzzleFromAnswer(' + answerList[k]['answer_id']+ ",'"
                    + answerList[k]['answer']
                    + "')\">"
                    + answerList[k]['answer']
                    + '</a></td></tr>';    
                    answersCheck.push(answerList[k]['answer'])
                }
            }
        }

        // Put the table body into the html
        var resultsTableElement = document.getElementById('results_table');
        if (resultsTableElement) {
            resultsTableElement.innerHTML = tableBody;
        }
    })

    // Log the error if anything went wrong during the fetch.
    .catch(function(error) {
        console.log(error);
    });

}

function onCluesSearch(searchText) {

    var url = getAPIBaseURL() + '/clues/' + searchText;

    // Send the request to the Crosswords API /authors/ endpoint
    fetch(url, {method: 'get'})

    // When the results come back, transform them from a JSON string into
    // a Javascript object (in this case, a list of author dictionaries).
    .then((response) => response.json())

    // Once you have your list of author dictionaries, use it to build
    // an HTML table displaying the author names and lifespan.
    .then(function(clueList) {
        // Build the table body.
        var tableBody = '';

        var searchResult = document.getElementById('search-result');
        if(clueList == 0) {
            searchResult.innerHTML = "No results found for:" + '"' + searchText + '"' + ' Try a different search!';
        }
        else {
            searchResult.innerHTML = "Showing results for: " + '"' + searchText + '"';

            for (var k = 0; k < clueList.length; k++) {
                tableBody += '<tr><td><a onclick="getPuzzleFromClue(' + clueList[k]['clue_id']+ ",'"
                    + clueList[k]['clue']  + "','"
                    + clueList[k]['answer'] 
                    + "')\">"
                    + clueList[k]['clue']
                    + '</a></td></tr>';

            }
        }
        // Put the table body we just built inside the table that's already on the page.
        var resultsTableElement = document.getElementById('results_table');
        if (resultsTableElement) {
            resultsTableElement.innerHTML = tableBody;
        }
        console.log(tableBody);
    })

    // Log the error if anything went wrong during the fetch.
    .catch(function(error) {
        console.log(error);
    });

}

function getPuzzleFromClue(clueID, clueName, answer) {
    // Very similar pattern to onAuthorsButtonClicked, so I'm not
    // repeating those comments here. Read through this code
    // and see if it makes sense to you.

    console.log("getPuzzleFromClue invoked!");
    var url = getAPIBaseURL() + '/puzzles/clue/' + clueID;


    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(puzzleList) {
        var tableBody = '<table>'
        tableBody = '<tr><td>' + '<b>' + clueName + '</b></td></tr>'

        for (var k = 0; k < puzzleList.length; k++) {
            tableBody += '<tr><td>' + 'Answer: ' + answer + ' </td></tr>';
            tableBody += '<tr><td>' + 'Title: <i> ' + puzzleList[k]['title'] + '</i>' + '</td></tr>';
            tableBody += '<tr><td>' + puzzleList[k]['publication_date'] + '</i>' + '</td></tr>';
            tableBody += '<tr><td>' + 'Source/Creator:' + puzzleList[k]['source'] + '</td></tr>';
            
            tableBody += '</table>';
            console.log(puzzleList[k]['publication_date'])
        }
    
        var resultsTableElement = document.getElementById('results_table');
        if (resultsTableElement) {
            resultsTableElement.innerHTML = tableBody;
        }
    })

    .catch(function(error) {
        console.log(error);
    });
}

function getPuzzleFromAnswer(answerID, answerName) {
    // Very similar pattern to onAuthorsButtonClicked, so I'm not
    // repeating those comments here. Read through this code
    // and see if it makes sense to you.

    console.log("getPuzzleFromClue invoked!");
    var url = getAPIBaseURL() + '/puzzles/answer/' + answerID;

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(puzzleList) {

        var tableBody = '<table>'
        tableBody = '<tr><td>' + '<b><u>' + answerName + '</b></u></td></tr>'

        for (var k = 0; k < puzzleList.length; k++) {
            tableBody += '<tr><td><b>' + k + '.' + '</b></td></tr>';
            tableBody += '<tr><td>' + 'Clue: ' + puzzleList[k]['clue'] + ' </td></tr>';
            tableBody += '<tr><td>' + 'Title: <i> ' + puzzleList[k]['title'] + '</i>' + '</td></tr>';
            tableBody += '<tr><td>' + puzzleList[k]['publication_date'] + '</i>' + '</td></tr>';
            tableBody += '<tr><td>' + 'Source/Creator:' + puzzleList[k]['source'] + '</td></tr>';
            tableBody += '</table>';
        }
        var resultsTableElement = document.getElementById('results_table');
        if (resultsTableElement) {
            resultsTableElement.innerHTML = tableBody;
        }
    })

    .catch(function(error) {
        console.log(error);
    });
}

function getPuzzlesFromDate(startDate, endDate) {
    // Very similar pattern to onAuthorsButtonClicked, so I'm not
    // repeating those comments here. Read through this code
    // and see if it makes sense to you.

    console.log("getPuzzlesFromDate invoked!");
    var url = getAPIBaseURL() + '/puzzles/dates/' + startDate + '/' + endDate;

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(puzzleList) {

        var tableBody = '<table>'
        tableBody = '<tr><td>' + '<b><u>' + answerName + '</b></u></td></tr>'

        for (var k = 0; k < puzzleList.length; k++) {
            tableBody += '<tr><td><b>' + k + '.' + '</b></td></tr>';
            tableBody += '<tr><td>' + 'Title: <i> ' + puzzleList[k]['title'] + '</i>' + '</td></tr>';
        }
        var resultsTableElement = document.getElementById('results_table');
        if (resultsTableElement) {
            resultsTableElement.innerHTML = tableBody;
        }
    })

    .catch(function(error) {
        console.log(error);
    });
}