use std::fs;

fn main() {
    let file = fs::read_to_string("day02.in").unwrap();
    println!("=== PART 1 ===");
    part1(&file);
    println!("=== PART 2 ===");
    part2(&file);
}

fn part1(file: &String) {
    let mut pos = vec![0, 0];

    let direction_key = |x| match x {
        "forward" => (1, 0),
        "down" => (0, 1),
        "up" => (0, -1),
        _ => (0, 0),
    };

    for line in file
        .strip_suffix("\n")
        .unwrap()
        .split('\n')
        .map(|x| x.split(" ").collect::<Vec<&str>>())
    {
        pos[0] += direction_key(line[0]).0 * i32::from_str_radix(line[1], 10).unwrap();
        pos[1] += direction_key(line[0]).1 * i32::from_str_radix(line[1], 10).unwrap();
    }
    println!("Current position: {:?}", pos);
    println!("Product: {:?}", pos.iter().product::<i32>());
}

fn part2(file: &String) {
    let mut pos = vec![0, 0, 0];

    for line in file
        .strip_suffix("\n")
        .unwrap()
        .split('\n')
        .map(|x| x.split(" ").collect::<Vec<&str>>())
    {
        if line[0] == "down" {
            pos[2] += i32::from_str_radix(line[1], 10).unwrap();
        } else if line[0] == "up" {
            pos[2] -= i32::from_str_radix(line[1], 10).unwrap();
        } else if line[0] == "forward" {
            pos[0] += i32::from_str_radix(line[1], 10).unwrap();
            pos[1] += pos[2] * i32::from_str_radix(line[1], 10).unwrap();
        }
    }
    println!("Current position: {:?}", pos);
    println!("Product: {:?}", pos[0] * pos[1]);
}
