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


## 2. Sorting with and without recursion
## 3. Searching with binary search, hash tables and search trees

**Binary Searching** is a way of searching through a sorted array of data. The best way to analogize it to a real event, is if you were to look for a specific student paper in a sorted stack of sutdent papers. You woulnd't go over them one by one from beginning to end, but rather you would estimate the whereabouts of the paper first, and then do it again. If we were to say they were sorted by first name letters, you can estimate that a person named Laura would be around in the middle of the stack, and a person named Albert would usually be in the front. This is basically what binary searching does, as it first of all checks the center element of the array and then decides wether the element you are searching for is in either the left side or the right side of the array. Again, this is why this only works on sorted arrays, as unsorted arrays does not have definite positions you can search for. This means that the time complexity for this algorithm is O(log(n)) as you are seeing how many times you can possible divide the array amount by 2 before you have a single element left. - In short, this is a search algorithm to find a *target* value in a *sorted* array.

**Hash tables** are actually really simple, as it simply uses a hashing algorithm to get a hashcode, which is used as an index in a way in an array. String/Key -> Hash -> Index. However there is one thing to be aware of when doing this, is that since there is an infinite amount of strings and only a finite amount of indexes, there can be *collisions*, which essentially is when two keys refers to the same index. This is usually solved with the array holding *lists* of the elements, so that an index can hold multiple elements in the list. Usually the time complexity for this way of searching is O(1) for good hashtables, that has very few collisions etc. and O(n) for a terrible hashtable, which has a lot of collisions.

**Binary trees** are in many ways similar to a binary search, however instead of it being an algorithm, it is basically a form of data structure for your data. This means that you cannot use array algorithms on this, however in its nature it is very easy to search for values in. The first node in the binary tree is called the *root*, each connected node is called a *child*, or *children*, unless theyre the last node of which they're called a *leaf*.

## 4. Graph properties, spanning trees and basic algorithms
## 5. Algorithms for shortest path in graphs
## 6. Critical path in graphs
## 7. Structure and use of conditional / propositional logic statements
## 8. Construction and use of regular expressions and finite state automata
## 9. Logical equivalence, De Morgan's laws, contradictions and tautologies
