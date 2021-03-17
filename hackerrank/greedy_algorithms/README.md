# Greedy algorithms

Greedy algorithms are those which make the **locally* optimal choice at each step. Therefore, they (might) not reach globally optimal solution but will reach to an acceptable one in an acceptable amount of time/steps.

e.g. given the following tree, get the longest path

```
        7
      /   \
    3      12
  /   \   /  \
99     8 5    6
```

The greedy algorithm would take the longest of the childs, whose solution would be then `7 -> 12 -> 6`, while the best one is `7 -> 3 -> 99`.