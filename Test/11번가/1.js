// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(A) {
    // write your code in JavaScript (Node.js 8.9.4)
    let flag = false;

    var getCombinations = (arr, j) => {
        const comb = [...Array(j)].fill(0);
        backTracking(comb, arr, j, 0, 0);
        return;
    }

    const backTracking = (comb, arr, j, idx, start) => {
        if (idx == j) {
            let and = comb.reduce((a,b) => {
                return a & b;
            },1);

            if (and > 0) {
                flag = true;
            }
            return;
        }
        for (let i=start; i <arr.length; i++) {
            comb[idx] = arr[i];
            backTracking(comb, arr, j, idx+1, i+1);
        if (flag) {
            return;
        }
        }
    };
    // AA = [13,7,3];

    // console.log(AA.reduce((a,b) => {
    //             return a & b;
    //         }));
    for (let i=A.length; i>0; i--) {
        getCombinations(A,i);
        if (flag) {
            return i
        }
    }
    return A.length;
}
