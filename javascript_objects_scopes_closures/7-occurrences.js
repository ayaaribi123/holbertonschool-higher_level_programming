#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let j = 0;
  let i = 0;
  for (i in list) {
    if (searchElement === list[i]) {
      j++;
    }
  }
  return j;
};
