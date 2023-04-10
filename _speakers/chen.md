---
name: Beidi Chen
role: Speaker
website: https://cs.stanford.edu/people/beidic/
affiliation: Meta
photo: chen0.jpeg
talk: "Hardware-aware Sparsity: Accurate and Efficient Foundation Model Training"
abstract: "Foundation models trained on complex and rapidly growing data consume enormous computational resources. In this talk, I will describe our recent work on exploiting model and activation sparsity to accelerate foundation model training in both data and model parallel settings. We show that adapting algorithms on current hardware leads to efficient model training with no drop in accuracy. I will start by describing Pixelated Butterfly and Monarch, simple yet efficient sparse model training frameworks on GPUs. They use simple static block-sparse patterns based on butterfly and low-rank matrices, taking into account GPU block-oriented efficiency. They train up to 2.5x faster (wall-clock) than the dense Vision Transformer and GPT-2 counterparts with no drop in accuracy.  Next, I will present AC-SGD, communication-efficient pipeline parallelism training frameworks over slow networks. Based on an interesting observation that model weights change slowly during the training, AC-SGD compresses activations or the change of activations with guarantees. It trains or fine-tunes DeBERTa and GPT2-1.5B 4.3x faster in slower networks without sacrificing model quality. I will conclude by outlining three future research directions - data efficiency,software-hardware codesign, and ML for science, and several ongoing projects including linear-time algorithm for large optimal transport problems, efficient autoregressive model (gpt3-style) inference, and ML for new material discovery."
---
