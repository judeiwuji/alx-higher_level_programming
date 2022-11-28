#!/usr/bin/node

function factorial (n) {
  if (n === 0 || isNaN(n)) {
    return 1;
  }

  return n * factorial(n - 1);
}

const num = parseInt(process.argv[2]);
const result = factorial(num);
console.log(result);
