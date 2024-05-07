function cleanSet(set, startString) {
  // Check if set is an object and startString is a non-empty string
  if (
    typeof set !== 'object'
    || typeof startString !== 'string'
    || startString.length === 0
  ) {
    return '';
  }

  const cleanedValues = [];

  // Iterate over each item in the set
  for (const item of set) {
    // Check if the item starts with startString
    if (typeof item === 'string' && item.startsWith(startString)) {
      // If it does, push the substring after startString to the cleanedValues array
      cleanedValues.push(item.slice(startString.length));
    }
  }

  // Join the cleaned values with '-'
  return cleanedValues.join('-');
}

export default cleanSet;
