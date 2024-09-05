use itertools::Itertools;

fn main() {}

fn get_first_marker(input: &str) -> u32 {
    let x = input.chars().tuple_windows().map(|(a, b, c, d)| ());
    println!("{:?}", x);
    todo!()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_get_first_marker() {
        assert_eq!(get_first_marker("bvwbjplbgvbhsrlpgdmjqwftvncz"), 5);
        assert_eq!(get_first_marker("nppdvjthqldpwncqszvftbrmjlhg"), 6);
        assert_eq!(get_first_marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"), 10);
        assert_eq!(get_first_marker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"), 11);
    }
}
