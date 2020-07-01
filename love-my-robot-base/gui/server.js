const express = require('express')
var bodyParser = require('body-parser');
var request = require('request-promise');
const app = express()
const port = 8080

app.use(express.static('public'))

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
let lmr = ""
app.get('/', (req, res) => res.sendFile('index.html'))

app.post('/save-user', function(req, res) {
    
    
    lmr = req.body.funcion;
    console.log(lmr)
    
})

app.get('/postdata',async function (req, res) {
    var data = {lmr}

    var options = {
        method: 'POST',
        uri: 'http://127.0.0.1:8085/lex',
        body: data, 
        json: true
    };

    var returndata;
    var sendrequest = await request(options)
        .then(function (parsedBody) {
            console.log(parsedBody); 
            returndata = parsedBody; 
        })
        .catch(function (err) {
            console.log(err);
        });

    res.send(returndata);

});
app.listen(port, () => console.log(`Example app listening on port ${port}!`))