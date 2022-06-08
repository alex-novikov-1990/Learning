let buildList head tail step =
    let cmp = if step > 0 then (>=) else (<=)
    let rec loop list i =
        if cmp i head then
            loop (i :: list) (i - step)
        else
            list
    loop [] tail

// 34.1
let upto n = buildList 1 n 1 // [ 1..n ]

// 34.2
let dnto n = buildList n 1 -1 // [n..(-1)..1]

// 34.3
let rec evenn n = buildList 0 (2 * n - 2) 2 // [ 0..2..(2*n-2) ]
