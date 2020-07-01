const express = require('express')
const pug = require('pug');
var bodyParser = require('body-parser');
const app = express()
const port = 3000

app.set('view engine', 'pug')
app.use(express.static('public'))

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

let names = ['Jose', 'Luis']

app.get('/', (req, res) => res.sendFile('index.html'))
app.get('/pug', (req, res) => res.render('pugIndex', {names}))
app.post('/save-user', function(req, res) {
    console.log(req.body);
    names.push(req.body.name);
    res.json({message:"New name added"})
})
app.post('/delete-user', function(req, res) {
    console.log(req.body);

    // for( var i = 0; i < names.length; i++){ 
    //     if ( names[i] === req.body.name) {
    //       names.splice(i, 1); 
    //       i--;
    //     }
    //  }
    names.pop(req.body.name);
    // res.json({message: req.body.name + " Deleted"})
})

app.listen(port, () => console.log(`Example app listening on port ${port}!`))