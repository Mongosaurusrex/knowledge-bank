At the end of this lecture, you will be able to do the following:  
- Understand and avoid the pitfalls of multiple hypothesis testing
- Use the Bonferroni method to control the Family Wise Error Rate (FWER)
- Use the Benjamini-Hochberg method to control the False Discovery Rate (FDR)
## The Dead Salmon Study: Why Multiple Testing Correction Matters

In a 2009 study, researchers placed a **dead Atlantic salmon** in an fMRI scanner and showed it pictures of people. They then ran a standard brain activity analysis — and found "statistically significant" brain activity.

### Why?
- fMRI scans involve tens of thousands of voxels (tests)
- Using a significance level of \( $\alpha = 0.05$ \) on ~60,000 tests yields ~3,000 expected false positives
- No correction was initially applied for multiple comparisons

### Moral of the story:
Even a dead fish shows significance if you don't correct for multiple testing. The study highlights the importance of statistical rigor in research and became a textbook example of the **multiple comparisons problem**.


## Multiple Testing

When testing multiple hypotheses (e.g. over many voxels in brain imaging), we are bound to make **false discoveries** unless we control for it.

### Problem
- We cannot draw conclusions about "all the voxels" at once without increasing the risk of false positives.
- Running many tests leads to an accumulation of Type I errors.

---

### Two Common Solutions

#### 1. Control Family-Wise Error Rate (FWER)
- Goal: Limit the probability of **at least one false discovery**.
- Find thresholds \( $C_1, \ldots, C_N$ \) such that:
  $$\mathbb{P}_{\mu_i = 0} \left( \bigcup_{i=1}^{N} \{ |T_i| > C_i \} \right) \leq \alpha$$
#### 2. Control False Discovery Rate (FDR)
- Goal: Limit the **expected proportion** of false discoveries among all discoveries.
- Find thresholds \( $C_1, \ldots, C_N$ \) such that:
$$  \text{FDR} = \mathbb{E} \left[ \frac{\#\{i : |T_i| > C_i \text{ and } \mu_i = 0\}}{\#\{i : |T_i| > C_i\}} \right] \leq \alpha$$

---

### Practical Approach
- It's easier to work with **p-values**:
$$  P_i = \mathbb{P}_{\mu = 0} \left( |T| > |t_i^{\text{obs}}| \right)$$
  where \( $t_i^{\text{obs}}$ \) is the observed value of the test statistic, and \( $T \sim t_{n-1}$ \).

## The Bonferroni Method

### Key Idea
- To **control the Family-Wise Error Rate (FWER)**, we use the **Bonferroni correction**.
- Instead of using significance level \( $\alpha$ \) for each test, we use a stricter threshold:
$$  \frac{\alpha}{N}$$

  where \( $N$ \) is the number of tests.

---

### Application Rule
- **Reject** the \( $i$ \)-th null hypothesis if:
$$  p_i < \frac{\alpha}{N}$$

---

### Example
- In the **salmon example**, given:
 $$ \alpha = 0.001,\quad N = 8{,}064$$
  each test is performed at:
$$  \frac{0.001}{8064} = 1.24 \times 10^{-7}$$

- This results in a very small threshold and is therefore **very conservative**, often leading to **no discoveries**.

---

### Theoretical Justification
- Using the **union bound**:
 $$ \mathbb{P}(A \cup B) \leq \mathbb{P}(A) + \mathbb{P}(B)$$
- The FWER can be bounded as:
$$  \text{FWER} = \mathbb{P}\left(\bigcup_{i=1}^{N} \left\{ P_i < \frac{\alpha}{N} \right\} \right)
  \leq \sum_{i=1}^N \mathbb{P}\left(P_i < \frac{\alpha}{N}\right)
  = N \cdot \frac{\alpha}{N}
  = \alpha
$$

---

### Conclusion
- The Bonferroni method successfully controls FWER at level \( $\alpha$ \), but it is often **overly conservative**.

## Benjamini–Hochberg (BH) Procedure Summary

The **Benjamini–Hochberg (BH)** procedure controls the **False Discovery Rate (FDR)** when conducting multiple hypothesis tests.  
Unlike Bonferroni (which controls the chance of *any* false positives), BH controls the **expected proportion** of false discoveries among all rejected hypotheses.

---

### **Inputs**
- A list of \( $N$ \) p-values: \( $p_1, p_2, \dots, p_N$ \)
- A desired FDR level \( $\alpha \in (0, 1)$ \)

---

### **Procedure**

1. **Sort the p-values** in increasing order:
   $$p_{(1)} \leq p_{(2)} \leq \dots \leq p_{(N)}$$
   
2. **Compute thresholds** for each rank \( $i$ \):
   $$\text{threshold}_i = \frac{i}{N} \cdot \alpha$$
3. **Find the largest \( i \)** such that:
$$   p_{(i)} \leq \frac{i}{N} \cdot \alpha$$

4. **Reject all null hypotheses** with ranks \( 1 \) through \( $i$ \).  
   (That is, reject all \( $H_{(j)}$ \) for \( $j \leq i$ \))

---

### **Notes**
- If **no** p-value satisfies the condition, reject none.
- BH is **less conservative** than Bonferroni, allowing more discoveries.
- Especially useful when many true positives are expected.
