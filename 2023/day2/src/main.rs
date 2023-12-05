use std::collections::HashMap;
use std::fs;
use std::str;

fn part1(
    game: &mut std::iter::Skip<str::SplitAsciiWhitespace<'_>>,
    limits: &HashMap<&str, u8>,
) -> bool {
    let mut valid = true;
    while let Some(n) = game.next() {
        let num: u8 = n.parse().unwrap();
        let color = game
            .next()
            .unwrap()
            .trim_end_matches(|c: char| !c.is_alphanumeric());
        if num > limits[&color] {
            valid = false;
        }
    }
    return valid;
}

fn part2(game: &mut std::iter::Skip<str::SplitAsciiWhitespace<'_>>) -> u32 {
    let mut color_mins: HashMap<&str, u32> = HashMap::from([("red", 0), ("green", 0), ("blue", 0)]);

    while let Some(n) = game.next() {
        let num: u32 = n.parse().unwrap();
        let color = game
            .next()
            .unwrap()
            .trim_end_matches(|c: char| !c.is_alphanumeric());
        if color_mins[color] < num {
            color_mins.insert(color, num);
        }
    }

    return color_mins["red"] * color_mins["green"] * color_mins["blue"];
}

fn main() {
    let color_limits: HashMap<&str, u8> = HashMap::from([("red", 12), ("green", 13), ("blue", 14)]);

    let contents = fs::read_to_string("input.txt").expect("Should have been able to read the file");
    let mut sum_pt1 = 0;
    let mut sum_pt2 = 0;

    for line in contents.lines().enumerate() {
        if part1(
            &mut line.1.split_ascii_whitespace().skip(2).into_iter(),
            &color_limits,
        ) {
            sum_pt1 += line.0 + 1;
        }
        sum_pt2 += part2(&mut line.1.split_ascii_whitespace().skip(2).into_iter());
    }
    println!("Part 1: {}", sum_pt1);
    println!("Part 2: {}", sum_pt2);
}
