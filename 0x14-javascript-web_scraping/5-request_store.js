#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const FileName = process.argv[3];
request(url, (_error, response, body) => {
  if (response && response.statusCode >= 200 && response.statusCode < 300) {
    try {
      fs.writeFile(FileName, body, (err) => {
        if (err) {
          console.error(err);
          process.exit(1);
        }
      });
    } catch (parseError) {
      console.error('Error parsing response body:', parseError);
    }
  }
});
