# Walds Test

Slug: Statistics/Hypothesis-Testing/walds-test

The Wald test is a general method for testing hypotheses about model parameters, especially in maximum likelihood estimation (MLE).  
It compares an estimated parameter to a hypothesized value, standardized by its estimated standard error.
Definition
Suppose \hat{\theta} is the maximum likelihood estimator of a parameter \theta, and SE(\hat{\theta}) is its estimated standard error.  
The Wald test statistic is:W = \frac{\hat{\theta} - \theta_0}{SE(\hat{\theta})}

Under the null hypothesis H_0: \theta = \theta_0, the statistic W approximately follows a standard normal distribution N(0,1).  
For two-sided tests, we often look at W^2, which approximately follows a \chi^2_1 distribution.

Hypotheses

H_0: \theta = \theta_0  
H_1: \theta \neq \theta_0 (two-sided)  
  or H_1: \theta &gt; \theta_0, H_1: \theta &lt; \theta_0 (one-sided).

Example
Suppose we observe a sample of patient waiting times:

Sample size: n = 25  
Sample mean: \hat{\mu} = 31 minutes  
Sample standard deviation: s = 10 minutes  

We want to test:  

H_0: \mu = 30  
H_1: \mu \neq 30  

Step 1. Compute the standard error  
The standard error of the sample mean is
SE(\hat{\mu}) = \frac{s}{\sqrt{n}} = \frac{10}{\sqrt{25}} = 2
Step 2. Wald statistic
W = \frac{\hat{\mu} - \mu_0}{SE(\hat{\mu})} 
= \frac{31 - 30}{2} 
= 0.5
Step 3. Approximate distribution

Under H_0, W \sim N(0,1).  

Step 4. p-value
p = 2 \times P(Z &gt; 0.5) \approx 0.62
Decision: At \alpha = 0.05, do not reject H_0.
Summary

The Wald test standardizes the difference between an estimate and its hypothesized value.  
Here, the standard error came from the formula SE(\hat{\mu}) = s/\sqrt{n}.  
Interpretation is the same as other test statistics: large |W| → stronger evidence against H_0.  
Limitation: accuracy can be poor in small samples or near parameter boundaries.
