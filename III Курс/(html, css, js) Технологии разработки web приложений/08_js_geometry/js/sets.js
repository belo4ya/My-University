export const intersection = (setA, setB) => {
    let smallerSet = setA.size > setB.size ? setB : setA;
    let largerSet = setA.size > setB.size ? setA : setB;
    return new Set([...smallerSet].filter(element => largerSet.has(element)))
}

export const union = (setA, setB) => {
    return new Set([...setA, ...setB]);
}
