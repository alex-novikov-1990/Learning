// 47.4.1
let f n = // imperative
    if n < 0 then
        failwith "n should not be less than 0"

    let i = ref 1
    let r = ref 1
    while ! i <= n do
        r := ! r * ! i
        i := ! i + 1
    ! r

// 47.4.2
let fibo n = // imperative
    if n < 0 then
        failwith "n should not be less than 0"
    elif n = 0 then
        0
    else
        let i = ref 1
        let prev = ref 0
        let result = ref 1
        while ! i < n do
            let prev_result = ! result
            result := ! result + ! prev
            prev := prev_result
            i := ! i + 1
        ! result
