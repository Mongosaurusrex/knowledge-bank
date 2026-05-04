At the end of this lecture, you will be able to:  
- Apply the **Delta method** to an asymptotically normal sequence of random variables.
- Estimate the parameter and construct **confidence intervals for an exponential statistical model** using the Delta method.
- Construct confidence intervals for a variety of statistical models using the Delta method and one of the **conservative** , **solve** , or **plug-in** methods.
- Give a **frequentist interpretation** of the meaning of a (asymptotic) confidence interval of level .
- Understand the basic principle behind hypothesis testing.

A 95% confidence interval is not a statement about the probability that a specific interval contains the true parameter. Rather, it reflects the reliability of the **interval construction method**. Imagine a blindfolded archer repeatedly shooting arrows at a hidden target. After each shot, someone draws a circle around the target in a way that is known to include the arrow 95% of the time. Over many repeated attempts, 95% of the circles will successfully capture the arrows. The archer, unable to see where the arrows land, gains confidence not from any individual shot, but from the reliability of the circle-drawing method.

In the same way, when we construct a confidence interval from data, we are using a method that, if applied across many repetitions, will contain the true parameter 95% of the time. Once we observe a specific interval — say [0.34, 0.57] — we can no longer speak in terms of probability about whether it contains the true parameter. The parameter is fixed, and the interval is now fixed too; it either does or doesn’t contain the parameter. What we can say is that we are 95% confident in the procedure that gave us this interval — just as the archer is confident in the circle-drawing method, even without seeing the outcome.

## Example: Modeling Inter-arrival Times of a subway system

Lets say that a subway arrives given an interval. If I have arrived and just missed the train T how much do I need to wait until the next one?
$$
P(T>t+s|T>t)
$$
So I have now waited t seconds how much more should I wait (s)?

Since this problem is exponential then the memorylessness property of an exponential makes it:
$$
e^{-\lambda t}=e^{-\lambda s}
$$

## The Delta Method

The **Delta Method** is used to find the **asymptotic distribution** of a **function of an estimator**.
Suppose you have an estimator Z_n such that:
$$
\sqrt{n}(Z_n - \theta) \xrightarrow{d} \mathcal{N}(0, \sigma^2)
$$
and a function g that is **differentiable at** \theta.
Then the delta method say:
$$
\sqrt{n}(g(Z_n) - g(\theta)) \xrightarrow{d} \mathcal{N}\left(0, [g’(\theta)]^2 \cdot \sigma^2\right)$$
#### When to use it:
- Your estimator $Z_n$ is approximately normal
- You’re interested in a **function** of $Z_n$, like $\log(Z_n), Z_n^2$, or $1/Z_n$
- You want to approximate standard errors or build confidence intervals for that transformed value