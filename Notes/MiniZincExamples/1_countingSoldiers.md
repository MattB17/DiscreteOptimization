### Coutning Soldiers
We initially had less than 800 soldiers in our army but some fled
* arranging the remaining into rows of length 5 leaves 2 out
* arranging the remaining into rows of length 7 leaves 2 out
* arranging the remaining into rows of length 12 leaves 1 out

count.mzn
```
var 100..800: army

constraint army mod 5 = 2;
constraint army mod 7 = 2;
constraint army mod 12 = 1;

solve satisfy;
```

`minizinc --all-solutions count.mzn` will print all solutions
