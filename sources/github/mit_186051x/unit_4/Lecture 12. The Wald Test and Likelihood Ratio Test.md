
## Objectives

At the end of this lecture, you will be able to do the following:  

- Construct one-sample and two-sample Wald tests with specified asymptotic level
- Compute the asymptotic p-value of a Wald test
- Construct the Wald test from an asymptotically normal maximum likelihood estimator
- Perform the **likelihood ratio test** for a family of hypothesis testing questions.

## Wald Test

### Concept
- We start with a **statistical model**:
$$
  (\mathcal{E}, \{ \mathbb{P}_\theta \}_{\theta \in \Theta})
$$
- Assume an **estimator** \($\hat{\theta}$) such that:
$$
  \frac{\hat{\theta} - \theta}{\sqrt{\widehat{\text{var}}(\hat{\theta})}} \xrightarrow{d} \mathcal{N}(0, 1) \quad \text{as } n \to \infty
  $$
- This tells us that the estimator becomes asymptotically normal when standardized by an estimate of its variance.
### Key Component
- \($\widehat{\text{var}}(\hat{\theta})$\): An estimator of the variance of \($\hat{\theta}$\).

### Example: Bernoulli Case

- Let \($\hat{p} = \bar{X}_n$\), the sample mean of i.i.d. Bernoulli variables.
- Then:
$$
  \widehat{\text{var}}(\hat{p}) = \frac{\hat{p}(1 - \hat{p})}{n}
$$
- The Wald statistic becomes:

$$  \frac{\hat{p} - p}{\sqrt{\widehat{\text{var}}(\hat{p})}} = \sqrt{n} \cdot \frac{\hat{p} - p}{\sqrt{\hat{p}(1 - \hat{p})}} \xrightarrow{d} \mathcal{N}(0, 1)$$

This forms the basis for using the **Wald test** to test hypotheses about the parameter \(p\).


### Wald Test Statistic
- The Wald test uses the following statistic:
$$
  W := \frac{\hat{\theta} - \theta_0}{\sqrt{\widehat{\text{var}}(\hat{\theta})}}
  $$
- Under \( $H_0$ \), the statistic \( $W \sim \mathcal{N}(0,1)$ \) asymptotically.
### Wald Test Decision Rules

| Hypotheses                        | Wald Test Decision Rule              |
| --------------------------------- | ------------------------------------ |
| \( $H_0: \theta = \theta_0$ \)    | Reject if \($\|W\|> q_{\alpha/2}$ \) |
| \( $H_0: \theta \leq \theta_0$ \) | Reject if \( $W > q_\alpha$ \)       |
| \( $H_0: \theta \geq \theta_0$ \) | Reject if \( $W < -q_\alpha$ \)      |

Where:
- \( $q_{\alpha/2}$ \): the upper \( $\alpha/2$ \) quantile of the standard normal distribution (used for two-sided tests).
- \( $q_\alpha$ \): the upper \( $\alpha$ \) quantile (used for one-sided tests).


## Asymptotic Level of the Wald Test (Case 1)

### Hypothesis Setup

We test:
$$
H_0: \theta = \theta_0 \quad \text{vs} \quad H_1: \theta \ne \theta_0
$$
---

### Wald Test Statistic
$$
W = \frac{\hat{\theta} - \theta_0}{\sqrt{\widehat{\text{Var}}(\hat{\theta})}}
\quad \xrightarrow{d} \quad \mathcal{N}(0, 1)
\quad \text{as } n \to \infty
$$

So for large \($n$\), the Wald statistic behaves like a standard normal under \($H_0$\).

---

### Asymptotic Level


$$\lim_{n \to \infty} \mathbb{P}_{\theta_0}[\psi = 1]
= \lim_{n \to \infty} \mathbb{P}_{\theta_0} \left[ |W| > q_{\alpha/2} \right]
= \mathbb{P}(|Z| > q_{\alpha/2}) = \alpha$$

This tells us:
- The **asymptotic probability of rejecting \($H_0$\)** when it's true is \($\alpha$\), the **test level**.
- This validates that the Wald test is **asymptotically level \($\alpha$\)**.


> It is essential that the same \( \theta_0 \) is used in both \( \mathbb{P}_{\theta_0} \) and in the Wald statistic \( W \)!

This means: when checking the level of the test, make sure you're computing everything under the **null hypothesis** value \( $\theta_0$ \).

### More than 2/3 of Americans get news on social media

#### **Context:**
A 2018 Pew study claims **more than 2/3** of Americans get their news via social media.
#### **Statistical Model:**
- Each person: $X_i \sim \text{Bern}(p)$
- $H_0: p \leq \frac{2}{3}, H_1: p > \frac{2}{3}$
  
#### **Sample:**
- n = 4,581
- Sample proportion: $\hat{p} = 0.68$
    
#### **Test Statistic:**
$$W_{\text{obs}} = \sqrt{4581} \cdot \frac{0.68 - \frac{2}{3}}{\sqrt{0.68(1 - 0.68)}} = 1.93$$

#### **Conclusion at 5% level:**
- Critical value at 95% confidence: $z_{0.95} = 1.645$
- Since $1.93 > 1.645, reject\ H_0$
#### **P-value:**
$$\alpha_0 = P(Z > 1.93) = 1 - 0.9732 = 2.68\%$$
#### **Conclusion at 1% level:**
- Since $\alpha_0 = 2.68\% > 1\%$, **fail to reject** $H_0$

## Wald Test: p-values and Asymptotic Approximations

### Definition of the Wald Statistic
$$
W = \frac{\hat{\theta} - \theta_0}{\sqrt{\widehat{\text{Var}}(\hat{\theta})}}
$$

- Measures how far the estimator \( \hat{\theta} \) is from the hypothesized value \( $\theta_0$ \), in standard error units.
- In the news example, the observed value is \( $W^{\text{obs}} = 1.93$ \).