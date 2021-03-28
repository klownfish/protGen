"use strict";
const { exec } = require("child_process");
let fs = require('fs');

if (process.argv.length < 4) {
    console.log(`usage: node INPUT_FILE OUTPUT_FILE`)
    return
}
let input = process.argv[2]
let output = process.argv[3]
let raw = fs.readFileSync(input).toString()
let schema = JSON.parse(raw);
let baseName = output + `/${schema.config.name}`

let file = `GENERATED FILE DO NOT EDIT\n\n`


function build_table(iterator) {
    let output = ''
    output += 
    `<table>\n` +
    `<thead>\n` +
    `<tr>\n` +
    `<th>ID</th>\n` +
    `<th>Source</th>\n` +
    `<th>Target</th>\n` +
    `<th>Datatype</th>\n` +
    `</tr>\n` +
    `</thead>\n` +
    `<tbody>\n`
    let count = 0;
    for (let id in iterator) {
        count++
        let msg = iterator[id];
        output += "<tr>\n"
        output += `<td>${msg.id}</td>\n`
        output += `<td>${msg.source}</td>\n`
        output += `<td>${msg.target}</td>\n`
        output += `<td>${msg.datatype}</td>\n`
        output += "</tr>\n"
    }
    output += `</tbody>\n</table>\n\n`
    if (count){
        return output
    } else {
        return "*nothing*\n"
    }
}

let sources = {}
let targets = {}
for (let unit in schema.enums.units.entries) {
    sources[unit] = []
    targets[unit] = []
}

for (let id in schema.messages) {
    let msg = schema.messages[id]
    sources[msg.source].push(msg)
    targets[msg.target].push(msg)
}

file += `# ${schema.config.name} - Description\n`
file += `## All messages\n`
file += build_table(schema.messages);

file += `## Messages per unit\n`
for (let unit in schema.enums.units.entries) {
    file += `### ${unit}\n`
    file += `#### ${unit} - receives\n`
    file += build_table(targets[unit])
    file += `#### ${unit} - sends\n`
    file += build_table(sources[unit])
}


file += `## Datatypes\n`
for (let name in schema.datatypes) {
    let datatype = schema.datatypes[name];
    file += `### ${name}\n`
    if (!datatype.bitField && datatype.fields.length == 0) {
        file += "*empty*\n"
    }
    if (datatype.bitField) {
        file += `#### bits\n`
        file +=
        `<table>\n` +
        `<thead>\n` +
        `<tr>\n` +
        `<th>name</th>\n` +
        `<th>bit</th>\n` +
        `</tr>\n` +
        `</thead>\n` +
        `<tbody>\n`
        for (let bit in datatype.bitField) {
            file += `<tr>\n`
            file += `<td>${datatype.bitField[bit]}</td>\n`
            file += `<td>${bit}</td>\n`
            file += `</tr>\n`
        }
        file += `</tbody>\n</table>\n\n`
    }

    if (datatype.fields.length > 0) {
        file += `#### fields\n`
        file +=
        `<table>\n` +
        `<thead>\n` +
        `<tr>\n` +
        `<th>name</th>\n` +
        `<th>type</th>\n` +
        `<th>native type</th>\n` +
        `<th>info</th>\n` +
        `</tr>\n` +
        `</thead>\n` +
        `<tbody>\n`

        for (let field of datatype.fields) {
            file += `<tr>\n`
            file += `<td>${field.name}</td>\n`
            file += `<td>${field.type}</td>\n`
            file += `<td>${field.nativeType}</td>\n`
            switch (field.type) {
                case "packedFloat":
                    file += `<td>min=${field.min} max=${field.max}</td>\n`
                    break;
                case "scaledFloat":
                    file += `<td>scale=${field.scale}</td>\n`
                    break;
                case "enum":
                    file += `<td>enum=${field.enumName}</td>\n`
                    break;
                default:
                    file += "<td>N/A</td>\n"
            }
            file += `</tr>\n`
        }
        file += `</tbody>\n</table>\n\n`
    }
}

file += `## Enums\n`
for (let key in schema.enums) {
    let enumerator = schema.enums[key];
    file += `### ${enumerator.name}\n`
    file +=
        `<table>\n` +
        `<thead>\n` +
        `<tr>\n` +
        `<th>name</th>\n` +
        `<th>value</th>\n` +
        `</tr>\n` +
        `</thead>\n` +
        `<tbody>\n`
    for (let entry in enumerator.entries) {
        file += `<tr>\n`
        file += `<td>${entry}</td>\n`
        file += `<td>${enumerator.entries[entry]}</td>\n`
        file += `</tr>\n`
    }
    file += `</tbody>\n</table>\n\n`
}
fs.writeFileSync(output, file);