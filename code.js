const sdk = require('./sdk');
    var d = sdk.parse('python3', 'transfer.txt');
    for (key of Object.keys(d)) {
        eval(`${key} = d['${key}'];`);
    }
    const f = (a, b) => {
const meta = require('./sdk').meta
__d__=meta(`    c = a + b
`, 'python3', {'a':a, 'b':b,}, ['c']);
for (key of Object.keys(__d__)) { eval(key + ' = __d__[' + key + ']'); }
    return c;
}
const g = f(2,3);
console.log(g);

sdk.makeTransferFile({});