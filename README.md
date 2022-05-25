# Discrete mathematics and Algorithms exam Spring 2022
## 1. Time, memory, scalability, big-o and examples of algorithms

Big-O notation is a way to analyze a given algorithm's efficiency. The complexity of the algorithm is given in terms of the input size, N. Since the analysis is solely based on the algorithm, the machine that it is being run on is irrelevant, in other words, this analysis is machine-independent. This makes us able to analyze the basic computer steps that are being taken throughout the algorithm.

There are different types of measurements when it comes to algorithms;
- worst-case
- average-case
- best-case

These are scenarios of data input that could either cause fast calculations (best-case) or really slow calculations (worst-case). When talking about Big-O notation, we typically look at the worst case, as we of course would like to prepare for the worst scenario.

Scaling is the term that defines how well the algorithm handles larger inputs. Almost every algorithm is efficient at an input of 3 objects, but there will be a significant difference in how well they scale if the input is 3 million objects. This of course means that if they scale badly, they take longer to compute which usually, but not always, is a bad thing (not bad in hashing algorithms as longer usually are more secure). But this is where time becomes a factor, as big inputs can mean very long computing times.

The restriction is not limited to time, but also memory of the used machine. Given an algorithm saving data in the memory in each recursion, then the O notation can also be a reflection of how much data the memory has to handle, which similar to time, can be a restriction when it comes to large amount of data inputs of the algorithm.


## 2. Sorting with and without recursio
## 3. Searching with binary search, hash tables and search trees
## 4. Graph properties, spanning trees and basic algorithms
## 5. Algorithms for shortest path in graphs
## 6. Critical path in graphs
## 7. Structure and use of conditional / propositional logic statements
## 8. Construction and use of regular expressions and finite state automata
## 9. Logical equivalence, De Morgan's laws, contradictions and tautologies
