// 5-typed_arrays.js
function createInt8TypedArray(length, position, value) {
  // Check if the position is within the range of the array length
  if (position < 0 || position >= length) {
    throw new Error('Position outside range');
  }

  // Create a new ArrayBuffer with the specified length
  const buffer = new ArrayBuffer(length);

  // Create a DataView to access and manipulate the bytes in the ArrayBuffer
  const dataView = new DataView(buffer);

  // Set the Int8 value at the specified position in the DataView
  dataView.setInt8(position, value);

  // Return the DataView
  return dataView;
}

export default createInt8TypedArray;
