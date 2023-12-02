const fs = require('node:fs');

var testData = [
	"Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
	"Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
	"Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
	"Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
	"Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
];

const parameters = {
	'red': 12,
	'green': 13,
	'blue': 14,
};

const sol1 = () => {
	fs.readFile("day2_input.txt", "utf8", (err, data) => {
		if (err) {
			console.log(err);
			return;
		}
		data = data.split("\n");
		let sum = 0;
		data.forEach((line) => {
			let game = line.slice(0, line.indexOf(":"));
			let gameID = Number.parseInt(game.split(" ")[1]);
			let rest = line.slice(line.indexOf(":") + 1);
			const isPossible = () => {
				let res = rest.split(";").every((set) => {
					let vals = set.split(",").every((part) => {
						let [ number, colour ] = part.trimStart().split(" ");
						return parameters[colour] >= number;
					});
					return vals;
				});
				return res;
			}
			if (isPossible()) sum += gameID;
		});
		console.log(sum);
	});
};

sol1();

const sol2 = () => {
	fs.readFile("day2_input.txt", "utf8", (err, data) => {
		if (err) {
			console.log(err);
			return;
		}
		data = data.split("\n");
		let sum = 0;
		data.forEach((line) => {
			let rest = line.slice(line.indexOf(":") + 1);
			const getFewest = () => {
				let red = 1, green = 1, blue = 1;
				rest.split(";").map((set) => {
					set.split(",").map((part) => {
						let [ number, colour ] = part.trimStart().split(" ");
						number = Number.parseInt(number);
						switch (colour) {
						case "red":
							if (number > red) red = number
							break;
						case "green":
							if (number > green) green = number
							break;
						default:
							if (number > blue) blue = number
							break;
						}
					});
				});
				return red * green * blue;
			};
			sum += getFewest();
		});
		console.log(sum);
	});
};

sol2();