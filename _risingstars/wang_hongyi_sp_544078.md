---
name: Hongyi Wang
role: Senior Project Scientist
affiliation: CMU
website: https://hwang595.github.io/
photo: wangh.png
talk: "Speeding up Large-Scale Machine Learning Model Development Using Low-Rank Models and Gradients"
abstract: "Large-scale machine learning (ML) models, such as GPT-4 and Llama2, are at the forefront of advances in the field of AI. Nonetheless, developing these large-scale ML models demands substantial computational resources and a deep understanding of distributed ML and systems. In this presentation, I will introduce three frameworks, namely ATOMO, Pufferfish, and Cuttlefish, which use low-rank approximations on model gradients and model weights to significantly expedite ML model training. ATOMO is a general compression framework that has experimentally established that using low-rank gradients, as opposed to sparse ones, can lead to substantially faster distributed training. Pufferfish further bypasses the cost of compression by directly training low-rank models. However, directly training low-rank models usually leads to a loss in accuracy. Pufferfish mitigates this issue by training a full-rank model and then converting to a low-rank model early in the training process. Nonetheless, Pufferfish necessitates extra hyperparameter tuning, such as determining the optimal transition time from full-rank to low-rank. Cuttlefish addresses this issue by automatically estimating and adjusting these hyperparameters during training. I will present extensive experimental results on the distributed training of large-scale ML models, including LLMs, to demonstrate the efficacy of these frameworks."
---
