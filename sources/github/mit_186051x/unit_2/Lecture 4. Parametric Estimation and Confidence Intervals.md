2At the end of this lecture, you will be able to
- Distinguish between an **estimator** and a **statistic** .
- Compute the **bias** , **variance** , and **quadratic risk** of an estimator.
- Determine whether or not an estimator is **consistent** .
- Construct a confidence interval for an unknown parameter.
- Explain the frequentist interpretation of the confidence interval.

## Statistics, Estimators, Consistency and Asymptotic Normality
- Statistic: Any measurable function of the sample
- Estimator of $\theta$: Any statistic whose expression does not depend on $\theta$
- An estimator $\hat\theta_n$ of $\theta$ is weakly (resp. strongly) consistent if $$\hat\theta_n \to \theta,\quad (w.r.t\ \mathbb{P}_\theta)$$
- An estimator $\hat\theta_n$ of $\theta$ is asymptotically normal if$$\sqrt{n}(\hat\theta_n-\theta) \to N(0,\sigma^2)$$
## Bias Estimators and an application of Jensen's inequality
![[Pasted image 20250517153616.png]]

## Variance of estimators

We recall the following useful formulas for the variance. First if $X$ is a random variable, then the variance of is defined by$$Var[X] = E[(X-E[X])^2]$$
The following equivalent 'shortcut' is convenient when we already know the expectation of $X$:$$Var[X] = E[X^2]+(E[X])^2$$
 Finally, in the class we often compute the variance of averages of random variables. If $X_1,\dots,X_n$ are i.i.d. each with variance $\sigma^2$ then $$Var[\bar X_n] = \frac{\sigma^2}{n}$$
 ## Quadratic Risk of Estimators
![[Pasted image 20250517161123.png]]

 ## Confidence intervals
 ![[Pasted image 20250520080746.png]]
 ![[Pasted image 20250520082743.png]]![[Pasted image 20250520085002.png]]
 ![[Pasted image 20250520131310.png]]
![[Pasted image 20250520133246.png]]