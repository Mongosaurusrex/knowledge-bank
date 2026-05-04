1. **Geometric PMF (Probability Mass Function):**

The Geometric Distribution models the number of trials until the first success in a sequence of independent and identical Bernoulli trials (think coin flips where each flip has the same probability of success).

•	The probability mass function (PMF) gives the probability that the first success happens on the k-th trial.
•	If the probability of success on any trial is p, then the PMF of a Geometric random variable X (the trial number of the first success) is:
$$
P(X = k) = (1 - p)^{k-1} \cdot p
$$

•	p is the probability of success on any given trial.
•	$(1 - p)^{k-1}$ is the probability that the first k-1 trials were failures, and the k-th trial is a success.

So the geometric distribution is all about “how many trials until the first success?”

2. **Memorylessness**:

The memorylessness property means that the probability of success from any point onward does not depend on what has happened before.

•	For example, if we are flipping a coin, and we know that the first few flips were failures, the probability of success on the next flip is still the same as it was in the beginning.

Mathematically, for a Geometric random variable X, memorylessness means:
$$P(X > n + k \mid X > n) = P(X > k)$$
This means that if you’ve already had n failures, the probability that you still need more than k additional trials for success is the same as it was at the start.

3. **Expectation (Mean)**:

The expectation (or mean) of a Geometric random variable tells us, on average, how many trials it takes to get the first success.

•	For a Geometric distribution with probability of success p, the expected number of trials until the first success is:
$$E[X] = \frac{1}{p}$$
This means if the probability of success is p, on average, it will take 1/p trials to get the first success. For example, if p = 0.2 (20% chance of success), you can expect the first success to happen after about 5 trials on average.

In summary:

•	The PMF tells us the probability of the first success on a specific trial.
•	Memorylessness means past failures don’t affect future success probabilities.
•	The expectation is the average number of trials it takes to get the first success.