use std::collections::HashMap;
use std::fs;

fn get_adjacent_points(start: (u16, u16), len: u16, bounds: (u16, u16)) -> Vec<(u16, u16)> {
    let mut pts: Vec<(u16, u16)> = Vec::new();
    let y = start.1;

    for i in 0..len {
        let x = start.0 + i;
        // left
        if x >= 1 {
            pts.push((x - 1, start.1));
        }

        // top left
        if x >= 1 && y >= 1 {
            pts.push((x - 1, y - 1))
        }

        // top
        if y >= 1 {
            pts.push((x, y - 1));
        }

        // top right
        if x + 1 < bounds.0 && y >= 1 {
            pts.push((x + 1, y - 1));
        }

        // right
        if x + 1 < bounds.0 {
            pts.push((x + 1, y));
        }

        // bottom right
        if x + 1 < bounds.0 && y + 1 < bounds.1 {
            pts.push((x + 1, y + 1));
        }

        // bottom
        if y + 1 < bounds.1 {
            pts.push((x, y + 1));
        }

        if y + 1 < bounds.1 && x >= 1 {
            pts.push((x - 1, y + 1));
        }
    }

    return pts;
}

fn main() {
    let contents = fs::read_to_string("input.txt").expect("Should have been able to read the file");

    let mut matrix: Vec<Vec<char>> = Vec::new();
    let mut nums: Vec<(u16, Vec<(u16, u16)>)> = Vec::new();

    for line in contents.lines().enumerate() {
        let mut str_digit = String::new();
        matrix.push(line.1.chars().collect::<Vec<char>>());

        for c in line.1.chars().enumerate() {
            if c.1 == '*' {}
            if c.1.is_ascii_digit() {
                str_digit.push_str(&c.1.to_string());
            } else {
                if str_digit.len() > 0 {
                    nums.push((
                        str_digit.parse().unwrap(),
                        get_adjacent_points(
                            (
                                TryInto::<u16>::try_into(c.0 - str_digit.len()).unwrap(),
                                line.0.try_into().unwrap(),
                            ),
                            str_digit.len().try_into().unwrap(),
                            (
                                line.1.len().try_into().unwrap(),
                                contents.lines().count().try_into().unwrap(),
                            ),
                        ),
                    ))
                }
                str_digit.clear();
            }
        }

        if str_digit.len() > 0 {
            nums.push((
                str_digit.parse().unwrap(),
                get_adjacent_points(
                    (
                        TryInto::<u16>::try_into(line.1.len() - str_digit.len()).unwrap(),
                        line.0.try_into().unwrap(),
                    ),
                    str_digit.len().try_into().unwrap(),
                    (
                        line.1.len().try_into().unwrap(),
                        contents.lines().count().try_into().unwrap(),
                    ),
                ),
            ))
        }
        str_digit.clear();
    }

    let mut part1_sum: u32 = 0;
    let mut part2_sum: u32 = 0;
    let mut gears: HashMap<(u16, u16), Vec<u32>> = HashMap::new();
    let mut part_added = false;
    let mut gear_added = false;
    for num in nums {
        for pt in num.1 {
            let c = matrix[usize::from(pt.1)][usize::from(pt.0)];
            if !c.is_digit(10) && c != '.' && !part_added {
                println!("{}", num.0);
                part1_sum += TryInto::<u32>::try_into(num.0).unwrap();
                part_added = true;
            }

            if c == '*' && !gear_added {
                if !gears.contains_key(&pt) {
                    gears.insert(pt, Vec::new());
                }
                gears
                    .get_mut(&pt)
                    .unwrap()
                    .push(TryInto::<u32>::try_into(num.0).unwrap());
                gear_added = true;
            }
        }
        part_added = false;
        gear_added = false;
    }

    for gear in gears {
        if gear.1.len() > 1 {
            // println!("Gear at ({}, {}) -> {:?}", gear.0 .0, gear.0 .1, gear.1);
            part2_sum += gear.1[0] * gear.1[1];
        }
    }

    println!("Part 1: {}", part1_sum);
    println!("Part 2: {}", part2_sum);
}
