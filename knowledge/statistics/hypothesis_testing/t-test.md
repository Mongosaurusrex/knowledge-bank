# T-Test

Slug: Statistics/Hypothesis-Testing/t-test

The Student’s t-distribution arises when we estimate the population mean from a sample, while also estimating the variance.
It is similar to the standard normal distribution but has heavier tails, reflecting the extra uncertainty introduced by estimating the variance.

As the sample size n increases, the t-distribution approaches the standard normal distribution (N(0,1)).
The shape of the t-distribution is determined by the degrees of freedom (df), usually related to the sample size.

One-Sample T-test
We test whether a sample mean \bar{x} differs from a hypothesized mean \mu_0.
T = \frac{\bar{x} - \mu_0}{s / \sqrt{n}}, \quad df = n-1


One-sided test

H_0: \mu = \mu_0
H_1: \mu &gt; \mu_0 (or H_1: \mu &lt; \mu_0)
Reject H_0 if T is greater (or smaller) than the critical value t_{df, 1-\alpha}.



Two-sided test

H_0: \mu = \mu_0
H_1: \mu \neq \mu_0
Reject H_0 if |T| &gt; t_{df, 1-\alpha/2}.



Two-Sample T-tests
We compare the means of two independent samples.
Student’s Two-Sample T-test (Equal Variances Assumed)
T = \frac{\bar{x}_1 - \bar{x}_2}{s_p \sqrt{\tfrac{1}{n_1} + \tfrac{1}{n_2}}}
where
s_p^2 = \frac{(n_1 - 1) s_1^2 + (n_2 - 1) s_2^2}{n_1 + n_2 - 2}

Degrees of freedom: df = n_1 + n_2 - 2.
One-sided: H_1: \mu_1 &gt; \mu_2 (or &lt;).
Two-sided: H_1: \mu_1 \neq \mu_2.

Welch’s T-test (Unequal Variances)
T = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{\tfrac{s_1^2}{n_1} + \tfrac{s_2^2}{n_2}}}

One-sided: H_1: \mu_1 &gt; \mu_2 (or &lt;).
Two-sided: H_1: \mu_1 \neq \mu_2.

Summary

One-sample t-test: Compare a sample mean to a hypothesized mean.
Two-sample Student’s t-test: Compare two sample means, assuming equal variances.
Welch’s t-test: Compare two sample means, without assuming equal variances.

Additional Resources
homepage.divms.uiowa.edu/~mbognar/applets/t.html