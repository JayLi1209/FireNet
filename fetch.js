const fetch = require('node-fetch');


// POST to http://127.0.0.1:5000/

const postToFlask = async () => {
    const data = { x: [[23, 1, 0, 1, 0.1, 0.0]] }

    const res = await fetch("http://127.0.0.1:5000/", {
        method: "POST",
        body: JSON.stringify(data),
        headers: { 'Content-Type': 'application/json' }

    });

    const json = await res.json();
    console.log(json)
}

// basic GET

/* const main = async () => {
    const res = await fetch("https://pokeapi.co/api/v2/pokemon/ditto", {
        method: "GET"
    });

    const json = await res.json();
// 
    console.log(json.abilities)
} */

postToFlask().catch(err => {
    process.exit(1);
})