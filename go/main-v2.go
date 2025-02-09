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


	results := make([]int, numTasks)

	var wg sync.WaitGroup


	for i := 0; i < numTasks; i++ {
		wg.Add(1)
		go callDb(3, i, &results, &wg)
	}

	wg.Wait()
	fmt.Println("Elapsed:", time.Since(start))

	// fmt.Println(results[:10])
}


func callDb(delay int, i int, results *[]int, wg *sync.WaitGroup) {
	defer wg.Done()

	time.Sleep(time.Duration(delay) * time.Second)
	(*results)[i] = i
}
