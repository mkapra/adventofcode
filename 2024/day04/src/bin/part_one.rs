use std::fs;

fn main() {
    let puzzle_file = fs::read_to_string("puzzle_input.txt").expect("Could not read puzzle input");
    let puzzle = puzzle_file
        .split("\n")
        .map(|s| s.chars().collect())
        .filter(|c: &Vec<char>| !c.is_empty())
        .collect::<Vec<Vec<char>>>();

    let width = puzzle[0].len() - 1;
    let height = puzzle.len() - 1;

    let xmas = "XMAS".chars().collect::<Vec<char>>();
    let xmas_rev = xmas.clone().into_iter().rev().collect::<Vec<char>>();
    let mut xmas_found = 0;

    for y in 0..=height {
        for x in 0..=width {
            if puzzle[y][x] != 'X' {
                continue;
            }

            // x+ direction
            if x + 3 <= width && puzzle[y][x..=x + 3] == xmas {
                xmas_found += 1;
            }

            // x- direction
            if x >= 3 && puzzle[y][x - 3..=x] == xmas_rev {
                xmas_found += 1;
            }

            // y+ direction
            if y + 3 <= height {
                for (n, c) in "MAS".chars().enumerate() {
                    if puzzle[y + n + 1][x] != c {
                        break;
                    }
                    if c == 'S' {
                        xmas_found += 1;
                    }
                }
            }

            // y- direction
            if y >= 3 {
                for (n, c) in "MAS".chars().enumerate() {
                    if puzzle[y - n - 1][x] != c {
                        break;
                    }
                    if c == 'S' {
                        xmas_found += 1;
                    }
                }
            }

            // diagonal
            if x + 3 <= width && y + 3 <= height {
                for (n, c) in "MAS".chars().enumerate() {
                    if puzzle[y + n + 1][x + n + 1] != c {
                        break;
                    }
                    if c == 'S' {
                        xmas_found += 1;
                    }
                }
            }
            if x + 3 <= width && y >= 3 {
                for (n, c) in "MAS".chars().enumerate() {
                    if puzzle[y - n - 1][x + n + 1] != c {
                        break;
                    }
                    if c == 'S' {
                        xmas_found += 1;
                    }
                }
            }
            if x >= 3 && y >= 3 {
                for (n, c) in "MAS".chars().enumerate() {
                    if puzzle[y - n - 1][x - n - 1] != c {
                        break;
                    }
                    if c == 'S' {
                        xmas_found += 1;
                    }
                }
            }
            if x >= 3 && y + 3 <= height {
                for (n, c) in "MAS".chars().enumerate() {
                    if puzzle[y + n + 1][x - n - 1] != c {
                        break;
                    }
                    if c == 'S' {
                        xmas_found += 1;
                    }
                }
            }
        }
    }

    println!("Found {} XMAS", xmas_found);
}
