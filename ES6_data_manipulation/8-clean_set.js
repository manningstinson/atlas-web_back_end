// 8-clean_set.js
function cleanSet(set, startString) {
  // Filter out values that start with startString and concatenate them into a string separated by -
  return Array.from(set)
    .filter((value) => value.startsWith(startString))
    .join('-');
}

export default cleanSet;
