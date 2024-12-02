# Knapsack
A variant of knapsack where we have 3 dishes
* want to place dishes on the table to maximize total satisfaction
* while not exceeding the capacity of the table

banquet.mzn
```
% variables needing data
enum DISH;
int: capacity
array[DISH] of int: satisf;
array[DISH] of int: size;

% decision variables
array[DISH] of var int: amt;

constraint forall(i in DISH)(amt[i] >= 0)
constraint sum(i in DISH)(size[i] * amt[i]) <= capacity;

solve maximize sum(i in DISH)(satisf[i] * amt[i]);

output ["Amount = ", show(amt), "\n"];
```

Note we can now change the size of the data to solve many different models
* the `DISH` enum could be any size

banquet.dzn
```
DISH = {SNAKESOUP, GONGBAOFROGS, MAPOTOFU};
capacity = 18;
satisf = [29, 19, 8];
size = [8, 5, 3];
```
