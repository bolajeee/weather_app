const EventEmitter = require("events");

const emitter = new EventEmitter();

emitter.on("log", (param) => {
  console.log("Logging...:", param);
});

const logging = (param) => {
//   console.log("logging", param);
  emitter.emit("log", param);
};

logging({
  id: "first log",
  message: "This is the first log",
});

module.exports.logging = logging;
