from pyDatalog import pyDatalog

pyDatalog.clear()

# ---------------- BASIC FACTS ----------------
pyDatalog.create_terms('has_leg, likes, brother_of, X, Y, Z')
+has_leg('John')
+likes('Raju','fish')
+brother_of('Raju','Rani')

print(has_leg(X))
print(likes('Raju',Y))
print(brother_of('Raju',Z))


# ---------------- EMPLOYEE DATA ----------------
pyDatalog.create_terms('employee, salary')
+employee('Alice',50000)
+employee('Bob',60000)

print(employee(X,Y))


# ---------------- ANCESTOR ----------------
pyDatalog.create_terms('parent, ancestor')
+parent('alex','sharon')
+parent('sharon','Charlie')

ancestor(X,Y) <= parent(X,Y)
ancestor(X,Y) <= (parent(X,Z) & ancestor(Z,Y))

print(ancestor(X,'Charlie'))


# ---------------- GRANDPARENT ----------------
pyDatalog.create_terms('grandparent')
+parent('Alan','Bobby')
+parent('Bobby','ange')
+parent('ange','Danny')

grandparent(X,Y) <= (parent(X,Z) & parent(Z,Y))

print(grandparent(X,Y))


# ---------------- VOTING ELIGIBILITY ----------------
pyDatalog.create_terms('age, citizen, can_vote, A')
+age('Alice',20)
+citizen('Alice','USA')
+age('JOHN',10)

can_vote(X) <= (age(X,A) & citizen(X,'USA') & (A>18))

print(can_vote(X))


# ---------------- LOW STOCK ----------------
pyDatalog.create_terms('has, low_stock, Q')
+has('ProductA',2)
+has('ProductB',5)
+has('ProductC',15)

low_stock(X) <= (has(X,Q) & (Q<10))

print(low_stock(X))


# ---------------- COURSE PREREQUISITE ----------------
pyDatalog.create_terms('enrolled, prerequisite, can_take')
+enrolled('Alice','Math101')
+enrolled('Alice','CS101')
+prerequisite('CS101','Math101')
+prerequisite('Math101','Math102')

can_take('Alice',X) <= (enrolled('Alice',Y) & prerequisite(Y,X))

print(can_take('Alice',X))


# ---------------- KING & GREEDY ----------------
pyDatalog.create_terms('king, greedy, evil')
+king('john')
+greedy('john')
+king('jack')
+greedy('jack')
+king('tom')

evil(X) <= (king(X) & greedy(X))

print(evil(X))

'''X
----
John

Y
----
fish

Z
----
Rani

X      | Y
--------------
Bob    | 60000
Alice  | 50000

X
---------
alex
sharon

X      | Y
--------------
Alan   | ange
Bobby  | Danny

X
-----
Alice

X
---------
ProductA
ProductB

X
---------
Math101
Math102

X
-----
jack
john'''