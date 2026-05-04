
![[Pasted image 20241010161233.png]]We used to calculate a discrete random variable's expectation/mean with a sum but with continuous variables the mean is now an integral

**Interpretation**: Average in large number of independent repetitions of the experiments

## Properties of expectation
 - If $X \geq 0$, then $E[X] \geq 0$
 - If $a \leq X \leq b$, then $a \leq E[X] \leq b$ 
 - Expected value rule:
	 - $E[g(x)] = \int_\infty^{-\infty}g(x)f_X(x)dx$ 
	 - F.e  $E[x^2] = \int_\infty^{-\infty}x^2f_X(x)dx$ 

## Variance
Remains as previous:
$$
var(X)=E[X^2]-(E[X])^2
$$
Standard deviation:
$$
\delta_X=\sqrt{var(X)}
$$
## Continuous uniform random variable:
![[Pasted image 20241010164949.png]]

## Exponential random variable
![[Pasted image 20241010170013.png]]