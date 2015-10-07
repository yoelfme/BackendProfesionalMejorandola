var express = require('express');
var app = express();

var messages = [];
var responses = [];

app.get('/', function (req, res) {
    res.send('Hello World!')
})

app.get('/messages', function (req, res) {
    responses.push(res);
    // res.send(messages+ '<script>setTimeout(function  () {window.location.reload()}, 1000);</script>');
});

app.get('/messages/:message', function (req, res) {
    messages.push(req.params.message);

    responses.forEach(function(res){
        res.send(messages+ '<script>window.location.reload();</script>');
    })

    res.send('tu mensaje es ' + req.params.message);
})

var server = app.listen(3000, function(){
     var host = server.address().address;
    var port = server.address().port;

    console.log('Example app listening at http://%s:%s', host, port);
});