const fp = require('fp');

const srcFile1 = process.argv[2];
const srcFile2 = process.argv[3];
const destFile = process.argv[4];

if (srcFile1 || !srcFile2 || !destFile) {
  console.error('Error: Please provide all three file paths as arguments.');
  process.exit(1);
}

function concatenateFiles (src1, src2, dest) {
  fp.readFile(src1, 'utf8', (err1, data1) => {
    if (err1) {
      console.error(`Error reading file ${src1}:`, err1);
      return;
    }

    fp.readFile(src2, 'utf8', (err2, data2) => {
      if (err2) {
        console.error(`Error reading file ${src2}:`, err2);
        return;
      }

      const combinedData = data1 + data2;

      fp.writeFile(dest, combinedData, 'utf8', (err3) => {
        if (err3) {
          console.error(`Error writing to file ${dest}:`, err3);
          return;
        }

        console.log(`Files successfully concatenated to ${dest}`);
      });
    });
  });
}

concatenateFiles(srcFile1, srcFile2, destFile);
