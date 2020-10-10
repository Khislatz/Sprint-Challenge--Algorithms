Please add your answers to the Analysis of Algorithms exercises here.
### Exercise I

a)  The time complexity of the block of code below is O(n). The statement a = 0 as well as the statement within the while loop is constant O(1). However, the time complexity of the loop itself is linear O(n) since the bigger the n the higher the number of iterations the loop will perform.  

```python
a = 0 #### O(1)
while (a < n * n * n):   #### O(n)
    a = a + n * n ### O(1)
```
b)  The time complexity of the block of code below is O(n^2). The statement that initiates the sum has a runtime of O(1). Then we calculate the time complexity of the outer loop, which is O(n) since it depends on the number of iterations n. After that we initialize the counter of the inner loop with j = 1, which has a runtime of O(1), followed by the inner loop itself, which has a time complexity O(n). The statement within the the inner while loop is O(1). Since we have a nested loop (a loop within the loop), the time complexity of the entire block of code is O(n^2).

```python
sum = 0 ### O(1)
for i in range(n): ### O(n)
    j = 1 ### O(1)
    while j < n: ### O(n)
    j *= 2  ### O(1)
    sum += 1 ### O(1)

```
c)  The time complexity of the function below is O(n). The runtime of the code in the function is O(1) times
the number the function is called (recursion), which is O(n). 

```python
def bunnyEars(bunnies):  ### O(1)
    if bunnies == 0: ### O(1)  
    return 0 ### O(1)

    return 2 + bunnyEars(bunnies-1) ### O(n)

```
### Exercise II

'''
Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

'''

### Pseudo Code: 

We could approach this problem using binary search algorithm. The first step is to find the middle floor, such as (high + low) // 2. Then we throw an egg, if it gets broken, then we don't need to consider higher floors, otherwise, there is no need to consider the lower floors. This algorithms gets repeated until we find the f. 


### Algorithm:

```python
Determine the number of floors as an array
get the lowest floor (intially assign to zero)
get the highest floor (assign to the length of the array)
keep repeating the steps below until the highest floor is less than or equal to the lowest floor:
    find middle floor # such as (higher + lower ) // 2
    throw an egg by decrementing the inventory by 1
        middle_floor = (lower+higher)//2
        throw an egg from the middle floor
        if the egg broke:
            set the middle floor's value as a new hightest floor
        else:
            set the middle floor's value as a new lowest floor 
    return the floor value
```
### Time Complexity:

The time complexity of my algorithm is logarithmic O(log(n)). Since we would use a for loop, the runtime would be O(n) meaning that we would iterate n times. After each iteration using on the binary search approach, the array of floors is being divided by 2, the time complexity of which is O(log(n)). Therefore, the time complexity of the algorithm is O(log(n)).

