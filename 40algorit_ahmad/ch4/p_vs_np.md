# The difference between P and NP

This summary is likely flawed in some ways. I am not a computer scientist, I am a physicist turned programmer and data scientist. Pardon my broad generalizations and use of non-standard language.

Both P (Polynomial) and NP (Non-Deterministic Polynomial) have to do with runtime of an algorithm. P problems are the class of problems that can be **solved** in polynomial time. There exists some solution with $O(n^k)$ runtime such that the problem can be solved. NP problems are the class of problem that there may not exist a polynomial time _solution_ to the problem, but **verifying** a solution once it is obtained can be done in $O(n^k)$ time.

The primary distinction comes from the separation of $t_r$, the time to get a solution/certificate, and $t_s$, the time to verify a certificate once it is obtained. P and NP apply to these times, respectively. 

# What about NP-hard and NP-complete

NP-hard means that something is NP and likely the most challenging of NP problems, but don't necessarily have to be NP problems. Best seen through examples I would argue. NP-complete problems are the real killers. The two main characteristics of NP-complete problems are that these problems are a) hard to generate solutions for, and b) hard to evaluate solutions once they exist. Finding a polynomial time algorityhm for any NP-complete problem would imply that every problem that is NP can be solved in poylnomial time. 

# Examples

- P: linear search, bubble sort, shortest path in a directed acyclic graph
- NP: prime factorization (hard to generate prime factors, but very easy to see if a proposed factorization works), subset sum problem (given a set, is there a subset that sums to a specific value)
- NP-hard: graph coloring (find the minimum number of colors required to color a graph s.t. no two adjacent nodes have the same color), hamiltonian cycle (find a cycle that visits every node in a graph once)
- NP-complete: the travelling salesman problem, the knapsack problem (given a set of items with weights and values, determine the number of item to include in a collection s.t. the total weight is less than a specified target but the value is maximized), bin packing (pack items of different sizes into a fixed number of bins, minimizing the number of bins used)

