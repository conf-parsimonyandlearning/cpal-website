---
name: "Zhenyu Zhang"
role: "Researcher"
affiliation: "University of Texas at Austin"
website: ""
photo: "image5.png"
talk: "Democratizing LLM Training via Low-Rank Methods"
abstract: "As Large Language Models (LLMs) continue to scale in size and capability, the cost and complexity of training -- particularly memory consumption from optimizer states -- have become critical bottlenecks. In this talk, we explore the evolution of low-rank optimization techniques for LLMs, tracing the progression from GaLore to APOLLO. GaLore introduces a memory-efficient training paradigm by applying low-rank projections to gradients and optimizer states, enabling the training of models with up to 7 billion parameters on consumer-grade GPUs such as the NVIDIA RTX 4090. Building on this foundation, APOLLO demonstrates the surprising effectiveness of rank-1 optimizer states with purely random projections, achieving SGD-level memory overhead while maintaining performance comparable to AdamW. This method brings substantial system-level improvements, including a 3x increase in throughput on 8xA100-80G GPUs and enhanced model scalability."
session: "1"
order: "5"
---
