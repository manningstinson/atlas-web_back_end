export default function taskBlock(trueOrFalse) {
  const task = false;
  const task2 = true;

  if (trueOrFalse) {
    task = true;  // Updated value without re-declaring
    task2 = false;  // Updated value without re-declaring
  }

  return [task, task2];
}
