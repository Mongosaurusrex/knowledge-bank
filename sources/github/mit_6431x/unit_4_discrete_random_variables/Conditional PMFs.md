A **Conditional Probability Mass Function (Conditional PMF)** provides the probability distribution of a discrete random variable given that another related event or random variable has occurred. 

If $X$ and $Y$ are two discrete random variables, the conditional PMF of $X$ given $Y = y$ is defined as $P(X = x | Y = y) = \frac{P(X = x, Y = y)}{P(Y = y)}$, assuming $P(Y = y) > 0$. 
The conditional PMF adjusts the original PMF of $X$ by focusing only on the scenario where $Y = y$ has happened, effectively narrowing the possible outcomes of $X$ to those consistent with this condition. Conditional PMFs are useful in scenarios where two or more random variables are interdependent, and one is trying to understand the distribution of one variable under specific outcomes of the other.

### Useful similarities
$$
\sum_x p_{X|Y}(x|y) = 1
$$
$$
p_{X|Y,Z}(x|y,z) = P(X=x|Y=y, Z=z)=\frac{P(X=x, Y=y, Z=z)}{P(Y=y,Z=z)}=\frac{p_{X,Y,Z}(x,y,z)}{p_{Y,Z}(y,z)}
$$
$$
p_{X,Y,Z}(x,y,z)=p_X(x)p_{Y|X}(y|x)p_{Z|X,Y}(z|x,y)
$$
## Conditional Expectations
Conditional expectation is the expected value (mean) of a random variable given that certain conditions or events are known to have occurred. If  X  is a random variable and  Y  is another random variable or event, the conditional expectation of  $X$  given  $Y = y$ , denoted as $E[X | Y = y]$, represents the average or expected value of  $X$  when we know that  $Y$  takes on the value  $y$ . The conditional expectation incorporates the knowledge of $Y$, updating the expectation of  $X$  based on this information.
$$
E[X]=\sum_xxp_X(x),\ E[X|A]=\sum_xxp_{X|A}(x),\ E[X|Y=y]=\sum_xxp_{X|Y}(x|y)
$$

## Total probability theorem
The Total Probability Theorem relates to how the probability of an event can be calculated by breaking it down into a collection of mutually exclusive events. If  $B_1, B_2, …, B_n$  form a partition of the sample space (i.e., they are mutually exclusive and exhaustive events), and  $A$  is some event, the total probability of  $A$  can be found using:
$$P(A) = \sum_{i=1}^{n} P(A | B_i) P(B_i)$$
This theorem is useful when it’s easier to compute conditional probabilities of  A  given different scenarios  $B_i$ . By using the weighted sum of these conditional probabilities, we account for the total probability of  A  across all possible conditions.

## Total Expectation Theorem (Law of Total Expectation)

The Total Expectation Theorem, also called the Law of Total Expectation, allows us to compute the expected value of a random variable  $X$  by conditioning on another random variable  $Y$ . Formally, it states:
$$E[X] = E[E[X | Y]]$$
This means that the expected value of  X  can be found by first calculating the conditional expectation  $E[X | Y = y]$  for each possible value $y$  of  $Y$ , and then taking the expectation of this conditional expectation over the distribution of  $Y$ . Essentially, the total expectation is the “weighted average” of the conditional expectations, where the weights are determined by the distribution of  $Y$ .