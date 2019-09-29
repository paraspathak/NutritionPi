const http = require('http');

const hostname = '127.0.0.1';
const port = 3000;

const request = require('requests')

// request.post('/getdata');

var server=http.createServer((function(request,response)
{
	response.writeHead(200,
	{"Content-Type" : "text/plain"});
	response.end("Hello World\n");
}));
server.listen(7000);
