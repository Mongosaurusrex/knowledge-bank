# Chi Squared Goodness of fit testing

Slug: Statistics/Nonparametric-Hypothesis-testing/chi-squared-goodness-of-fit-testing

What is the purpose of the test
Suppose you have a dataset, and you want to evaluate how well it aligns with a particular discrete probability distribution. The Chi-Squared test helps you assess whether the observed frequencies in your dataset deviate significantly from what you’d expect under the hypothesized distribution.
Assumptions

The data is binned into discrete categories (e.g. 5 bins).
The sample size in each bin is reasonably large (typically ≥ 5 expected counts per bin).
Observations are independent.

The Test
The test statistic is computed as:

T_n = \sum_{i=1}^k \frac{(O_i - E_i)^2}{E_i}

Where:

( O_i ): Observed frequency in bin ( i )
( E_i ): Expected frequency in bin ( i ) under the null hypothesis
( k ): Number of bins

Large values of ( T_n ) suggest a poor fit between the data and the expected distribution.
Example
First lets generate some poisson data with a \lambda of 3.
bin_edges = np.arange(-0.5, 10.5, 1)
bin_centers = 0.5 * (bin_edges[1:] + bin_edges[:-1])
 
np.random.seed()
poisson_data = poisson.rvs(mu=3, size=1000)
 
observed, _ = np.histogram(poisson_data, bins=bin_edges)

Which we can see is definitely poisson in its distribution.
expected_poisson = poisson.pmf(np.arange(len(observed)), mu=3) * observed.sum()
expected_gaussian = (
    norm.pdf(bin_centers, loc=3, scale=1)
    * (bin_edges[1] - bin_edges[0])
    * observed.sum()
)
 
expected_poisson *= observed.sum() / expected_poisson.sum()
expected_gaussian *= observed.sum() / expected_gaussian.sum()
 
stat_poisson, p_poisson = chisquare(f_obs=observed, f_exp=expected_poisson)
stat_gaussian, p_gaussian = chisquare(f_obs=observed, f_exp=expected_gaussian)
Which in turn gives us:
\begin{aligned}
T_{poiss}=1.8236827300439549\\
p_{poiss}=0.9939587753318262\\
\\
T_{N}=698370.901071352\\
p_{N}=0.0
\end{aligned}
Given the high p-value under the Poisson model and the extremely low p-value under the Gaussian model, the evidence strongly favours the Poisson distribution for this data.
Degrees of freedom
df=\text{number of bins}-1-\text{number of estimated parameters}
For example, if you have:

5 bins
and estimate 2 parameters (like the mean and variance of a Gaussian)

Then:
df=5-1-2=2
Good to know

The Chi-Squared test is asymptotic, so the approximation becomes better as n \to \infty.
For small sample sizes, you should use exact p-values from tables.

You can find \chi^2 tables here