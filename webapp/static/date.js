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
    
    // var searchSelect = document.getElementById('search-select');
    var startElement = document.getElementById('start_date');
    var endElement = document.getElementById('end_date');

    reformatDate(startElement.value);

    // if (searchSelect.value == 'puzzles') {
    onDateSearch(reformatDate(startElement.value), 
    reformatDate(endElement.value));
    // }
    
}

function reformatDate(date) {

    year = date.slice(0, 4);
    month = date.slice(5, 7);
    day = date.slice(8, 11);

    newDate = "'" + year + '-' + month + '-' + day + "'";
    console.log(newDate);

    return newDate;
}


function onDateSearch(startText, endText) {

    var url = getAPIBaseURL() + '/puzzles/dates/' + startText + '/' + endText;

    // Send the request to the Crosswords API /authors/ endpoint
    fetch(url, {method: 'get'})

    // When the results come back, transform them from a JSON string into
    // a Javascript object (in this case, a list of author dictionaries).
    .then((response) => response.json())

    // Once we have our list of puzzle dictionaries, we use it to build
    // an HTML table displaying the puzzle titles.
    .then(function(puzzleList) {

        // Initialize table html string
        var tableBody = '';

        // Initialize search result text
        var searchResult = document.getElementById('search-result');
        
        // No search results found.
        if(puzzleList == 0) {
            searchResult.innerHTML = "No results from: " + startText + " to " + endText + '.';
        }
        else {
            searchResult.innerHTML = "Showing results from: " + startText + " to " + endText + '.';

            for (var k = 0; k < puzzleList.length; k++) {
                tableBody += '<tr><td><a onclick="getPuzzleFromAnswer(' + puzzleList[k]['id'] + ",'"
                    + puzzleList[k]['title'] + "','"
                    + puzzleList[k]['publication_date']
                    + "')\">"
                    + puzzleList[k]['title']
                    + '</a></td></tr>';
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

function getPuzzleFromAnswer(puzzleID, puzzleTitle, puzzleDate) {
    // Very similar pattern to onAuthorsButtonClicked, so I'm not
    // repeating those comments here. Read through this code
    // and see if it makes sense to you.

    var url = getAPIBaseURL() + '/clues_answers/puzzle/' + puzzleID;

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(clueList) {

        var tableBody = '<table>'
        tableBody += '<tr><td>' + '<b><u>' + puzzleTitle + '</b></u></td></tr>';
        tableBody += '<tr><td>' + '<i>' + puzzleDate + '</i></td></tr>';
        
        for (var k = 0; k < clueList.length; k++) {
            tableBody += '<tr><td><b>' + k + '.' + '</b></td></tr>';
            tableBody += '<tr><td>' + 'Clue: ' + clueList[k]['clue'] + ' </td></tr>';
            tableBody += '<tr><td>' + 'Answer: ' + clueList[k]['answer'] + ' </td></tr>';
            
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