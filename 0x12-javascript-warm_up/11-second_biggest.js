#!/usr/bin/node

const nums = [];

if (process.argv.length === 1 || process.argv.length === 2) {
  console.log(0);
} else {
  for (let i = 2; i < process.argv.length; i++) {
    nums.push(parseInt(process.argv[i]));
  }

  let largest = nums[0];
  let secondLargest = 0;

  for (let i = 1; i < nums.length; i++) {
    if (nums[i] > largest) {
      secondLargest = largest;
      largest = nums[i];
    }

    if (nums[i] < largest && nums[i] > secondLargest) {
      secondLargest = nums[i];
    }
  }

  console.log(secondLargest);
}
