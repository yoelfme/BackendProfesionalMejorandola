$(document).ready(function(){
    window.io = io.connect();

    io.on('connect', function(socket){
        console.log('Hi');
        io.emit('hello?');
    })

    io.on('saludo', function(data){
        console.log(data);
    })
});