async function main() {
  console.log("starting");
  const t = Date.now();

  const promises = [];
  const results: number[] = [];

  for (let i = 0; i < 5000000; i++) {
    promises.push(callDb(3, i, results));
  }

  await Promise.all(promises);
  console.log(`${(Date.now() - t) / 1000} seconds`);
  // console.log(results);
}

async function callDb(delay: number, i: number, results: number[]) {
  await new Promise((resolve) => setTimeout(resolve, delay * 1000));
  //console.log(`item : ${i} slept for ${delay} seconds`);
  results.push(i);
}

main();

