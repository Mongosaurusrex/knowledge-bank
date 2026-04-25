# The Kolmogorov–Smirnov (KS) Test

Slug: Statistics/Nonparametric-Hypothesis-testing/kolmogorov-smirnov

Links: Statistics/Nonparametric-Hypothesis-testing/chi-squared-goodness-of-fit-testing

The KS test is a non-parametric method used to determine whether a sample comes from a specific continuous distribution.
Unlike the Chi-Squared test, which compares binned frequencies, the KS test compares the empirical cumulative distribution function (ECDF) of your sample with the theoretical cumulative distribution function (CDF) of the hypothesised distribution.
Purpose
To measure the maximum vertical distance between the ECDF and the CDF of a specified distribution. Formally, the test statistic is:
D_n = \sup_x |F_n(x) - F(x)|

( F_n(x) ): empirical CDF from the sample
( F(x) ): theoretical CDF under the null hypothesis
( D_n ): KS test statistic

Assumptions

The hypothesised distribution is continuous
The sample is independent and identically distributed (i.i.d.)
No ties in the data (KS is sensitive to discrete data)

Example: Testing Poisson Data
To demonstrate the KS test in its natural setting, let’s generate data from a standard normal distribution ( \mathcal{N}(0,1) ) and compare it against:

The correct distribution: ( \mathcal{N}(0,1) )
A slightly incorrect distribution: ( \mathcal{N}(1,1) )

from scipy.stats import norm, kstest
import numpy as np
 
np.random.seed(42)
normal_data = norm.rvs(loc=0, scale=1, size=1000)
 
# Test against correct distribution
ks_stat_true, p_val_true = kstest(normal_data, &#039;norm&#039;, args=(0, 1))
 
# Test against incorrect distribution
ks_stat_wrong, p_val_wrong = kstest(normal_data, &#039;norm&#039;, args=(1, 1))
This yields:
\begin{aligned}
D_{\mathcal{N}(0,1)} &amp;= 0.0173 \\
p_{\mathcal{N}(0,1)} &amp;= 0.9197 \\
\\
D_{\mathcal{N}(1,1)} &amp;= 0.3916 \\
p_{\mathcal{N}(1,1)} &amp;= 1.11 \times 10^{-138}\\
\\
\end{aligned}
Interpretation

The high p-value when testing against (\mathcal{N}(0,1) ) suggests the sample is consistent with the hypothesised distribution.
The extremely low p-value when testing against ( \mathcal{N}(1,1) ) strongly rejects the fit.
