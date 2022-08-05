# Constraint Programming
Computational paradigm
* use constraints to reduce the set of values that each variable can take
* remove values that cannot appear in any solution
* make a choice when no more deduction can be performed

Modeling methodology
* convey the structure of the problem as explicitly as possible
* express substructures of the problem
* give solvers as much information as possible

Branch and Prune
* pruning
  * reduce the search space as much as possible
  * use constraints to remove, from the variable domains, values that cannot belong to any solution
* branching
  * decomposes the problem into subproblems and explores the subproblems

Complete method, not a heuristic
* given enough time, it will find a solution to a satisfaction problem
* given enough time, it will find an optimal solution to an optimization problem

The focus is on feasibility
* how to use constraints to prune the search space by eliminating values that cannot belong to any solution

The algorithms use dedicated algorithms for each constraint
* they exploit the structure and properties of the constraint

The propagation engine
* the core of any constraint-programming solver
* a simple (fixpoint) algorithm
```
propagate() {
  repeat
    select a constraint c;
    if c is infeasible given the domain store then
      return failure;
    else
      apply the pruning algorithm associated with c;
  until no constraint can remove any value from the domain of its variables;
  return success;
}
```
