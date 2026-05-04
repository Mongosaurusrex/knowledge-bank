@@### Probability distribution types

| **Distribution**         | **Type**   | **Support (Values it can take)**         | **Typical Applications**                                                                   | **Key Characteristics**                                                              |
| ------------------------ | ---------- | ---------------------------------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| **Bernoulli**            | Discrete   | 0 or 1                                   | Modeling a single trial with two outcomes (e.g., success/failure)                          | One trial, two possible outcomes, parameterized by \( p \) (probability of success). |
| **Binomial**             | Discrete   | 0, 1, 2, ..., n                          | Modeling the number of successes in a fixed number of independent Bernoulli trials         | Sum of multiple Bernoulli trials.                                                    |
| **Poisson**              | Discrete   | 0, 1, 2, ... (all non-negative integers) | Counting the number of events in a fixed interval of time or space (e.g., emails per hour) | Events are independent, occur at a constant average rate.                            |
| **Geometric**            | Discrete   | 1, 2, 3, ...                             | Modeling the number of trials until the first success                                      | Memoryless property, each trial is independent.                                      |
| **Gaussian (Normal)**    | Continuous | All real numbers (-∞, ∞)                 | Modeling naturally continuous variables (e.g., height, weight, test scores)                | Bell-shaped curve, characterized by mean (\(\mu\)) and variance (\(\sigma^2\)).      |
| **Exponential**          | Continuous | $x \geq 0$                               | Modeling the time between events in a Poisson process (e.g., time between calls)           | Memoryless property, rate of occurrence is constant.                                 |
| **Uniform (Discrete)**   | Discrete   | A finite set of integers                 | Rolling a fair die, selecting a random card from a deck                                    | Every outcome is equally likely.                                                     |
| **Uniform (Continuous)** | Continuous | A finite interval [a, b]                 | Randomly picking a point within a segment on a line                                        | Every point in the interval is equally likely.                                       |
### Expectation and Variance for probability distributions
| **Distribution**         | **Definition**                                                                      | **Mean (Expected Value)**           | **Variance**                                   | **Formula Explanation**                                             | PMF/PDF                                                                     | Normalization Series sum/ integral                                          | Result of the sum |
| ------------------------ | ----------------------------------------------------------------------------------- | ----------------------------------- | ---------------------------------------------- | ------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | ----------------- |
| **Bernoulli**            | Takes value 1 with probability \(p\) and 0 with probability \(1 - p\).              | $\mathbb{E}[X] = p$                 | $\operatorname{Var}(X) = p(1 - p)$             | The variance is the product of success and failure probabilities.   | $P(X=k) = p^k (1-p)^{1-k}, k \in \{0, 1\}$                                  | $\sum_{k=0}^1 p^k (1-p)^{1-k}$                                              | $1$               |
| **Binomial**             | Sum of \(n\) independent Bernoulli trials with success probability \(p\).           | $\mathbb{E}[X] = np$                | $\operatorname{Var}(X) = np(1 - p)$            | Scales with the number of trials and the spread of success/failure. | $P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}$                                     | $\sum_{k=0}^n \binom{n}{k} p^k (1-p)^{n-k}$                                 | $1$               |
| **Poisson**              | Counts the number of events occurring in a fixed interval, with rate \( \lambda \). | $\mathbb{E}[X] = \lambda$           | $\operatorname{Var}(X) = \lambda$              | Mean and variance are both equal to the rate parameter.             | $P(X=k) = \frac{\lambda^k e^{-\lambda}}{k!}$                                | $P(X=k) = \frac{\lambda^k e^{-\lambda}}{k!}$                                | $e^{\lambda}$     |
| **Uniform (Discrete)**   | Equally likely outcomes over a range \(1, 2, \dots, n\).                            | $\mathbb{E}[X] = \frac{n + 1}{2}$   | $\operatorname{Var}(X) = \frac{n^2 - 1}{12}$   | Symmetric distribution with equal spread.                           | $P(X=k) = \frac{1}{N}, k \in \{1, 2, \dots, N\}$                            | $\sum_{k=1}^N \frac{1}{N}$                                                  | $1$               |
| **Uniform (Continuous)** | Equally likely outcomes over an interval \([a, b]\).                                | $\mathbb{E}[X] = \frac{a + b}{2}$   | $\operatorname{Var}(X) = \frac{(b - a)^2}{12}$ | The variance depends on the square of the interval's width.         | $f(x) = \frac{1}{b - a}, a \leq x \leq b$                                   | $\int_a^b \frac{1}{b - a} dx$                                               | $1$               |
| **Geometric**            | Counts the number of trials until the first success.                                | $\mathbb{E}[X] = \frac{1}{p}$       | $\operatorname{Var}(X) = \frac{1 - p}{p^2}$    | The mean is the inverse of the probability of success.              | $P(X=k) = (1-p)^{k-1} p$                                                    | $\sum_{k=1}^\infty (1-p)^{k-1}$                                             | $1$               |
| **Normal (Gaussian)**    | Continuous, symmetric distribution centered at \( \mu \).                           | $\mathbb{E}[X] = \mu$               | $\operatorname{Var}(X) = \sigma^2$             | Mean and variance are the parameters of the distribution.           | $f(x) = \frac{1}{\sqrt{2 \pi \sigma^2}} e^{-\frac{(x - \mu)^2}{2\sigma^2}}$ | $f(x) = \frac{1}{\sqrt{2 \pi \sigma^2}} e^{-\frac{(x - \mu)^2}{2\sigma^2}}$ | $1$               |
| **Exponential**          | Time between events in a Poisson process with rate \( \lambda \).                   | $\mathbb{E}[X] = \frac{1}{\lambda}$ | $\operatorname{Var}(X) = \frac{1}{\lambda^2}$  | Inversely proportional to the rate.                                 | $f(x) = \lambda e^{-\lambda x}, x \geq 0$                                   | $\int_0^\infty \lambda e^{-\lambda x} dx$                                   | $1$               |
| **Gamma**                | Generalization of the exponential, with shape \( k \) and rate \( \lambda \).       | $\mathbb{E}[X] = \frac{k}{\lambda}$ | $\operatorname{Var}(X) = \frac{k}{\lambda^2}$  | Scales with shape and rate parameters.                              | $f(x) = \frac{\lambda^k x^{k-1} e^{-\lambda x}}{\Gamma(k)}, x \geq 0$       | $\int_0^\infty \frac{\lambda^k x^{k-1} e^{-\lambda x}}{\Gamma(k)} dx$       | $1$               |
| **Negative Binomial**    | Counts the number of trials to achieve \( r \) successes.                           | $\mathbb{E}[X] = \frac{r}{p}$       | $\operatorname{Var}(X) = \frac{r(1 - p)}{p^2}$ | Extends geometric distribution to multiple successes.               | $P(X=k) = \binom{k+r-1}{k} p^k (1-p)^r$                                     | $P(X=k) = \binom{k+r-1}{k} p^k (1-p)^r$                                     | $1$               |

## Gaussian and normalizing
### Example 1
If you have, for example, $P(X > 3)$, you would normalize it:
$$
P(X > 3) = P\left(Z > \frac{3 - 1}{1.5}\right) = P(Z > \frac{2}{1.5}) = P(Z > 1.33)
$$
  Now, you go to the table and look up 1.33, which would give you the area to the **left** of 1.33. To find the right-hand side (which is what you want), you subtract from 1:
$$P(Z > 1.33) = 1 - P(Z \leq 1.33)$$
### Example 2
$$P(|X - 2| \leq 1)$$
This is equivalent to saying:
$$P(1 \leq X \leq 3)$$
#### **Step 1: Normalize the boundaries:**
Recall that $X \sim N(1, 2.25)$, and its standard normal form is:
$$Z = \frac{X - 1}{1.5}$$
Normalize the boundaries:
- For $X = 1, Z = \frac{1 - 1}{1.5} = 0$
- For $X = 3, Z = \frac{3 - 1}{1.5} = \frac{2}{1.5} = 1.33$
#### **Step 2: Find the probability:**
We want the probability that Z is between these two points:
$$P(0 \leq Z \leq 1.33)$$
To get this, go to the standard normal table:
- $P(Z \leq 1.33) \approx 0.9082$
- $P(Z \leq 0) = 0.5$

So, the area in between is:
$$0.9082 - 0.5 = 0.4082$$
#### **Final Answer:**
$$P(|X - 2| \leq 1) = 0.4082$$
$$\left|\frac{\sqrt{n}}{\sqrt{\lambda}} (\bar{X} - \lambda) \right| \le 1.96$$

Absolutely — here’s a **cheat sheet** for both:

---

# **🚀 KL Divergence — Cheat Sheet**

### **General formula:**
$$
\mathrm{KL}(P, Q) = \mathbb{E}_P \left[ \ln \frac{p(x)}{q(x)} \right] = \int p(x) \ln \frac{p(x)}{q(x)} dx
$$
  

### **How to compute step-by-step:**

  

1️⃣ Write p(x), q(x), domain of each.

2️⃣ Compute \ln \frac{p(x)}{q(x)}.

3️⃣ Take expectation under P:

- Plug in known $\mathbb{E}_P[x], \mathbb{E}_P[x^2]$, etc.
    
    4️⃣ Simplify the expression.
    

---

### **Useful formulas:**

| **Distribution pair**                                           | **KL(P,Q)**                                                               |
| --------------------------------------------------------------- | ------------------------------------------------------------------------- |
| $\mathcal{N}(a, \sigma^2) \to \mathcal{N}(b, \sigma^2)$         | $\frac{(a - b)^2}{2\sigma^2}$                                             |
| $\mathrm{Bern}(a) \to \mathrm{Bern}(b)$                         | $a \ln \frac{a}{b} + (1-a) \ln \frac{1-a}{1-b}$                           |
| $\mathrm{Unif}([0, \theta_1]) \to \mathrm{Unif}([0, \theta_2])$ | $\ln \frac{\theta_2}{\theta_1}, if \theta_1 < \theta_2; \infty otherwise$ |
| $\mathrm{Exp}(\lambda) \to \mathrm{Exp}(\mu)$                   | $\ln \frac{\lambda}{\mu} + \frac{\mu}{\lambda} - 1$                       |

---

# **🚀 Total Variation (TV) Distance — Cheat Sheet**

  

### **General formula:**

  

$$\mathrm{TV}(P, Q) = \frac{1}{2} \sum_x |P(x) - Q(x)|$$

  

**Intuition:** it is the _maximum difference in probabilities_ across all events.

---

### **Steps:**

  

1️⃣ Identify the supports of P and Q.

2️⃣ See if there is overlap or if they are disjoint:

- **No overlap → TV = 1.**
    
- **Perfect match → TV = 0.**
    
    3️⃣ For overlapping parts:
    
- Compute $\frac{1}{2} \sum |P(x) - Q(x)|$
    

---

### **Example:** $X \sim \mathrm{Ber}(p), Q = X + c$

| **Case**                  | **TV(P,Q)**                              |     |
| ------------------------- | ---------------------------------------- | --- |
| $c \notin \{ -1, 0, 1 \}$ | 1                                        |     |
| $c = 0$                   | 0                                        |     |
| $c = 1 or c = -1$         | $\frac{1}{2} (1 + \mathrm{abs}(2p - 1))$ |     |
|                           |                                          |     |

---
## 🔢 Likelihood, Derivatives, and MLEs

| Distribution            | Likelihood                                                         | Log-Likelihood                                                            | First Derivative                      | Second Derivative                          | MLE                                                                            |
| ----------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------------------- | ------------------------------------- | ------------------------------------------ | ------------------------------------------------------------------------------ |
| **Bernoulli(p)**        | $p^x (1-p)^{1-x}$                                                  | $x \log p + (1 - x) \log(1 - p)$                                          | $\frac{x}{p} - \frac{1 - x}{1 - p}$   | $-\frac{x}{p^2} - \frac{1 - x}{(1 - p)^2}$ | $\hat{p} = \bar{X}_n$                                                          |
| **Binomial(n, p)**      | $\binom{n}{x} p^x (1-p)^{n-x}$                                     | $\log \binom{n}{x} + x \log p + (n - x) \log(1 - p)$                      | $\frac{x}{p} - \frac{n - x}{1 - p}$   | $-\frac{x}{p^2} - \frac{n - x}{(1 - p)^2}$ | $\hat{p} = \frac{x}{n}$                                                        |
| **Poisson(λ)**          | $\frac{e^{-\lambda} \lambda^x}{x!}$                                | $-\lambda + x \log \lambda - \log x!$                                     | $-1 + \frac{x}{\lambda}$              | $-\frac{x}{\lambda^2}$                     | $\hat{\lambda} = \bar{X}_n$                                                    |
| **Uniform(a, b)**       | $\frac{1}{b-a} \mathbf{1}_{[a,b]}(x)$                              | $-\log(b - a)$                                                            | 0                                     | 0                                          | $\hat{a} = \min x_i, \hat{b} = \max x_i$                                       |
| **Geometric(p)**        | $(1 - p)^{x - 1} p$                                                | $(x - 1) \log(1 - p) + \log p$                                            | $-\frac{x - 1}{1 - p} + \frac{1}{p}$  | $-\frac{x - 1}{(1 - p)^2} - \frac{1}{p^2}$ | $\hat{p} = \frac{1}{\bar{X}_n}$                                                |
| **Normal(μ, σ²)**       | $\frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x - \mu)^2}{2\sigma^2}}$ | $-\frac{1}{2} \log(2\pi\sigma^2) - \frac{(x - \mu)^2}{2\sigma^2}$         | $\frac{x - \mu}{\sigma^2}$            | $-\frac{1}{\sigma^2}$                      | $\hat{\mu} = \bar{X}_n, \hat{\sigma}^2 = \frac{1}{n} \sum (x_i - \bar{X}_n)^2$ |
| **Exponential(λ)**      | $\lambda e^{-\lambda x}$                                           | $\log \lambda - \lambda x$                                                | $\frac{1}{\lambda} - x$               | $-\frac{1}{\lambda^2}$                     | $\hat{\lambda} = \frac{1}{\bar{X}_n}$                                          |
| **Gamma(α, β)**         | $\frac{\beta^\alpha}{\Gamma(\alpha)} x^{\alpha - 1} e^{-\beta x}$  | $\alpha \log \beta - \log \Gamma(\alpha) + (\alpha - 1) \log x - \beta x$ | $\frac{\alpha}{\beta} - x$*(w.r.t β)* | $-\frac{\alpha}{\beta^2}$ *(w.r.t β)*      | $\hat{\beta} = \frac{\alpha}{\bar{X}_n}$                                       |
| **Neg. Binomial(r, p)** | $\binom{x+r-1}{x} (1-p)^r p^x$                                     | $\log \binom{x+r-1}{x} + r \log(1 - p) + x \log p$                        | $\frac{x}{p} - \frac{r}{1 - p}$       | $-\frac{x}{p^2} - \frac{r}{(1 - p)^2}$     | $\hat{p} = \frac{r}{r + \bar{X}_n}$                                            |
