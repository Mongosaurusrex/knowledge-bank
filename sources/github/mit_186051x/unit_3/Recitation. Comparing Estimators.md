
## **Comparing Estimators: Mean Squared Error (MSE)**

  

Given:

- $X_1, \ldots, X_n \overset{\text{iid}}{\sim} P_0$
    
- Estimate $\Theta \rightarrow \hat{\Theta} (a function of X_1, \ldots, X_n)$
    

  

### **🎯 Definition of MSE**

$$\text{MSE}(\hat{\Theta}) = \mathbb{E}_{X_1,\dots,X_n}[(\hat{\Theta} - \Theta)^2]$$
$$= \mathbb{E}[\hat{\Theta}^2] - 2\Theta \mathbb{E}[\hat{\Theta}] + \Theta^2$$
$$= \text{Var}(\hat{\Theta}) + \left( \mathbb{E}[\hat{\Theta}] - \Theta \right)^2$$
$$= \text{Var}(\hat{\Theta}) + \text{Bias}(\hat{\Theta})^2$$

---

## **🧪 Example: Estimators for $Poisson(\lambda)$

Assume:
$$X_1, \ldots, X_n \overset{\text{iid}}{\sim} \text{Poisson}(\lambda)$$

Define estimators:

- $\hat{\lambda}_1 = X_1$
- $\hat{\lambda}_2 = \bar{X}n = \frac{1}{n} \sum{i=1}^n X_i$
---

### **🔹 (a) For** $\hat{\lambda}_1$
- $\text{Var}(\hat{\lambda}_1) = \text{Var}(X_1) = \lambda$
- $\text{Bias}(\hat{\lambda}_1) = \mathbb{E}[X_1] - \lambda = 0$
- $\text{MSE}(\hat{\lambda}_1) = \lambda + 0^2 = \lambda$
---

### **🔹 (b) For** $\hat{\lambda}_2$
- $\text{Var}(\hat{\lambda}2) = \text{Var} \left( \frac{1}{n} \sum{i=1}^n X_i \right) = \frac{1}{n^2} \sum_{i=1}^n \lambda = \frac{\lambda}{n}$
- $\text{Bias}(\hat{\lambda}_2) = \mathbb{E}[\hat{\lambda}_2] - \lambda = \lambda - \lambda = 0$
- $\text{MSE}(\hat{\lambda}_2) = \frac{\lambda}{n} + 0^2 = \frac{\lambda}{n}$
---
