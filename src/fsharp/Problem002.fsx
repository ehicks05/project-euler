﻿// Each new term in the Fibonacci sequence is generated by adding the previous two terms.
// By starting with 1 and 2, the first 10 terms will be:
//
// 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
//
// By considering the terms in the Fibonacci sequence whose values do not exceed four million,
// find the sum of the even-valued terms.

let fibonacciUnfolder (f1, f2) =
    // return value and new threaded state
    let fNext = f1 + f2
    let newState = (f2, fNext)
    // f1 will be in the generated sequence
    Some(f1, newState)

let fibonacci = Seq.unfold fibonacciUnfolder (1, 1)

fibonacci
    |> Seq.takeWhile (fun x -> x <= 4_000_000)
    |> Seq.filter (fun x -> x % 2 = 0)
    |> Seq.sum