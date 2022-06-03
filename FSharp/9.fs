// 23.4.1
// (g, s, c) is (0..max_int,0..19,0..11) or (min_int..0,-19..0,-11..0)
let (.+.) (g_x, s_x, c_x) (g_y, s_y, c_y) =
    let g = g_x + g_y
    // hack to tackle with int overflow
    let g_part = if g > 0 then +1 elif g < 0 then -1 else 0
    // easyest way to properly support (1,0,0) .+. (0,0,-1)
    let r = 240 * (g_part) + 12 * (s_x + s_y) + c_x + c_y
    (g - g_part + r / 240, (r / 12) % 20, r % 12)

let (.-.) x (g_y, s_y, c_y) = x .+. (-g_y, -s_y, -c_y)

// 23.4.2
// complex numbers
let (.+) (x_r: float, x_i: float) (y_r, y_i) = (x_r + y_r, x_i + y_i)
let (.-) (x_r: float, x_i: float) (y_r, y_i) = (x_r - y_r, x_i - y_i)
let (.*) (x_r: float, x_i: float) (y_r, y_i) = (x_r * y_r - x_i * y_i, x_i * y_r + x_r * y_i)
let (./) (x: float * float) (y_r, y_i) =
  let y_mod_sqr = y_r * y_r + y_i * y_i
  x .* (y_r / y_mod_sqr, -y_i / y_mod_sqr)
