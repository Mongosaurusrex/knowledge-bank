At the end of this lecture, you will be able to do the following:  
- Describe properties of the **total variation distance** and **Kullback-Leibler (KL) divergence** .
- Compute the total variation distance and KL divergence between two distributions.
- Derive the **maximum likelihood principle** using the KL divergence.
- Define and **compute the likelihood** of a discrete distribution.

## Definition of Total Variation Distance

The total variation distance between two probability measures $\mathbb{P_\theta}$ and $\mathbb{P_{\theta'}}$
is defined by:$$
TV(\mathbb{P_\theta}, \mathbb{P_{\theta'}})= max|\mathbb{P_{\theta}}(A)-\mathbb{P_{\theta'}(A)}|
$$The **Total Variation Distance (TVD)** is a measure of how different two probability distributions are. For two discrete probability distributions P and Q defined over the same sample space, the total variation distance is defined as:$$\text{TV}(P, Q) = \frac{1}{2} \sum_{x} |P(x) - Q(x)|$$
It quantifies the maximum difference between the probabilities that the two distributions assign to the same event. Intuitively, it can be thought of as the largest possible difference in the probabilities that P and Q assign to the same subset of outcomes. A TVD of 0 means the distributions are identical, while a TVD of 1 means they are completely disjoint. This metric is widely used in statistics and machine learning for comparing models, evaluating convergence, and bounding the difference in expectations between distributions.

The difference between a discrete example and a continuous example is as always that we use integrals instead of sums:
$$
\mathrm{TV}(\mathbb{P}, \mathbb{Q}) = \frac{1}{2} \int_{-\infty}^{\infty} |p(x) - q(x)| \, dx
$$
## Properties of Total Variation Distance

- $\mathrm{TV}(\mathbb{P}, \mathbb{Q}) = \mathrm{TV}(\mathbb{Q}, \mathbb{P})$ (symmetric)
- $\mathrm{TV}(\mathbb{P}, \mathbb{Q}) \geq 0$, $\mathrm{TV}(\mathbb{P}, \mathbb{Q}) \leq 1$ (positive)
- If $\mathrm{TV}(\mathbb{P}, \mathbb{Q}) = 0$, then $\mathbb{P}= \mathbb{Q}$ (definite)
- $\mathrm{TV}(\mathbb{P}, \mathbb{Q}) \leq \mathrm{TV}(\mathbb{Q}, \mathbb{R}) + \mathrm{TV}(\mathbb{R}, \mathbb{Q})$ (triangle inequality)

These imply that the total variation is a distance between probability distributions.

## Kullback-Leibler (KL) Divergence
The reason we have KL divergence is to give us a tool to measure how different two probability distributions are — where 0 means they are exactly the same, and any positive value means they are not.
$$
D_{\text{KL}}(P \parallel Q) = \sum_{x} P(x) \log \left( \frac{P(x)}{Q(x)} \right)
$$
$$D_{\text{KL}}(P \parallel Q) = \int_{-\infty}^{\infty} p(x) \log \left( \frac{p(x)}{q(x)} \right) dx$$
## Properties of KL Divergence
- $\mathrm{KL}(\mathbb{P}, \mathbb{Q}) \neq \mathrm{KL}(\mathbb{Q}, \mathbb{P})$
- $\mathrm{KL}(\mathbb{P}, \mathbb{Q})\geq 0$
- $\mathrm{KL}(\mathbb{P}, \mathbb{Q})=0,\quad \mathbb{P}=\mathbb{Q}$
- $\mathrm{KL}(\mathbb{P}, \mathbb{Q}) \not\leq \mathrm{KL}(\mathbb{P}, \mathbb{R}) + \mathrm{KL}(\mathbb{R}, \mathbb{Q})$ 

The KL divergence is NOT a distance, but a divergence