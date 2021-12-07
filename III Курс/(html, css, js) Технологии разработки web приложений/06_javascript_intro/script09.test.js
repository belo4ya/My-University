import {deepEqual} from "./script09.js";

const testObj = {name: 'Misha', order: {price: 20}};
const testObjPropertiesInDifferentOrder = {
  order: {price: 20},
  name: 'Misha',
};
const testObjExtraNullProperty = {
  name: 'Misha',
  order: {price: 20},
  extraField: null,
};
const testObjChangedProperty = {
  order: {price: 20},
  name: 'Petya',
};
const testObjChangedPropertyInNestedObj = {
  name: 'Misha',
  order: {price: 1000},
};
const testObjExtraNullPropertyInNestedObj = {
  name: 'Misha',
  order: {price: 20, extraField: null},
};

const deepObject = {
  name: 'Misha',
  order: {
    price: 20,
    count: 1,
    taxes: {
      vat: {name: 'vat', amount: {uah: 10, usd: 0.37}},
    },
    total: {
      withoutTaxes: {uah: 20, usd: 0.74},
      withTaxes: {vat: {uah: 30, usd: 1.11}},
    },
  }
};

const deepObjectPropsInDifferentOrder = {
  name: 'Misha',
  order: {
    count: 1,
    price: 20,
    taxes: {
      vat: {name: 'vat', amount: {uah: 10, usd: 0.37}},
    },
    total: {
      withTaxes: {vat: {uah: 30, usd: 1.11}},
      withoutTaxes: {usd: 0.74, uah: 20},
    },
  }
};

const deepObjectExtraNullProperty = {
  name: 'Misha',
  order: {
    price: 20,
    count: 1,
    taxes: {
      vat: {name: 'vat', amount: {uah: 10, usd: 0.37}},
    },
    total: {
      withoutTaxes: {uah: 20, usd: 0.74},
      withTaxes: {vat: {uah: 30, usd: 1.11, eur: null}},
    },
  }
};

const deepObjectChangedProperty = {
  name: 'Misha',
  order: {
    price: 20,
    count: 1,
    taxes: {
      vat: {name: 'vat', amount: {uah: 10, usd: 0.37}},
    },
    total: {
      withoutTaxes: {uah: 20, usd: 575},
      withTaxes: {vat: {uah: 30, usd: 1.11, eur: null}},
    },
  }
};

test('5 and 5 should be equal', () => {
  expect(deepEqual(5, 5))
    .toBe(true);
});

test('null and null should be equal', () => {
  expect(deepEqual(null, null))
    .toBe(true);
});

test(
  `Objects with same properties but in different order should be equal
  input:
    - a = ${JSON.stringify(testObj)},
    - b = ${JSON.stringify(testObjPropertiesInDifferentOrder)}`,
  () => {
    expect(deepEqual(testObj, testObjPropertiesInDifferentOrder))
      .toBe(true);
  });

test(
  `Nested Objects with same properties but in different order should be equal
  input:
    - a = ${JSON.stringify({test: testObj})},
    - b = ${JSON.stringify({test: testObjPropertiesInDifferentOrder})}`,
  () => {
    expect(deepEqual(
      {test: testObj},
      {test: testObjPropertiesInDifferentOrder}
    ))
      .toBe(true);
  });

test('5 and 6 should NOT be equal', () => {
  expect(deepEqual(5, 6))
    .toBe(false);
});

test('0 and false should NOT be equal', () => {
  expect(deepEqual(0, false))
    .toBe(false);
});

test('null and 5 should NOT be equal', () => {
  expect(deepEqual(null, 5))
    .toBe(false);
});

test(
  `Object and null should NOT be equal
  input:
    - a = ${JSON.stringify(testObj)},
    - b = null`,
  () => {
    expect(deepEqual(testObj, null))
      .toBe(false);
  });

test(
  `Object and its copy with extra null property should not be equal
  input:
    - a = ${JSON.stringify(testObj)},
    - b = ${JSON.stringify(testObjExtraNullProperty)}`,
  () => {
    expect(deepEqual(testObj, testObjExtraNullProperty))
      .toBe(false);
  });

test(
  `Object and its copy with changed property should not be equal
  input:
    - a = ${JSON.stringify(testObj)},
    - b = ${JSON.stringify(testObjChangedProperty)}`,
  () => {
    expect(deepEqual(testObj, testObjChangedProperty))
      .toBe(false);
  });

test(
  `Object and its copy with changed nested property should not be equal
  input:
    - a = ${JSON.stringify(testObj)},
    - b = ${JSON.stringify(testObjChangedPropertyInNestedObj)}`,
  () => {
    expect(deepEqual(
      testObj,
      testObjChangedPropertyInNestedObj
    ))
      .toBe(false);
  });

test(
  `Object and its copy with extra null property in nested object
   shouldn't be equal
   input:
    - a = ${JSON.stringify(testObj)},
    - b = ${JSON.stringify(testObjExtraNullPropertyInNestedObj)}`,
  () => {
    expect(deepEqual(
      testObj,
      testObjExtraNullPropertyInNestedObj
    ))
      .toBe(false);
  });

test(
  `Deep object and its copy with extra null property shouldn't be equal
   input:
    - a = ${JSON.stringify(deepObject)},
    - b = ${JSON.stringify(deepObjectExtraNullProperty)}`,
  () => {
    expect(deepEqual(
      deepObject,
      deepObjectExtraNullProperty
    ))
      .toBe(false);
  });

test(
  `Deep object and its copy with properties in different order should be equal
   input:
    - a = ${JSON.stringify(deepObject)},
    - b = ${JSON.stringify(deepObjectPropsInDifferentOrder)}`,
  () => {
    expect(deepEqual(
      deepObject,
      deepObjectPropsInDifferentOrder
    ))
      .toBe(true);
  });

test(
  `Deep object and its copy with changed property shouldn't be equal
   input:
    - a = ${JSON.stringify(deepObject)},
    - b = ${JSON.stringify(deepObjectChangedProperty)}`,
  () => {
    expect(deepEqual(
      deepObject,
      deepObjectChangedProperty
    ))
      .toBe(false);
  });
