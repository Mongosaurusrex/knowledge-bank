# Maximum Likelihood Estimation (MLE)

Slug: Statistics/Estimation/mle

Maximum Likelihood Estimation (MLE) is a method to estimate unknown parameters of a probability distribution or statistical model.  
The principle: choose the parameter values that make the observed data most likely.
Definition
Suppose we have independent observations x_1, x_2, \dots, x_n from a distribution with parameter \theta and probability density/mass function f(x \mid \theta).  
The likelihood function is:
L(\theta) = \prod_{i=1}^n f(x_i \mid \theta)
The MLE is the parameter value \hat{\theta} that maximizes L(\theta):
\hat{\theta} = \arg \max_{\theta} L(\theta)
Often, we maximize the log-likelihood instead:
\ell(\theta) = \log L(\theta) = \sum_{i=1}^n \log f(x_i \mid \theta)
Fisher Information
The Fisher Information measures how much information an observable random variable carries about an unknown parameter.  
It is defined as:

Equivalently:
I(\theta) = - \mathbb{E}\!\left[ \frac{\partial^2}{\partial \theta^2} \log f(X \mid \theta) \right]
Connection to MLE


For large samples, the MLE \hat{\theta} is approximately normally distributed:
\hat{\theta} \sim N\!\left( \theta, \, \frac{1}{n I(\theta)} \right)


The Fisher Information thus determines the variance of the MLE.  


A higher I(\theta) means the data provide more information about \theta, leading to a more precise estimate.


Example
Suppose we flip a coin n times and observe k heads.  
Let p = probability of heads.  
The likelihood is:
L(p) = p^k (1-p)^{n-k}
Log-likelihood:
\ell(p) = k \log p + (n-k) \log(1-p)
Differentiate and solve:
\frac{d\ell}{dp} = \frac{k}{p} - \frac{n-k}{1-p} = 0
\hat{p} = \frac{k}{n}
So the MLE of p is just the sample proportion of heads.
Properties of MLE

Consistency: \hat{\theta} \to \theta as n \to \infty.  
Asymptotic normality: For large n,  \hat{\theta} \sim N\!\left(\theta, \, \frac{1}{I(\theta)}\right)
  where I(\theta) is the Fisher information.  
Efficiency: Achieves the lowest possible variance asymptotically.

MLE Table of various distributions





















































































DistributionLikelihoodLog-LikelihoodFirst DerivativeSecond DerivativeMLE(Bernoulli(p))p^x (1-p)^{1-x}x \log p + (1 - x) \log(1 - p)\frac{x}{p} - \frac{1 - x}{1 - p}-\frac{x}{p^2} - \frac{1 - x}{(1 - p)^2}\hat{p} = \bar{X}_nBinomial(n, p)\binom{n}{x} p^x (1-p)^{n-x}\log \binom{n}{x} + x \log p + (n - x) \log(1 - p)\frac{x}{p} - \frac{n - x}{1 - p}-\frac{x}{p^2} - \frac{n - x}{(1 - p)^2}\hat{p} = \frac{x}{n}Poisson(λ)\frac{e^{-\lambda} \lambda^x}{x!}-\lambda + x \log \lambda - \log x!-1 + \frac{x}{\lambda}-\frac{x}{\lambda^2}\hat{\lambda} = \bar{X}_nUniform(a, b)\frac{1}{b-a} \mathbf{1}_{[a,b]}(x)-\log(b - a)00\hat{a} = \min x_i, \hat{b} = \max x_iGeometric(p)(1 - p)^{x - 1} p(x - 1) \log(1 - p) + \log p-\frac{x - 1}{1 - p} + \frac{1}{p}-\frac{x - 1}{(1 - p)^2} - \frac{1}{p^2}\hat{p} = \frac{1}{\bar{X}_n}Normal(μ, σ²)\frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x - \mu)^2}{2\sigma^2}}-\frac{1}{2} \log(2\pi\sigma^2) - \frac{(x - \mu)^2}{2\sigma^2}\frac{x - \mu}{\sigma^2}-\frac{1}{\sigma^2}\hat{\mu} = \bar{X}_n, \hat{\sigma}^2 = \frac{1}{n} \sum (x_i - \bar{X}_n)^2Exponential(λ)\lambda e^{-\lambda x}\log \lambda - \lambda x\frac{1}{\lambda} - x-\frac{1}{\lambda^2}\hat{\lambda} = \frac{1}{\bar{X}_n}Gamma(α, β)\frac{\beta^\alpha}{\Gamma(\alpha)} x^{\alpha - 1} e^{-\beta x}\alpha \log \beta - \log \Gamma(\alpha) + (\alpha - 1) \log x - \beta x\frac{\alpha}{\beta} - x(w.r.t β)-\frac{\alpha}{\beta^2} (w.r.t β)\hat{\beta} = \frac{\alpha}{\bar{X}_n}Neg. Binomial(r, p)\binom{x+r-1}{x} (1-p)^r p^x\log \binom{x+r-1}{x} + r \log(1 - p) + x \log p\frac{x}{p} - \frac{r}{1 - p}-\frac{x}{p^2} - \frac{r}{(1 - p)^2}\hat{p} = \frac{r}{r + \bar{X}_n}
Summary

MLE finds parameter values that maximize the likelihood of the observed data.  
Simple to apply to many models, though sometimes requires numerical optimization.  
Forms the basis for many other statistical methods (Wald test, likelihood ratio test, confidence intervals).
Fisher Information quantifies the precision of those estimates.
