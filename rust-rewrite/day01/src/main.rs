use std::fs;

fn main() {
    let file = fs::read_to_string("day01.in").unwrap();

    let mut nums: Vec<u32> = vec![];
    for line in file.split('\n') {
        if line != "" {
            nums.push(u32::from_str_radix(line, 10).unwrap());
        }
    }
    let count_a = count_inc(&nums);

    let mut nums2: Vec<u32> = vec![];
    for (i, _) in nums.iter().enumerate() {
        if i + 2 < nums.len() {
            nums2.push(nums[i..i + 3].iter().sum());
        }
    }
    let count_b = count_inc(&nums2);

    println!("Part 1: {}", count_a);
    println!("Part 2: {}", count_b);
}

fn count_inc(input: &Vec<u32>) -> usize {
    let mut count = 0;
    let mut prev: u32 = 0;
    for num in input.iter() {
        if num > &prev && prev != 0 {
            count += 1;
        }
        prev = *num;
    }
    count
}
