// 10-update_uniq_items.js
function updateUniqueItems(map) {
  // Check if the argument is a map
  if (!(map instanceof Map)) {
    throw new Error('Cannot process');
  }

  // Iterate over the entries of the map
  for (const [item, quantity] of map.entries()) {
    // If quantity is 1, update it to 100
    if (quantity === 1) {
      map.set(item, 100);
    }
  }
}

export default updateUniqueItems;
