---
name: Yaodong Yu
role: Ph.D. Student
affiliation: UC Berkeley
website: https://yaodongyu.github.io/
photo: yu.jpg
talk: "White-Box Transformers via Sparse Rate Reduction"
abstract: "In this talk, I will present the white-box transformer --- CRATE (i.e., Coding RAte reduction TransformEr). We contend that the objective of representation learning is to compress and transform the distribution of the data, say sets of tokens, towards a mixture of low-dimensional Gaussian distributions supported on incoherent subspaces. The quality of the final representation can be measured by a unified objective function called sparse rate reduction. From this perspective, popular deep networks such as transformers can be naturally viewed as realizing iterative schemes to optimize this objective incrementally. Particularly, we show that the standard transformer block can be derived from alternating optimization on complementary parts of this objective: the multi-head self-attention operator can be viewed as a gradient descent step to compress the token sets by minimizing lossy coding rate. This leads to a family of white-box transformer architectures which are mathematically interpretable. Our experiments show that these networks indeed learn to optimize the designed objective: they compress and sparsify representations of large-scale real-world vision datasets such as ImageNet, and achieve performance very close to thoroughly engineered transformers (ViTs). I will also present some recent theoretical and empirical results of CRATE on emergence behavior, language modeling, and auto-encoding."
---
