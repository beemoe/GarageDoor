//Aw yiss
var net = require('net');
var path = require('path');
var http = require('http'),
    fs = require("fs")


var app = http.createServer(function (req, res) {
    console.log(req.url);
    var filePath = '..' + req.url;

    console.log(filePath);
    if(filePath == '../'){
            var contentType = 'text/html'
            fs.readFile('../content/index.html', function(error, content){
            if(error)
            {
                res.writeHead(404, {'Content-Type': contentType});
                res.end("", 'utf-8')
            }
            else{
                res.writeHead(200, {'Content-Type': contentType});
                res.end(content, 'utf-8');
            }

        });
    }
    else{
        var extname = path.extname(filePath);
        var contentType = 'image/png';
        console.log(filePath)
        fs.readFile(filePath, function(error, content){
            if(error)
            {
                res.writeHead(404, {'Content-Type': contentType});
                res.end("", 'utf-8')
            }
            else{
                res.writeHead(200, {'Content-Type': contentType});
                res.end(content, 'utf-8');
            }

        });
    }
});


var io = require("socket.io").listen(app);

//Server port
var HOST = "127.0.0.1";
var PORT = "8406";

var server = net.createServer(function (sock) {
    console.log("Connection >> " + sock.remoteAddress + ":" + sock.remotePort);
    console.log("Client device connected!");
    
    sock.on("data", function (data) {
        console.log(JSON.parse(data));
        io.emit('doorUpdate', JSON.parse(data));
    });

    sock.on("close", function (data) {
        console.log('Closed >>');
    });

});

server.listen(PORT);
console.log("TCP Listen starrt...");

app.listen(8080);
console.log("Web server start...");

