![[Pasted image 20241031201907.png]]
**Key Points:**

  

1. **Problem Setup**:

• $\Theta$  can take values from a discrete set, e.g., $\{1, 2, 3\}$.

• $X = \Theta + W$ , where  $W$  is independent noise, normally distributed as $W \sim \mathcal{N}(0, \sigma^2)$.

• The distribution  $f_{X|\Theta}(x | \theta)$  represents the likelihood of observing  $X$  given a specific value of  $\Theta$ .

2. **MAP Rule**:

• The MAP rule is to select the value of  $\Theta$  that maximizes the posterior probability  $p_{\Theta|X}(\theta | x)$  given the observation  $X = x$ .

• In the example, the MAP estimate $\hat{\theta}$  is 2, indicating that when using this rule,  $\Theta = 2$  is the most likely estimate given the observed data.

3. **Posterior Calculation**:

• The posterior probability  $p_{\Theta|X}(\theta | x)$  is calculated using Bayes’ rule:
$$
p_{\Theta|X}(\theta | x) = \frac{p_{\Theta}(\theta) f_{X|\Theta}(x | \theta)}{f_X(x)}
$$
  • Here,  $f_X(x)$ is the marginal likelihood obtained by summing over all possible values of  $\Theta$ .

4. **Error Probabilities**:

• **Conditional Probability of Error**: This is the probability that the MAP estimate  $\hat{\Theta} \neq \Theta$  given  X = x . The MAP rule minimizes this error.

• **Overall Probability of Error**: This is the average error probability over all possible values of  $\Theta$, calculated by:
$$P(\hat{\Theta} \neq \Theta) = \sum_{\theta} P(\hat{\Theta} \neq \theta | \Theta = \theta) p_{\Theta}(\theta)$$
