const exec = require('child_process').exec;
const fs = require('fs');

const fileEndings = {'python3': 'py'};
const fileDelimiter = ":";

function makeTransferFile(input) {
    //Input is a dictionary
    var data = '';
    const keys = Object.keys(input);
    for (var i=0;i<keys.length;i++) {
        const key = keys[i];
        const val = input[key];
        const type = typeof val;
        const name = key;
        if (i != 0) {
            data += "\n";
        }
        data += name + fileDelimiter + type + fileDelimiter + String(val);
    }
    //transfer.txt will be overwritten each time because it isn't needed any longer than its first use
    fs.writeFile("transfer.txt", data, (err) => {
        if (err) throw "Error writing to input file: " + err.message;
    });
}

async function meta(code, lang, input, output) {

    const codeFile = fs.writeFile("code." + fileEndings[lang], code, (err) => {
        if (err) throw "Error writing to input file: " + err.message;
    });
    //input is a dictionary
    makeTransferFile(input);

    const promise = new Promise(function(resolve, reject) {
        exec(`python3 run.py input.txt javascript ${lang} code.${fileEndings[lang]} ${output}`, (err, stdout, stderr) => {
            variables = parse(lang, "transfer.txt");
            resolve(variables);
        });
    });
    return promise;
}

function convert(lang, typ, data) {
    //Data comes in Javascript String form
    switch (lang) {
        case "python3":
            switch (typ) {
                case "str":
                    return data;
                case "int":
                    return parseInt(data);
                default:
                    return data;
            }
    
        default:
            console.log("Unsupported language: " + lang);
    }
}

function parse(lang, filename) {
    //Takes input file and outputs dictionary of converted variables
    var variables = {};

    const lines = fs.readFileSync('transfer.txt', 'utf8').split('\n');
    for (line of lines) {
        //Process line of output file
        const comps = line.split(fileDelimiter);
        if (comps[0] != '') {
            //Don't make a ghost variable for extra blank lines
            variables[comps[0]] = convert(lang, comps[1], comps[2]);
        }
    }
    return variables;
}

exports.meta = meta;
exports.parse = parse;
exports.makeTransferFile = makeTransferFile;
exports.convert = convert;