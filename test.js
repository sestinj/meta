const sdk = require("./sdk");

var a = 5;
var b = 3;

sdk.meta("c = a + b", "python3", {"a":a,"b":b}, ["c"]).then((data) => {
    const vars = Object(data);
    console.log(vars);
}, (err) => {
    console.log("METAERR: " + err);
});
