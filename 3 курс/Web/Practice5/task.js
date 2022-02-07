console.log('\nЗАДАНИЕ 1');
/* Треугольник. Напишите цикл, который выводит такой треугольник.*/

i = 1;
while (i <= 7) {
    console.log("#".repeat(i));
    i+=1;
}


console.log('\nЗАДАНИЕ 2');
/*
2) FizzBuzz. Напишите программу, которая выводит через console.log все числа от 1 до 100, с двумя исключениями.
Для чисел, нацело делящихся на 3, она должна выводить ‘Fizz’, а для чисел, делящихся на 5 (но не на 3) – ‘Buzz’,
Когда сумеете – исправьте её так, чтобы она выводила «FizzBuzz» для всех чисел, которые делятся и на 3 и на 5.
 */
for (let i = 1; i < 100; i++) {
    result = "";
    if (i % 3 === 0) {
        result += "Fizz"
    }
    if (i % 5 === 0) {
        result += "Buzz"
    }
    if (result.length === 0) {
        result = i;
    }
    console.log(result)
}


console.log('\nЗАДАНИЕ 3');
/*
3)	Шахматная доска. Напишите программу, создающую строку, содержащую решётку 8х8, в которой линии разделяются символами новой строки.
На каждой позиции либо пробел, либо #. В результате должна получиться шахматная доска.
 */
let size = 8;
for (let i = 0; i < 8; i++) {
    if (i % 2 === 0) {
        console.log("# ".repeat(size / 2));
    } else {
        console.log(" #".repeat(size / 2));
    }
}


console.log('\nЗАДАНИЕ 4');
/*4) Минимум. Напишите функцию min, принимающую два аргумента, и возвращающую минимальный из них.*/
function min(a1, a2) {
    if (a1 < a2) {
        return a1;
    } else {
        return a2;
    }
}

console.log(min(4, 16));


console.log('\nЗАДАНИЕ 5');
/*
5) Считаем бобы.
Символ номер N строки можно получить, добавив к ней .charAt(N) ( “строчка”.charAt(5) ) – схожим образом с получением длины строки при помощи .length.
Возвращаемое значение будет строковым, состоящим из одного символа (к примеру, “к”).
У первого символа строки позиция 0, что означает, что у последнего символа позиция будет string.length – 1.
Другими словами, у строки из двух символов длина 2, а позиции её символов будут 0 и 1.
Напишите функцию countBs, которая принимает строку в качестве аргумента, и возвращает количество символов “B”, содержащихся в строке.
Затем напишите функцию countChar, которая работает примерно как countBs, только принимает второй параметр — символ, который мы будем искать в
строке (вместо того, чтобы просто считать количество символов “B”).
Для этого переделайте функцию countBs.
 */
function countBs(string) {
    let count = 0;
    for (let i = 0; i < string.length; i++) {
        if (string.charAt(i) === "B") {
            count++;
        }
    }
    console.log(count)
}

function countChar(string, smb) {
    let count = 0;
    for (let i = 0; i < string.length; i++) {
        if (string.charAt(i) === smb) {
            count++;
        }
    }
    console.log(count)
}

const text = "MAYBE ONE DAY I'LL BE....";
countBs(text)
countChar(text, "E")


console.log('\nЗАДАНИЕ 6');
/*
6) Сумма диапазона. Напишите функцию range, принимающую два аргумента, начало и конец диапазона, и возвращающую массив, который содержит все числа из него,
включая начальное и конечное.
Затем напишите функцию sum, принимающую массив чисел и возвращающую их сумму.
Запустите указанную выше инструкцию и убедитесь, что она возвращает 55.
В качестве бонуса дополните функцию range, чтобы она могла принимать необязательный третий аргумент – шаг для построения массива.
Если он не задан, шаг равен единице.
Вызов функции range(1, 10, 2) должен будет вернуть [1, 3, 5, 7, 9].
Убедитесь, что она работает с отрицательным шагом так, что вызов range(5, 2, -1) возвращает [5, 4, 3, 2].
*/
function range(start, end, step) {
    const array = [];
    while (step > 0 ? start <= end : start >= end) {
        array.push(start);
        start += step;
    }
    return array;
}

function sum(array) {
    let summ = 0;
    for (let i = 0; i < array.length; i++)
        summ += array[i];
    return summ
}

result = range(5, 2, -1)
console.log(result);
console.log(sum(result));


console.log('\nЗАДАНИЕ 7');
/*
7) Обращаем массив вспять.
Напишите две функции, reverseArray и reverseArrayInPlace.
Первая получает массив как аргумент и выдаёт новый массив, с обратным порядком элементов.
Вторая работает как оригинальный метод reverse – она меняет порядок элементов на обратный в том массиве, 
который был ей передан в качестве аргумента. Не используйте стандартный метод reverse.
*/
function reverseArray(array) {
    let result = [];
    for (let i = array.length - 1; i >= 0; i--)
        result.push(array[i]);
    return result;
}

function reverseArrayInPlace(array) {

    for (let i = 0; i < Math.floor(array.length / 2); i++) {
        let j = array.length - 1 - i;
        let buff = array[i];
        array[i] = array[j];
        array[j] = buff;
    }
    return array;
}


let array = [10, 20, 30, 40, 50];
console.log(array);
console.log(reverseArray(array));
console.log(reverseArrayInPlace(array));


console.log('\nЗАДАНИЕ 8');
/* 8) Список. Объекты могут быть использованы для построения различных структур данных. Часто встречающаяся структура – список (не путайте с массивом).
Список – связанный набор объектов, где первый объект содержит ссылку на второй, второй – на третий, и т.п.
Списки удобны тем, что они могут делиться частью своей структуры. Например, можно сделать два списка, {value: 0, rest: list} и {value: -1, rest: list},
где list – это ссылка на ранее объявленную переменную. Это два независимых списка, при этом у них есть общая структура list,
которая включает три последних элемента каждого из них. Кроме того, оригинальный список также сохраняет свои свойства как отдельный список из трёх элементов.
Напишите функцию arrayToList, которая строит такую структуру, получая в качестве аргумента [1, 2, 3], а также функцию listToArray, которая создаёт массив из списка.
Также напишите вспомогательную функцию prepend, которая получает элемент и создаёт новый список, где этот элемент добавлен спереди к первоначальному списку,
и функцию nth, которая в качестве аргументов принимает список и число, а возвращает элемент на заданной позиции в списке,
или же undefined в случае отсутствия такого элемента.
Если ваша версия nth не рекурсивна, тогда напишите её рекурсивную версию.
*/
function arrayToList(array) {
    let list = {value: array[0], rest: null};
    let current = list;
    for (let i = 1; i < array.length; i++) {
        current.rest = {};
        current.rest.value = array[i];
        current.rest.rest = null;
        current = current.rest;
    }
    return list;

}

function listToArray(list) {
    let array = [];
    while (list != null) {
        array.push(list.value);
        list = list.rest;
    }

    return array;
}

function prepend(list, elem) {
    return {value: elem, rest: list};
}

function nth(list, index, current = 0) {
    if (index === current) {
        return list.value;
    } else {
        if (list != null) {
            return nth(list.rest, index, current + 1);
        } else {
            return undefined;
        }
    }
}

l = arrayToList([1, 2, 3]);
console.log(l);
console.log(nth(l, 2));
console.log(listToArray(l));
l = prepend(l, 4);
console.log(l);
console.log(nth(l, 1));


console.log('\nЗАДАНИЕ 9');
/*
9)	Глубокое сравнение. Оператор == сравнивает переменные объектов, проверяя, ссылаются ли они на один объект.
Но иногда полезно было бы сравнить объекты по содержимому.
Напишите функцию deepEqual, которая принимает два значения и возвращает true, только если это два одинаковых значения или это объекты, свойства которых имеют
одинаковые значения, если их сравнивать рекурсивным вызовом deepEqual.
Чтобы узнать, когда сравнивать величины через ===, а когда – объекты по содержимому, используйте оператор typeof.
Если он выдаёт “object” для обеих величин, значит нужно делать глубокое сравнение.
Не забудьте об одном дурацком исключении, случившемся из-за исторических причин: “typeof null” тоже возвращает “object”
*/
function deepEqual(a, b) {
    if (a === b) {
        return true;
    }

    if (a == null || b == null || typeof(a) != "object" || typeof(b) != "object") {
        return false;
    }

    for (let i in a) {
        if (!(i in b) || !deepEqual(a[i], b[i])) {
            return false;
        }
    }
    return true;
}

const sample = {one: 1, more: {two: 2, three: 3}};
console.log(deepEqual(sample, sample));
console.log(deepEqual(sample, {more: {two: 2, three: 3}, one: 1}));
console.log(deepEqual(sample, {one: 1, two: 2}));


console.log('\nЗАДАНИЕ 10');
/* 10) Свертка. Используйте метод reduce в комбинации с concat для свёртки массива массивов в один массив, у которого есть все элементы входных массивов.*/
let arr = [["my_cat"], ["other_cats"], ["white", 1], ["brown", 10], ["black", 5], ["parent's_cat"]];
arr = arr.reduce((a, b) => a.concat(b));

console.log(arr);


console.log('\nЗАДАНИЕ 11');
/*
11)	Разница в возрасте матерей и их детей.
Используя набор данных из примера, подсчитайте среднюю разницу в возрасте между матерями и их детьми (это возраст матери во время появления ребёнка).
Можно использовать функцию average, приведённую в главе.
Обратите внимание – не все матери, упомянутые в наборе, присутствуют в нём.
Здесь может пригодиться объект byName, который упрощает процедуру поиска объекта человека по имени.
 */
const data = JSON.stringify([
    {
        "name": "Carolus Haverbeke",
        "sex": "m",
        "born": 1832,
        "died": 1905,
        "father": "Carel Haverbeke",
        "mother": "Maria van Brussel"
    },
    {
        "name": "Emma de Milliano",
        "sex": "f",
        "born": 1876,
        "died": 1956,
        "father": "Petrus de Milliano",
        "mother": "Sophia van Damme"
    },
    {
        "name": "Maria de Rycke",
        "sex": "f",
        "born": 1683,
        "died": 1724,
        "father": "Frederik de Rycke",
        "mother": "Laurentia van Vlaenderen"
    },
    {
        "name": "Jan van Brussel",
        "sex": "m",
        "born": 1714,
        "died": 1748,
        "father": "Jacobus van Brussel",
        "mother": "Joanna van Rooten"
    },
    {
        "name": "Philibert Haverbeke",
        "sex": "m",
        "born": 1907,
        "died": 1997,
        "father": "Emile Haverbeke",
        "mother": "Emma de Milliano"
    },
    {
        "name": "Jan Frans van Brussel",
        "sex": "m",
        "born": 1761,
        "died": 1833,
        "father": "Jacobus Bernardus van Brussel",
        "mother": null
    },
    {
        "name": "Pauwels van Haverbeke",
        "sex": "m",
        "born": 1535,
        "died": 1582,
        "father": "N. van Haverbeke",
        "mother": null
    },
    {
        "name": "Clara Aernoudts",
        "sex": "f",
        "born": 1918,
        "died": 2012,
        "father": "Henry Aernoudts",
        "mother": "Sidonie Coene"
    },
    {
        "name": "Emile Haverbeke",
        "sex": "m",
        "born": 1877,
        "died": 1968,
        "father": "Carolus Haverbeke",
        "mother": "Maria Sturm"
    },
    {
        "name": "Lieven de Causmaecker",
        "sex": "m",
        "born": 1696,
        "died": 1724,
        "father": "Carel de Causmaecker",
        "mother": "Joanna Claes"
    },
    {
        "name": "Pieter Haverbeke",
        "sex": "m",
        "born": 1602,
        "died": 1642,
        "father": "Lieven van Haverbeke",
        "mother": null
    },
    {
        "name": "Livina Haverbeke",
        "sex": "f",
        "born": 1692,
        "died": 1743,
        "father": "Daniel Haverbeke",
        "mother": "Joanna de Pape"
    },
    {
        "name": "Pieter Bernard Haverbeke",
        "sex": "m",
        "born": 1695,
        "died": 1762,
        "father": "Willem Haverbeke",
        "mother": "Petronella Wauters"
    },
    {
        "name": "Lieven van Haverbeke",
        "sex": "m",
        "born": 1570,
        "died": 1636,
        "father": "Pauwels van Haverbeke",
        "mother": "Lievijne Jans"
    },
    {
        "name": "Joanna de Causmaecker",
        "sex": "f",
        "born": 1762,
        "died": 1807,
        "father": "Bernardus de Causmaecker",
        "mother": null
    },
    {
        "name": "Willem Haverbeke",
        "sex": "m",
        "born": 1668,
        "died": 1731,
        "father": "Lieven Haverbeke",
        "mother": "Elisabeth Hercke"
    },
    {
        "name": "Pieter Antone Haverbeke",
        "sex": "m",
        "born": 1753,
        "died": 1798,
        "father": "Jan Francies Haverbeke",
        "mother": "Petronella de Decker"
    },
    {
        "name": "Maria van Brussel",
        "sex": "f",
        "born": 1801,
        "died": 1834,
        "father": "Jan Frans van Brussel",
        "mother": "Joanna de Causmaecker"
    },
    {
        "name": "Angela Haverbeke",
        "sex": "f",
        "born": 1728,
        "died": 1734,
        "father": "Pieter Bernard Haverbeke",
        "mother": "Livina de Vrieze"
    },
    {
        "name": "Elisabeth Haverbeke",
        "sex": "f",
        "born": 1711,
        "died": 1754,
        "father": "Jan Haverbeke",
        "mother": "Maria de Rycke"
    },
    {
        "name": "Lievijne Jans", 
        "sex": "f", 
        "born": 1542, 
        "died": 1582, 
        "father": null, 
        "mother": null
    },
    {
        "name": "Bernardus de Causmaecker",
        "sex": "m",
        "born": 1721,
        "died": 1789,
        "father": "Lieven de Causmaecker",
        "mother": "Livina Haverbeke"
    },
    {
        "name": "Jacoba Lammens",
        "sex": "f",
        "born": 1699,
        "died": 1740,
        "father": "Lieven Lammens",
        "mother": "Livina de Vrieze"
    },
    {
        "name": "Pieter de Decker",
        "sex": "m",
        "born": 1705,
        "died": 1780,
        "father": "Joos de Decker",
        "mother": "Petronella van de Steene"
    },
    {
        "name": "Joanna de Pape",
        "sex": "f",
        "born": 1654,
        "died": 1723,
        "father": "Vincent de Pape",
        "mother": "Petronella Wauters"
    },
    {
        "name": "Daniel Haverbeke",
        "sex": "m",
        "born": 1652,
        "died": 1723,
        "father": "Lieven Haverbeke",
        "mother": "Elisabeth Hercke"
    },
    {
        "name": "Lieven Haverbeke",
        "sex": "m",
        "born": 1631,
        "died": 1676,
        "father": "Pieter Haverbeke",
        "mother": "Anna van Hecke"
    },
    {
        "name": "Martina de Pape",
        "sex": "f",
        "born": 1666,
        "died": 1727,
        "father": "Vincent de Pape",
        "mother": "Petronella Wauters"
    },
    {
        "name": "Jan Francies Haverbeke",
        "sex": "m",
        "born": 1725,
        "died": 1779,
        "father": "Pieter Bernard Haverbeke",
        "mother": "Livina de Vrieze"
    },
    {
        "name": "Maria Haverbeke",
        "sex": "m",
        "born": 1905,
        "died": 1997,
        "father": "Emile Haverbeke",
        "mother": "Emma de Milliano"
    },
    {
        "name": "Petronella de Decker",
        "sex": "f",
        "born": 1731,
        "died": 1781,
        "father": "Pieter de Decker",
        "mother": "Livina Haverbeke"
    },
    {
        "name": "Livina Sierens",
        "sex": "f",
        "born": 1761,
        "died": 1826,
        "father": "Jan Sierens",
        "mother": "Maria van Waes"
    },
    {
        "name": "Laurentia Haverbeke",
        "sex": "f",
        "born": 1710,
        "died": 1786,
        "father": "Jan Haverbeke",
        "mother": "Maria de Rycke"
    },
    {
        "name": "Carel Haverbeke",
        "sex": "m",
        "born": 1796,
        "died": 1837,
        "father": "Pieter Antone Haverbeke",
        "mother": "Livina Sierens"
    },
    {
        "name": "Elisabeth Hercke",
        "sex": "f",
        "born": 1632,
        "died": 1674,
        "father": "Willem Hercke",
        "mother": "Margriet de Brabander"
    },
    {
        "name": "Jan Haverbeke",
        "sex": "m",
        "born": 1671,
        "died": 1731,
        "father": "Lieven Haverbeke",
        "mother": "Elisabeth Hercke"
    },
    {
        "name": "Anna van Hecke",
        "sex": "f",
        "born": 1607,
        "died": 1670,
        "father": "Paschasius van Hecke",
        "mother": "Martijntken Beelaert"
    },
    {
        "name": "Maria Sturm",
        "sex": "f",
        "born": 1835,
        "died": 1917,
        "father": "Charles Sturm",
        "mother": "Seraphina Spelier"
    },
    {
        "name": "Jacobus Bernardus van Brussel",
        "sex": "m",
        "born": 1736,
        "died": 1809,
        "father": "Jan van Brussel",
        "mother": "Elisabeth Haverbeke"
    }
])

const ancestry = JSON.parse(data);

function average(array) {
    function plus(a, b) {
        return a + b;
    }
    return array.reduce(plus) / array.length;
}

var byName = {};
ancestry.forEach(function (person) {
    byName[person.name] = person;
});

let differentes = ancestry.filter(person => byName[person.mother] != null).map(
    function (person) {
        return person.born - byName[person.mother].born;
});

console.log(average(differentes).toFixed(1));


console.log('\nЗАДАНИЕ 12');
/*
12)	Историческая ожидаемая продолжительность жизни.
Мы считали, что только последнее поколение людей дожило до 90 лет.
Давайте рассмотрим этот феномен поподробнее.
Подсчитайте средний возраст людей для каждого из столетий.
Назначаем столетию людей, беря их год смерти, деля его на 100 и округляя: Math.ceil(person.died / 100).
 */

function getCenturyDict(array) {
    let result = {};
    array.forEach(function (person) {
        let cent = Math.ceil(person.died / 100);
        if (result[cent] === undefined) {
            result[cent] = [];
        }
        result[cent].push(person)
    });
    return result;
}

let centuries = getCenturyDict(ancestry);

for (let century in centuries) {
    console.log(century,  "->", average(centuries[century].map(person => person.died - person.born)).toFixed(1));
}


console.log('\nЗАДАНИЕ 13');
/* 13)	Every и some
У массивов есть ещё стандартные методы every и some.
Они принимают как аргумент некую функцию, которая, будучи вызванной с элементом массива в качестве аргумента, возвращает true или false.
Так же, как && возвращает true, только если выражения с обеих сторон оператора возвращают true, метод every возвращает true,
когда функция возвращает true для всех элементов массива.
Соответственно, some возвращает true, когда заданная функция возвращает true при работе хотя бы с одним из элементов массива.
Они не обрабатывают больше элементов, чем необходимо – например, если some получает true для первогоэлемента, он не обрабатывает оставшиеся.
Напишите функции every и some, которые работают так же, как эти методы, только принимают массив в качестве аргумента.
 */
function isStr(a) {
    if (typeof a === 'string') {
        return true
    } else {
        false
    }
}

function some(array, func) {
    for (let i = 0; i < array.length; i++) {
        if (func(array[i]))
            return true;
    }
    return false;
}

function every(array, func) {
    for (let i = 0; i < array.length; i++) {
        if (!func(array[i]))
            return false;
    }
    return true;
}

console.log(every([1, 2, 3], isStr));
console.log(every([1, 2, 3, "meow", NaN, 4], isStr));
console.log(some([1, 2, 3], isStr));
console.log(some([1, 2, 3, "meow", NaN, 4], isStr));