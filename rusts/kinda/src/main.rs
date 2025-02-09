use futures::future::join_all;
use std::sync::Arc;
use std::time::Instant;
use tokio::sync::Mutex;
use tokio::time::{sleep, Duration};

#[tokio::main]
async fn main() {
    println!("starting");
    let start = Instant::now();

    let results = Arc::new(Mutex::new(Vec::with_capacity(5_000_000)));

    let mut tasks = Vec::with_capacity(5_000_000);

    for i in 0..5_000_000 {
        let results = results.clone();
        tasks.push(tokio::spawn(async move {
            sleep(Duration::from_secs(3)).await;

            // println!("item: {} slept for 3 seconds", i);

            results.lock().await.push(i);
        }));
    }

    join_all(tasks).await;

    println!("{} seconds", start.elapsed().as_secs_f64());

    // let results = results.lock().await;
    // println!("results: {:?}", &*results);
}
