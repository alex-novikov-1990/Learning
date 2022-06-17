// 42.3
let rec allSubsets n k =
    if k <= 0 || n <= k then
        set [set []]
    else if k <= n/2 then
        // TODO: ensure best choice of internal types
        let rec combinations i k =
            if k > 0 then
                [i..(n-k+1)]
                |> List.map (fun x ->
                    (combinations (x+1) (k-1))
                    |> List.map (fun l -> x::l))
                |> List.concat
            else
                [[]]

        combinations 1 k
        |> List.map (fun x -> set x)
        |> set
    else
        allSubsets n (n - k)
        |> Set.map (Set.difference (set [1..n]))
