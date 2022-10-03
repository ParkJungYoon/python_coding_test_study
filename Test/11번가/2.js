// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(N, K) {
  // write your code in JavaScript (Node.js 8.9.4)
  // 정답 여부를 체크하는 함수
  let flag = false;
  // const getCombinations = (arr, selectNumber) => {
  //     const result = [];
  //     if (selectNumber === 1) return arr.map(v => [value]);
  //     arr.forEach((f,idx,o) => {
  //         const r = o.slice(idx+1);
  //         const combi = getCombinations(r,selectNumber-1);
  //         const att = combi.map(combi => [f,...combi]);
  //         result.push(...att)
  //     });
  //     return result;
  // }
  var getCombinations = (arr, j, K) => {
    const result = [];
    const comb = [...Array(j)].fill(0);
    backTracking(result, comb, arr, j, 0, 0, K);
    return;
  };
  const backTracking = (result, comb, arr, j, idx, start, K) => {
    if (idx === j) {
      let sum = comb.reduce((a, b) => {
        return a + b;
      }, 0);
      if (sum == K) {
        flag = true;
      }
      return;
    }

    for (let i = start; i < arr.length; i++) {
      comb[idx] = arr[i];
      backTracking(result, comb, arr, j, idx + 1, i + 1, K);
      if (flag) {
        return;
      }
    }
  };
  if (N >= K) {
    return 1;
  } else {
    const getList = [];
    for (i = 1; i <= N; i++) {
      getList.push(i);
    }
    for (let i = 2; i <= N; i++) {
      const getResult = getCombinations(getList, i, K);
      if (flag) {
        return i;
      }
    }
    return -1;
  }
}
