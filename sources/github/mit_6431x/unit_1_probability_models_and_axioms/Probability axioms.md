The construction of a sample space which is a description of the possibility of outcomes of a probabilistic space.

Event: A subset of sample space
-  The probability is assigned to events
	-  $P(A)$ is the probability of a subset A in a sample space, all probabilities are in a range of [0,1]
		- $P(A)$ basically say, "The probability of an event A"
Axioms:
- Non negativity: $P(A)\geq 0$ 
- Normalization: $P(\Omega) = 1$ , given that $\Omega$ is the total sample space
- (Finite) additivity: If $A\cap B=Ø$ , then $P(A\cup B) = P(A) + P(B)$ . Ø is an empty set

### Simple consequences of the axioms

$$
A\cup A^c = \Omega
$$
$$
A\cap A^c = Ø
$$
$$
1 = P(\Omega) = P(A\cup A^c)
$$
$$
1 = P(A) + P(A^c) 
$$
$$
P(A)=1 - P(A^c) \leq 1
$$
$$
1 = P(\Omega) + P(\Omega^c)
$$
$$
1 = 1 + P(Ø)
$$
$$
P(Ø) = 0
$$
_____________________________
If $A_1, ... , A_k$ are disjoint then:
$$
P(A_1\cup...A_k) = \sum_{i=1}^kP(A_i)
$$
### More consequences of the axioms
$$
If A \subset B,\  then \ P(A) \leq P(B) 
$$
$$
P(A\cup B) = P(A) + P(B) - P(A\cap B)
$$
$$
P(A\cup B) \leq P(A) + P(B), \ (aka, the\ union\ bound)
$$
$$
P(A\cup B \cup C) = P(A)+P(A^c\cap B) + P(A^c\cap B^c \cap C)
$$
