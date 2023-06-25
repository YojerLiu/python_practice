Complete the 2 tasks below in [exercise_2.py](exercise_2.py).

1. Given two different lists:

```Python
lst_1 = ['amy', 'cindy', 'bob', 'anthony']
lst_2 = ['dylan', 'zion', 'ezra']
```
Use for-loop to create a new list holding all the elements of both lists above, in which each element is capitalized and sorted in the alphabetical order.

Sample output:

```
['AMY', 'ANTHONY', 'BOB', 'CINDY', 'DYLAN', 'EZRA', 'ZION']
```

2. Given a list of 3 integer elements. Each element is exactly a coefficient of a univariate quadratic equation. Recall that the solution of equation $ax^2 + bx + c = 0$ is:

$$
x_{1,2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
$$

Now we have a list `lst = [1, -3, -18]`. Use the formula above to solve the equation.

Hint: $\sqrt{2}$ is equal to $2^{0.5}$

Sample output:
```
x1 = 6.0
x2 = -3.0
```