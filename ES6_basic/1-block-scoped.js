export default function taskBlock(trueOrFalse) {
  let task = false;
  let task2 = true;

  if (trueOrFalse) {
   const task = true;  // Updated value without re-declaring
   const task2 = false;  // Updated value without re-declaring
  }

  return [task, task2];
}