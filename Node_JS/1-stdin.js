console.log("Welcome to Holberton School, what is your name?");

process.stdin.setEncoding('utf8');

process.stdin.on('data', (data) => {
    const input = data.trim();  // Trim to remove any extra spaces or newlines
    console.log(`Your name is: ${input}`);
    console.log("This important software is now closing");
    process.exit();  // Exit the program
});
