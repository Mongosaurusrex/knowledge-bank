A standard way of describing this is by:
$$
f_{X|A}(x)= P(x\leq X\leq x+\delta\ |\ A)
$$
$$
P(X\in B)=\int_Bf_X(x)dx
$$
$$
P(X\in B | A)= \int_Bf_{X|A}(x)dx
$$
$$
\int f_{X|A}(x)dx = 1
$$

>[!important] Definition
>$$f_{X|X\in A}(x) = 
>\begin{cases}
>0,\ if\ x\notin A,
>\frac{f_X(x)}{P(A)},\ if\ x\in A
>\end{cases}$$

