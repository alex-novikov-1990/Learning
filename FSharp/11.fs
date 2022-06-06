type F =
  | AM
  | PM

type TimeOfDay = { hours : int; minutes : int; f: F }

let (.>.) (x: TimeOfDay) (y: TimeOfDay) = if x.f <> y.f then x.f > y.f else x > y
