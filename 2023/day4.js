const fs = require('node:fs');

var testData = [
	"Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
	"Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
	"Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
	"Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
	"Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
	"Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
];

const sol1 = () => {
	fs.readFile("day4_input.txt", "utf8", (err, data) => {
		if (err) {
			console.log(err);
			return
		}
		data = data.split("\n");
		let sum = 0;
		data.forEach((line) => {
			let [ winningNums, gameNums ] = line.substring(line.indexOf(":") + 1).split("|");
			winningNums = winningNums.split(" ").map(Number); gameNums = gameNums.split(" ").map(Number);
			const intersect = winningNums.filter(nums => gameNums.includes(nums)).filter(num => num !== 0);
			const count = intersect.length > 2 ? Math.pow(2, intersect.length - 1) : intersect.length;
			sum += count;
		});
		console.log(sum);
	});
};

sol1();

const sol2 = () => {
	fs.readFile("day4_input.txt", "utf8", (err, data) => {
		if (err) {
			console.log(err);
			return
		}
		data = data.split("\n");
		const cardsWon = data.map(() => 1);
		data.forEach((line, idx) => {
			let [ winningNums, gameNums ] = line.substring(line.indexOf(":") + 1).split("|");
			winningNums = winningNums.split(" ").map(Number); gameNums = gameNums.split(" ").map(Number);
			const count = winningNums.filter(nums => gameNums.includes(nums)).filter(num => num !== 0).length;
			for (let i = 0; i < count; i++) {
				cardsWon[idx + 1 + i] += cardsWon[idx];
			}
		});
		console.log(cardsWon.reduce((acc, n) => acc + n));
	});
};

sol2();