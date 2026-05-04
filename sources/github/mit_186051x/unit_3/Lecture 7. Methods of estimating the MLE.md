# **📜 MLE & Log-Likelihood Cheat Sheet**

## **Concept**

- **Maximum Likelihood Estimation (MLE)** finds parameter values that maximize the probability of the observed data.
- Use **log-likelihood** instead of likelihood for numerical stability and easier optimization.

---

## **General Steps**

1. Write the **likelihood** $L(\theta)$
2. Compute the **log-likelihood** $\log L(\theta)$
3. Take the derivative $\frac{d}{d\theta} \log L(\theta)$
4. Solve $\frac{d}{d\theta} \log L(\theta) = 0$ for $\hat{\theta}_{\text{MLE}}$

---

## **Likelihood & Log-Likelihood for Common Distributions**

### **Bernoulli** $\text{Ber}(p)$

**Likelihood:**
$$L(p) = p^{\sum x_i}(1-p)^{n-\sum x_i}$$
**Log-Likelihood:**
$$\log L(p) = \left( \sum x_i \right) \log p + \left( n - \sum x_i \right) \log(1 - p)$$
---

### **Poisson** $\text{Pois}(\lambda)$
**Likelihood:**
$$L(\lambda) = \frac{\lambda^{\sum x_i}}{\prod x_i!} e^{-\lambda n}$$
**Log-Likelihood:**

$$\log L(\lambda) = \left( \sum x_i \right) \log \lambda - \lambda n - \sum \log (x_i!)$$

---
### **Gaussian** $\mathcal{N}(\mu, \sigma^2)$

**Likelihood:**
$$L(\mu, \sigma) = \frac{1}{(\sigma \sqrt{2\pi})^n} e^{-\frac{1}{2\sigma^2} \sum (x_i - \mu)^2}$$

**Log-Likelihood:**
$$\log L(\mu, \sigma) = -n \log (\sigma \sqrt{2\pi}) - \frac{1}{2\sigma^2} \sum (x_i - \mu)^2$$
---
### **Exponential** $\text{Exp}(\lambda)$
**Likelihood:**

$$L(\lambda) = \lambda^n e^{-\lambda \sum x_i}$$
**Log-Likelihood:**

$$\log L(\lambda) = n \log \lambda - \lambda \sum x_i$$
---
### **Uniform** $U(0, b)$

**Likelihood:**

$$L(b) = \frac{1}{b^n} I(\max x_i \leq b)$$

**Log-Likelihood:**
$$\log L(b) =

\begin{cases}

-n \log b, & \text{if } \max x_i \leq b \

-\infty, & \text{otherwise}

\end{cases}$$
---

## **Summary Notes**

- **Likelihood** is a product → log-likelihood is a sum.
    
- MLE finds parameters that maximize \log L(\theta).
    
- Often optimize **negative log-likelihood** numerically in practice.
    

---

## **Python implementation**

```python
from scipy.optimize import minimize

# Example: Gaussian log-likelihood
def log_likelihood_gaussian(mu, sigma, x):
    n = len(x)
    return -n * np.log(sigma * np.sqrt(2 * np.pi)) - (1 / (2 * sigma**2)) * np.sum((x - mu)**2)

# To find MLE: minimize negative log-likelihood
neg_log_likelihood = lambda params: -log_likelihood_gaussian(params[0], params[1], x_data)
result = minimize(neg_log_likelihood, x0=[0, 1])
```
