var http = require("http");
var console = require("console");
var config = require("config");

module.exports.function = function sendCommand (command) {

  var sendcommand = "";

  var options = {
    passAsJson: true,
    returnHeaders: true,
    headers: { "Content-Type": "application/json; charset=UTF-8" },
    format: 'json'
  };

  var commandJson = {
    "command": command
  };

  let uuid = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
    var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
    return v.toString(16);
  });
  var response = http.postUrl("http://641c9556a92c.ngrok.io/command?uuid="+uuid, commandJson, options);

  console.log(response);

  return {
    sendedcommand: command
  }
}