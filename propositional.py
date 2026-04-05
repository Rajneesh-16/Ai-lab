import sympy
from sympy.logic.boolalg import And, Or, Not, Implies, Equivalent
from sympy.logic.inference import satisfiable

# Define variables
p, q, r = sympy.symbols('p q r')

# Define propositions
prop1 = p
prop2 = Not(p)
prop3 = And(p, q)
prop4 = Or(p, q)
prop5 = Implies(p, q)
prop6 = Equivalent(p, q)

# Laws
prop7 = Or(p, Not(p))          # Excluded middle
prop8 = And(p, Not(p))         # Contradiction
prop9 = And(p, p)              # Identity
prop10 = Or(p, p)

# Commutative
prop11 = Equivalent(Or(p, q), Or(q, p))
prop12 = Equivalent(And(p, q), And(q, p))

# Associative
prop13 = Equivalent(Or(p, Or(q, r)), Or(Or(p, q), r))
prop14 = Equivalent(And(p, And(q, r)), And(And(p, q), r))

# Distributive
prop15 = Equivalent(Or(p, And(q, r)), And(Or(p, q), Or(p, r)))

# Assign values
values = {p: True, q: False}

# Evaluate
print("p =", values[p], "q =", values[q])
print("p AND q =", prop3.subs(values))
print("p OR q =", prop4.subs(values))
print("p → q =", prop5.subs(values))

# Check satisfiability
print("Satisfiable (p AND q):", satisfiable(prop3))

# CNF & DNF
print("DNF:", sympy.to_dnf(prop4))
print("CNF:", sympy.to_cnf(prop4))
'''p = True q = False
p AND q = False
p OR q = True
p → q = False
Satisfiable (p AND q): {p: True, q: True}
DNF: p | q
CNF: p | q'''