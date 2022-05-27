// 17.1
let rec pow (s, n) = 
    // powTail is for tail recursion
    let rec powTail s n acc = if n <= 0 then acc else powTail s (n - 1) (acc + s)
    powTail s n ""

// 17.2
let rec isIthChar(s, n, c) = n >= 0 && n < (String.length s) && s.[n] = c

// 17.3
let rec occFromIth(s, n, c) = 
    // occFromIthTail is for tail recursion
    let rec occFromIthTail s n c acc =
        if n >= (String.length s) then
            acc
        else
            let inc = if s.[n] = c then 1 else 0
            occFromIthTail s (n + 1) c (acc + inc)
    occFromIthTail s n c 0