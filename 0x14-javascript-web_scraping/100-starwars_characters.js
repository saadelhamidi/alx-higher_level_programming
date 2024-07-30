#!/usr/bin/node
const request = require('request');
if (process.argv.length === 3) {
  const id = process.argv[2];
  const url = 'https://swapi-api.alx-tools.com/api/films/' + id;
  request(url, (_error, _response, body) => {
    if (body) {
      try {
        const filmData = JSON.parse(body);
        const FilmCharacters = filmData.characters;
        // console.log(FilmCharacters)
        for (let i = 0; i < FilmCharacters.length; i++) {
          const urlpeople = FilmCharacters[i];
          // console.log(urlpeople)
          request(urlpeople, (_error, _response, bodyPeople) => {
          // console.log(body_people)
            const peopleData = JSON.parse(bodyPeople);
            console.log(peopleData.name);
            // console.log(peopleData.name)
          });
        }
      } catch (parseError) {
        console.error('Error parsing response body:', parseError);
      }
    }
  });
}
