const sdk = require('./sdk');
    var d = sdk.parse('python3', 'transfer.txt');
    for (key of Object.keys(d)) {
        eval(`${key} = d['${key}'];`);
    }
    const neww = old.substr(0, 2);
sdk.makeTransferFile({'neww':neww});