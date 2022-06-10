// 39.1
let rec rmodd l = 
    match l with
    | [] -> []
    | [_] -> []
    | _ :: head2 :: tail -> head2 :: (rmodd tail)

// 39.2
let rec del_even l = 
    match l with
    | [] -> []
    | head :: tail when head % 2 = 0 -> del_even tail
    | head :: tail -> head :: del_even tail

// 39.3
let multiplicity x xs =
    let rec loop xs n =
        match xs with
        | [] -> n
        | head :: tail when head = x -> loop tail (n + 1)
        | head :: tail -> loop tail n
    loop xs 0
        

// 39.4
let split l =
    let rec loop l l1 l2 =
        match l with
        | [] -> (List.rev l1, List.rev l2)
        | [h1] -> loop [] (h1 :: l1) l2
        | h1::h2::tail -> loop tail (h1 :: l1) (h2 :: l2)
    loop l [] []

exception NonEqualLists

// 39.5
let zip (xs1,xs2) =
    let rec loop xs1 xs2 r =
        match xs1, xs2 with
        | [], [] -> List.rev r
        | _, [] | [], _ -> raise NonEqualLists
        | h1::t1, h2::t2 -> loop t1 t2 ((h1,h2)::r)
    loop xs1 xs2 []