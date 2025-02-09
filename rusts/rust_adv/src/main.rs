use rayon::prelude::*;
use std::time::{Duration, Instant};

fn main() {
    println!("starting");
    let t = Instant::now();

    (0..5000000).into_par_iter().for_each(|i| {
        call_db(3, i);
    });

    println!("{:?}", t.elapsed());
}

fn call_db(delay: u64, _i: i32) {
    std::thread::sleep(Duration::from_secs(delay));
    // println!("item : {} slept for {} seconds", i, delay);
    // No stupid explicit mut or results collection
}
