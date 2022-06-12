// 40.1
let sum (p, xs) = 
    let rec loop xs sum =
        match xs with
        | [] -> sum
        | head :: tail when p head -> loop tail (sum + head)
        | head :: tail -> loop tail sum
    loop xs 0

// 40.2
// xs.[i] <= xs.[i+1]

// 40.2.1
let count (xs, n) =
    let rec loop xs cnt =
        match xs with
        | [] -> cnt
        | head :: tail when head > n -> cnt
        | head :: tail when head = n -> loop tail (cnt + 1)
        | head :: tail -> loop tail cnt
    loop xs 0

// 40.2.2
let insert (xs, n) = 
    let rec loop xs rev_start =
        match xs with
        | [] -> List.rev (n :: rev_start)
        | head :: tail when head >= n -> (List.rev rev_start) @ (n :: xs)
        | head :: tail -> loop tail (head :: rev_start)

    loop xs []
        

// 40.2.3
let intersect (xs1, xs2) =
    let rec loop (xs1, xs2) (r: int list) =
        match (xs1, xs2) with
        | ([], _) | (_, []) -> List.rev r
        | (h1::t1, h2::t2) when h1 < h2 -> loop (t1, h2::t2) r
        | (h1::t1, h2::t2) when h1 > h2 -> loop (h1::t1, t2) r
        | (h1::t1, h2::t2) when h1 = h2 -> loop (t1, t2) (h1::r)
        | _ -> failwith "Unexpected error"

    loop (xs1, xs2) []

// 40.2.4
let rec plus (xs1, xs2) = 
    let rec loop (xs1, xs2) (r: int list) =
        match (xs1, xs2) with
        | ([], []) -> List.rev r
        | ([], h2::t2) -> loop ([], t2) (h2::r)
        | (h1::t1, []) -> loop (t1, []) (h1::r)
        | (h1::t1, h2::t2) when h1 <= h2 -> loop (t1, h2::t2) (h1::r)
        | (h1::t1, h2::t2) when h1 >= h2 -> loop (h1::t1, t2) (h2::r)
        | _ -> failwith "Unexpected error"

    loop (xs1, xs2) []


// 40.2.5
let rec minus (xs1, xs2) =
    let rec loop (xs1, xs2) (r: int list) =
        match (xs1, xs2) with
        | ([], _) -> List.rev r
        | (xs1, []) -> List.rev ((List.rev xs1) @ r)
        | (h1::t1, h2::t2) when h1 < h2 -> loop (t1, h2::t2) (h1::r)
        | (h1::t1, h2::t2) when h1 > h2 -> loop (h1::t1, t2) r
        | (h1::t1, h2::t2) when h1 = h2 -> loop (t1, t2) r
        | _ -> failwith "Unexpected error"

    loop (xs1, xs2) []

// // 40.3.1
let smallest xs = 
    match xs with
    | [] -> None
    | head :: tail ->
        let rec loop xs min =
            match xs with
            | [] -> Some min
            | head :: tail when head < min -> loop tail head
            | head :: tail -> loop tail min
        loop tail head

// 40.3.2
let delete (n, xs) =
    let rec loop xs rev_xs =
        match xs with
        | [] -> List.rev rev_xs
        | head :: tail when head = n -> (List.rev rev_xs) @ tail
        | head :: tail -> loop tail (head :: rev_xs)
    loop xs []

// 40.3.3 (sort using smallest and delete)
let rec sort xs =
    let rec loop xs r =
        match smallest xs with
        | None -> List.rev r
        | Some n -> loop (delete (n, xs)) (n :: r)
    loop xs []

// 40.4
let revrev xss = 
    let rec loop xss r =
        match xss with
        | [] -> r
        | head :: tail -> loop tail ((List.rev head) :: r)
    loop xss []
