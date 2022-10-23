const express = require('express')
const app = express()
const port = 8383

const bodyParser = require('body-parser')

app.use(express.static('public'))
app.set('views', __dirname + '/public');
app.set('view engine', 'ejs');




/* app.get('/', (req, res) => {
    res.status(200).send('<h1>hi</h1>')
}) */

// parse application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({ extended: false }))

// parse application/json
app.use(bodyParser.json())


app.get('/', function (req, res, next) {
    res.render('index', { title: 'Cool, huh!', condition: true, anyArray: [1, 2, 3] });
});

app.get('/test/:id', function (req, res, next) {
    res.render('test.ejs', { output: req.params.id });
})

app.post('/test/submit', function (req, res, next) {
    var id = req.body.county;
    console.log(id)
    res.redirect('/test/' + id);
})

app.listen(port, () => console.log(`Server has started on port: ${port}`))