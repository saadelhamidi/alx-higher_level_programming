#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;
request(url, (_error, response, body) => {
  if (response && response.statusCode >= 200 && response.statusCode < 300) {
    try {
      const filmData = JSON.parse(body);
      console.log(filmData.title);
    } catch (parseError) {
      console.error('Error parsing response body:', parseError);
    }
  } else {
    console.error('Film Not Found!');
  }
});
