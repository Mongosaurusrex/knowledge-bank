# The Kolmogorov-Lilliefors Test

Slug: Statistics/Nonparametric-Hypothesis-testing/kolmogorov-lilliefors

Links: Statistics/Nonparametric-Hypothesis-testing/kolmogorov-smirnov

The Lilliefors test is a modification of the Kolmogorov–Smirnov (KS) test that accounts for the fact that we often don’t know the population mean and variance in advance — and instead estimate them from the sample.
This violates the assumptions of the regular KS test, which requires those parameters to be fixed. The Lilliefors test corrects for that by adjusting the distribution of the test statistic.
The null hypothesis assumes normality, but allows the parameters to be estimated from the sample. This makes the Lilliefors test more realistic than the classical KS test for normality testing.
When to Use It

You’re testing for normality.
You estimated the mean and standard deviation from your sample.
Your sample is continuous (not binned or discrete).

The Test
Let ( D ) be the maximum distance between the empirical CDF of your sample and the theoretical CDF of a normal distribution fit to your data (i.e., using the sample mean and standard deviation). The Lilliefors test uses the same test statistic as KS:
D_n = \sup_x \left| F_n(x) - F(x; \hat{\mu}, \hat{\sigma}) \right|
But it compares it to a different null distribution, accounting for the parameter estimation.
Example (Python)
import numpy as np
 
from statsmodels.stats.diagnostic import lilliefors
 
# Generate a sample from a normal distribution
np.random.seed(42)
normal_data = np.random.normal(loc=0, scale=1, size=1000)
 
# Run the Lilliefors test (KS test adjusted for estimated mean and std)
stat_lillie, p_lillie = lilliefors(normal_data)
 
This gives us:
\begin{aligned}
D_{Lilliefors} &amp;= 0.0214 \\
p &amp;= 0.4051
\end{aligned}
Because the p-value is relatively high, we fail to reject the null hypothesis — there’s no strong evidence that the data deviates from normality.
Summary

Use the Lilliefors test instead of KS when you’re testing normality and have fit the parameters.
The output is a KS-like statistic and a p-value based on simulations or adjusted tables.
It’s a quick and useful test for normality when you can’t assume known parameters.
