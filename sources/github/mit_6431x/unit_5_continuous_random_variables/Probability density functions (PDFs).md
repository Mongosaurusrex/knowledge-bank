![[Pasted image 20241008181614.png]]
Instead of looking at probabilities with a discrete probabilistic model, probabilities that are continuous and can be described by a function of the real line $x$ are written as $f_X(x)$ 
Lets say that we want to model the probability that $P(a\leq X \leq b)$ then that is:
$$
P(a\leq X \leq b) = \int_a^bf_X(x)dx
$$
In the discrete PMFs we get that:
$$
\sum_xp_X(x)=1, p_X(x)\geq0
$$
But in the PDFs we get:
$$
\int_{-\infty}^{\infty}f_X(x)dx=1, f_X(x)\geq1
$$
>[!info] Definition of continious variables
>**A random variable is continious if it can be described by a PDF**

![[Pasted image 20241008182813.png]]
If we were to calculate $P(a\leq x \leq a+\delta)$ : 
$$
P(a\leq x \leq a+\delta)\approx f_X(a)*\delta 
$$
Also worth noting:
$$
P(X=a) = 0
$$
![[Pasted image 20241008202230.png]]
PDFs don't need to be continious functions