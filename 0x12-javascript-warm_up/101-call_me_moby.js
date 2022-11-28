#!/usr/bin/node

function callMeMoby (x, theFunction) {
  while (x) {
    theFunction();
    --x;
  }
}

module.exports = {
  callMeMoby
};
