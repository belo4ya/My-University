/* 12. Историческая ожидаемая продолжительность жизни.
Мы считали, что только последнее поколение людей дожило до 90 лет.
Давайте рассмотрим этот феномен поподробнее. Подсчитайте средний
возраст людей для каждого из столетий. Назначаем столетию людей,
беря их год смерти, деля его на 100 и округляя: Math.ceil(person.died / 100).
 */

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