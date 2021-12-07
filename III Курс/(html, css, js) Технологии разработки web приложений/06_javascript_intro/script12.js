import {data} from "./script11.js";

const ancestry = JSON.parse(data);

const average = (arr) => {
  return arr.reduce((prev, curr) => prev + curr, 0) / arr.length;
}

const centuries = {};
ancestry.forEach((person) => {
  const century = Math.ceil(person.died / 100);
  if (!Array.isArray(centuries[century])) {
    centuries[century] = [];
  }
  centuries[century].push(person.died - person.born)
});

Object.keys(centuries).forEach((key) => {
  centuries[key] = Math.round(average(centuries[key]) * 10) / 10;
});

console.log(centuries);