![[Pasted image 20241021151831.png]]
## Covariance properties
$$
cov(X,X) = E[(X-E[X])^2]=var(X)=E[X^2]-(E[X])^2
$$
$$
cov(X,Y)=E[(X-E[X])*(Y-E[Y])] = E[XY]-E[XE[Y]]-E[E[X]Y]+E[E[X]E[Y]]
$$
$$
= E[XY]-E[X]E[Y]-E[X]E[Y]+E[X]E[Y]= E[XY]-E[X]E[Y]
$$
>[!important] Altenative defintion of covariance
>$$
\text{cov}(A, B) = E[AB] - E[A]E[B]
>$$

>[!important] Linearity of covariance
>$$
>cov(aX+b,Y)= a*cov(X,Y)
>$$

>[!important]
>$$
>cov(X,Y+Z) = cov(X,Y)+cov(X,Z)
>$$

## Variance of a sum of random variables
![[Pasted image 20241021180527.png]]
If the variables are independent the cov becomes 0
![[Pasted image 20241021180749.png]]


