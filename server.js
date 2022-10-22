const express = require('express')
const app = express()
const port = 8383

app.use(express.static('public'))

/* app.get('/', (req, res) => {
    res.status(200).send('<h1>hi</h1>')
}) */

app.get('/', function(req, res, next) {
    res.render('index', {title: 'Cool, huh!', condition: true, anyArray: [1,2,3]});
});

app.get('/test/:id', function(req, res, next){
    res.render('test', {output: req.params.id});
}) 

app.post('/test/submit', function(req, res, next){
    var id = req.body.sth;
    res.redirect('/test/' + id);
})

app.listen(port, () => console.log(`Server has started on port: ${port}`))