A **joint probability mass function** (joint PMF) describes the probability distribution of two or more discrete random variables occurring simultaneously. For two random variables X and Y, the joint PMF, denoted as P(X = x, Y = y) or $p_{X,Y}(x,y)$ , gives the probability that X takes the value x and Y takes the value y at the same time. The notation continues with infinite amount of variables.

The individual PMFs in the joint PMFs are called **marginal PMFs**

## Example

| Y/X | 1    | 2    | 3    | 4    |
| --- | ---- | ---- | ---- | ---- |
| 4   | 1/20 | 2/20 | 2/20 |      |
| 3   | 2/20 | 4/20 | 1/20 | 2/20 |
| 2   |      | 1/20 | 3/20 | 1/20 |
| 1   |      | 1/20 |      |      |
$$p_{X,Y}(1,3)=2/20
$$$$
p_X(4)=\frac{1}{20}+\frac{2}{20}
$$$$
p_Y(2)=\frac{1}{20}+\frac{3}{20}+\frac{1}{20}
$$
$$
P(X=Y)=\frac{1}{20}+\frac{1}{20}
$$
## Functions of multiple random variables
Let say that $Z = g(X,Y)$
$$
PMF: p_Z(z) = P(Z=z) = P(g(X,Y)=z) = \sum_{(x,y): g(x,y)=z}p_{X,Y}(x,y)
$$

