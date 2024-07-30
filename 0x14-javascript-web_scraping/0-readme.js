#!/usr/bin/node
const fs = require('fs');

const FileName = process.argv[2];
fs.readFile(FileName, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }
  console.log(data);
});
