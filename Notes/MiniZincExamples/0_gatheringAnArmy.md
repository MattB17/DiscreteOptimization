# Gathering an Army
Gathering a army and want to maximize strength while not spending more than the budget

army.mzn
```
int: budget = 10000;
var 0..1000: F;
var 0..400: L;
var 0..500: Z;
var 0..150: J;

solve maximize 6*F + 10*L + 8*Z + 40*J;

constraint 13*F + 21*L + 17*Z + 100*J <= budget;

output ["F = \(F), L = \(L), Z = \(Z), J = \(J)"];
```
