use std::fs;

fn part1(winning_nums: &Vec<&str>, nums: &Vec<&str>) -> u32 {
    let mut total: u32 = 0;
    for num in nums {
        if winning_nums.contains(num) {
            if total == 0 {
                total = 1;
            } else {
                total *= 2;
            }
        }
    }
    total
}

fn part2(winning_nums: &Vec<&str>, nums: &Vec<&str>) -> u8 {
    let mut matches: u8 = 0;
    for num in nums {
        if winning_nums.contains(num) {
            matches += 1;
        }
    }
    matches
}

fn main() {
    let contents = fs::read_to_string("input.txt").expect("Should have been able to read the file");
    let mut part1_sum: u32 = 0;
    let mut card_copies: Vec<u32> = vec![1; 203];

    let mut card_idx;

    for line in contents.lines().enumerate() {
        card_idx = line.0;

        for card in line
            .1
            .split(':')
            .collect::<Vec<&str>>()
            .iter()
            .map(|c| c.trim())
            .skip(1)
            .step_by(2)
        {
            let tmp = card.split('|').map(|s| s.trim()).collect::<Vec<&str>>();
            let winning_numbers = tmp[0].split_ascii_whitespace().collect::<Vec<&str>>();
            let card_numbers = tmp[1].split_ascii_whitespace().collect::<Vec<&str>>();

            part1_sum += part1(&winning_numbers, &card_numbers);
            let copies_to_be_made = card_copies[card_idx];

            for copy in card_idx + 1
                ..card_idx
                    + TryInto::<usize>::try_into(part2(&winning_numbers, &card_numbers)).unwrap()
                    + 1
            {
                card_copies[copy] += copies_to_be_made;
            }
        }
    }
    println!("Part 1: {}", &part1_sum);
    println!("Part 2: {}", &card_copies.iter().sum::<u32>())
}
