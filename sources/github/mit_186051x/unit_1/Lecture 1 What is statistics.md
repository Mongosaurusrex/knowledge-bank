>[!note]
> I love to say and I will say it again and again that 99% of statistics is taking averages and then maybe doing something fancy
> - Philippe Rigollet

## Review: Probability and randomness

Statistics, Data science, Machine Learning
- All use data to gather insights and ultimately make decisions
- Statistics is at the core of the data processing part
- Nowadays, computational aspects play an important role as data becomes larger

Computational view: data is a large sequence of numbers that needs to be processed by a relatively fast algorithm: approximate nearest neighbors, low dimensional embeddings, spectral methods, distributed optimation, etc.
Statistical view: Data comes from  *random process*. The goal is to learn how this process works in order to make predicitons or to understand what plays a role in it.

To understand randomness, we need PROBABILITY

### Probability
- Probability studies randomness
- Sometimes the physical process is completely known: dice, cards, roulette, coin toss ...

#### Simple examples:
Rolling one die:
- Alice gets $1 if # of dots $\leq$ 3 -> $E[A] = \frac{1}{2}\cdot 1 = 0.5$
- Bob gets $2 if # dots $\leq$ 2 -> $E[B] = \frac{1}{3} \cdot 2 = 0.66$
Rolling two dice:
- Choose a number between 2 and 12
- Win $100 dollars if you choose the sum of the two dice
Which number should you choose?
7 because that is the most probable = $E[W | 7] = 100 \cdot \frac{1}{6} = 16.6$

## Statistical modelling and the dogma of statistics and probability

The dogma of statistics and probability lies in the belief that uncertainty in the world can be quantified, modeled, and reasoned about using mathematical structures. It assumes that randomness, whether arising from natural phenomena or incomplete information, follows definable patterns governed by probability distributions. This framework enables practitioners to make informed decisions, estimate unseen quantities, and draw conclusions from data—despite inherent noise or variability. While interpretations differ—frequentist, Bayesian, or otherwise—the core dogma remains: that rigorous probabilistic reasoning provides the most coherent way to understand and navigate uncertainty in both science and society.

- **Probability** starts with known models and assumptions about a population or process and asks: _what is likely to happen?_ For example, given a fair six-sided die, what’s the chance of rolling a 4? It’s about predicting outcomes based on known parameters.
    
- **Statistics**, on the other hand, starts with observed data and asks: _what can we infer about the underlying model or population?_ For example, if we roll a die many times and record the results, can we tell if it’s fair? It’s about using data to make estimates, test hypotheses, or build models.

## What this course is about and not about

### What this course is about

- Understand the mathematical underpinning of statistical methods.
    
- How to give quantitative statements from modeling assumptions.
    
- Discover mathematical phenomena arising from statistics.
    
- Develop a framework that allows to give mathematical statements about new models.
    

### What this course is **not** about

- How to set up a statistical model for complicated real world examples;
    
- Implement statistical computational routines;
    
- Learn a lot of different specialized methods.

## Modeling Assumptions

Coming up with a model consists of making assumptions on the observations $R_i, i= 1,\dots, n$ in order to draw statistical conclusions. Here are some assumptions that we could potentially make:

1. Each $R_i$ is a random variable
2. Each of the random variables $R_i$ can is a Ber/Binom etc. with parameter p
3. $R_1, \dots, R_n$ are mutually independent.

## Population versus samples

We need to understand probabilistic aspects of the distribution of the random variable:
 $$
\hat p = \overline{R_n}=\frac{1}{n}\sum_{i=1}^n
R_i$$
 Specifically, we need to be able to answer questions such as:
 - Is the expected value of $\hat p$ close to the unknown $p$?
 - Does $\hat p$ take values close to $p$ with high probability?
 - Is the variance of $\hat p$ large? 
We need probabilistic tools! Most of them are about average of independent random variables