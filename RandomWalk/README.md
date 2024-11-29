# Performance Comparison - 1D Random Walk Simulation

Simulating a 1D random walk to estimate the probability of reaching the origin point at least once can require an extremely large sample size. 
However, the runtime and memory performance can vary significantly depending on the implementation. Below, we compare two methods: 
Python Loop and NumPy Vectorization, using a simulation of 1 million samples.

---
## Simulation Method

Method 1: Python Loop
- Simulating each walk and step individually in a loop.
  - For each trial simulates the random walk repeatedly by updating the position incrementally
  - Checks the condition pos <=0 after each step

Method 2: Numpy Vectorization
- Generates all samples data at once by `np.rand.binomial() `and reshape into 2D array
- Calculate cumulative sums and then evaluate the conditions across all trials simultaneously


| Method                        | runtime (s) | Peak Memory Usage (MB) | Peek Memory Block(Count/Size) | 
|:------------------------------|-------------|------------------------|-------------------------------|
| Python Loop| 10.2325     | 42.55MB                | 49 /   4710B                  |
| Numpy Vectorization          | 0.3760      | 182.02MB               | 2 /    571B                   |

  

---
## Analysis 

### Method 1: Python Loop
For method 1, operations are performed element-by-element in Python loops, reason behind the slowness is due to 
Python's interpretive overhead (including evaluating executing python bytecode and managing memory references) for each iteration. 
For example, Updating position `pos` at each step involves decoding bytecode, accessing the integer memory chunk through its reference, creating a new Python integer object, 
allocating new memory and storing its new pointer reference into `pos`. Furthermore, each integer or object occupies a distinct memory chunk, accessing these objects 
may require extra time to jump between non-contiguous memory locations leading to a poor memory access performance, even leading to fragmented memory.

### Method 2: NumPy Vectorization
Regarding method 2, numpy array is stored at raw data bypassing the Python overhead problem. The array is pre-allocated with a contiguous block of memory during initialization.
For the 2D array in this example, rows are stored one after another, ensuring efficient access. The CPU could be able to prefetch chunks of data into its cache because the data is laid out sequentially in memory.
For example a 2D array in this example, rows are stored one after another, ensuring efficient access.
Execution are happening at the speed of low-level C code.
As for the entire random walk process, all trials (whole chunk of data) are computed in parallel and directly on the memory block without creating new objects.
Operations like `np.cumsum `and comparisons (e.g., `<= 0`) are applied simultaneously across the entire array, leveraging batch processing and parallelization.
