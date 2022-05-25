// 16.1
let notDivisible (n, m) = m % n = 0 // true if n is divisor of m

// 16.2
let prime n =
    match n with
    | 2 | 3 -> true
    | _ when n < 2 || n % 2 = 0 -> false
    | _ ->
      let rec loop i =
        if n % i = 0 then
          false
        elif i * i > n then
          true
        else
          loop (i + 2)
      loop 3
