type TimeOfDay = { 
    hours: int;   // 0..11
    minutes: int; // 0..59
    f: string;    // "AM"/"PM"
}

let (.>.) (x: TimeOfDay) (y: TimeOfDay) = if x.f <> y.f then x.f > y.f else x > y