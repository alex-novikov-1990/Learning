type TimeOfDay = { 
    hours: int;   // 0..11
    minutes: int; // 0..59
    f: string;    // "AM"/"PM"
}

let (.>.) (x: TimeOfDay) (y: TimeOfDay) = x.f > y.f || x > y