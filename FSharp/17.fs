// 43.3
let try_find key m = // Map.tryFind
    if Map.containsKey key m then
        Some(Map.find key m)
    else
        None
