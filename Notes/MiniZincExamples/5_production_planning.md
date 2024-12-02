# Production Planning
Many production planning problems have a similar form
* limit on resources
* maximize profit

We can make a generic model

prod-plan.mzn
```
% products
enum PRODUCT;
% Profit per unit for each product
array[PRODUCT] of float: profit;

% resources
enum RESOURCE;
% Amount of each resource available
array[RESOURCE] of float: capacity;

% Units of each resource required to produce 1 unit of product
array[PRODUCT, RESOURCE] of float: consumption;

% variables: how much should we make of each product
array[PRODUCT] of var int: produce;

% must produce a non-negative amount
constraint forall(p in PRODUCT) (produce[p] >= 0);

% Production can only use the available resources:
constraint forall(r in RESOURCE) (
  sum (p in PRODUCT) (consumption[p, r] * produce[p] <= capacity[r])
);

% maximize profit
solve maximize sum(p in PRODUCT) (profit[p] * produce[p]);

output ["\(p): \(produce[p])\n" | p in PRODUCT];
```

prod-plan.dzn
```
PRODUCT = {AXE, SWORD, PIKE, SPEAR, CLUB};
profit = [11.0, 18.0, 15.0, 17.0, 11.0];
RESOURCE = {IRON, WOOD, SMITH, CARPENTER};
capacity = [5000, 7500, 4000, 3000];
consumption = [| 1.5, 1.0, 1.0, 1.0
               | 2.0, 0.0, 2.0, 0.0
               | 1.5, 0.5, 1.0, 1.0
               | 0.5, 1.0, 0.9, 1.5
               | 0.1, 2.5, 0.1, 2.5 |];
```

An array comprehension is of the form `[expr | generator1, generator2, ... where test]`
* the `where test` is a condition and is optional
* eg. `[i + j | i, j in 1..4 where i < j]`

Can flatten an nD array into a list with comprehension
* `array[1..20] of int: list = [consumption[i, j] | i in 1..5, j in 1..4];`

Can iterate over an array with operations like `sum`, `product`, `min`, `max`, `forall`, `exists`
* eg. `forall([a[i] != a[j] | i, j in 1..10 where i < j])`
