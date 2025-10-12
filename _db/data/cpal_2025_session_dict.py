#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Paper-title-to-session dictionary created by claude


def create_session_paper_mapping():
    """
    Creates a dictionary mapping (session_number, paper_number) tuples to paper titles.

    Returns:
        dict: A dictionary with keys as (session_number, paper_number) tuples and values as paper titles.
    """
    session_paper_mapping = {
        # Group 1: Sparsity, Efficiency, and Model Compression (Session 1)
        (
            1,
            1,
        ): "Progressive Gradient Flow for Robust N:M Sparsity Training in Transformers",
        (
            1,
            2,
        ): "Sparse MoE as a New Treatment: Addressing Forgetting, Fitting, Learning Issues in Multi-Modal Multi-Task Learning",
        (1, 3): "Theoretical and Empirical Advances in Forest Pruning",
        (
            1,
            4,
        ): "On How Iterative Magnitude Pruning Discovers Local Receptive Fields in Fully Connected Neural Networks",
        (
            1,
            5,
        ): "Dimension Mixer: Group Mixing of Input Dimensions for Efficient Function Approximation",
        (1, 6): "HSR-Enhanced Sparse Attention Acceleration",
        (
            1,
            7,
        ): "Taming Sensitive Weights : Noise Perturbation Fine-tuning for Robust LLM Quantization",
        (
            1,
            8,
        ): "Greedy Output Approximation: Towards Efficient Structured Pruning for LLMs Without Retraining",
        (
            1,
            9,
        ): "Q-GaLore: Quantized GaLore with INT4 Projection and Layer-Adaptive Low-Rank Gradients",
        (
            1,
            10,
        ): "Adaptive Batch Size Schedules for Distributed Training of Language Models with Data and Model Parallelism",
        (
            1,
            11,
        ): "A unified Framework for Sparse plus Low-Rank Matrix Decomposition for LLMs",
        (1, 12): "Unlock the Theory behind Scaling 1-bit Neural Networks",
        (
            1,
            13,
        ): "Adversarially Robust Spiking Neural Networks with Sparse Connectivity",
        (
            1,
            14,
        ): "SGD with Weight Decay Secretly Minimizes the Ranks of Your Neural Networks",
        (
            1,
            15,
        ): "Sparse Training from Random Initialization: Aligning Lottery Ticket Masks using Weight Symmetry",
        (
            1,
            16,
        ): "Mixture-of-Transformers: A Sparse and Scalable Architecture for Multi-Modal Foundation Models",
        (
            1,
            17,
        ): "Mixture-of-Mamba: Enhancing Multi-Modal State-Space Models with Modality-Aware Sparsity",
        (
            1,
            18,
        ): "Training Bayesian Neural Networks with Sparse Subspace Variational Inference",
        (
            1,
            19,
        ): "WAGLE: Strategic Weight Attribution for Effective and Modular Unlearning in Large Language Models",
        (1, 20): "Masks, Signs, And Learning Rate Rewinding",
        (1, 21): "Streaming Kernel PCA Algorithm With Small Space",
        (
            1,
            22,
        ): "Collaborative and Efficient Personalization with Mixtures of Adaptors",
        (
            1,
            23,
        ): "Pruning neural network models for gene regulatory dynamics using data and domain knowledge",
        (
            1,
            24,
        ): "Towards Vector Optimization on Low-Dimensional Vector Symbolic Architecture",
        (
            1,
            25,
        ): "Mix-LN: Unleashing the Power of Deeper Layers by Combining Pre-LN and Post-LN",
        (
            1,
            26,
        ): "Approximate Nullspace Augmented Finetuning for Robust Vision Transformers",
        (
            1,
            27,
        ): "Learning of Patch-Based Smooth-Plus-Sparse Models for Image Reconstruction",
        (
            1,
            28,
        ): "Prior Mismatch and Adaptation in PnP-ADMM with a Nonconvex Convergence Analysis",
        (
            1,
            29,
        ): "Stable Minima Cannot Overfit in Univariate ReLU Networks: Generalization by Large Step Sizes",
        (
            1,
            30,
        ): "Certified Robustness against Sparse Adversarial Perturbations via Data Localization",
        (
            1,
            31,
        ): "The Computational Limits of State-Space Models and Mamba via the Lens of Circuit Complexity",
        (
            1,
            32,
        ): "Fast John Ellipsoid Computation with Differential Privacy Optimization",
        (
            1,
            33,
        ): "Understanding How Nonlinear Networks Create Linearly Separable Features for Low-Dimensional Data",
        (1, 34): "On Generalization Bounds for Neural Networks with Low Rank Layers",
        (1, 35): "Fast and Efficient Matching Algorithm with Deadline Instances",
        # Group 2: Learning Dynamics, Optimization, and Theoretical Foundations (Session 2)
        (
            2,
            1,
        ): "AdaProx: A Novel Method for Bilevel Optimization under Pessimistic Framework",
        (
            2,
            2,
        ): "Revisiting the Initial Steps in Adaptive Gradient Descent Optimization",
        (2, 3): "Exact and Rich Feature Learning Dynamics of Two-Layer Linear Networks",
        (
            2,
            4,
        ): "Hamiltonian Mechanics of Feature Learning: Bottleneck Structure in Leaky ResNets",
        (2, 5): "Quantum EigenGame for excited state calculation",
        (
            2,
            6,
        ): "Asymptotic Behavior of the Coordinate Ascent Variational Inference in Singular Models",
        (
            2,
            7,
        ): "Grouped Sequential Optimization Strategy - the Application of Hyperparameter Importance Assessment in Deep Learning",
        (
            2,
            8,
        ): "Provable Model-Parallel Distributed Principal Component Analysis with Parallel Deflation",
        (
            2,
            9,
        ): "AgentHPO: Large Language Model Agent for  Hyper-Parameter Optimization",
        (
            2,
            10,
        ): "FedOSAA: Improving Federated Learning with One-Step Anderson Acceleration",
        (2, 11): "Unlocking Global Optimality in Bilevel Optimization: A Pilot Study",
        (2, 12): "On the Crucial Role of Initialization for Matrix Factorization",
        (
            2,
            13,
        ): "Geometry of Neural Reinforcement Learning in Continuous State and Action Spaces",
        (2, 14): "Learning Gaussian Multi-Index Models with Gradient Flow: Time Complexity and Directional Convergence",
        (
            2,
            15,
        ): "Learning Dynamics of Deep Matrix Factorization Beyond the Edge of Stability",
        (
            2,
            16,
        ): "Non-convex matrix sensing: Breaking the quadratic rank barrier in the sample complexity",
        (2, 17): "Relaxed Contrastive Learning for Federated Learning",
        (
            2,
            18,
        ): "Do Global and Local Perform Cooperatively or Adversarially in Heterogeneous Federated Learning?",
        (
            2,
            19,
        ): "FedPeWS: Personalized Warmup via Subnetworks for Enhanced Heterogeneous Federated Learning",
        (2, 20): "Characterizing ResNet’s Universal Approximation Capability",
        (
            2,
            21,
        ): "A Validation Approach to Over-parameterized Matrix and Image Recovery",
        (
            2,
            22,
        ): "WHOMP: Optimizing Randomized Controlled Trials via Wasserstein Homogeneity",
        (2, 23): "What's in a Prior? Learned Proximal Networks for Inverse Problems",
        (2, 24): "Provable Probabilistic Imaging using Score-based Generative Priors",
        (2, 25): "Principle Component Trees and their Persistent Homology",
        (2, 26): "FlowDAS: A Flow-Based Framework for Data Assimilation",
        (2, 27): "Large-Scale Multiway Clustering with Seeded Clustering",
        (2, 28): "Are all layers created equal: A neural collapse perspective",
        (
            2,
            29,
        ): "Geometry of Concepts in Next-token Prediction: Neural-Collapse Meets Semantics",
        (2, 30): "Deep Neural Regression Collapse",
        (2, 31): "Geometric Algebra Planes: Convex Implicit Neural Volumes",
        (
            2,
            32,
        ): "A Robust Kernel Statistical Test of Invariance: Detecting Subtle Asymmetries",
        (2, 33): "Learning with Exact Invariances in Polynomial Time",
        (2, 34): "Primal-Dual Spectral Representation for Off-policy Evaluation",
        (2, 35): "Dependence Induced Representations",
        (2, 36): "MoXCo: How I learned to stop exploring and love my local minima?",
        # Group 3: Representation Learning, Interpretability, and Applications (Session 3)
        (
            3,
            1,
        ): "Improving Neuron-level Interpretability with White-box Language Models",
        (3, 2): "Vanishing Feature: Diagnosing Model Merging and Beyond",
        (
            3,
            3,
        ): "A Case Study of Low Ranked Self-Expressive Structures in Neural Network Representations",
        (
            3,
            4,
        ): "You Only Debias Once: Towards Flexible Accuracy-Fairness Trade-offs at Inference Time",
        (
            3,
            5,
        ): "RecCrysFormer: Refined Protein Structural Prediction from 3D Patterson Maps via Recycling Training Runs",
        (
            3,
            6,
        ): "Dual Reasoning: A GNN-LLM Collaborative Framework for Knowledge Graph Question Answering",
        (3, 7): "Meta ControlNet: Enhancing Task Adaptation via Meta Learning",
        (
            3,
            8,
        ): "Bridging Domain Adaptation and Graph Neural Networks: A Tensor-Based Framework for Effective Label Propagation",
        (3, 9): "Concept Bottleneck Model with Zero Performance Loss",
        (
            3,
            10,
        ): "Enhancing Video Representation Learning with Temporal Differentiation",
        (
            3,
            11,
        ): "Explaining and Mitigating the Modality Gap in Contrastive Multimodal Learning",
        (
            3,
            12,
        ): "Learning Effective Dynamics across Spatio-Temporal Scales of Complex Flows",
        (3, 13): "White-box Error Correction Code Transformer",
        (
            3,
            14,
        ): "Curse of Attention: A Kernel-Based Perspective for Why Transformers Fail to Generalize on Time Series Forecasting and Beyond",
        (
            3,
            15,
        ): "Active-Dormant Attention Heads: Mechanistically Demystifying Extreme-Token Phenomena in LLMs",
        (
            3,
            16,
        ): "Diffusion models learn low-dimensional distributions via subspace clustering",
        (3, 17): "Visual Prompting Reimagined: The Power of Activation Prompts",
        (
            3,
            18,
        ): "Understanding Diffusion-based Representation Learning via Low-Dimensional Modeling",
        (3, 19): "Simplifying DINO by Coding Rate Regularization",
        (
            3,
            20,
        ): "Closure Discovery for Coarse-Grained Partial Differential Equations Using Grid-based Reinforcement Learning",
        (
            3,
            21,
        ): "Heterogeneous Decision Making in Mixed Traffic: Uncertainty-aware Planning and Bounded Rationality",
        (
            3,
            22,
        ): "CompeteAI: Understanding the Competition Dynamics of Large Language Model-based Agents",
        (
            3,
            23,
        ): "DyVal: Dynamic Evaluation of Large Language Models for Reasoning Tasks",
        (
            3,
            24,
        ): "Knowledge-aware Parsimony Learning: A Perspective from Relational Graphs",
        (3, 25): "Understanding and Mitigating Bottlenecks of State Space Models through the Lens of Recency and Over-smoothing",
        (
            3,
            26,
        ): "Rethinking Addressing in Language Models via Contextualized Equivariant Positional Encoding",
        (
            3,
            27,
        ): "Implicit Geometry of Next-token Prediction: From Language Sparsity patterns to Model Representations",
        (3, 28): "Dynamic Rescaling for Training GNNs",
        (3, 29): "Image Reconstruction Via Autoencoding Sequential Deep Image Prior",
        (
            3,
            30,
        ): "SITCOM: Step-wise Triple-Consistent Diffusion Sampling for Inverse Problems",
        (
            3,
            31,
        ): "SFT Memorizes, RL Generalizes: A Comparative Study of Foundation Model Post-training",
        (3, 32): "Attention-Only Transformers via Unrolled Subspace Denoising",
        (
            3,
            33,
        ): "Out-of-distribution generalization via composition: a lens through induction heads in Transformers",
        (3, 34): "Sufficient and Necessary Explanations (and What Lies in Between)",
        (
            3,
            35,
        ): "Generative Learning for Solving Non-Convex Problem with Multi-Valued Input-Solution Mapping",
        (
            3,
            36,
        ): "Shallow Diffuse: Robust and Invisible Watermarking through Low-Dimensional Subspaces in Diffusion Models",
    }

    return session_paper_mapping
