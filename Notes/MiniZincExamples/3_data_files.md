# Data Files
Can specify data files with values for variables

armyd.mzn
```
int: budget;
var 0..1000: F;
var 0..400: L;
var 0..500: Z;
var 0..150: J;

constraint 13*F + 21*L + 17*Z + 100*J <= budget;

solve maximize 6*F + 10*L + 8*Z + 40*J;

output ["F = \(F), L = \(L), Z = \(Z), J = \(J)"];
```

Can have a single line in `army.dzn` as `budget = 20000;`
* then call `minizinc armyd.mzn army.dzn`

Can also call without a data file
* `minizinc armyd.mzn -D"budget = 20000;"`

### Money Lending Example
The money lenders will lend an amount `P` the principal which is the initial balance
* every quarter they require a regular repayment `R`
* the quarterly interest rate is `I`
* at the end of the `i`th quarter the balance owing `Bi` is given by
  * the previous balance
  * plus the interest on the previous balance
  * minus the repayment

loan.mzn
```
var float: R;
var float: P;
var 0.0 .. 2.0: I

var float: B1;
var float: B2;
var float: B3;
var float: B4;

constraint B1 = P * (1.0 + I) - R;
constraint B2 = B1 * (1.0 + I) - R;
constraint B3 = B2 * (1.0 + I) - R;
constraint B4 = B3 * (1.0 + I) - R;

solve satisfy;
```

Now can specify different data files to ask different questions
* ie. fix `R`, `P`, and `I` and ask how much owing at the end (the value of `B4`)
* or fix `R`, `I` and want `B4 = 0` (no owing), how much can be borrowed
