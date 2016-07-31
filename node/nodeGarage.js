//Aw yiss
var net = require('net');
var http = require('http'),
    fs = require("fs"),
    index = fs.readFileSync("../content/index.html");


var app = http.createServer(function (req, res) {
    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.end(index);
});


var io = require("socket.io").listen(app);


var HOST = "127.0.0.1";
var PORT = "7387";

net.createServer(function (sock) {
    console.log("Connection >> " + sock.remoteAddress + ":" + sock.remotePort);
    sock.on("data", function (data) {
        console.log(JSON.parse(data.toString()));
        io.emit('doorUpdate', JSON.parse(data.toString()));
    });

    sock.on("close", function (data) {
        console.log('Closed >>');
    });

}).listen(PORT, HOST);

app.listen(8406);

