## Two important probability tools

Let $X,X_1,X_2,\dots, X_n$ be independent random variables with $\mu=E[X]$ and $\sigma^2 = V[X]$ 

#### Laws (weak and strong) of large numbers (LNN):
$$
\bar X_ n:=\frac{1}{n}\sum _{i=1}^ n X_ i \xrightarrow [n\to \infty ]{\mathbf{P},\mbox{ a.s.}} \mu
$$
 where the convergence is in probability (as denoted by P on the convergence arrow) and almost surely (as denoted by a.s. on the arrow) for the weak and strong laws respectively.

- **WLLN**: The average converges in probability to the mean—it’s about the likelihood that $\bar{X}_n$ is close to $\mu$.
    
- **SLLN**: The average converges almost surely, which implies it happens with probability 1. It’s a stronger guarantee: not only does it approach $\mu$, but it does so for almost every realization of the sequence.

## Central limit theorem (CLT):
$$\displaystyle \sqrt{n}\, \frac{\bar X_ n-\mu }{\sigma }$$
Or equivalently
$$
\displaystyle \sqrt{n}\, \left(\bar X_ n-\mu \right)
$$
The **sample mean** of independent, identically distributed random variables converges to a **normal distribution** as the sample size increases, regardless of the original distribution. The expression $\sqrt{n} \frac{\bar{X}_n - \mu}{\sigma}$ standardizes the sample mean, scaling its deviation from the true mean $\mu$ by the standard error, resulting in convergence to a standard normal distribution $\mathcal{N}(0, 1)$ as $n$ grows.

## Gaussian Distribution

Because of the CLT, the Gaussian (aka. Normal) distribution is ubiquitous in statistics. It is named after German Mathematician Carl Friedrich Gauss (1777-1855) in the context of the method of least squares (regression)
- $X \sim N(\mu, \sigma^2)$
- $\mathbb{E}[X]=\mu$
- $Var(X)=\sigma^2 > 0$

#### Equation
$$
f_ X(x)=\frac{1}{\sigma \sqrt{2\pi }} \exp \left(-\frac{(x-\mu )^2}{2 \sigma ^2}\right).
$$

## Properties of Gaussians
Perhaps the most useful property of the gaussian family is that it's invariant under affine tranformation:
- $X \sim N(\mu, \sigma^2)$ then for any $a, b \in \mathbb{R}$:$$a\cdot X + b \sim N(a\mu + b, a^2\sigma^2)$$
- __Standardisation__ (aka. Normalization/Z-score): if $X \sim N(\mu, \sigma^2)$, then:$$Z=\frac{X-\mu}{\sigma}\sim N(0,1)$$
  Which is useful to compute probabilities from CDF of $Z \sim N(0,1)$:$$\mathbb{P}(u\leq X \leq v) = \mathbb{P}(\frac{u-\mu}{\sigma}\leq Z \leq Z \frac{v-\mu}{\sigma})$$
- Symmetry: If $X \sim N(0, \sigma^2)$ then $-X \sim N(0,\sigma^2)$: if $x>0$$$\mathbb{P}(|X| > x) = \mathbb{P}(X>x) + \mathbb{P}(-X> x) = 2\mathbb{P}(X>x)$$
## Gaussian Probability Tables and Quantiles
![[Pasted image 20250509154747.png]]

### Examples
Assume that $Z \sim N(0,1)$ and compute
- $\mathbb{P}(Z\leq 1)= 0.8413$ 
- $\mathbb{P}(Z\geq -1)=\mathbb{P}(-Z\leq 1)= \mathbb{P}(Z\leq 1)= 0.8413$ 
- $\mathbb{P}(|Z| > -1)=2\mathbb{P}(Z\gt 1)=2\cdot (1-0.8413)=0.31$

Assume that the score distribution for a final exam is approximately $X \sim N(85,4)$, compute
- $\mathbb{P}(X\gt 90)=\mathbb{P}(\frac{x-85}{2}\gt \frac{90-85}{2})=\mathbb{P}(Z>2.5)=0.62\%$
- $\mathbb{P}(80<X<90)=\mathbb{P}(-2.5 < Z < 2.5)=0.9876$
## Quantiles
![[Pasted image 20250509160924.png]]The **quantile of order** $1 - \alpha$ of a random variable $X$ is the cutoff value $q_\alpha$ $such that the probability of $X$ being less than or equal to $q_\alpha$ is $1 - \alpha$, or equivalently, the probability of exceeding it is $\alpha$.
#### **Key Points:**

- $F(q_\alpha) = 1 - \alpha$, where $F$ is the CDF of $X$.
    
- If $F$ is invertible, $q_\alpha = F^{-1}(1 - \alpha)$.
    
- For a standard normal distribution:$$q_{0.025} = 1.96, q_{0.05} = 1.65, q_{0.1} = 1.28$$
## Convergence almost surely, in probability and in distribution

### Three types of convergence
- $(T_n)_{n\geq 1}$ is a sequence of random variables
- $T$ is a random variable ($T$ may be deterministic)

- Almost surely convergence:$$T_n \xrightarrow{a.s.} T \quad \text{iff} \quad P \left(\left\{\omega :T_n(\omega) \xrightarrow{n \to \infty} T(\omega)\right\}\right) = 1$$
	- **Meaning**: $T_n$ converges to $T$ for almost every outcome $\omega$ in the sample space. The probability that the sequence does not converge to $T$ is exactly $0$.
	- **Intuition**: If you were to observe infinitely many samples, you would **almost always** see the sequence $T_n$ getting arbitrarily close to $T$.
	- **Strength**: This is the **strongest form** of convergence. It implies both convergence in probability and convergence in distribution.
	  
- Converges in probability:$$T_n \xrightarrow{\mathbb{P}} T \quad \text{iff} \quad P(|T_n - T| \geq \epsilon) \xrightarrow{n \to \infty} 0, \quad \forall \epsilon > 0$$
	- **Meaning**: For any small margin of error $\epsilon$, the probability that $T_n$ is not within $\epsilon$ of $T$ **goes to zero** as n increases.
	- **Intuition**: With increasing $n$, the sequence $T_n$ is more and more likely to be close to $T$.
	- **Strength**: This is **weaker than almost sure convergence**. Convergence in probability does not guarantee that every individual path converges, only that “most of the time” it does.
	  
- Convergence in distribution: $$T_n \xrightarrow{d} T \quad \text{iff} \quad \mathbb{E}[f(T_n)] \xrightarrow{n \to \infty} \mathbb{E}[f(T)]$$
	- **Meaning**: The **distribution** of $T_n$ converges to the **distribution** of $T$ as $n \to \infty$.
	- **Intuition**: If you plot the distribution of $T_n$, it will look more and more like the distribution of $T$ as $n$ grows.
	- **Strength**: This is the **weakest form of convergence**. It does not require individual outcomes to get close; it only requires the distributions to match in the limit.

For all continious and bounded functions $f$

## Addition, multiplication, division

... only for a.s and $\mathbb{P}$...
Assume$$T_n \to T\ \text{and}\ U_n \to U$$
Then,
$$T_n+U_n \to T + U$$
$$T_nU_n \to TU$$
$$\frac{T_n}{U_n},\ U_n\neq 0$$
### Slutsky's theorem
Some partial results exist for convergence in distribution, described by **Slutsky’s Theorem**.
#### **Conditions:**
Let $(T_n), (U_n)$ be two sequences of random variables such that:
$U_n \xrightarrow{P} u$
where:
- $T$ is a random variable (r.v.),
- $u$ is a given real number (deterministic limit, meaning $\mathbb{P}(U = u) = 1)$.
    
### **Results:**
If the conditions hold, then:

1. **Sum converges in distribution:**
	$T_n + U_n \xrightarrow{(d)} T + u$ 
2. **Product converges in distribution:**
	$T_n + U_n \xrightarrow{(d)} T + u$
3. **Quotient converges in distribution** (if $u \neq 0$):
	$\frac{T_n}{U_n} \xrightarrow{(d)} \frac{T}{u}$
	
Slutsky is only your friend if one part is “almost constant” (converging in probability to a number).

## Continuous Mapping Theorem
If $f$ is a continuous function:
$$T_ n\xrightarrow [n\to \infty ]{\mbox{a.s.}/\mathbf{P}/(d)}T\hspace{3mm}\Rightarrow \hspace{3mm} f(T_ n)\xrightarrow [n\to \infty ]{\mbox{a.s.}/\mathbf{P}/(d)}f(T).$$
## **Recap**

- Averages of random variables occur naturally in statistics.
- We make modeling assumptions to apply probability results.
- For large sample sizes, they are **consistent** (LLN - Law of Large Numbers) and we know their distribution (CLT - Central Limit Theorem).
- CLT gives the **weakest form of convergence** (convergence in distribution), but it is still enough to compute probabilities.
- We use **standardization** and **Gaussian tables** to compute probabilities and quantiles.
- We can make operations (addition, multiplication, continuous functions) on sequences of random variables.