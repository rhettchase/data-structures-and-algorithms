module.exports = function (wallaby) {
  return {
    files: ["challenges-06.test.js", "jest.config.js"],

    runAllTestsWhenNoAffectedTests: true,

    tests: ["challenges-06.test.js"],

    testFramework: "jest",

    env: {
      type: "node",
      runner: "node",
    },

    setup: function (wallaby) {
      // Additional setup if needed
    },
  };
};
