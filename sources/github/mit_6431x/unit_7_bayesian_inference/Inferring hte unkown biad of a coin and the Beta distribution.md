![[Pasted image 20241103202044.png]]
1. **Problem Setup**:

• A coin has an unknown bias, denoted by $\Theta$, and a prior $f_\Theta(\cdot)$.

• For a fixed number of coin tosses n, K is the observed number of heads.

• Assume the prior $f_\Theta(\cdot)$ is uniform over [0,1].

2. **Posterior Distribution**:

• The posterior $f_{\Theta|K}(\theta | k)$ is derived using Bayes’ theorem:
$$f_{\Theta|K}(\theta | k) = \frac{f_\Theta(\theta) p_{K|\Theta}(k | \theta)}{p_K(k)}$$

  

• $p_K(k)$ is a normalization factor that integrates out \theta.

3. **Beta Distribution**:

• When the prior is uniform, the posterior simplifies to a Beta distribution with parameters k+1 and n-k+1:$$f_{\Theta|K}(\theta | k) \propto \theta^k (1 - \theta)^{n-k}$$

  

• If the prior is a Beta distribution with parameters $\alpha$ and $\beta$, the posterior is also a Beta distribution, with updated parameters $\alpha + k$ and $\beta + n - k$