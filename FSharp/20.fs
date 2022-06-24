// 49.5.1
let even_seq = Seq.initInfinite (fun i -> 2*i + 2)

// 49.5.2
let fac_seq = Seq.initInfinite (fun i ->
    let rec fac = function
      | 0 -> 1
      | n -> n * fac (n-1)

    fac i
)

// 49.5.3
let seq_seq = Seq.initInfinite (fun i -> (i + 1)/2*(((i + 1) % 2)*2 - 1))
