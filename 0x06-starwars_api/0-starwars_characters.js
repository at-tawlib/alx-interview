#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = "https://swapi-api.alx-tools.com/api/films/" + movieId;

request(url, (error, response, body) => {
    if (error) {
        console.log(error);
    } else {

        const charactersUrls = JSON.parse(body).characters;

        if (charactersUrls.length === 0) {
            return;
        }

        // send another request to get actors names
        for (i = 0; i < charactersUrls.length; i++)
        {
            const actorUrl = charactersUrls[i];
            request(actorUrl, (error, res,  body1) => {
                if (error) {
                    console.log(error);
                } else {
                    const name = JSON.parse(body1).name;
                    console.log(name);
                }
            });
        }
    }
});