let curry (f:(int * int -> int)) x y = f(x,y)

let uncurry (f:(int -> int -> int)) (x, y) = f x y
