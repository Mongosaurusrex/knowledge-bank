# Bayesian Statistics

Slug: Statistics/Bayesian-Statistics/bayesian-inference

Links: Statistics/Bayesian-Statistics/bayesian-prior, Statistics/Bayesian-Statistics/bayesian-posterior, Statistics/Bayesian-Statistics/bayes-theorem

The core idea behind Bayesian inference is to update our beliefs about an unknown parameter \theta after observing data. This is done by combining a likelihood function L_n(\theta) with a prior distribution \pi(\theta)—which reflects our initial beliefs about \theta—to obtain a posterior distribution, representing our updated beliefs.
In many real-world situations, we have some prior knowledge about the unknown parameter \theta. This may come from expert opinion, historical data, previous studies, or even subjective judgment.
After observing new data, we use this information to update our prior belief into a posterior belief through Bayes’ theorem.
Bayes formula
The Bayes formula states:
\pi(\theta \mid X_1, \ldots, X_n) \propto \pi(\theta) L_n(X_1, \ldots, X_n \mid \theta), \quad \forall \theta \in \Theta
This means the posterior is proportional to the product of the prior and the likelihood. The constant of proportionality ensures that the posterior is a valid probability distribution (i.e., it integrates to 1).
The full expression includes a normalization constant in the denominator:
\pi(\theta \mid X_1, \ldots, X_n) = \frac{\pi(\theta) L_n(X_1, \ldots, X_n \mid \theta)}{\int_\Theta \pi(\theta) L_n(X_1, \ldots, X_n \mid \theta) d\theta}, \quad \forall \theta \in \Theta
The denominator ensures that the posterior distribution is properly scaled—it integrates to 1—but it does not generally equal 1 by itself. Instead, it plays a crucial role in turning the unnormalized posterior into a valid probability density function.
Example: The Kiss study
We are interested in the proportion p of couples that turn their heads to the right when kissing.

Let the data be X_1, \dots, X_n \overset{i.i.d}{\sim} \text{Ber}(p)

Frequentist Approach:

Estimate p using MLE
Construct confidence intervals for p
Perform hypothesis testing, e.g.
H_0: p = 0.5 vs. H_1: p \ne 0.5

Bayesian Insight:

Before seeing the data, we may believe p \approx \frac{1}{2}
Use the Bayesian approach to update that prior belief into a posterior using observed data
