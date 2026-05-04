A Geometric random variable is used in probability theory to model the number of trials needed to get the first success in a sequence of independent and identically distributed (i.i.d.) Bernoulli trials (where each trial has two possible outcomes: success or failure). Here’s a concise summary:

Key Concepts of Geometric Random Variables:

1.	**Definition**: A Geometric random variable,  X , represents the number of trials until the first success occurs.
2.	**Probability Mass Function (PMF)**:
	•	The probability that the first success occurs on the  k -th trial is given by: $P(X = k) = (1 - p)^{k-1} p$
3.	**Expectation and Variance**:
	•	Expected Value (Mean): $E(X) = \frac{1}{p}$ . This means, on average, it takes  $\frac{1}{p}$  trials to get the first success.
	•	Variance: $\text{Var}(X) = \frac{1 - p}{p^2}$ .
4. **Memoryless Property**: Geometric random variables have a memoryless property, meaning the probability of success on the next trial is independent of how many failures have already occurred.

2. **Applications**: Geometric distributions are commonly used in scenarios where you want to model the waiting time until the first occurrence of an event, such as the first heads in a sequence of coin tosses, or the first defective item in a manufacturing process.
