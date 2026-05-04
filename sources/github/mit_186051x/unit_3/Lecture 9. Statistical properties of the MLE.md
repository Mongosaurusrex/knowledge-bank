At the end of this lecture, you will be able to do the following:  
- Derive the maximum likelihood estimator for the uniform statistical model and prove its consistency.
- Recognize that the maximum likelihood estimator is consistent.
- Compute the Fisher information of a statistical model
- Establish asymptotic normality of a maximum likelihood estimator and compute its asymptotic variance using Fisher information

## Consistency of maximum likelihood estimator
![[Pasted image 20250613131909.png]]
Given i.i.d samples $X_1, \ldots , X_ n\sim \mathbf{P}_{\theta ^*}$ and an associated statistical model$\displaystyle \left(E,\{ \mathbf{P}_\theta \} _{\theta \in \Theta }\right),\,$ the maximum likelihood estimator $\widehat{\theta }_ n^{\text {MLE}}$ of $\theta^*$ is a **consistent** estimator under mild regularity conditions (e.g. continuity in $\theta$ of the pdf $p_\theta$ almost everywhere), i.e.
$$
\displaystyle  \displaystyle \widehat{\theta }_ n^{\text {MLE}}\xrightarrow [(p)]{n\to \infty } \theta ^*.
$$
## Fisher Information
![[Pasted image 20250613132959.png]]
For most well-behaved distributions, the MLE is asymptotically Gaussian with variance $1 / (n \cdot \mathcal{I}(\theta^))$_, where_ $\mathcal{I}(\theta^)$ is the Fisher information. However, for the Uniform distribution, this formula does not apply because the support depends on $\theta^*$, and the MLE $(\max X_i)$ follows a different, non-Gaussian limiting behaviour.


## Example Fisher Information Calculation

![[Pasted image 20250613135531.png]]
