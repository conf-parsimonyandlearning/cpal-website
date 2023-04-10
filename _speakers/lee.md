---
name: Jason Lee
role: Speaker
website: https://jasondlee88.github.io/
affiliation: Princeton
photo: lee.jpeg
talk: Feature Learning with gradient descent 
abstract: 'Significant theoretical work has established that in specific regimes, neural networks trained by gradient descent behave like kernel methods. However, in practice, it is known that neural networks strongly outperform their associated kernels. In this work, we explain this gap by demonstrating that there is a large class of functions which cannot be efficiently learned by kernel methods but can be easily learned with gradient descent on a two layer neural network outside the kernel regime by learning representations that are relevant to the target task. We also demonstrate that these representations allow for efficient transfer learning, which is impossible in the kernel regime.  Specifically, we consider the problem of learning polynomials which depend on only a few relevant directions, i.e. of the form f⋆(x)=g(Ux) where U: \R^d \to \R^r with d≫r. When the degree of f⋆ is p, it is known that n≍d^p samples are necessary to learn f⋆ in the kernel regime. Our primary result is that gradient descent learns a representation of the data which depends only on the directions relevant to f⋆. This results in an improved sample complexity of n≍rd^2+pd^r. Furthermore, in a transfer learning setup where the data distributions in the source and target domain share the same representation U but have different polynomial heads we show that a popular heuristic for transfer learning has a target sample complexity independent of d.  This is joint work with Alex Damian and Mahdi Soltanolkotabi.'
---
