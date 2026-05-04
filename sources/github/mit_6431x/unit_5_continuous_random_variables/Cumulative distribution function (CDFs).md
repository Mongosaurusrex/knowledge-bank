A Cumulative Distribution Function (CDF) is a function that gives the probability that a random variable  X  will take a value less than or equal to a certain value  x . For a given value  x , the CDF, typically denoted as  F(x) , is calculated as:
$$
F_X(x)=P(X \leq x)
$$
For continuous random variables:
$$
F_X(x)=P(X\leq x)= \int_{-\infty}^xf_X(t)dt
$$
For discrete random variables:
$$
F_X(x)=P(X\leq x)=\sum_{k\leq x}p_X(k)
$$
## CDF to calculate PDF
the CDF can indeed be used to calculate the Probability Density Function (PDF) for a continuous random variable. Here’s how it works:

1. Relationship between CDF and PDF for Continuous Random Variables

For a continuous random variable  X  with CDF  F(x)  and PDF  f(x) , the PDF is the derivative of the CDF:

$$
f(x) = \frac{d}{dx} F(x)
$$

This means that if you have the CDF of a continuous random variable, you can find its PDF by differentiating the CDF with respect to  x .

2. Example of Finding the PDF from the CDF

Suppose the CDF of a continuous random variable  X  is given by:

$$
F(x) = \begin{cases}
0 & x < a \\
\frac{x - a}{b - a} & a \leq x \leq b \\
1 & x > b
\end{cases}
$$


To find the PDF, differentiate  F(x)  with respect to  x :

$$
f(x) = \frac{d}{dx} F(x) = \begin{cases}
0 & x < a \\
\frac{1}{b - a} & a \leq x \leq b \\
0 & x > b
\end{cases}
$$

This is the PDF of a continuous uniform distribution on the interval [a, b].

3. Key Takeaway

The PDF is simply the rate of change of the CDF at any point  x . For continuous distributions, it tells you the likelihood of observing a value within an infinitesimally small interval around  x .

## General CDF properties
$$
F_X(x)=P(X\leq x)
$$
$$
If\ y\geq x \to F_X(y)\geq F_X(x)
$$
$$
F_X(x)\ tends\ to\ 1,\ as\ x\to\infty
$$
$$
F_X(x)\ tends\ to\ 0,\ as\ x\to-\infty
$$
