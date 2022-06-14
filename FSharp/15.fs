// 41.4.1 = List.filter via List.foldBack
let list_filter f xs =
    let filter_folder x acc = if f x then x::acc else acc
    List.foldBack filter_folder xs []

// 41.4.2
let sum (p, xs) =
    let sum_folder acc x = if p x then x + acc else acc
    List.fold sum_folder 0 xs

// 41.4.3
let revrev xss =
    let rev xs = xs |> List.fold (fun acc x -> x :: acc) []
    xss |> List.fold (fun acc xs -> (rev xs) :: acc) []
