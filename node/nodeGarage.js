//Aw yiss
var net = require('net');
<<<<<<< HEAD
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
=======
var http = require('http'),
    fs = require("fs"),
    index = fs.readFileSync("../content/index.html");


var app = http.createServer(function (req, res) {
    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.end(index);
>>>>>>> 485f5882fd646486c841c8a190b43aed3451b1f5
});


var io = require("socket.io").listen(app);

<<<<<<< HEAD
//Server port
var HOST = "127.0.0.1";
var PORT = "8406";

var server = net.createServer(function (sock) {
    console.log("Connection >> " + sock.remoteAddress + ":" + sock.remotePort);
    console.log("Client device connected!");
    
    sock.on("data", function (data) {
        console.log(JSON.parse(data));
        io.emit('doorUpdate', JSON.parse(data));
=======

var HOST = "127.0.0.1";
var PORT = "7387";

net.createServer(function (sock) {
    console.log("Connection >> " + sock.remoteAddress + ":" + sock.remotePort);
    sock.on("data", function (data) {
        console.log(JSON.parse(data.toString()));
        io.emit('doorUpdate', JSON.parse(data.toString()));
>>>>>>> 485f5882fd646486c841c8a190b43aed3451b1f5
    });

    sock.on("close", function (data) {
        console.log('Closed >>');
    });

<<<<<<< HEAD
});

server.listen(PORT);
console.log("TCP Listen starrt...");

app.listen(8080);
console.log("Web server start...");
=======
}).listen(PORT, HOST);

app.listen(8406);
>>>>>>> 485f5882fd646486c841c8a190b43aed3451b1f5

