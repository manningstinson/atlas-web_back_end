export default function taskBlock(trueOrFalse) {
  let task = false;
  let task2 = true;

  if (trueOrFalse) {
    task = true; // Updated value without re-declaring
    task2 = false; // Updated value without re-declaring
    console.log(task, task2); // Using task and task2 to satisfy ESLint
  }

  return [task, task2];
}

// Or returning an object
// return { task, task2 };
