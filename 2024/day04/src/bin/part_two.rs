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

    let mut xmas_found = 0;

    for y in 0..=height {
        for x in 0..=width {
            if puzzle[y][x] != 'A' || x < 1 || y < 1 || x == width || y == height {
                continue;
            }

            // Check top-left and bottom-right diagonal
            let diag1 = (puzzle[y - 1][x - 1] == 'M' && puzzle[y + 1][x + 1] == 'S')
                || (puzzle[y - 1][x - 1] == 'S' && puzzle[y + 1][x + 1] == 'M');

            // Check top-right and bottom-left diagonal
            let diag2 = (puzzle[y - 1][x + 1] == 'M' && puzzle[y + 1][x - 1] == 'S')
                || (puzzle[y - 1][x + 1] == 'S' && puzzle[y + 1][x - 1] == 'M');

            // println!("tl/br={} tr/bl={}", diag1, diag2);
            // If neither diagonal contains 'M' and 'S', continue to the next iteration
            if diag1 && diag2 {
                // println!("Found for x={}, y={}", x, y);
                xmas_found += 1;
            }

            // println!("Not found for x={}, y={}", x, y);
        }
    }

    println!("Found {} XMAS", xmas_found);
}
