# Prior

Slug: Statistics/Bayesian-Statistics/bayesian-prior

Links: Statistics/Distributions/beta, Statistics/Distributions/bernoulli, Statistics/Distributions/binomial

What Is a Prior?
The prior expresses uncertainty about the true value of a parameter \theta before any data is observed. It captures our beliefs or assumptions, which may be based on:

Expert knowledge
Historical data
Symmetry or intuition
Or simply a desire to remain vague

Priors can be:

Informative, when we have strong beliefs or prior evidence.
Weakly informative or non-informative, when we prefer to let the data drive inference.

The strength of the prior affects how much influence the data has—stronger priors can pull the posterior toward prior beliefs, especially in small-sample settings.
Example: Kiss Study
Suppose we believe p, the probability that a couple turns right when kissing, is close to 0.5, but we are somewhat uncertain.
We could encode this belief with a Beta(5, 5) prior, which is centered at 0.5 and expresses moderate confidence. This allows observed data to meaningfully update our belief while still reflecting our initial assumption.
The Jeffreys Prior
When we lack strong prior knowledge and wish to remain as objective as possible, we can use the Jeffreys prior. It is a type of non-informative prior derived from the Fisher information and has the appealing property of being invariant under reparameterization.
The general form the Jeffrey prior is:
\pi_J(\theta) \propto \sqrt{I(\theta)} = \sqrt{ -\mathbb{E} \left[ \frac{\partial^2}{\partial \theta^2} \log f(X \mid \theta) \right] }
For the Bernoulli/Binomial case (like the kiss study), the Jeffreys prior for the parameter p is:

\pi(p) \propto \frac{1}{\sqrt{p(1 - p)}} \quad \Rightarrow \quad \text{Beta}\left(\tfrac{1}{2}, \tfrac{1}{2}\right)

This prior is more diffuse near 0 and 1, reflecting greater uncertainty in extreme values and giving slightly more weight to those possibilities than a uniform prior.
Common Jeffreys Priors


















































Likelihood / ModelParameter(s)Jeffreys PriorBernoulli/Binomialp \in (0, 1)\pi(p) \propto \dfrac{1}{\sqrt{p(1 - p)}}Poisson\lambda &gt; 0\pi(\lambda) \propto \dfrac{1}{\sqrt{\lambda}}Exponential\lambda &gt; 0\pi(\lambda) \propto \dfrac{1}{\lambda}Normal (known variance)\mu \in \mathbb{R}\pi(\mu) \propto 1Normal (known mean)\sigma^2 &gt; 0\pi(\sigma^2) \propto \dfrac{1}{\sigma^2}Normal (unknown mean and variance)(\mu, \sigma^2)\pi(\mu, \sigma^2) \propto \dfrac{1}{\sigma^2}Uniform [0, \theta]\theta &gt; x_{\\text{max}}\pi(\theta) \propto \dfrac{1}{\theta}Multinomial\vec{p} \in \Delta_k\pi(\vec{p}) \propto \left( \prod_{i=1}^k p_i \right)^{-1/2}