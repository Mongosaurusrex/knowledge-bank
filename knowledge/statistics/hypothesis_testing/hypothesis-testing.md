# Hypothesis Testing

Slug: Statistics/Hypothesis-Testing/hypothesis-testing

Links: Statistics/Hypothesis-Testing/walds-test, Statistics/Hypothesis-Testing/t-test, Statistics/Hypothesis-Testing/p-value

At the core of statistics lie the questions we pose to data. Hypothesis testing provides a structured way to ask and answer these questions. Central to this framework is the null hypothesis (H_0): a formal statement representing the default or baseline assumption. It serves as the starting point against which evidence from data is evaluated. By testing the null hypothesis, we assess whether the observed results could reasonably be explained by chance alone, or whether there is enough evidence to favor an alternative hypothesis (H_1).
For example:

H_0: The average waiting time at a hospital is 30 minutes.
H_1: The average waiting time at a hospital is longer than 30 minutes.

Here, H_0 captures the status quo (“on average, patients wait 30 minutes”), while H_1 represents the competing claim we want to investigate. The statistical test then quantifies how consistent the data is with H_0, and whether it provides sufficient grounds to reject it in favor of H_1.
Errors in hypothesis testing
Consider the following table in terms of what kind of error we are witnessing:




















Decision/RealityH_0 trueH_1 trueReject H_0Type I errorCorrectDo not reject H_0CorrectType II error
The Hypothesis Testing Procedure

State the hypotheses
Clearly define H_0 (the baseline claim) and H_1 (the competing claim).
Choose a significance level (\alpha)
This is the probability of rejecting H_0 when it is actually true (a Type I error). Common choices are 0.05 or 0.01. So this say at what level do we tolerate a probability to have a Type I error
Select a test statistic
A function of the data (e.g. a Wald Test or a T-test) that measures the discrepancy between the observed data and what H_0 predicts.
Determine the sampling distribution under H_0
This tells us what values of the test statistic we should expect if H_0 were true.
Compute the p-value
The probability, under H_0, of obtaining a test statistic at least as extreme as the one observed.
Make a decision

If the p-value \leq \alpha, reject H_0 (evidence favors H_1).
If the p-value &gt; \alpha, do not reject H_0 (insufficient evidence against it).


