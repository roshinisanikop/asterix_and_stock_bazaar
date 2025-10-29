# Asterix and the Stock Bazaar  

## Overview  

This project implements a distributed stock trading system inspired by the adventures of the Gauls from *Asterix*. The goal was to explore system design at different abstraction levels — starting with handwritten low-level threading and sockets, and later adopting modern RPC frameworks.  

The work is divided into three main parts:  
1. **Custom Socket + ThreadPool Implementation**  
2. **gRPC with Built-in ThreadPool**  
3. **Evaluation and Performance Measurement**  

Through this lab, I gained hands-on experience with **thread pools, synchronization, gRPC, and performance testing in distributed applications**.  

---

## Part 1: Socket Connection with Handwritten Thread Pool  

In this part, I implemented an **online stock trading client-server system** using raw sockets.  

- The **server** supports one operation: `Lookup(stockName)`  
  - Returns the price of a meme stock (e.g., `15.99`).  
  - Returns `-1` if the stock is not found.  
  - Returns `0` if the stock exists but trading is suspended.  
- The server maintains an **in-memory catalog** with:  
  - Stock names (`GameStart`, `RottenFishCo`)  
  - Current price  
  - Trading volume  

The server design:  
- Listens on a configurable port (e.g., 8888).  
- Accepts client connections and enqueues requests.  
- Uses a **handwritten thread pool** with a static number of worker threads.  
- Each worker pulls requests from the queue, executes them, and sends results back.  

Important design decisions:  
- **No built-in ThreadPool frameworks** were used. I implemented my own queue, thread management, and synchronization primitives (locks/semaphores) to ensure thread safety.  
- **Thread-per-request model**: The client opens a socket, issues a request, waits for a reply, then closes the connection.  

The **client** is a simple loop that sends lookup queries sequentially, but multiple clients can run concurrently to stress-test the thread pool.  

---

## Part 2: gRPC with Built-in Thread Pool  

To highlight the difference between low-level and high-level abstractions, I reimplemented the stock trading system using **gRPC** and the language’s built-in thread pool support.  

The **server** exposes three RPC methods:  
1. `Lookup(stockName)` → returns stock price and trading volume (or `-1` if invalid).  
2. `Trade(stockName, N, type)` → supports buying/selling `N` stocks, updates trading volume.  
   - Returns `1` for success, `0` if trading suspended, `-1` for invalid stock.  
3. `Update(stockName, price)` → updates stock prices.  
   - Returns `1` for success, `-1` for invalid stock, `-2` for invalid price.  

Enhancements:  
- Expanded catalog to four stocks: **GameStart, RottenFishCo, BoarCo, MenhirCo**.  
- Implemented error handling for invalid names, invalid prices, and suspended trading.  
- Used protobuf definitions for message structures.  
- Leveraged the **dynamic thread pool** provided by gRPC, with configurable concurrency limits.  

The **client**:  
- Issues lookup and trade calls in a loop.  
- Multiple client processes can run in parallel.  
- A special client was implemented to update stock prices periodically at random intervals.  

---

## Part 3: Evaluation and Performance  

I conducted performance testing across both implementations (Part 1 and Part 2).  

Setup:  
- Clients and servers ran inside **Docker containers**.  
- Load tests varied the number of clients from 1 to 5.  

Metrics measured:  
1. **Latency of Lookup (Sockets vs gRPC)** — gRPC is more efficient under higher loads.  
2. **Latency as client load increases** — response time rises as the number of concurrent clients exceeds thread pool size.  
3. **Lookup vs Trade latency** — trade is slower due to synchronization overhead, whereas lookup is faster.  
4. **Thread pool saturation** — in Part 1, once client count exceeded pool size, requests queued up, increasing response times.  

Plots were generated with:  
- X-axis: number of clients  
- Y-axis: response time/latency  
- Separate graphs for **lookup** and **trade** requests.  

---

## References  

- [Asterix (Gauls)](https://en.wikipedia.org/wiki/Asterix)  
- [Meme stocks](https://en.wikipedia.org/wiki/Meme_stock)  
- [gRPC in Python](https://grpc.io/docs/languages/python/basics/)  
- [gRPC in Java](https://grpc.io/docs/languages/java/basics/)  
- [gRPC in C++](https://grpc.io/docs/languages/cpp/basics/)  
- [Git & GitHub basics](https://docs.github.com/en/get-started/using-git/about-git)  
- [Python ThreadPoolExecutor](https://docs.python.org/3/library/concurrent.futures.html#threadpoolexecutor)  
- [Java Thread Pools](https://docs.oracle.com/javase/tutorial/essential/concurrency/pools.html)  
