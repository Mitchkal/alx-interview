#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

if (!movieId) {
  console.error('Provide Movie Id as argument');
  process.exit(1);
}
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Failed to fetch data:', error);
    return;
  }
  if (response.statusCode === 200) {
    const movieData = JSON.parse(body);
    const characterUrls = movieData.characters;

    const fetchCharacterDetails = (index) => {
      if (index < characterUrls.length) {
        request(characterUrls[index], (error, response, body) => {
          if (error) {
            console.error('Failed to fetch data:', error);
            return;
          }
          if (response.statusCode === 200) {
            const characterData = JSON.parse(body);
            console.log(characterData.name);

            fetchCharacterDetails(index + 1);
          }
        });
      }
    };
    fetchCharacterDetails(0);
  } else {
    console.error(
      'Failed to fetch movie data. HTTP Status Code:',
      response.statusCode
    );
  }
});
