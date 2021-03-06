#!/usr/bin/env node
// Load the fs (filesystem) module
var fs = require('fs');

//https://nodejs.org/api/fs.html#fs_fs_readfile_filename_options_callback
// Read the contents of the file into memory.
fs.readFile('example_log.log', function (err, logData) {
    // If an error occurred, throwing it will
    // display the exception and end our app.
    if (err) throw err;

    // logData is a Buffer, convert to string.
    var text = logData.toString();
    console.log(text)

    var results = {};

    // Break up the file into lines.
    var lines = text.split('\n');

    lines.forEach(function(line) {
        var parts = line.split(' ');
        var letter = parts[1];
        var count = parseInt(parts[2]);

        if(!results[letter]) {
            results[letter] = 0;
            }

        results[letter] += parseInt(count);
    });
    console.log(results);
});