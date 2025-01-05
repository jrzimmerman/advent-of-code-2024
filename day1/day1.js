import { readFile } from '../utils/utils.js';

// const file = readFile(import.meta.dirname, 'test.txt');
const file = readFile(import.meta.dirname, 'input.txt');

const lines = file.split('\n');
const alist = [];
const blist = [];
for (let line of lines) {
    const [a,b] = line.trim().split('   ');
    if (a && b) {
        alist.push(Number(a));
        blist.push(Number(b));
    }
}

alist.sort();
blist.sort();

let part1 = 0;
for (let i = 0; i < alist.length; i++) {
    let ai = alist[i];
    let bi = blist[i];
    part1 += Math.abs(ai - bi);
}
console.log('Part 1: ', part1);

const map = {};
for (let i = 0; i < alist.length; i++) {
    let ai = alist[i];
    map[ai] = 0;
}

for (let j = 0; j < blist.length; j++) {
    let bi = blist[j];
    map[bi] += 1;
}

console.log(map);

let part2 = 0;
for (let [key, value] of Object.entries(map)) {
    if (value) {
        part2 += key * value;
    }
}
console.log('Part 2: ', part2);
