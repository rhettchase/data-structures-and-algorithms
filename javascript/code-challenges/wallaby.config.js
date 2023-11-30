module.exports = function (wallaby) {
  return {
    files: [
      'challenges-03.test.js',
      'jest.config.js',
    ],

    runAllTestsWhenNoAffectedTests: true,

    tests: [
      'challenges-03.test.js',
    ],

    testFramework: 'jest',

    env: {
      type: 'node',
      runner: 'node',
    },

    setup: function (wallaby) {
      // Additional setup if needed
    },
  };
};
