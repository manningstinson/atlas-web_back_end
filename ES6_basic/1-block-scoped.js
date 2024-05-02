export default function taskBlock(trueOrFalse) {
  let task = false;
  let task2 = true;

  if (trueOrFalse) {
    task = true;  // No need to declare again with let, just assign the value
    task2 = false;  // Same here
  }

  return [task, task2];
}
