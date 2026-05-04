At the end of this lecture, you will be able to do the following:  
- Construct a **statistical model** .
- Give several examples of statistical models involving commonly used distributions (e.g. Gaussian, Poisson)
- Distinguish between **parametric** and **non-parametric** statistical models.
- Determine whether or not a parameter in a statistical model is **identified**.

## Goals
In this unit, we introduce a mathematical formalization of statistical modeling to make a principled sense of the **Trinity of statistical inference**.
We will make sense of the following statements:
1. Estimation:
   "$\hat p = \bar R_n$ is an estimator for the proportion $p$ of couples that turn their head to the right"
2. Confidence intervals:
   "[0.56, 0.73] is a 95% confidence interval for p"
3. Hypotesis testing:
   "We find statistical evidence that more couples turn their head to the right when kissing"

## The rationale behind statistical modeling
- Let $X_1, \dots, X_n$ be $n$ independent copies of $X$
- The goal of statistics is to learn the distribution of $X$
- If $X \in \{0,1\}$, easy! It's a Bernoulli and we only have to learn the parameter $p$
- Can be more more complicated. For example, here is a (partial) dataset with number of siblings (including self) that were collected from college students a few years back: 2, 3, 2, 4, 1, 3, 1, 1, 1, 1, 1, 2, 2, 3....
- We could make no assumption and try to learn the pmf:
  ![[Pasted image 20250513194143.png]]
- Or we could assume that $X-1 \sim Poiss(\lambda)$. Thats 1 parameter to learn

## Statistical model

### Formal definition

Let the observed outcome of a statistical experiment be a ==sample== $X_1, \dots, X_n$ of $n$ i.i.d random variables in some measurable space $E$ (usually $E \subseteq \mathbb{R}$) and denote $\mathbb{P}$ their common distribution. A ==statistical model== associated to that statistical experiment is a ==pair==
$$(E, (\mathbb{P}_\theta)_{\theta\in \Theta}),$$
Where:
- $E$ is called sample space
- $(\mathbb{P}_\theta)_{\theta\in \Theta}$ is a family of probability measures on $E$;
- $\Theta$ is any set, called parameter set
## Parametric, nonparametric and semiparametric models

Usually we will assume that the statistical model is well specified, i.e. defined such that $\exists\theta$ such that $\mathbb{P}=\mathbb{P}_\theta$  

This particular $\theta$ is called the true parameter, and is unknown: The aim of the statistical experiment is to find $\theta$, or check it's properties when they have a special meaning.

We often assume that $\Theta\subseteq \mathbb{R}^d$ for some $d\geq 1$ : Then the model is called parametric
Sometimes we could have $\Theta$ be infinite dimensional in which case the model is called nonparametric

There are also variants with combinational $\Theta$ which are infinite or finite dimensions, which case the model is called semiparametric.

## Examples of parametric models
![[Pasted image 20250514150905.png]]

## Gaussian Mixtures

![[Pasted image 20250515122237.png]]
Above we can see a data collected of the cherry blossom run in Washington DC in 2017, here we can see that there are two peak around 2000 and another one around 6000. This makes the gaussian improper for modelling this kind of a distribution.
We need to find a family of distribution that takes into account that there are two subpopulations within this bigger population of running times.
And the thing we're actually going to use for this scenario is what's called a mixture of two Gaussians.

### Sub populations
Assume that each sub-population is Gaussian:
$$
N(\mu_1, \sigma^2_1)\quad and\quad N(\mu_2,\sigma_2^2)
$$
We also need to specify the size (or proportion) of each sub-population
- $\pi \in (0,1)$: proportion of first sub-populations
- $1-\pi$: proportion of second sub-population
### Example graph
![[Pasted image 20250515123714.png]]
Mixture of $f_1(x)=N(0,0.5^2)$ and $f_2(x)=N(1,0.75^2)$ and $\pi=0.3$
Therefore:
$$
f(x)=\pi*f_1(x)+(1-\pi)f_2(x)
$$

## Another representation of Gaussian Mixtures

$X$ follows a mixture of two Gaussians if and only if
$$
X=ZX_1+(1-Z)X_2
$$
Where $Z\sim Ber(\pi), X_1 \sim N(\mu_1,\sigma_1^2), X_2 \sim N(\mu_2,\sigma_2^2)$ and $Z$ is independend of $X_1$ and $X_2$
![[Pasted image 20250515131152.png]]

## Identifiability
![[Pasted image 20250515143313.png]]