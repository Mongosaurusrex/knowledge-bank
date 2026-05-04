![[Pasted image 20241031193357.png]]
1. **Hypothesis Values**: The values of $\Theta$ represent different alternative hypotheses. The probability distribution $p_{\Theta|X}(\theta | x)$ for different values of $\theta$ is shown on a bar graph. For this example:

• $p_{\Theta|X}(1|x) = 0.1$

• $p_{\Theta|X}(2|x) = 0.6$

• $p_{\Theta|X}(3|x) = 0.3$

2. **MAP Rule**: The Maximum A Posteriori (MAP) rule selects $\hat{\theta} = 2$ because it has the highest conditional probability given X = x.

3. **LMS (Least Mean Square)**: The least mean square estimator $\hat{\theta} = E[\Theta | X = x] = 2.2$.

4. **Probability of Error**:

• **Conditional Probability of Error**: $P(\hat{\Theta} \neq \Theta | X = x) = 0.4$, which is minimized under the MAP rule.

• **Overall Probability of Error**: Calculated by summing over possible values of x, using both p_X(x) and the conditional probability of error $P(\hat{\Theta} \neq \Theta | X = x).$

5. **Formulas**:

• The conditional probability formula $p_{\Theta | X}(\theta | x) = \frac{p_\Theta(\theta) p_{X|\Theta}(x|\theta)}{p_X(x)}$ is shown in a blue box.

• $p_X(x)$ is given as a sum over all possible values of $\theta: p_X(x) = \sum_{\theta{\prime}} p_\Theta(\theta{\prime}) p_{X|\Theta}(x|\theta{\prime})$. 