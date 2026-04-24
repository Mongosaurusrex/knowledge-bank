# Posterior

Slug: Statistics/Bayesian-Statistics/bayesian-posterior

What Is a Posterior?
The posterior distribution represents our updated belief about an unknown parameter \theta after we have observed data.
It combines:

The prior distribution \pi(\theta), representing beliefs before seeing the data
The likelihood function L_n(\theta) = f(X_1, \dots, X_n \mid \theta), which describes how likely the observed data are under different values of \theta

Interpretation

The posterior reflects how the data have updated our prior belief
It gives the relative plausibility of each value of \theta after seeing the data
The shape and concentration of the posterior depend on:

The data (through the likelihood)
The prior belief (through \pi(\\theta))



Bayesian Updating
Bayesian inference is an iterative process:

Begin with a prior
Collect data and form a posterior
Use this posterior as a new prior for future updates
