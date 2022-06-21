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

Sorting algorithms can utulize recursion, as it allows the method to have a time complexity of O(nlogn), instead of the bubble sorts time complexity of O(n^2). Recursion simply means that you call the method within itself.

First of all we can look at the *mergesort* algorithm.

The mergesort algorithm is basically a division of an array until all elements are atomically divided, and are then merged into eachother based on their values.

Non recursive sorting methods, like a bubble sort usually is less effective, as they have a high time complexity. If we take the bubble sort example, we iterate over the array O(n^2) times in worse case scenario.

## 3. Searching with binary search, hash tables and search trees

**Binary Searching** is a way of searching through a sorted array of data. The best way to analogize it to a real event, is if you were to look for a specific student paper in a sorted stack of sutdent papers. You woulnd't go over them one by one from beginning to end, but rather you would estimate the whereabouts of the paper first, and then do it again. If we were to say they were sorted by first name letters, you can estimate that a person named Laura would be around in the middle of the stack, and a person named Albert would usually be in the front. This is basically what binary searching does, as it first of all checks the center element of the array and then decides wether the element you are searching for is in either the left side or the right side of the array. Again, this is why this only works on sorted arrays, as unsorted arrays does not have definite positions you can search for. This means that the time complexity for this algorithm is O(log(n)) as you are seeing how many times you can possible divide the array amount by 2 before you have a single element left. - In short, this is a search algorithm to find a *target* value in a *sorted* array.

**Hash tables** are actually really simple, as it simply uses a hashing algorithm to get a hashcode, which is used as an index in a way in an array. String/Key -> Hash -> Index. However there is one thing to be aware of when doing this, is that since there is an infinite amount of strings and only a finite amount of indexes, there can be *collisions*, which essentially is when two keys refers to the same index. This is usually solved with the array holding *lists* of the elements, so that an index can hold multiple elements in the list. Usually the time complexity for this way of searching is O(1) for good hashtables, that has very few collisions etc. and O(n) for a terrible hashtable, which has a lot of collisions.

**Binary trees** are in many ways similar to a binary search, however instead of it being an algorithm, it is basically a form of data structure for your data. This means that you cannot use array algorithms on this, however in its nature it is very easy to search for values in. The first node in the binary tree is called the *root*, each connected node is called a *child*, or *children*, unless theyre the last node of which they're called a *leaf*.

## 4. Graph properties, spanning trees and basic algorithms

A graph is a structure made up of nodes / **vertices** (**vertex**) and connections between them (**edge**s). The basic properties:

* Distance between two vertices
* Eccentricity of a vertex
* Radius of connected Graph
* Diameter of a Graph
* Central point
* Circumference
* Girth

**Distance** is basically the number of edges in a shortest path between vertex X and vertex Y. If there are many paths connecting two vertices, then the **shortest path is considered as the distance**  between the two vertices. Distance between two vertices is denoted by d(X, Y).

**Eccentricity** of a vertex is the maximum distance between a vertex to all other vertices. It is denoted by e(V).

The **radius** of a connected graph is the minimum eccentricity from all the vertices. In other words, the minimum among all the distances between a vertex to all other vertices is called as the radius of the graph. It is denoted by r(G).

**Diameter** of a graph is the maximum eccentricity from all the vertices. In other words, the maximum among all the distances between a vertex to all other vertices is considered as the diameter of the graph G. It is denoted by d(G).

If the eccentricity of the graph is equal to its radius, then it is known as **central point** of the graph.

The total number of edges in the longest cycle of graph G is known as the **circumference** of G.

The total number of edges in the shortest cycle of graph G is known as **girth**. It is denoted by g(G).

**Spanning trees** is the idea of removing edges from a graph and still have all vertices connected, but no circuits. If the spanning trees appear to be identical, even if different edges are removed, you call them *isomorphic*, if they appear to be unique, then they're non-isomorphic.

**Prims Algorithm** Minimum Spanning Tree (MST) - This algorithm finds the algorithm with the tree with the smallest edge weight of the graph.
![Before](/Pictures/Minimum%20Spanning%20Tree.JPG "Minimum Spanning Tree")
![After](/Pictures/Minimum%20Spanning%20Tree%20Result.JPG "Minimum Spanning Tree Result")

## 5. Algorithms for shortest path in graphs

**Dijkstra's algorithm** is an excellent example of how to find the shortest path from one vertex to another in a graph.

First the graph must have weighted edges, so there's a path to calculate from, and second we assign values to all vertices in the given graph. The start point we assign 0, as there is no distance from starting point to starting point, and every other vertices is assigned value infinite, as we want to make sure that first value compared is less. We pick the vertex with minimum cost, in this case Vertex 0, and then update adjacent vertices to check if their distance is shorter than already given. The updated value is the chosen vertex distance and edge of connection. This is done repeately through the entire graph until every vertex has been updated with a value.

![Visualization1](/Pictures/Dijkstras%20Algorithm%201.JPG "Dijkstras Algorithm 1")
![Result1](/Pictures/Dijkstras%20Algorithm%20Result%201.JPG "Dijkstras Algorithm Result 1")
![Visualization2](/Pictures/Dijkstras%20Algorithm%202.JPG "Dijkstras Algorithm 2")
![Result2](/Pictures/Dijkstras%20Algorithm%20Result%202.JPG "Dijkstras Algorithm Result 2")

## 6. Critical path in graphs

**Critical path** in graphs is the longest path to the given end vertex. However, this means that not only must vertices have values (typically called tasked and reffered to time of completion), edges must also have directions. A path is a complete sequence from first task to end vertex.

The critical path algorithm Looks for the longest path and then removes the first task in the path. The path is saved in a list, that we call the priority list. This is done repeately until there is no tasks left.

![CritPath1](/Pictures/Critical%20Path%20Algorithm%201.JPG "Critical Path 1")
![CritPath2](/Pictures/Critical%20Path%20Algorithm%202.JPG "Critical Path 2")
![PriorityList1](/Pictures/Critical%20Path%20Priority%20List%201.JPG "Priority List 1")

After having created the priority list of the graph, we can now create the optimized schedule of how we should prioritize the tasks. If we have 2 processesors the tasks is then divided by priority and when theyre ready to be completed (as the requirement is for previous tasks to be completed).

![Schedule](/Pictures/Critical%20Path%20Schedule.JPG "Schedule")

## 7. Structure and use of conditional / propositional logic statements

A proposition is an assertion, statement, or declarative sentence that can either be true or false but not both. For example, the sentence "It is raining" can either be true or false, it cannot be both. However the sentence "X is greater than 10" is not a proposition as it cannot be stated true or false without the value of N. This is used in progamming logic when something must be done if certain conditions are met.

Other things that cannot be propositional statements are for example:

*   Questions
*   Imperatives (commands)

Usually in conditional statements, the propersitions are denoted with p, q and r.

With connectives we can change or combine propersitions meanings. There's a few ways to create connectives, and this is done with following notations:

* *¬p*      - not p (inverse)
* *p ∧ q*   - p and q
* *p ∨ q*   - p or q
* *p → q*   - if p, then q (implication)

When connecting two propersitional statements with connectives, we have created a compound statement. This is where truth tables comes in handy, as we can see result of each possible scenario.

![Schedule](/Pictures/Truthtable.JPG "Schedule")

## 8. Construction and use of regular expressions and finite state automata


## 9. Logical equivalence, De Morgan's laws, contradictions and tautologies

The correct definition:

The compound propositions p and q are said to be logically equivalent if p ↔ q is a Tautology. Logical Equivalence is denoted by ≡ or (pil med to streger begge veje).

From this we need to know what a tautology is, and the definition of a tautology is: *a statement that is true by necessity or by virtue of its logical form.*. This is denoted as **t**.

Opposite a tautology, we have a condradiction, that is an assertion of Propositional Logic that is false in all situations; that is, it is false for all possible values of its variables. This is denoted as **c**.

![DeMorgan1](/Pictures/De%20Morgans%20Law%201.JPG "De Morgans Law 1")
![DeMorgan2](/Pictures/De%20Morgans%20Law%202.JPG "De Morgans Law 2")