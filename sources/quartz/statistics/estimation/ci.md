# Confidence Intervals (CIs)

Slug: Statistics/Estimation/ci

Links: Statistics/Distributions/bernoulli, Statistics/Distributions/binomial, Statistics/Hypothesis-Testing/walds-test

A confidence inteval (CI) provides a range of plausible values for an unknown parameter, based on sample data.
a (1-\alpha) CI means that if we were to repeat the experiment many times, about (1-\alpha)\times 100\% of the constructed intervals would contain the true parameter.
General Definition
If \hat{\theta} is an estimator of \theta and SE(\hat{\theta}) is its standard error, then:
\hat{\theta} \pm z_{1-\alpha/2} \cdot SE(\hat{\theta})
is a common (1-\alpha) CI under large-sample normal approximations.  
But there are different ways to derive these intervals.
1. Conservative Bound Method
This method uses simple inequalities (like Chebyshev’s or Hoeffding’s inequality) that hold without assuming normality.  
Example (Bernoulli p):  
By Hoeffding’s inequality,
P\!\left( |\hat{p} - p| &gt; \varepsilon \right) \leq 2 \exp(-2n \varepsilon^2)
So, with probability at least 1-\alpha:
|\hat{p} - p| \leq \sqrt{\frac{1}{2n} \log \frac{2}{\alpha}}
This gives a conservative CI:
\left[\hat{p} - \sqrt{\tfrac{1}{2n}\log \tfrac{2}{\alpha}}, \; \hat{p} + \sqrt{\tfrac{1}{2n}\log \tfrac{2}{\alpha}} \right]
This method is always valid, but often too wide (over-conservative).
2. Quadratic Equation Method (Exact / Inversion)
We invert the test:  
For each candidate \theta_0, ask whether H_0: \theta=\theta_0 would be rejected at level \alpha.  
The set of all \theta_0 not rejected forms the CI.
Example (Binomial proportion p):  
The Wald test statistic is
W = \frac{\hat{p} - p}{\sqrt{p(1-p)/n}}
We want all p such that
\left| \frac{\hat{p} - p}{\sqrt{p(1-p)/n}} \right| \leq z_{1-\alpha/2}
Squaring and rearranging leads to a quadratic inequality in p.  
Solving this quadratic gives exact interval:
p \in [0,1] : \text{inequality holds}
This method is precise, but algebraically heavier. Often implemented in software.
3. Plug-In (Wald) Method
Here we approximate the variance of \hat{\theta} by plugging in \hat{\theta} itself.  
For a sample proportion \hat{p}:
SE(\hat{p}) \approx \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}
So the (1-\alpha) CI is:
\hat{p} \pm z_{1-\alpha/2} \cdot \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}
This method is very common, yet simple. Works well for large n and p not too close to 0 or 1. Can perform poorly for small n or extreme p.