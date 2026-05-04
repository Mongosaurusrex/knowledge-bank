# Bayes' Theorem

Slug: Statistics/Bayesian-Statistics/bayes-theorem

When you’re talking about statistics, it’s impossible not to see the direct connection to probability. And in probability, few tools are as central—or as powerful—as Bayes’ Theorem.
Bayes’ Theorem provides a principled way to update our beliefs in light of new evidence. It combines prior knowledge with new data to produce a posterior belief—making it invaluable in science, machine learning, and even everyday reasoning.
The theorem
Mathematically, Bayes’ Theorem is written as:

P(A \mid B) = \frac{P(B \mid A) \cdot P(A)}{P(B)}

Where:

P(A) is the prior probability of A, our initial belief.
P(B \mid A) is the likelihood, the probability of observing B given that A is true.
P(B) is the evidence, the total probability of observing B under all possible hypotheses.
P(A \mid B) is the posterior: the updated belief about A after observing B.

This formula essentially tells us: how should we revise our belief about A after seeing B
Example
Suppose a certain disease affects 1% of the population. A test for the disease is 99% accurate, meaning:

If someone has the disease, the test returns positive 99% of the time.
If someone does not have the disease, it returns negative 99% of the time.

Now, imagine you take the test and get a positive result. What is the probability you actually have the disease?
Let:

D = you have the disease
T = test result is positive

We want to compute P(D \mid T), the probability of disease given a positive test.
Using Bayes’ Theorem:

P(D \mid T) = \frac{P(T \mid D) \cdot P(D)}{P(T)}

We know:

P(D) = 0.01
P(T \mid D) = 0.99
P(T \mid \neg D) = 0.01
P(\neg D) = 0.99

Then:

P(T) = P(T \mid D) \cdot P(D) + P(T \mid \neg D) \cdot P(\neg D) \

= 0.99 \cdot 0.01 + 0.01 \cdot 0.99 = 0.0198

So:

P(D \mid T) = \frac{0.99 \cdot 0.01}{0.0198} \approx 0.5

Surprisingly, even with a positive test, you only have about a 50% chance of actually having the disease! That’s the power of Bayes: it forces you to account for the base rate.