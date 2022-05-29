// 20.3.1
let vat n x = x * (1.0 + (float n) / 100.0)

// 20.3.2
let unvat n x = x / (1.0 + (float n) / 100.0)

// 20.3.3
let min f = 
    let rec loop f n =
        if (f n) = 0 then
            n
        else
            loop f (n+1)
    loop f 1
