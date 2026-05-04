At the end of this lecture, you will be able to do the following:
- Identify situations in which you cannot use the Wald test
- Use the T-test to when sample sizes are small
- Perform T-tests at fixed levels and compute exact p-values
- Understand the chi-squared distribution and the Student's t distribution and how they relate to the Gaussian distribution

## The Wald test and sample sizes

- **Issue**: When sample sizes are small, we can’t reliably use the Central Limit Theorem (CLT) or Slutsky’s theorem, which are essential for the **Wald test**.
- **Example**: This is typical in **early-phase clinical trials** (Phase I), where sample sizes are very limited.
- **Implication**: In such cases, we must **assume the data is Gaussian (normally distributed)** to proceed with statistical inference.

## Example: Home Wind Turbines
- The U.S. Department of Energy (DoE) recommends a **minimum average wind speed of 10 mph** for a grid-connected wind turbine.
- A candidate home was monitored **once per month for a year**, resulting in **12 measurements**:
$$
  X_1, X_2, \dots, X_{12}
$$
- Assume the measurements are i.i.d. from a normal distribution:
$$
  X_1, \dots, X_n \sim \mathcal{N}(\mu, \sigma^2)
$$
- The objective is to test whether the location has sufficient wind speed.

### Hypotheses
- Null hypothesis:  
$$  
  H_0: \mu \leq 10
  $$
- Alternative hypothesis:  
$$  H_1: \mu > 10$$
- This is a **one-sided test** to determine if the home qualifies for a wind turbine installation
Absolutely — here is the **Chi-Squared distribution summary** in clean, Obsidian-ready markdown, with no emojis:
## **Chi-Squared Distribution Summary**

### **Definition**

A **Chi-Squared distribution** with k degrees of freedom, denoted $\chi^2_k$, is the distribution of the sum of squares of k independent standard normal random variables:

$$Z_1, Z_2, \dots, Z_k \overset{iid}{\sim} \mathcal{N}(0, 1) \Rightarrow X = \sum_{i=1}^k Z_i^2 \sim \chi^2_k
$$
---

### **Properties**
**Support**:
$$
x \in (0, \infty)

  $$
**Probability Density Function (PDF)**:
$$
f(x; k) = \frac{1}{2^{k/2} \Gamma(k/2)} x^{(k/2) - 1} e^{-x/2}, \quad x > 0
$$
### **Expectation and Variance**

- **Mean**:
    $\mathbb{E}[X] = k$
- **Variance**:
    $\text{Var}(X) = 2k$
### **Likelihood Function**

Given a sample $x_1, x_2, \dots, x_n \sim \chi^2_k$, the **likelihood function** is:
$$L(k) = \prod_{i=1}^n \frac{1}{2^{k/2} \Gamma(k/2)} x_i^{k/2 - 1} e^{-x_i/2}$$
### **Log-Likelihood Function**

Taking the logarithm:
$$
\ell(k) = \log L(k) = -n \log \Gamma(k/2) - \frac{nk}{2} \log 2 + \left(\frac{k}{2} - 1\right) \sum_{i=1}^n \log x_i - \frac{1}{2} \sum_{i=1}^n x_i
$$

## Sample Variance and Cochran's Theorem

### Sample Variance

The unbiased sample variance is defined as:
$$
S_n^2 = \frac{1}{n - 1} \sum_{i=1}^n (X_i - \bar{X}_n)^2

$$
### Cochran's Theorem

If \($X_1, \dots, X_n \overset{iid}{\sim} \mathcal{N}(\mu, \sigma^2)$ \), then:
$$
\frac{(n - 1) S_n^2}{\sigma^2} = \sum_{i=1}^n \left( \frac{X_i - \bar{X}_n}{\sigma} \right)^2 \sim \chi^2_{n - 1}
$$

- The scaled sample variance follows a chi-squared distribution with \( $n - 1$ \) degrees of freedom.
- \( $\bar{X}_n$ \) and \( $S_n^2$ \) are independent random variables.
### Result: t-Statistic
$$\frac{ \sqrt{n} (\bar{X}_n - \mu)/\sigma }{ \sqrt{ S_n^2 / \sigma^2 } } = \frac{Z}{\sqrt{V/(n-1)}}$$
Where:
- \( $Z \sim \mathcal{N}(0, 1)$ \)
- \( $V \sim \chi^2_{n - 1}$ \)
- \( $Z$ \) and \( $V$ \) are independent

This ratio follows a **Student’s t-distribution** with \( $n - 1$ \) degrees of freedom.
### Interpretation

This forms the basis for:
- Confidence intervals for the population mean when variance is unknown
- Hypothesis testing using the t-statistic

## Student’s t-Distribution

### Definition

For a positive integer \( $k$ \), the **Student's t-distribution** with \( $k$ \) degrees of freedom (denoted \( $t_k$ \)) is the distribution of the random variable:
$$T = \frac{Z}{\sqrt{V / k}}$$
where:
- \( $Z \sim \mathcal{N}(0, 1)$ \)
- \( $V \sim \chi^2_k$ \)
- \( $Z$ \) and \( $V$ \) are independent

---

### Key Relationship in Estimation

If \( $X_1, \dots, X_n \sim \mathcal{N}(\mu, \sigma^2$) \), then the standardized sample mean (with sample variance) is:
$$
\frac{\sqrt{n} (\bar{X}_n - \mu)}{S_n} = \frac{Z}{\sqrt{V / (n - 1)}} \sim t_{n - 1}
$$
This quantity follows a Student’s t-distribution with \( $n - 1$ \) degrees of freedom.


## P-values for the T-test

### Test Setup

For a one-sample t-test, the statistic is:

$$
T = \sqrt{n} \cdot \frac{\bar{X}_n - \mu_0}{S_n} \sim t_{n-1}
$$

We consider three common test types:

| Hypotheses                                   | Test Condition        | p-value Expression                 |
| -------------------------------------------- | --------------------- | ---------------------------------- |
| $H_0: \mu = \mu_0$ <br> $H_1: \mu \ne \mu_0$ | $T> t_{n-1,\alpha/2}$ | $\mathbb{P}(\|T\|>T_{\text{obs}})$ |
| $H_0: \mu \le \mu_0$ <br> $H_1: \mu > \mu_0$ | $T > t_{n-1,\alpha}$  | $\mathbb{P}(T > T_{\text{obs}})$   |
| $H_0: \mu \ge \mu_0$ <br> $H_1: \mu < \mu_0$ | $T < -t_{n-1,\alpha}$ | $\mathbb{P}(T < T_{\text{obs}})$   |

---

### Example: Home Wind Turbines

- Sample size: $n = 12 \Rightarrow df = 11$
- Sample mean: $\bar{X} = 14.3$
- Sample standard deviation: $S_n = 4.7$
- Null hypothesis mean: $\mu_0 = 10$

Test statistic:

$$
T_{\text{obs}} = \sqrt{12} \cdot \frac{14.3 - 10}{4.7} = 3.17
$$

Since this is a **one-sided** test:

- $H_0: \mu \le 10$
- $H_1: \mu > 10$

We compute the p-value:

$$
\mathbb{P}(t_{11} > 3.17) = 0.00446 = 0.446\%
$$

**Conclusion:** Very strong evidence against the null hypothesis.

## Wald Test vs T-Test

The **t-test** is a classical statistical test used primarily to test hypotheses about the mean of a normally distributed population when the variance is unknown. It relies on the **t-distribution**, which provides **exact (non-asymptotic)** p-values in small samples. The t-test assumes either Gaussian data or, for large samples, leverages the Central Limit Theorem to approximate normality.

The **Wald test**, in contrast, is a more general framework used to test hypotheses about parameters in a wide range of models (e.g., regression coefficients). It relies on the **asymptotic normality** of the estimator and produces **approximate** p-values that become accurate as the sample size increases. It does **not require the data to be Gaussian**, only that the estimator is asymptotically normal.

For large enough samples, the Wald test and t-test often yield similar conclusions. However, in small samples, the t-test is typically preferred due to its exact distributional properties.

## **Clinical Trial Example (1): Two-Sample Test**

We are comparing the **expected decrease in LDL levels** between two groups:

- **Test group** (treated): expected decrease $\mu_d > 0$
    
- **Control group**: expected decrease $\mu_c > 0$
### **Hypothesis Testing Problem**
We want to test if the treatment leads to a greater LDL decrease than the control:

$$H_0: \mu_d - \mu_c \leq 0$$

$$H_1: \mu_d - \mu_c > 0 \quad \text{(i.e., the treatment is more effective)}$$
### **Observed Data**

We observe two independent samples:

- $X_1, \dots, X_n \overset{iid}{\sim} \mathcal{N}(\mu_d, \sigma_d^2)$ from the test group
- $Y_1, \dots, Y_m \overset{iid}{\sim} \mathcal{N}(\mu_c, \sigma_c^2)$ from the control group

### **Test Statistic**
The standardized statistic used for testing is:
$$\frac{\bar{X}_n - \bar{Y}_m - (\mu_d - \mu_c)}{\sqrt{\frac{\sigma_d^2}{n} + \frac{\sigma_c^2}{m}}} \sim \mathcal{N}(0, 1) \quad \text{under } H_0$$

  

This is used for a **two-sample test** when variances are known.

## **Two-Sample T-Test (Welch’s t-test)**

When the variances in two independent samples may be unequal, we use the **Welch–Satterthwaite (WS)** approximation to perform the t-test.
### **Test Statistic**

$$\frac{\bar{X}_n - \bar{Y}_m - (\mu_d - \mu_c)}{\sqrt{\frac{S_d^2}{n} + \frac{S_c^2}{m}}} \sim t_N$$
Where $S_d^2$ and $S_c^2$ are the sample variances of the test and control groups.
### **Degrees of Freedom (Welch–Satterthwaite Approximation)**
$$N = \frac{\left( \frac{S_d^2}{n} + \frac{S_c^2}{m} \right)^2} {\frac{S_d^4}{n^2(n-1)} + \frac{S_c^4}{m^2(m-1)}}$$

This approximated degrees of freedom N satisfies:
$$N \geq \min(n, m)$$
### **Sanity Check**

In the limit where one sample becomes infinitely large (e.g. $m \to \infty$), the formula simplifies:

$$N \to n - 1$$

This corresponds to the **one-sample t-test**.


## **Non-Asymptotic Test (Welch’s t-test Example)**

This is an example applying the **two-sample t-test** with **Welch–Satterthwaite approximation** for degrees of freedom.

### **Given**

- Sample sizes: $n = 12, m = 22$
    
- Sample means: $\bar{X}_n = 156.4, \bar{Y}_m = 132.7$
    
- Sample standard deviations: $S_d = 22.5, S_c = 8.7$
    
### **Test Statistic**
  
$$T = \frac{156.4 - 132.7}{\sqrt{\frac{22.5^2}{12} + \frac{8.7^2}{22}}} = 3.51$$


### **Degrees of Freedom (WS Formula)**
$$
N = \frac{\left( \frac{22.5^2}{12} + \frac{8.7^2}{22} \right)^2} {\frac{22.5^4}{12^2 \cdot 11} + \frac{8.7^4}{22^2 \cdot 21}} = 12.82$$

Rounded down to:
$\ell = \min(n, m) = \min(12, 22) = 12$

---

### **p-value**
$$
\text{p-value} = P(t_{12} > 3.51) = 0.215\%
$$
### **Conclusion**
Since the p-value is very small, we **reject the null hypothesis**.
There is **strong evidence** that the drug is effective (i.e., the treatment group saw a significantly greater reduction in LDL).