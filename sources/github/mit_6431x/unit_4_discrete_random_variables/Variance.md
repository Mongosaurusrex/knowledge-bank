Variance is a measure of the spread or dispersion of a probability mass function (PMF) that quantifies how much the values of a random variable deviate from their mean (expected value). It is calculated as the expected value of the squared deviations from the mean, capturing the average of these squared differences. A larger variance indicates that the values are more spread out from the mean, showing higher variability, while a smaller variance suggests that the values are closer to the mean, indicating lower variability. Variance is essential in understanding the consistency and predictability of a random variable’s outcomes.

>[!info]  Definition of variance
>$$var(X)=E[(X-\mu)^2]$$
>$$Useful\ formula:\ var(X)=E[X^2]-(E[X])^2$$
## Properties of the variance
$$
var(aX+b)=a^2var(X)
$$
## Variance of the Bernoulli random variable
The variance of a Bernoulli random variable captures the variability of the outcomes (successes and failures) in a single trial.

For a Bernoulli random variable X, which takes the value 1 with probability p (success) and 0 with probability 1 - p (failure), the variance is given by:
$$\text{Var}(X) = p(1 - p).$$
Key Points:
•	Mean (\mu): For a Bernoulli random variable, the mean is \mu = p.
•	Variance Formula: The variance measures how much the values (0 and 1) deviate from the mean. Since X can only take two values, the spread depends on how balanced the probabilities p and 1 - p are.
•	Behavior: Variance is highest when  p = 0.5 , indicating maximum spread (equal likelihood of success and failure). It decreases as p moves closer to 0 or 1, reflecting lower variability when one outcome dominates.

The variance of a Bernoulli random variable succinctly quantifies the uncertainty or unpredictability of a single binary event.

## Variance of the Uniform random variable
The variance of a discrete Uniform random variable also measures the spread of its possible values around the mean, but since the variable takes on a finite set of equally likely values, the derivation differs slightly from the continuous case.

### Discrete Uniform Distribution

For a discrete Uniform random variable $(X)$, it takes on $(n)$ equally likely values, say $( 1, 2, 3, \ldots, n )$. Each value has an equal probability of $(\frac{1}{n})$.

### Variance of \( X \)

The variance of $(X)$ denoted $(\text{Var}(X))$, is given by:
$$
\text{Var}(X) = E[X^2] - (E[X])^2
$$

1. **Finding the Mean \( E[X] \):**

   The expected value (mean) of $(X)$ is:$$
   E[X] = \frac{1}{n} \sum_{k=1}^{n} k = \frac{1}{n} \cdot \frac{n(n+1)}{2} = \frac{n + 1}{2}
   $$

2. **Finding $E[X^2]$:**

   The expected value of $( X^2 )$ is:   $$
   E[X^2] = \frac{1}{n} \sum_{k=1}^{n} k^2 = \frac{1}{n} \cdot \frac{n(n+1)(2n+1)}{6}
   $$
3. **Variance $Var(X)$:**

   Plug $E[X]$ and $E[X^2]$ into the variance formula:$$
   \text{Var}(X) = E[X^2] - (E[X])^2 = \frac{(n+1)(2n+1)}{6} - \left(\frac{n + 1}{2}\right)^2
   $$

   Simplifying this expression:$$
   \text{Var}(X) = \frac{n^2 - 1}{12}
   $$Thus, the variance of a discrete Uniform random variable with values from \( 1 \) to \( n \) is:$$
\text{Var}(X) = \frac{n^2 - 1}{12}
$$This result shows that the variance increases as $n$ increases, reflecting the greater spread of values when there are more possible outcomes.

4. **Alternative**:
$$
Var(X) = \frac{1}{12}(b-a)(b-a+2)
$$
 ## Useful stuff:
Let say that you scale the mean by the constant $c$ then the variance is:
$$
Var(cX)=E[(c(X-E[X]))^2] = c^2E[(X-E[X])^2]=c^2Var(X)
$$
Given this proof, we can then say that for instance when $X=\{0,2,4,\dots,2n\}, Y=X/2$:
$$
Var(Y)=\frac{n(n+2)}{12}\to Var(X) = Var(2Y) = 2^2*Var(Y)=4*\frac{n(n+2)}{12}=\frac{n(n+2)}{3}
$$