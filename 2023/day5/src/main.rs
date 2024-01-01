use std::fs;

struct Range {
    start: i64,
    end: i64,
    is_mapped: bool,
}

fn convert_value(map: &Vec<Vec<i64>>, value: &i64) -> i64 {
    for range in map {
        if value >= &range[1] && value <= &(range[1] + range[2]) {
            return &range[0] + (value - range[1]);
        }
    }
    *value
}

fn clean_up(range: &mut Vec<Range>) {
    let mut idx_to_delete: Vec<usize> = Vec::new();
    for i in 0..range.len() {
        for j in 0..range.len() {
            if i == j {
                continue;
            }

            let idx = if range[i].is_mapped { j } else { i };
            if range[i].start <= range[j].end
                && range[i].end >= range[j].start
                && !idx_to_delete.contains(&idx)
            {
                idx_to_delete.push(idx);
            }
        }
    }

    let mut num_deleted = 0;
    idx_to_delete.sort();
    for idx in idx_to_delete {
        range.remove(idx - num_deleted);
        num_deleted += 1;
    }
}

fn convert_value_range(map: &Vec<Vec<i64>>, value: &Range) -> Vec<Range> {
    let mut new_value: Vec<Range> = Vec::new();
    let mut created_new_range = false;

    for range in map {
        let src_start = range[1];
        let src_end = range[1] + range[2] - 1;

        let dst_start = range[0];
        let dst_end = range[0] + range[2] - 1;

        let value_start = value.start;
        let value_end = value.end;

        if value_start >= src_start && value_end <= src_end {
            // value range fits completely inside destination range
            let diff: i64 = (dst_start - src_start).try_into().unwrap();
            new_value.push(Range {
                start: value_start + diff,
                end: value_end + diff,
                is_mapped: true,
            });
            created_new_range = true;
            break;
        }

        if value_start < src_start {
            // value range STARTS BEFORE src range STARTS and...
            if value_end <= src_start {
                // ...value range ENDS BEFORE src range STARTS
                if value_end == src_start {
                    new_value.push(Range {
                        start: value_start,
                        end: value_end,
                        is_mapped: false,
                    });
                    new_value.push(Range {
                        start: dst_end,
                        end: dst_end,
                        is_mapped: true,
                    });
                    println!("Good thing I checked for this");
                    created_new_range = true;
                    break;
                } else {
                    // new_value.push([value_start, value_end]);
                    // created_new_range = true;
                    // break;
                }
            } else if value_end <= src_end {
                new_value.push(Range {
                    start: value_start,
                    end: src_start,
                    is_mapped: false,
                });
                new_value.push(Range {
                    start: dst_start,
                    end: dst_end - (src_end - value_end),
                    is_mapped: true,
                });
                created_new_range = true;
                // break;
            } else {
                // ...value range ENDS AFTER src range ENDS
                new_value.push(Range {
                    start: value_start,
                    end: value_end,
                    is_mapped: false,
                });
                new_value.push(Range {
                    start: dst_start,
                    end: dst_end,
                    is_mapped: true,
                });
                created_new_range = true;
                break;
            }
        } else {
            // value range STARTS AFTER src range STARTS and...
            if value_start > src_end {
                // value range STARTS AFTER src range ENDS
                // new_value.push([value_start, value_end});
                // created_new_range = true;
                // break;
            } else if value_end > src_end {
                // value range STARTS BEFORE src range ENDS and value range ENDS after src range ENDS
                let diff: i64 = (dst_start - src_start).try_into().unwrap();
                // new_value.push([dst_start + (value_start - src_start), dst_end});

                new_value.push(Range {
                    start: src_end + 1,
                    end: value_end,
                    is_mapped: false,
                });

                new_value.push(Range {
                    start: value_start + diff,
                    end: dst_end,
                    is_mapped: true,
                });

                if new_value.iter().any(|x| x.start == value_start) {
                    let idx = new_value.iter().position(|x| x.start == value_start);
                    new_value.remove(idx.unwrap());
                }
                created_new_range = true;
                // break;
            }
        }
    }

    if !created_new_range {
        return vec![Range {
            start: value.start,
            end: value.end,
            is_mapped: false,
        }];
    }
    new_value
}

fn main() {
    let contents = fs::read_to_string("input.txt").expect("Should have been able to read the file");

    let mut map: Vec<Vec<i64>> = Vec::new();
    let mut seeds_pt1 = Vec::new();
    let mut seeds_pt2: Vec<Range> = Vec::new();

    for line in contents.lines().enumerate() {
        if line.0 == 0 {
            seeds_pt1 = line.1.split(':').collect::<Vec<&str>>()[1]
                .trim()
                .split_ascii_whitespace()
                .map(|c: &str| c.parse::<i64>().unwrap())
                .collect::<Vec<i64>>();
            break;
        }
    }

    for s in (0..seeds_pt1.len()).step_by(2) {
        seeds_pt2.push(Range {
            start: seeds_pt1[s],
            end: seeds_pt1[s] + seeds_pt1[s + 1] - 1,
            is_mapped: false,
        });
    }

    for line in contents.lines().enumerate() {
        if line.1 == "" {
            if map.len() > 0 {
                for i in 0..seeds_pt1.len() {
                    seeds_pt1[i] = convert_value(&map, &seeds_pt1[i]);
                }
                let mut tmp_seeds_pt2: Vec<Range> = Vec::new();
                for i in 0..seeds_pt2.len() {
                    for v in convert_value_range(&map, &seeds_pt2[i]) {
                        tmp_seeds_pt2.push(v);
                    }
                }
                clean_up(&mut tmp_seeds_pt2);
                seeds_pt2 = tmp_seeds_pt2;

                map.clear();
            }
            continue;
        }

        if line.1.as_bytes()[0].is_ascii_alphabetic() {
            continue;
        }

        map.push(
            line.1
                .split_ascii_whitespace()
                .map(|c: &str| c.parse::<i64>().unwrap())
                .collect::<Vec<i64>>(),
        );
    }

    for i in 0..seeds_pt1.len() {
        seeds_pt1[i] = convert_value(&map, &seeds_pt1[i]);
    }

    println!("Part 1: {:?}", seeds_pt1.iter().min().unwrap());
    let mut min = std::i64::MAX;
    for s in seeds_pt2 {
        let local_min = s.start;
        if local_min < min {
            min = local_min;
        }
    }
    println!("Part 2: {:?}", min);
}
