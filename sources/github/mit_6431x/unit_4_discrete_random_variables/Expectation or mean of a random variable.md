The Expectation (or Mean) of a random variable is a measure of the central or average value that the variable takes on over many trials or observations. In simpler terms, it tells us what we can expect the outcome to be on average if we were to repeat an experiment or random process many times.

>[!info]  Definition
>$$E[X]=\sum_xp_X(x)$$

## Example:
You play a game 1000 times, random gain at each play as follows:

| Gain | P    |
| ---- | ---- |
| 1    | 2/10 |
| 2    | 5/10 |
| 4    | 3/10 |
The average gain can be then calculated as:
$$
\frac{1*200+2*500+4*300}{1000} = 1*\frac{2}{10}+2*\frac{5}{10}+4*\frac{3}{10}
$$
## Elementary properties:
- If $X \geq 0$, then $E[X] \geq 0$ 
- If $a \leq X \leq b$, then $a\leq E[X] \leq b$ 
- If $c$ is a constant, $E[c] = c$
## If the value takes form of $E[g(x)]$
![[Pasted image 20240927062551.png]]
If we average over $y$:
$$
E[Y]=\sum_y
yp_Y(y)=3(0.1+0.2)+4(0.3+0.4)$$
If we average over $x$:
$$
3*0.1+3*0.2+4*0.3+4*0.4
$$
Which gives us:
>[!info]  Definition
>$$E[X]=E[g(x)]=\sum_xg(x)p_X(x)$$

>[!error]  Caution in general
>$$E[g(x)] \neq g(E[X])$$

## Linearity of expectation
>[!info]  Definition
>$$E[aX + b] = aE[X]+b$$
