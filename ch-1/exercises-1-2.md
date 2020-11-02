1.2-1: Give an example of an application that requires algorithmic content at the application level, and discuss the function of the algorithms involved.

Maps - shortest path
Spreadsheets - sorting

1.2-2: Suppose we are comparing implementations of insertion sort and merge sort on the same machine. For inputs of size n, insertion sort runs in 8n2 steps, while merge sort runs in 64n lg n steps. For which values of n does insertion sort beat merge sort?

n = 2:
IS = 32
MS = 128

n = 10:
IS = 800
MS = ~2126

n = 1000
IS = 8000
MS = 42496

n = 1000
IS = 8000000
MS = 437810

1.2-3: What is the smallest value of n such that an algorithm whose running time is 100n2 runs faster than an algorithm whose running time is 2n on the same machine?

