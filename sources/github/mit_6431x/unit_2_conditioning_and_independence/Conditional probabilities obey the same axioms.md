## Examples:
$$P(A|B) \geq 0\ assuming\ P(B) > 0$$ 
$$P(\Omega|B) = \frac{P(\Omega \cap B)}{P(B)}=\frac{P(B)}{P(B)}= 1$$
$$P(B|B) = \frac{P(B\cap B)}{P(B)} = 1$$
$$A \cap C = \emptyset,\ then\ P(A\cup C|B)=P(A|B) + P(C|B)$$
### Radar example
Event A: Airplane is flying above
Event B: Something registers on the radar screen


```mehrmaid
graph TD
R -- "$0.05$" ---A
R -- "$0.95$" ---B
A -- "$0.99$" ---C
A -- "$0.01$" ---D
B -- "$0.10$" ---E
B -- "$0.90$" ---F
R(("*"))
A(("$A$"))
B(("$A^c$"))
C(("$A\cap B$"))
D(("$A\cap B^c$ (Miss)"))
E(("$A^c \cap B$ (False alarm)"))
F(("$A^c \cap B^c$ "))
```
$$
P(A\cap B) = P(A)* P(B|A) = 0.05*0.99 = 0.0495
$$
$$
P(B) = (0.05 * 0.99) + (0.95 * 0.10) = 0.1445
$$
$$
P(A|B)= \frac{0.05 * 0.99}{0.1445} = 0.34
$$
### The multiplication rule
$$
P(A|B) = \frac{P(A\cap B)}{P(B)}
$$
$$
P(A\cap B) = P(B)*P(A|B) = P(A)*P(B|A)
$$
$$
P(A_1\cap A_2 \cap \dots \cap A_n)=P(A_1) \prod_{i=2}^n P(A_i | A_1 \cap \dots \cap A_{i-1})
$$
