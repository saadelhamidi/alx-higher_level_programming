#!/usr/bin/node
const fs = require('fs');

const FileName = process.argv[2];
const data = process.argv[3];
fs.writeFile(FileName, data, (err) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }
});
