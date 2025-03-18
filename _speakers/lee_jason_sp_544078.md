---
name: "Jason Lee"
role: "Speaker"
affiliation: "Princeton University"
website: "https://jasondlee88.github.io/"
photo: "lee.jpeg"
talk: "Emergence and Scaling Laws for SGD Learning and Learning Compositional Functions with Transformers"
abstract: "This is a two part talk. (1) We study the sample and time complexity of online stochastic gradient descent (SGD) for learning a two-layer neural network with $P$ orthogonal neurons on isotropic Gaussian data. We focus on the challenging regime $$P\\gg 1$$ and allow for large condition number in the second-layer, covering the power-law scaling $$a_p= p^{-\\beta}$$ as a special case. We characterize the SGD dynamics for the training of a student two-layer network to minimize the squared loss, and identify sharp transition times for the recovery of each signal direction. In the power-law setting, our analysis entails that while the learning of individual teacher neurons exhibits abrupt phase transitions, the juxtaposition of $$P\\gg 1$$ emergent learning curves at different timescales leads to a smooth scaling law in the cumulative squared loss. (2) Transformer-based language models have demonstrated impressive capabilities across a range of complex reasoning tasks. Prior theoretical work exploring the expressive power of transformers has shown that they can efficiently perform multi-step reasoning tasks. However, the learnability of such constructions, particularly the conditions on the data distribution that enable efficient learning via SGD, remains an open question. Towards answering this question, we study the learnability of a task called $$k$$-fold composition, which requires computing an interleaved composition of $$k$$ input permutations and $$k$$ hidden permutations, and can be expressed by a transformer with $$O(\\log k)$$ layers. We show that this function class can be efficiently learned, with runtime and sample complexity polynomial in $$k$$, by gradient descent on an $$O(\\log k)$$-depth transformer via mixed training: one in which data consists of $$k'$$-fold composition functions with $$k' \\le k$$ trained on simultaneously. Our work sheds light on the necessity and sufficiency of having both easy and hard examples in the data distribution for transformers to learn complex compositional tasks. A corresponding statistical query lower bound shows that without mixed training requires $$\\exp(k)$$ samples and time."
bio: "TBA"
day: "2"
start: "3:00 PM"
end: "4:00 PM"
location: "Simonyi Conference Center"
---
