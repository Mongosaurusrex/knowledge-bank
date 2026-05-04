Lets consider 3 tosses of a biased coin: P(H) = p, P(T) = 1 - p

![[Pasted image 20240911194533.png]]
Given the outcome of HHH we can model it like
$$
H \to P(H_1)
$$
$$
HH \to P(H_2 | H_1)
$$
$$
HHH \to P(H_3 | H_1 \cap H_2)
$$

### Multiplication rule
$$
P(THT) = (1-p)p(1-p)
$$
### Total probability
$$
P(1\ Head) = 3p(1-p)^2
$$
### Bayes rule
$$
P(first\ toss\ is\ H | 1\ head)= \frac{P(H_1 \cap 1\ head)}{P(1\ head)}= \frac{p(1-p)^2}{3p(1-p)^2}=\frac{1}{3}
$$
## Independence of two events
- Intuitive "definition": $P(B|A) = P(B)$
	-  Occurrence of A provides no new information about B
	$$
	P(A\cap B) = P(A)P(B|A) = P(A)P(B)
	$$
$$
Definition\ of\ independence: P(A\cap B) = P(A)*P(B)
$$
- Symmetric with respect to A and B
- Implies $P(A | B) = P(A)$
- Applies even if $P(A) = 0$ 
## Indepencende of two events complements
- If A and B are independent, then A and $B^c$ are independent
	- Intuitive argument

### Formal proof
$$
A=(A\cap B)\cup(A\cap B^c)
$$
$$
P(A) = P(A\cap B)+P(A\cap B^c) = P(A)P(B) +P(A\cap B^c)
$$
$$
P(A\cap B^c) = P(A) - P(A)P(B) = P(A)(1 - P(B)) = P(A)P(B^c)
$$
