const fs = require('node:fs');

// first attempt with a more imperative approach
const DIGITS = [
	"one",
	"two",
	"three",
	"four",
	"five", "six", "seven",
	"eight",
	"nine"
];

const testData = [
	"two1nine",
	"eightwothree",
	"abcone2threexyz",
	"xtwone3four",
	"4nineeightseven2",
	"zoneight234",
	"7pqrstsixteen"
];

const sol1 = () => {
	fs.readFile("day1_input.txt", "utf8", (err, data) => {
		if (err) {
			console.log(err);
			return;
		}
		const getNum = (str) => {
			let nums = str.split("").filter((x) => !isNaN(x));
			if (nums.length > 1) return nums[0] + nums[nums.length - 1];
			else return nums[0] + nums[0];
		};
		let sum = 0;
		data.split("\n").forEach((line) => sum += Number.parseInt(getNum(line)));
		console.log(sum);
	});
};
console.log(sol1());

const sol2 = () => {
	fs.readFile("day1_input.txt", "utf8", (err, data) => {
		if (err) {
			console.log(err);
			return;
		}
		const getNum = (str) => {
			let nums = {};
			// can also be done with regex, but this is easier to test and debug :)
			DIGITS.forEach((digit, index) => {
				let idx = str.indexOf(digit);
				while (idx !== -1) {
					nums[idx] = index + 1;
					idx = str.indexOf(digit, idx + 1);
				}
			});
			nums = Object.fromEntries(Object.entries(nums).sort(([keyA], [keyB]) => keyA - keyB));
			str.split("").map((x, index) => {
				if (!isNaN(x)) {
					nums[index] = x;
				}
			});
			// ugly ugly ugly...
			let num = Object.values(nums)[0].toString() + nums[Object.keys(nums)[Object.keys(nums).length - 1]].toString();
			return num;
		};
		let sum = 0;
		data.split("\n").forEach((line) => sum += Number.parseInt(getNum(line)));
		console.log(sum);
	});
};

sol2();