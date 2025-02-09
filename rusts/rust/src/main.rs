use std::sync::{Arc, Mutex};
use std::thread;
use std::time::{Duration, Instant};

fn main() {
    println!("starting");
    let t = Instant::now();

    let results = Arc::new(Mutex::new(Vec::new()));
    let mut handles = vec![];

    for i in 0..5000000 {
        let results_clone = Arc::clone(&results);
        handles.push(thread::spawn(move || {
            call_db(3, i, results_clone);
        }));
    }

    for handle in handles {
        handle.join().unwrap();
    }

    println!("{:?}", t.elapsed());
    // println!("{:?}", results.lock().unwrap());
}

fn call_db(delay: u64, i: i32, results: Arc<Mutex<Vec<i32>>>) {
    thread::sleep(Duration::from_secs(delay));
    // println!("item : {} slept for {} seconds", i, delay); // Commented out println!
    let mut results_lock = results.lock().unwrap();
    results_lock.push(i);
}
