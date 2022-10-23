const fetch = require("node-fetch");
const express = require("express");
const app = express();
const port = 8383;

const bodyParser = require("body-parser");

app.use(express.static("public"));
app.set("views", __dirname + "/public");
app.set("view engine", "ejs");

/* app.get('/', (req, res) => {
    res.status(200).send('<h1>hi</h1>')
}) */

// parse application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({ extended: false }));

// parse application/json
app.use(bodyParser.json());

app.get("/", function (req, res, next) {
  res.render("index", {
    title: "Cool, huh!",
    condition: true,
    anyArray: [1, 2, 3],
  });
});

app.get("/test/:id", function (req, res, next) {
  res.render("test.ejs", { output: req.params.id });
});

var id;

let arr;

app.post("/test/submit", async function (req, res, next) {
  id = req.body.county;
  // console.log(typeof(id));
  console.log(id);

  const fs = require("fs");
  const XLSX = require("xlsx");
  const jsontoxml = require("jsontoxml");

  const workbook = XLSX.readFile("CountiesUS.csv");

  let worksheets = {};
  for (const sheetName of workbook.SheetNames) {
    worksheets[sheetName] = XLSX.utils.sheet_to_json(
      workbook.Sheets[sheetName]
    );
  }

  // searchName(worksheets);

  arr = searchName(worksheets);

  //successfully printed out arr.
  //below are fetching for weather data.

  const url =
    "https://api.openweathermap.org/data/2.5/weather?lat=" +
    arr[0] +
    "&lon=" +
    arr[1] +
    "&appid=532e78e0ddfe62456dbf382511c56ece";

  const data = await fetch(url);
  const json = await data.json();
//   console.log("heyy", json);

  const flaskRes = await postToFlask(
    json.coord.lat,

    json.coord.lon,
    json.main.temp - 273,
    json.wind.speed,
    json.main.humidity
  );

  console.log(flaskRes)

  // const generateWeather = (data) => {
  //     const result = data.weather[0];
  //     const card = `
  //     <p style= "margin-top: 200px; margin-left: 200px">
  //     ${result.description} is ${data.name}'s weather.
  //     </p>
  //     `;
  //     document.body.innerHTML += card;
  // };

  // console.log(getWeather(arr));

  res.redirect("/test/" + flaskRes.Risk);
});

const postToFlask = async (latitude, longtitude, temp, wind, hum) => {
  const data = { x: [[latitude, longtitude, temp, wind, hum]] };

  const res = await fetch("http://127.0.0.1:5000/", {
    method: "POST",
    body: JSON.stringify(data),
    headers: { "Content-Type": "application/json" },
  });

  const json = await res.json();
  return json;
};

// const getWeather = (arr[0], arr[1]) => {
//     // console.log(result);
//     fetch(result)
//       .then((data) => data.json())
//       // .then((data) => console.log(data));
//       .then((data) => generateWeather(data));
//   };

// const generateWeather = (data) => {
//     const result = data.weather[0];
//     const card = `
//     <p style= "margin-top: 200px; margin-left: 200px">
//     ${result.description} is ${data.name}'s weather.
//     </p>
//     `;
//     document.body.innerHTML += card;
// };

function searchName(worksheets) {
  console.log(typeof id);
  for (i = 0; i < worksheets.Sheet1.length; ++i) {
    if (worksheets.Sheet1[i].county.toString() == id) {
      return [worksheets.Sheet1[i].lat, worksheets.Sheet1[i].lng];
    }
  }
}

app.listen(port, () => console.log(`Server has started on port: ${port}`));
