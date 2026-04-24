# QQ-Plots

Slug: Statistics/Nonparametric-Hypothesis-testing/qq-plots

A QQ-plot (Quantile–Quantile plot) is a graphical tool used to assess whether your sample data comes from a specific theoretical distribution — most commonly, the normal distribution.
It works by plotting:

The quantiles of the theoretical distribution (x-axis)
Against the quantiles of your sample data (y-axis)

More specifically, it plots the points:

\left( F^{-1}\left(\frac{1}{n}\right), F_n^{-1}\left(\frac{1}{n}\right) \right), 

\left( F^{-1}\left(\frac{2}{n}\right), F_n^{-1}\left(\frac{2}{n}\right) \right), \ldots,

\left( F^{-1}\left(\frac{n-1}{n}\right), F_n^{-1}\left(\frac{n-1}{n}\right) \right)

If your data closely follows the target distribution, the points will fall approximately along the 45-degree line (y = x).
Interpreting the QQ-plot
Below are QQ-plots illustrating common deviations from normality:


Right Skew (Exp(1)): Long right tail; points bend upward to the right.
Left Skew (-Exp(1)): Long left tail; points bend downward to the left.
Heavy Tails (t-distribution, df=3): More extreme values than normal; points curve outwards at both ends.
Light Tails (Uniform[0,1]): Fewer extreme values; QQ-plot shows an S-shape hugging the diagonal in the middle.
