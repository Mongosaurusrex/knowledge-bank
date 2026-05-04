At the end of this lecture, you will be able to compute the maximum likelihood estimator in a variety of models including: Bernoulli, Poisson, Gaussian, Uniform.

You will also learn about mixtures of Gaussians as a flexible statistical model and you will be able to apply the Expectation-Maximization (EM) algorithm to compute the maximum likelihood estimator in this model.

## Bernoulli estimator

**Likelihood:**
$$L(p) = p^{\sum x_i}(1-p)^{n-\sum x_i}$$
**Log-Likelihood:**
$$\log L(p) = \left( \sum x_i \right) \log p + \left( n - \sum x_i \right) \log(1 - p)$$

**First Derivative:**
$$\frac{d}{dp} \log L(p) = \frac{\sum x_i}{p} - \frac{n - \sum x_i}{1 - p}=\bar X_n$$

**Second Derivative:**
$$\frac{d^2}{dp^2} \log L(p) = -\frac{\sum x_i}{p^2} - \frac{n - \sum x_i}{(1 - p)^2}$$
## Poisson estimator

**Likelihood:**
$$L(\lambda) = \frac{\lambda^{\sum x_i}}{\prod x_i!} e^{-\lambda n}$$
**Log-Likelihood:**

$$\log L(\lambda) = \left( \sum x_i \right) \log \lambda - \lambda n - \sum \log (x_i!)$$
**First Derivative:**

$$\frac{d}{d\lambda} \log L(\lambda) = \frac{\sum x_i}{\lambda} - n=\bar X_n$$
**Second Derivative:**

$$\frac{d^2}{d\lambda^2} \log L(\lambda) = -\frac{\sum x_i}{\lambda^2}$$
## Gaussian estimator

**Likelihood:**
$$L(\mu, \sigma) = \frac{1}{(\sigma \sqrt{2\pi})^n} e^{-\frac{1}{2\sigma^2} \sum (x_i - \mu)^2}$$
**Log-Likelihood:**
$$\log L(\mu, \sigma) = -n \log (\sigma \sqrt{2\pi}) - \frac{1}{2\sigma^2} \sum (x_i - \mu)^2$$
### **w.r.t.** $\mu$
**First Derivative:**
$$\frac{d}{d\mu} \log L(\mu, \sigma) = \frac{1}{\sigma^2} \sum (x_i - \mu)$$
**Second Derivative:**
$$\frac{d^2}{d\mu^2} \log L(\mu, \sigma) = -\frac{n}{\sigma^2}$$
### **w.r.t.** $\sigma^2(call\ v = \sigma^2)$:
**First Derivative:**
$$\frac{d}{dv} \log L(\mu, v) = -\frac{n}{2v} + \frac{1}{2v^2} \sum (x_i - \mu)^2$$
**Second Derivative:**
$$\frac{d^2}{dv^2} \log L(\mu, v) = \frac{n}{2v^2} - \frac{1}{v^3} \sum (x_i - \mu)^2$$

## When is the MLE applicable

The Maximum Likelihood Estimator (MLE) is a general method for estimating parameters by maximizing the likelihood function based on observed data. In principle, the MLE can be defined even when the likelihood is not smooth, but for the estimator to possess desirable properties—such as consistency, asymptotic normality, and efficiency—certain regularity conditions must be met. These typically include the requirement that the log-likelihood is differentiable (ideally twice differentiable) with respect to the parameter, and that certain technical conditions (such as the ability to interchange differentiation and integration) are satisfied. When these conditions fail, as in the case of the Uniform distribution where the likelihood is not smooth, the MLE still exists but its theoretical properties must be analyzed with care, as standard asymptotic results may not apply.

## The EM algorithm
![[Pasted image 20250611141753.png]]

The EM algorithm aims at maximizing the log likelihood or the likelihood of a mixture of gaussians

![[Pasted image 20250611142950.png]]
![[Pasted image 20250611143317.png]]
![[Pasted image 20250611145132.png]]
