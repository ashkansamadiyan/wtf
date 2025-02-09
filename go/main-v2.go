package main

import (
	"fmt"
	"sync"
	"time"
)

func main() {
	fmt.Println("starting")
	start := time.Now()

	const numTasks = 5000000

	// Preallocate the slice with the exact number of elements.
	// This way, every goroutine can write to its own slot.
	results := make([]int, numTasks)

	var wg sync.WaitGroup

	// Launch numTasks goroutines.
	for i := 0; i < numTasks; i++ {
		wg.Add(1)
		// Pass a pointer to results and a pointer to the WaitGroup.
		go callDb(3, i, &results, &wg)
	}

	wg.Wait()
	fmt.Println("Elapsed:", time.Since(start))
	// Optionally, inspect a few values:
	// fmt.Println(results[:10])
}

// callDb simulates a blocking call (like a DB call) by sleeping for `delay` seconds,
// and then writes its index to the preallocated results slice.
func callDb(delay int, i int, results *[]int, wg *sync.WaitGroup) {
	defer wg.Done()

	// Simulate a delay.
	time.Sleep(time.Duration(delay) * time.Second)
	// Write to the appropriate index.
	(*results)[i] = i
}
