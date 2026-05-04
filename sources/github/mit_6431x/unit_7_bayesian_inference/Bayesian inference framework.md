![[Pasted image 20241030091209.png]]
1. **Unknown Parameter (Θ)**:

• We start with an unknown value we want to learn about, called Θ. We assume it has some initial distribution (called the **prior**) based on our current knowledge or assumptions.

2. **Observation (X)**:

• We collect data (called **observation** X), which depends on Θ in some way. This data gives us more information about Θ.

3. **Updating Belief with Bayes’ Rule**:

• Using Bayes’ rule, we combine our prior beliefs and the new data to get an **updated belief** about Θ, known as the **posterior**. This posterior tells us what we now believe about Θ after seeing the data.

4. **Choosing a Prior**:

• The choice of the prior can come from different sources: it could be based on past studies, symmetry, a known range of values, or even subjective judgment.

![[Pasted image 20241030093214.png]]
1. **Posterior Distribution**:

• The result of Bayesian inference is a posterior distribution, which can be expressed as a **PMF (Probability Mass Function)** for discrete variables  p_{\Theta|X}(\cdot | x)  or a **PDF (Probability Density Function)** for continuous variables  f_{\Theta|X}(\cdot | x) .

• This distribution gives the updated probabilities (or densities) for different values of the unknown parameter Θ after observing data  X .

2. **Examples of Posterior Distributions**:

• The diagrams on the left show examples of posterior distributions. These could have different shapes depending on the data and prior beliefs.

• The plot on the right shows an example applied to a real-world scenario: an electoral vote distribution for a candidate, showing the probability of different outcomes based on prior data and the observation process.

3. **Inference Workflow**:

• The bottom diagram shows the Bayesian workflow:

• Start with a **prior** distribution for Θ.

• Incorporate data  X  through an **observation process**.

• Calculate the **posterior** distribution using Bayes’ rule.

• Use the posterior to obtain **point estimates** (like the mean or median) and conduct **error analysis** or other types of inference.

![[Pasted image 20241030093736.png]]
1. **Posterior Distribution**:

• The main result in Bayesian inference is the posterior distribution (either PMF or PDF), which describes the updated beliefs about the parameter Θ after observing data .

2. **Estimate vs. Estimator**:

• **Estimate** () is a specific value derived from data.

• **Estimator** () is a function of the data and is considered a random variable because it depends on .

3. **Types of Point Estimates**:

• **MAP (Maximum A Posteriori)**: The value of Θ that maximizes the posterior distribution. This is the most likely value for Θ given the observed data.

• For discrete Θ: 

• For continuous Θ: 

• **Conditional Expectation**: The mean of the posterior distribution, , often used in **Least Mean Squares (LMS)** estimation.
