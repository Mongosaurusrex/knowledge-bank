# P-values

Slug: Statistics/Hypothesis-Testing/p-value

A p-value is the probability, under the assumption that the null hypothesis (H_0) is true, of obtaining data at least as extreme as what we observed.

A small p-value indicates that the observed data would be very unlikely if H_0 were true, providing evidence against H_0.
A large p-value indicates that the observed data is consistent with H_0, and thus we do not have enough evidence to reject it.

It is important to note:

The p-value does not tell us the probability that H_0 is true or false.
Instead, it quantifies how surprising the observed data is under the assumption that H_0 holds.

Example: Welch’s T-test and p-value
Suppose we want to test whether the average waiting time differs between Hospital A and Hospital B.  
We do not assume equal variances, so we use Welch’s t-test.

Sample A: \bar{x}_1 = 32, s_1 = 5, n_1 = 25  
Sample B: \bar{x}_2 = 30, s_2 = 4, n_2 = 20  

Step 1: Hypotheses

H_0: \mu_1 = \mu_2  
H_1: \mu_1 \neq \mu_2  

Step 2: Test statistic
T \approx 1.49
Step 3: Degrees of freedom (Welch–Satterthwaite)
df \approx 42
Step 4: p-value
For T = 1.49 with df \approx 42 in a two-sided test:
p \approx 2 \times P(T_{42} &gt; 1.49) \approx 0.14
Step 5: Decision
At significance level \alpha = 0.05, we do not reject H_0.  
The p-value of 0.14 indicates that the observed difference (2 minutes) could plausibly occur just by chance if the true means were equal.
Conventional significance levels






























p-value rangeSignificance levelTypical interpretationp \leq 0.01Highly significantVery strong evidence against H_00.01 &lt; p \leq 0.05SignificantModerate evidence against H_00.05 &lt; p \leq 0.10Marginally significantWeak evidence against H_0p &gt; 0.10Not significantNo convincing evidence against H_0