// 50.2.1
let fac_seq = seq {
    yield 1
    let mutable i = 1
    let mutable v = 1
    while true do
        v <- v * i
        i <- i + 1
        yield v
}

// 50.2.2
let seq_seq = seq {
    yield 0
    let mutable v = 1
    while true do
        yield -v
        yield v
        v <- v + 1
}