// 1. Variable declaration & dynamic typing
let score = 95;
console.log(score); // 95

score = "Excellent";
console.log(score); // "Excellent"

// 2. Decision-making with if and switch
let fruit = prompt("Enter your favorite fruit:");

if (fruit === "apple") {
  console.log("You like apples!");
} else {
  switch (fruit) {
    case "banana":
      console.log("Bananas are great for energy.");
      break;
    case "orange":
      console.log("Oranges are full of vitamin C.");
      break;
    default:
      console.log("That's a nice choice!");
  }
}

// 3. Iterative control structures
// for loop
for (let i = 1; i <= 5; i++) {
  console.log(i);
}

// while loop
let j = 1;
while (j <= 5) {
  console.log(j);
  j++;
}

// do...while loop
let k = 1;
do {
  console.log(k);
  k++;
} while (k <= 5);
