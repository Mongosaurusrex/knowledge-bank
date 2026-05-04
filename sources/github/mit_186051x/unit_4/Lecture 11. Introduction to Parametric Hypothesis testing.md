At the end of this lecture, you will be able to do the following:  
- Reformulate experimental questions in terms of a **hypothesis test** by specifying an appropriate **null hypothesis** and an **alternative hypothesis** .
- **Design** statistical **tests** to decide between a null and alternative hypothesis.
- Understand the types of error of a test
- Compute the power function of a test
- Design statistical tests with a specific level or asymptotic level.
- Apply a test to a given sample to determine whether or not the null hypothesis should be rejected.
- Compute a test from a confidence interval
- Compute and interpret the p-value associated to a statistical test.

## Statistical formulation of hypothesis testing

- **Sample & Model**:
    Consider a sample $X_1, \dots, X_n$ of i.i.d. random variables under a statistical model $(\mathcal{E}, (\mathbb{P}\theta){\theta \in \Theta})$.
- **Parameter Partition**:
    Let $\Theta_0$ and $\Theta_1$ be a **partition** of the parameter space $\Theta$.
    This means:
    - $\Theta_0 \cup \Theta_1 = \Theta$
    - $\Theta_0 \cap \Theta_1 = \emptyset$
- **Hypotheses**:
    $\begin{cases} H_0: \theta \in \Theta_0 & \text{(Null hypothesis)} \\ H_1: \theta \in \Theta_1 & \text{(Alternative hypothesis)} \end{cases}$
- **Goal**:
    We say we **test** $H_0$ **against** $H_1$.

### 🧪 Testing Lexicon

#### Simple vs Composite Hypotheses

For $k = 0 (H_0)$ or $k = 1  (H_1)$:

- $\Theta_k$ is a **simple hypothesis** if:
  $\Theta_k = \{ \theta_k \}$
-  $\Theta_k$ is a **composite hypothesis** if it takes one of the following forms:
  - $\Theta_R = \{ \theta : \theta > \theta_k \}$
  - $\Theta_R = \{ \theta : \theta < \theta_k \}$
  - $\Theta_R = \{ \theta : \theta \ne \theta_k \}$

#### 🔍 Test Types
A test is typically either **one-sided** or **two-sided**.
##### Two-sided test:
$$
\begin{cases}
H_0: \theta = \theta_0 \\
H_1: \theta \ne \theta_0
\end{cases}$$

##### One-sided tests:
$$
\begin{cases}
H_0: \theta \le \theta_0 \\
H_1: \theta > \theta_0
\end{cases}
\quad \text{or} \quad
\begin{cases}
H_0: \theta \ge \theta_0 \\
H_1: \theta < \theta_0
\end{cases}
$$
## Asymmetry in the Hypotheses

- In hypothesis testing, the goal is to **reject** the null hypothesis \( $H_0$ \) — we look for **evidence against** \( $H_0$ \) in the data.
- The null and alternative hypotheses do **not play symmetric roles**:
  - \( $H_0$ \): represents the **status quo**
  - \( $H_1$ \): represents a **(scientific) discovery**
- The data is used **only to try to disprove** \( $H_0$ \), not to confirm it.
- Importantly, **lack of evidence** against \( $H_0$ \) does **not mean** that \( $H_0 $\) is true.
  - This is similar to the principle of: **"innocent until proven guilty"**.

## **🧪 What is a test?**

- A **test** is a statistic $\psi \in {0, 1}$ that does **not depend on unknown quantities** and behaves as follows:
    - If $\psi = 0$, then $H_0$ is **not rejected**
    - If $\psi = 1$, then $H_0$ is **rejected**
    
- **Important remark**:
    We can always write the test as:
    $\psi = \mathbb{I}{R}$
    where $R$ is the **rejection region** (i.e., the event that leads to rejection of $H_0$)
    Equivalent to: $\psi = \mathbb{I}(\psi = 1)$
## **🏥 Example Tests**
### **1. Waiting time in the ER**
- Hypotheses:
$$
    
    H_0: \mu \leq 30 \
    
    H_1: \mu > 30
    
    $$
- Test:
    $$
    \psi = \mathbb{I}\{\bar{X}_n > C\}
    $$
### **2. Kiss experiment**
- Hypotheses:
$$
    
    H_0: p = 0.5 \
    
    H_1: p \neq 0.5
    
    $$
- Test:$$
    
    \psi = \mathbb{I}\{ | \bar{X}_n - \frac{1}{2} | > C \}
    
    $$
### **3. Clinical trials**
- Hypotheses:
    
$$
    
    H_0: \mu_d \leq \mu_c \
    
    H_1: \mu_d > \mu_c
    
    $$
- Test:$$
    \psi = \mathbb{I}\{ \bar{X}_n - \bar{Y}_n > C \}
    $$
## **Errors in Hypothesis Testing**
1. $H_0$ **is true** and we **fail to reject** $H_0$ → ✅ _Correct decision_
2. $H_0$ **is true** and we **reject** $H_0$→ ❌ _Type I error_
3. $H_1$ **is true** and we **fail to reject**$ $H_0$ → ❌ _Type II error_
4. $H_1$ **is true** and we **reject** $H_0$ → ✅ _Correct decision_

## **Power Function**

The **power function** is defined as:
$$
\beta(\theta) = \mathbb{P}_\theta[\psi = 1]
$$
  
This represents the **probability of rejecting** the null hypothesis when the true parameter is $\theta$

### **🔸 When** $\theta \in \Theta_0$**:**

- $\beta(\theta) = \mathbb{P}_\theta[\text{Type I error}]$
- ✅ We want $\beta(\theta)$ to be **small**
### **🔹 When** \theta \in \Theta_1**:**
- $\beta(\theta) = 1 - \mathbb{P}_\theta[\text{Type II error}]$
- ✅ We want $\beta(\theta)$ to be **large**

### **The Neyman–Pearson Paradigm**

**Hypotheses (ER waiting time example):**
- $H_0: \mu \leq 30$
- $H_1: \mu > 30$
- Test statistic: $\psi = \mathbb{I} \{\bar{X}_n > C\}$

**The dilemma: How to choose threshold** $C$**?*:
- To make **Type I error** tend to 0: take $C \to +\infty$
- To make **Type II error** tend to 0: take $C \to -\infty$
- It is not possible to make both errors small at the same time.

**The Neyman–Pearson approach:**
1. Choose a maximum acceptable probability of Type I error:
    $\mathbb{P}[\text{Type I error}] \leq \alpha \quad \text{(e.g., } \alpha = 5\%, 1\%, \ldots \text{)}$
2. Minimize the probability of **Type II error** subject to this constraint.

### **Level of a Test**
- The value $\alpha \in (0, 1)$ chosen in the Neyman–Pearson paradigm is called the **level** of a test.
- It refers to the **maximum probability of a Type I error** under the null hypothesis $\Theta_0$.
#### **A test** $\psi$ **has** **level** $\alpha$ **if:**
$$\max_{\theta \in \Theta_0} \mathbb{P}_\theta[\psi = 1] \leq \alpha$$
This ensures the worst-case Type I error under the null is no greater than $\alpha$.
#### **A sequence of tests** $\psi_n$ **has** **asymptotic level** $\alpha$ **if:**
$$\lim_{n \to \infty} \max_{\theta \in \Theta_0} \mathbb{P}_\theta[\psi_n = 1] \leq \alpha$$
This means the level condition is satisfied in the limit as the sample size grows.

### **Building a Test from a Confidence Interval**
- Suppose $I = [A, B]$ is a $1 - \alpha$ confidence interval for parameter $\theta$:$$
    \mathbb{P}_\theta(\theta \in [A, B]) \geq 1 - \alpha
    $$
- To test the hypotheses:$$H_0: \theta = \theta_0 \quad\quad H_1: \theta \ne \theta_0$$
- A natural test is:$$\psi = \mathbb{I} \{ \theta_0 \notin [A, B] \}$$
- **Level of the test** under $H_0$:
$$\mathbb{P}{\theta_0}(\psi = 1) = \mathbb{P}{\theta_0}(\theta_0 \notin I) = 1 - \mathbb{P}_{\theta_0}(\theta_0 \in I) \leq \alpha$$
- Therefore, this test has **level** $\alpha$.

## What if we change the level?

We are analyzing how different significance levels (α) affect our hypothesis testing decision using the conservative confidence interval:

### Given:
- Conservative confidence interval:  
  $\mathcal{I}_{\text{conserv}} = [0.56, 0.73]$
- This interval is used to test \( $H_0$ \) (e.g., \( $H_0: \theta = 0.5$ \)).

---

### Table of Decisions

| α     | \( $q_{\alpha/2}$ \) | \( $\mathcal{I}_{\text{conserv}}$ \) | Decision            |
| ----- | -------------------- | ------------------------------------ | ------------------- |
| 10%   | 1.64                 | [0.57, 0.72]                         | Reject \( $H_0$ $\) |
| 5%    | 1.96                 | [0.56, 0.73]                         | Reject \( $H_0$ \)  |
| 1%    | 2.76                 | [0.52, 0.77]                         | Reject \( $H_0$ $\) |
| 0.1%  | 3.29                 | [0.497, 0.79]                        | Fail to reject      |
| 0.01% | 3.89                 | [0.47, 0.82]                         | Fail to reject      |

---

### Key Insight:
- As α decreases (more conservative), the interval becomes wider.
- At stricter levels, the interval includes the null value (e.g., 0.5), leading to a **"fail to reject"** decision.
- The **smallest α** at which we still reject \( H_0 \) is called the:

###  **p-value**
> The value of α across which we switch from "reject" to "fail to reject" is called the *p-value*.

## p-value Summary

### Definition
The (asymptotic) *p-value* of a test \( \psi \) is the **smallest (asymptotic) level** \( \alpha \) at which the test rejects the null hypothesis \( H_0 \).

---

### Golden Rule
- If \( \text{p-value} \leq \alpha \), then we **reject** \( H_0 \)
- If \( \text{p-value} > \alpha \), then we **fail to reject** \( H_0 \)

---

### Example (Kiss example)

We want to find the smallest \( $\alpha_0$ \) such that:
$$
\bar{R}_n - \frac{q_{\alpha_0/2}}{2\sqrt{n}} = 0.5
$$

Given:
- \( $bar{R}_n = 0.645$ \)
- \( $n = 124$ \)
- This gives \( $q_{\alpha_0/2} = 3.23$ \)

Use the standard normal table:
$$
\mathbb{P}(Z > 3.23) = 1 - \mathbb{P}(Z \leq 3.24) = 1 - 0.9994 = 0.0006 = 0.06\%
$$
So:
$$
\frac{\alpha_0}{2} = 0.06\% \Rightarrow \alpha_0 = 2 \times 0.06\% = \boxed{0.12\%}
$$
### Conclusion
The **p-value is 0.12%**, meaning we:
- **Reject** \( $H_0$ \) if \( $\alpha > 0.12\%$ \)
- **Fail to reject** \( $H_0$ \) if \( $\alpha \leq 0.12\%$ \)

## **Evidence Scale for p-values**

### **Mental Conversion Used by Statisticians**

Rather than saying “reject/fail to reject at level α,” statisticians often communicate directly using **p-values** to describe the strength of evidence against the null hypothesis $H_0$.

| **p-value**  | **Evidence Against** $H_0$ |
| ------------ | -------------------------- |
| > 10\%       | almost none                |
| [5\%, 10\%)  | weak                       |
| [1\%, 5\%)   | strong                     |
| [0.1\%, 1\%) | very strong                |
| < 0.1\%      | undisputable               |

## Summary

When testing a **null hypothesis** $H_0$, we want to determine whether the observed data provides enough evidence to **reject** it in favor of an **alternative hypothesis** $H_1$.

- There exists a **critical region** (based on a chosen significance level \alpha) such that if the test statistic falls in this region, we reject $H_0$.
- If the observed test statistic falls outside this critical region (i.e., within the acceptance region), we **fail to reject** $H_0$.
- This threshold (or critical value) corresponds to the **boundary in the probability distribution** under the assumption that $H_0$ is true.
### **Confidence Intervals and Hypothesis Testing**

- A **confidence interval** gives a range of plausible values for a parameter.
- If a hypothesized value (e.g., $\theta_0$) **falls outside** the confidence interval, we would **reject** $H_0$ at the corresponding confidence level (e.g., 95%).
### **p-values**

- The **p-value** is the probability, under $H_0$, of observing a test statistic at least as extreme as the one obtained.
- A **small p-value** indicates strong evidence against $H_0$; if it’s smaller than the significance level $\alpha$, we reject $H_0$.$
- The **smaller** the p-value, the **stronger** the evidence against the null hypothesis.
