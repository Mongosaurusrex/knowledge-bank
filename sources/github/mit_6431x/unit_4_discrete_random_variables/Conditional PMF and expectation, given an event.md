The conditional PMF provides the probability distribution of a discrete random variable given that another event or random variable has occurred or taken a particular value. Mathematically, the conditional PMF is derived from the joint distribution of the involved variables and normalized over the event in question. Conditional expectation, on the other hand, represents the expected value of a random variable given some condition or information, serving as a refined version of the expectation that accounts for additional knowledge about the system. These concepts are central to understanding dependent events, Bayesian inference, and updating probabilities in dynamic or uncertain environments.

>[!important]  Notation
>$$p_{X|A}(x) = P(X=x | A)$$

## Example
```dataviewjs
const labels = ['1', '2', '3', '4'];
const data = [1/4, 1/4, 1/4, 1/4];
const chartData = {  
    type: 'bar',
    data: {
        labels,
        datasets: [{
            label: 'x',
            data: data
        }],
        color: "red"
    }
}

window.renderChart(chartData, this.container)
```
Each outcome of the scenario has 1/4 probability
$$
E[X] = \frac{1+2+3+4}{4}=2.5
$$
$$
Var(X)= \frac{4^2-1}{12}=\frac{15}{12}=\frac{5}{4}
$$
$$
Let\ A=\{X\geq 2\}
$$
```dataviewjs
const labels = ['1', '2', '3', '4'];
const data = [0, 1/3, 1/3, 1/3];
const chartData = {  
    type: 'bar',
    data: {
        labels: labels,
        datasets: [{
            label: 'Numbers',
            data: data
        }]
    }
}

window.renderChart(chartData, this.container)
```

Each outcome has 1/3 probability
$$
E[X|A]=3
$$
$$
Var(X|A) = \frac{3^2-1}{12}=\frac{8}{12}=\frac{2}{3}
$$
