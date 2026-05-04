A probabilistic model of a sample space can be made into two steps:
- Describe possible outcomes
- Describe beliefs about likelihood of outcomes

#### List (set) of possible outcomes
- List must be mutually exclusive
- Collectively exhaustive
- At the "right" granularity

Suppose that you flip a coin and look at the weather
- H and rains
- H and no rain
- T and rains
- T and no rain

But for the relevant sample space for answering "which side of the coin will happen" then the sample space should be [H, T]

### Examples
##### Two rolls of a tetrahedral die (discrete/finite example)
Y = Second roll
X = First roll

| Y/X | 1   | 2   | 3   | 4   |
| --- | --- | --- | --- | --- |
| 4   |     |     |     |     |
| 3   |     | 2,3 |     |     |
| 2   |     |     | 3,2 |     |
| 1   | 1,1 |     |     |     |
Could also be described as a sequential description (tree) and is finite because the outcome can only be (4x4) possibilities

##### Continuous example
![[Pasted image 20240904074144.png]]
