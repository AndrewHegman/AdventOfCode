use std::fs;

fn main() {
    let contents = fs::read_to_string("input.txt").expect("Should have been able to read the file");
    let mut part1_sum: u16 = 0;
    let mut part2_sum: u16 = 0;

    let part2_nums = [
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
        ("one", "1"),
        ("two", "2"),
        ("three", "3"),
        ("four", "4"),
        ("five", "5"),
        ("six", "6"),
        ("seven", "7"),
        ("eight", "8"),
        ("nine", "9"),
    ];

    for line in contents.lines() {
        // **************** BEGIN PART 1 ****************
        part1_sum += [
            line.chars().collect::<Vec<char>>()[line.find(char::is_numeric).unwrap()].to_string(),
            line.chars().collect::<Vec<char>>()[line.rfind(char::is_numeric).unwrap()].to_string(),
        ]
        .join("")
        .parse::<u16>()
        .unwrap();
        // **********************************************

        // **************** BEGIN PART 2 ****************
        let mut num1_pos = 10000;
        let mut num1 = String::new();
        let mut num2_pos = 0;
        let mut num2 = String::new();

        for n in part2_nums {
            if let Some(p) = line.find(n.0) {
                if p < num1_pos {
                    num1_pos = p;
                    num1 = n.1.to_string();
                }
            }

            if let Some(p) = line.rfind(n.0) {
                if p >= num2_pos {
                    num2_pos = p;
                    num2 = n.1.to_string();
                }
            }
        }
        part2_sum += vec![num1.to_string(), num2.to_string()]
            .join("")
            .parse::<u16>()
            .unwrap();
    }
    // **********************************************

    println!("Part 1: {}", part1_sum);
    println!("Part 2: {}", part2_sum);
}
