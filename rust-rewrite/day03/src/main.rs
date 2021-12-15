use std::fs;

fn main() {
    let file = fs::read_to_string("day03.in").unwrap();
    let data = ingest_data(file);
    println!("=== PART 1 ===");
    part1(&data);
    println!("=== PART 2 ===");
}

fn ingest_data(input: String) -> Vec<String> {
    let mut data: Vec<String> = vec![];
    for line in input.strip_suffix('\n').unwrap().split('\n') {
        data.push(line.to_string());
    }
    data
}

fn common_bit(data: &Vec<String>, bit: usize, invert: bool) -> char {
    let mut bit_count = (0, 0);
    for x in data {
        match x.chars().nth(bit).unwrap() {
            '0' => bit_count.0 += 1,
            '1' => bit_count.1 += 1,
            _ => (),
        }
    }
    if bit_count.0 <= bit_count.1 {
        if invert {
            '0'
        } else {
            '1'
        }
    } else {
        if invert {
            '1'
        } else {
            '0'
        }
    }
}

fn part1(data: &Vec<String>) {
    let mut gamma: String = "".to_string();
    let mut epsilon: String = "".to_string();
    for bit in 0..data[0].len() {
        gamma.push(common_bit(data, bit, false));
        epsilon.push(common_bit(data, bit, true));
    }
    let gamma_i = usize::from_str_radix(&gamma, 2).unwrap();
    let epsilon_i = usize::from_str_radix(&epsilon, 2).unwrap();
    println!("Gamma: {}", gamma_i);
    println!("Epsilon: {}", epsilon_i);
    println!("Power consumption: {}", gamma_i * epsilon_i);
}
