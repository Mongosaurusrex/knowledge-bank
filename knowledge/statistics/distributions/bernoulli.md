# Bernoulli Distribution

Slug: Statistics/Distributions/bernoulli

Links: Statistics/Distributions/binomial, Statistics/Distributions/beta, Statistics/Bayesian-Statistics/bayesian-inference

The Bernoulli distribution is one of the simplest and most fundamental probability distributions. It models a binary outcome — success or failure, yes or no, 1 or 0.
Definition
A random variable X follows a Bernoulli distribution with parameter p \in [0,1] if:
\mathbb{P}(X = 1) = p, \quad \mathbb{P}(X = 0) = 1 - p
We write this as:
X \sim \text{Bernoulli}(p)
Probability Mass Function (PMF)
f(x \mid p) = p^x (1 - p)^{1 - x}, \quad x \in \{0, 1\}
Support
x \in \{0, 1\}, \quad p \in [0, 1]
Expectation
\mathbb{E}[X] = p
Variance
\\text{Var}(X) = p(1 - p)
Maximum Likelihood Estimation (MLE)
Given n i.i.d. observations X_1, \dots, X_n \sim \text{Bernoulli}(p), the likelihood is:
L(p) = \prod_{i=1}^n p^{x_i} (1 - p)^{1 - x_i}
Taking logs:
\log L(p) = \left( \sum x_i \right) \log p + \left( n - \sum x_i \right) \log(1 - p)
First derivative:
\frac{d}{dp} \ell(p) = \frac{S}{p} - \frac{n - S}{1 - p}
Second derivative:
\frac{d^2}{dp^2} \ell(p) = -\frac{S}{p^2} - \frac{n - S}{(1 - p)^2}
Setting the first derivative to zero and solving yields the MLE:

\hat{p}_{\text{MLE}} = \frac{1}{n} \sum_{i=1}^n X_i

Fisher Information
The Fisher information for one observation is:
I(p) = -\mathbb{E} \left[ \frac{d^2}{dp^2} \log f(X \mid p) \right] = \frac{1}{p(1 - p)}
This means:

Information is highest near p = 0 or p = 1
Information is lowest at p = 0.5, where outcomes are most unpredictable

Applications

Coin flips
Binary classification
Modeling individual trials in a Binomial or logistic regression framework

Related Distributions

Binomial: sum of independent Bernoulli trials
Beta: conjugate prior for p in Bayesian analysis
