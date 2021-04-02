"use strict";
const { exec } = require("child_process");
let fs = require('fs');

if (process.argv.length < 4) {
    console.log(`usage: node INPUT_output OUTPUT_output`)
    return
}
let input = process.argv[2]
let file = process.argv[3]
let raw = fs.readFileSync(input).toString()
let schema = JSON.parse(raw);
let baseName = file + `/${schema.config.name}`

let output = `GENERATED output DO NOT EDIT\n\n`


function build_small_table(iterator) {
    let output = ''
    output += 
    `<table>\n` +
    `<thead>\n` +
    `<tr>\n` +
    `<th>ID</th>\n` +
    `<th>Source</th>\n` +
    `<th>Target</th>\n` +
    `<th>name</th>\n` +
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
        output += `<td>${msg.name}</td>\n`
        output += "</tr>\n"
    }
    output += `</tbody>\n</table>\n\n`
    if (count){
        return output
    } else {
        return "*nothing*\n"
    }
}

function build_message_table(msg) {
    let output = ''
    output += `### ${msg.name}: ${msg.source} &rarr; ${msg.target}\n`
    if (!msg.bitField && msg.fields.length == 0) {
        output += "*empty*\n"
        return output
    }
    if (msg.bitField) {
        output += "#### bits\n"
        output += 
        `<table>\n` +
        `<thead>\n` +
        `<tr>\n` +
        `<th>bit</th>\n` +
        `<th>name</th>\n` +
        `</tr>\n` +
        `</thead>\n` +
        `<tbody>\n`
        
        for (let index in msg.bitField) {
            output += "<tr>\n"
            output += `<td>${index}</td>\n`
            output += `<td>${msg.bitField[index]}</td>\n`
            output += "</tr>\n"
        }
        output += `</tbody>\n</table>\n\n`
    }

    if (msg.fields.length > 0) {
        output += `#### fields\n`
        output +=
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

        for (let field of msg.fields) {
            output += `<tr>\n`
            output += `<td>${field.name}</td>\n`
            output += `<td>${field.type}</td>\n`
            output += `<td>${field.nativeType}</td>\n`
            switch (field.type) {
                case "packedFloat":
                    output += `<td>min=${field.min} max=${field.max}</td>\n`
                    break;
                case "scaledFloat":
                    output += `<td>scale=${field.scale}</td>\n`
                    break;
                case "enum":
                    output += `<td>enum=${field.enumName}</td>\n`
                    break;
                default:
                    output += "<td>N/A</td>\n"
            }
            output += `</tr>\n`
        }
        output += `</tbody>\n</table>\n\n`
    }
    return output
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

output += `# ${schema.config.name} - Description\n`
output += `## All messages\n`
output += build_small_table(schema.messages);

for (let key in schema.messages) {
    let msg = schema.messages[key]
    output += build_message_table(msg)
}

output += `## Enums\n`
for (let key in schema.enums) {
    let enumerator = schema.enums[key];
    output += `### ${enumerator.name}\n`
    output +=
        `<table>\n` +
        `<thead>\n` +
        `<tr>\n` +
        `<th>name</th>\n` +
        `<th>value</th>\n` +
        `</tr>\n` +
        `</thead>\n` +
        `<tbody>\n`
    for (let entry in enumerator.entries) {
        output += `<tr>\n`
        output += `<td>${entry}</td>\n`
        output += `<td>${enumerator.entries[entry]}</td>\n`
        output += `</tr>\n`
    }
    output += `</tbody>\n</table>\n\n`
}
fs.writeFileSync(file, output);