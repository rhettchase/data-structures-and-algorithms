"use strict";

/* ------------------------------------------------------------------------------------------------
These objects and arrays are global and will be used for each assignment. DO NOT ALTER THEM
------------------------------------------------------------------------------------------------ */

const people = ["Kookla", "Fran", "Ollie"];

const stuff = {
  tv: "huge",
  radio: "old",
  toys: 57,
  toothbrush: "frayed",
  cars: ["Toyota", "Mazda"],
};

/* ------------------------------------------------------------------------------------------------
CHALLENGE 1

In the addPeople function, use spread and destructuring assignments to:
  - Create a new array called newPeople as a copy of the people array
  - Add a person named 'Odie' added to the beginning of the array
  - Add another one named 'Garfield' added to the end of the array

Prove that the original people array is unchanged

------------------------------------------------------------------------------------------------ */

const addPeople = (arr) => {
  console.log(arr);
  let newPeople = ["Odie", ...arr, "Garfield"]; // using destructuring
  // newPeople.push('Garfield');
  // newPeople.unshift('Odie');
  return newPeople;
};

/* ------------------------------------------------------------------------------------------------
CHALLENGE 2

In the setSate function, use spread and destructuring assignments to:
  - Create and return a state object with 2 keys:
    people, which will contain a copy of the people array
    stuff, which will contain a copy of the stuff object

Ensure that the original people array and stuff objects are unchanged

------------------------------------------------------------------------------------------------ */

const setState = (arr, obj) => {
  const newState = {
    people: [...arr],
    stuff: { ...obj },
  };
  return newState;
};

/* ------------------------------------------------------------------------------------------------
CHALLENGE 3

In the newState function, use only spread and destructuring assignments to:
  - Create and return a state object with 2 keys:
    people, which will contain a copy of the people array
    stuff, which will contain a copy of the stuff object
    Add a new car ("Ford") added to the list of cars
    Change the toothbrush from "frayed" to "brand new"
    Add 1 to the number of toys

Ensure that the original people array and stuff objects are unchanged

------------------------------------------------------------------------------------------------ */

const newState = (arr, obj) => {
  const newPeople = [...arr];
  const newStuff = { ...obj };
  newStuff.cars = [...newStuff.cars, "Ford"]; // Add a new car ("Ford") to the list of cars
  newStuff.toothbrush = "brand new";
  newStuff.toys += 1;

  const newState = {
    people: newPeople,
    stuff: newStuff,
  };
  return newState;
};

const updatedState = newState(people, stuff);

console.log("Original people array:", people);
console.log("Original stuff object:", stuff);
console.log("Updated state:", updatedState);

/* ------------------------------------------------------------------------------------------------
TESTS

All the code below will verify that your functions are working to solve the challenges.

DO NOT CHANGE any of the below code.

Run your tests from the console: jest challenges-03.test.js
------------------------------------------------------------------------------------------------ */

describe("Testing challenge 1", () => {
  test("It should return a copy of the people array with 2 new values", () => {
    const orig = ["Kookla", "Fran", "Ollie"];
    const expected = ["Odie", "Kookla", "Fran", "Ollie", "Garfield"];
    const copy = addPeople(people);
    expect(copy).toStrictEqual(expected);
    expect(orig).toStrictEqual(people);
  });
});

describe("Testing challenge 2", () => {
  test("It should return a state object with 2 keys", () => {
    const originalPeople = ["Kookla", "Fran", "Ollie"];
    const originalStuff = {
      tv: "huge",
      radio: "old",
      toys: 57,
      toothbrush: "frayed",
      cars: ["Toyota", "Mazda"],
    };
    const expected = { people: originalPeople, stuff: originalStuff };
    const copy = setState(people, stuff);
    expect(copy).toStrictEqual(expected);
    expect(originalPeople).toStrictEqual(people);
    expect(originalStuff).toStrictEqual(stuff);
  });
});

describe("Testing challenge 3", () => {
  test("It should return a state object with 2 keys and new values", () => {
    const originalPeople = ["Kookla", "Fran", "Ollie"];
    const originalStuff = {
      tv: "huge",
      radio: "old",
      toys: 57,
      toothbrush: "frayed",
      cars: ["Toyota", "Mazda"],
    };
    const expected = {
      people: ["Kookla", "Fran", "Ollie"],
      stuff: {
        tv: "huge",
        radio: "old",
        toys: 58,
        toothbrush: "brand new",
        cars: ["Toyota", "Mazda", "Ford"],
      },
    };
    const copy = newState(people, stuff);
    expect(copy).toStrictEqual(expected);
    expect(originalPeople).toStrictEqual(people);
    expect(originalStuff).toStrictEqual(stuff);
  });
});
