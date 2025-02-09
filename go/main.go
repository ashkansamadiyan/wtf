package main

import (
	"fmt"
	"sync"
	"time"
)

var wg = sync.WaitGroup{}
var mux = sync.Mutex{}

var results = []int{}

func main() {

	fmt.Println("starting")
	t := time.Now()

	for i := 0; i < 5_000_000; i++ {
		wg.Add(1)
		go callDb(3, i)
	}

	wg.Wait()
	fmt.Println(time.Since(t))
	// fmt.Println(results)

}

// func count() {
//
//	i := 0
//	for i < 1000000 {
//		i++
//	}
//
// }
func callDb(delay int, i int) {

	time.Sleep(time.Duration(delay) * time.Second)
	// fmt.Printf("item : %d slept for %d seconds \n ", i, delay)
	mux.Lock()
	results = append(results, i)
	mux.Unlock()
	wg.Done()

}
