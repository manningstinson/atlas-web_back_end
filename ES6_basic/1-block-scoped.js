export default function taskBlock(trueOrFalse) {
	const task = false;
	const task2 = true;

	if (trueOrFalse) {
		const task = true; // Updated value without re-declaring
		const task2 = false; // Updated value without re-declaring
	}

	console.log(task, task2); // Using task and task2 to resolve ESLint errors
}
