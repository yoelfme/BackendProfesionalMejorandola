$(document).ready(function(){
    window.io = io.connect();

    io.on('connect', function (socket) {
        console.log('Hi');
        io.emit('hello?');
    })

    io.on('saludo', function (data) {
        console.log(data);
    })

    io.on('log-in', function (data) {
        $('#users').append(
            $('<li>', { text: data.username })
        );
    })

    io.on('log-out', function (data) {
        $('#users li').each(function(i, item) {
            if(item.innerText == data.username) {
                $(item).remove();
            }
        })
    })
});