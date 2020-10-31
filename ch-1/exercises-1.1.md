1.1-1: Give a real-world example that requires sorting or a real-world example that requires computing a convex hull.

Alphanetically sorting tracks in a playlist.

1.1-2: Other than speed, what other measures of efficiency might one use in a real-world setting?

Efficient use of space. 
Growth.

1.1-3: Select a data structure that you have seen previously, and discuss its strengths and limitations.

Linked list

- O(n) lookup
- O(1) insert
- O(1) delete

Good for data that gets changed a lot at runtime. Can be slow for lookup. Memory is not contiguous so cannot be opotimised and cached like a regular array. 

1.1-4: How are the shortest-path and traveling-salesman problems given above similar? How are they different?

Shortest path and traveling-salesman are both graph problems. For the shortest path we build a model and we can efficiently determine the shortest path given point a and point b. The traveling-salesman problem modifies the problem slightly to include needing to vidsit each node. This is an NP-complete problem with no known efficient solution.


1.1-5: Come up with a real-world problem in which only the best solution will do. Then come up with one in which a solution that is “approximately” the best is good enough.


