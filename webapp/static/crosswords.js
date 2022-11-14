/*
 * crosswords.js
 * Sam Hiken and James Brink
 * For assignment due 9 Nov 2022
 */

window.onload = initialize;
console.log("starting..");

function initialize() {
    let element = document.getElementById('clues_button');
    element.onclick = onCluesButtonCicked;
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

function onCluesButtonCicked() {
    
    var url = getAPIBaseURL() + '/clues/';

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
        for (var k = 0; k < clueList.length; k++) {

            tableBody += '<tr>';
            tableBody += '<td>' +  clueList[k]['clue'] + '</td>';
            tableBody += '<td>' +  clueList[k]['answer'] + '</td>';
            tableBody += '</tr>';
        }

        // Put the table body we just built inside the table that's already on the page.
        var resultsTableElement = document.getElementById('clue_table');
        if (resultsTableElement) {
            resultsTableElement.innerHTML = tableBody;
        }
    })

    // Log the error if anything went wrong during the fetch.
    .catch(function(error) {
        console.log(error);
    });

}


/*
function getClue(clueID, clueName) {

    // Very similar pattern to onAuthorsButtonClicked, so I'm not
    // repeating those comments here. Read through this code
    // and see if it makes sense to you.
    var url = getAPIBaseURL() + '/clues/' + authorID;

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(clueList) {
        var tableBody = '<tr><th>' + clueName + '</th></tr>';
        for (var k = 0; k < clueList.length; k++) {
            tableBody += '<tr>';
            tableBody += '<td>' + clueList[k]['clue'] + '</td>';
            tableBody += '</tr>';
        }
        var resultsTableElement = document.getElementById('clue_table');
        if (resultsTableElement) {
            resultsTableElement.innerHTML = tableBody;
        }
    })

    .catch(function(error) {
        console.log(error);
    });
}

*/