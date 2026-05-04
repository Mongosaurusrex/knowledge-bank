At the end of this lecture, you will be able to do the following:  
- Extend the principles of maximum likelihood estimation to the more general M-estimation approach favored in machine learning.
- Define an **M-estimator** for the **mean** , **median** , and $\alpha$-**quantile** of an unknown distribution.
- Compare and contrast the maximum likelihood estimator and the method of moments .

## M - Estimation

M-estimation, short for _maximum likelihood-type estimation_, is a broad framework in statistics for estimating parameters by optimizing (typically minimizing or maximizing) an objective function based on observed data. The general form of an M-estimator is defined as the value of the parameter that minimizes the sum (or average) of a function of the data and the parameter—often written as $\hat{\theta} = \arg\min_\theta \sum_{i=1}^n \rho(x_i, \theta)$, where $\rho$ is a loss or criterion function. The Maximum Likelihood Estimator (MLE) is a special case of M-estimation, where the objective function is the negative log-likelihood. That is, in MLE, we choose the parameter $\theta$ $that maximizes the likelihood (or equivalently, minimizes the negative log-likelihood), making it a specific type of M-estimator. This unifying view helps extend classical estimation methods to more robust or flexible alternatives by changing the form of the function $\rho$.


## Robust Statistics

Robust statistics is a field focused on developing methods that remain reliable and informative even when the data contains outliers, noise, or deviations from ideal assumptions like normality. A classic example that illustrates the core idea is the difference between the mean and the median: while the mean is sensitive to extreme values—shifting dramatically even if a single outlier is added—the median remains stable, making it a more robust measure of central tendency. This reasoning underpins many robust methods, where estimators are designed to resist the influence of a small fraction of contaminated data. Robust statistics is particularly useful in real-world settings where data imperfections are common and traditional techniques like the MLE can break down due to their sensitivity to outliers.

## Moments

In probability theory, the **k-th moment** of a random variable $X$ is the expected value of $X^k$:
$m_k = \mathbb{E}[X^k]$

Moments are used to describe the shape of a distribution.
- The **first moment** is the **mean**.
- The **second central moment** is the **variance**.
- Higher-order moments give information about **skewness** (3rd) and **kurtosis** (4th).

Moments are either:
- **Raw moments**: $\mathbb{E}[X^k]$
- **Central moments**: $\mathbb{E}[(X - \mathbb{E}[X])^k]$
- Moments can also be computed via the **moment generating function (MGF)** if available.

