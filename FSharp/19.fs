// 48.4.1
let rec fibo1 n n1 n2 =
    match n with
    | 0 -> n2
    | 1 -> n1
    | n -> fibo1 (n-1) (n1+n2) n1

// 48.4.2
let rec fibo2 n c =
    let c0 = c 0
    let c1 = c 1
    match n with
    | 0 -> c0
    | 1 -> c1
    | n -> fibo2 (n-1) (fun i -> if i = 0 then c1 else c0 + c1)

// 48.4.3
let rec bigList n k =
    let acc = k []
    if n=0 then acc
    else bigList (n-1) (fun _ -> 1::acc)
