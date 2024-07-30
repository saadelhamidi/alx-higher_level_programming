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
        const promises = [];

        for (let i = 0; i < FilmCharacters.length; i++) {
          const urlpeople = FilmCharacters[i];
          const characterPromise = new Promise((resolve, reject) => {
            request(urlpeople, (_error, _response, bodyPeople) => {
              if (_error) {
                reject(_error);
              } else {
                const peopleData = JSON.parse(bodyPeople);
                const characterName = peopleData.name;
                // console.log(characterName);
                resolve(characterName);
              }
            });
          });

          promises.push(characterPromise);
        }

        Promise.all(promises)
          .then((myList) => {
            for (const i in myList) {
              console.log(myList[i]);
            }
          })
          .catch((error) => {
            console.error('Error fetching character data:', error);
          });
      } catch (parseError) {
        console.error('Error parsing response body:', parseError);
      }
    }
  });
}
