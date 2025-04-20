---
layout: page
title: List of Tutorials
description: Information about first-day tutorials at CPAL 2025
parent: Tutorials
nav_order: 4
---

{% include splash.html %}

# General Information

{: .highlight}
{: .fs-5}
Attendees must [register]({{site.baseurl}}/registration) for the tutorial
package to attend the tutorials.

The first day of CPAL 2025 features six tutorial presentations, arranged
into two parallel tracks across three sessions throughout the day.
Each tutorial consists of 2.5 hours of lectures from leading experts in the
intersection between low-dimensional modeling and deep learning, with topics
ranging from theory to practice and presentations in an accessible format.
See the [schedule]({{site.baseurl}}/program_schedule) for the precise times and locations of each tutorial.

The content of the six tutorials is summarized below. 


# List of Tutorials


## T1: Deep Representation Learning: from Knowledge to Intelligence

#### Presenters: Sam Buchanan (TTIC), Yi Ma (HKU, UC Berkeley), Druv Pai (UC Berkeley), Peng Wang (University of Michigan)

#### Abstract:
Modern generative AI systems, powered by deep learning, are currently revolutionizing science and engineering. At the same time, a fundamental lack of transparency in the way these systems learn from data and make decisions presents safety concerns of ever-increasing severity. This tutorial aims to provide a rigorous and systematic overview of the mathematical and computational principles of deep learning. The tutorial will commence with a broad overview of the history and current state of the field of AI, and then focus in on an important common problem: how to effectively and efficiently learn a low-dimensional distribution of data in a high-dimensional space and then transform the distribution to a compact and structured representation, referred to as a memory. The tutorial will show, starting from classical linear models and building up to general data distributions, how a general framework for learning structured memories arises from a universal computational principle: compression. Particularly, popular approaches for representation learning (such as denoising score-matching) as well as modern network architectures (such as residual networks and transformers) can be understood and improved as (unrolled) optimization algorithms to achieve better compression and representation. To chart a path beyond the current practices of representation learning towards developing truly autonomous and intelligent systems, the tutorial will conclude with a discussion of effective autoencoding architectures centered around the powerful framework of closed-loop transcription, enabling networks to self-improve via closed-loop feedback. Concepts will be illustrated throughout with experiments on supervised and unsupervised learning of diverse data modalities.

## T2: Foundations on Interpretable AI

#### Presenters: Rene Vidal (University of Pennsylvania), Jeremias Sulam (Johns Hopkins University), Aditya Chattopadhyay (Amazon)

#### Abstract:
In recent years, interpretability has emerged as a significant barrier to the widespread adoption of deep learning techniques, particularly in domains where AI decisions can have consequential impacts on human lives, such as healthcare and finance. Recent attempts at interpreting the decisions made by a deep network can be broadly classified in two categories, (i) methods that seek to explain existing models (post-hoc explainability), and (ii) methods that seek to build models that are explainable by design. This tutorial aims to provide a comprehensive overview of both approaches along with a discussion on their limitations.

## T3: Methods, Analysis, and Insights from Multimodal LLM Pre-training and Post-training

#### Presenters: Zhe Gan (Apple), Haotian Zhang (Apple)

#### Abstract:
Multimodal Large Language Models (LLMs) have become an increasing hot research topic. In this tutorial, we will present how to build performant multimodal LLMs, along several fronts: (1) multimodal LLM pre-training, with focus on crucial design lessons for model architectures and pre-training data choices; (2) multimodal LLM post-training, with focus on text-rich image understanding, visual referring and grounding, and multi-image reasoning; (3) visual encoder pre-training, with focus on training objective design and pre-training data curation; and (4) generalist UI agents, with focus on how to adapt multimodal LLMs into generalist UI agents capable of control digital devices to complete human tasks.

## T4: Harnessing Low Dimensionality in Diffusion Models: From Theory to Practice

#### Presenters: Yuxin Chen (University of Pennsylvania, Wharton), Qing Qu (University of Michigan), Liyue Shen (University of Michigan)

#### Abstract:
Diffusion models have recently gained attention as a powerful class of deep generative models, achieving state-of-the-art results in data generation tasks. In a nutshell, they are designed to learn an unknown data distribution starting from Gaussian noise, mimicking the process of non-equilibrium thermodynamic diffusion. Despite their outstanding empirical successes, the mathematical and algorithmic foundations of diffusion models remain far from mature. For instance: (i) Generalization: it remains unclear how diffusion models, trained on finite samples, can generate new and meaningful data that differ from the training set; (ii) Efficiency: due to the enormous model capacity and the requirement of many sampling steps, they often suffer from slow training and sampling speeds; (iii) Controllability: it remains computationally challenging to guide and control diffusion models for solving inverse problems across many scientific imaging applications, due to the necessity of data consistency and the limitations imposed by limited and noisy measurements. This tutorial will introduce a mathematical framework for understanding the generalization and improving the efficiency of diffusion models, through exploring the low-dimensional structures in both the data and model. We show how to overcome fundamental barriers to improve the generalization, efficiency, and controllability in developing diffusion models, by exploring how these models adaptively learn underlying data distributions, how to achieve faster convergence at the sampling stage, and unveiling the intrinsic properties of the learned denoiser. Leveraging the theoretical studies, we will show how to effectively employ diffusion models for solving inverse problems in scientific imaging applications.

## T5: A Function-Space Tour of Data Science

This tutorial has a dedicated website with slides and more:
[https://function-space-tour.github.io/cpal/](https://function-space-tour.github.io/cpal/)

#### Presenters: Rahul Parhi (UC San Diego), Greg Ongie (Marquette University)

#### Abstract:
Parametric methods aim to explain data with a finite number of learnable parameters. These models are typically applied in settings where the number of data is greater than the number of parameters. Nonparametric methods, on the other hand, model data using infinite-dimensional function spaces and/or allow the number of parameters to grow beyond the number of data (a.k.a. the overparameterized regime). Many classical methods in data science fit into this latter framework, including kernel methods and wavelet methods. Furthermore, modern methods based on overparameterized neural networks also fit into this framework. The common theme being that these methods aim to minimize a quantity in function space. This tutorial will provide a tour of nonparametric methods in data science through the lens of function spaces starting with classical methods such as kernel methods (reproducing kernel Hilbert spaces) and wavelet methods (bounded variation spaces, Besov spaces) and ending with modern, high-dimensional methods such as overparameterized neural networks (variation spaces, Barron spaces). Remarkably, all of these methods can be viewed through the lens of abstract representer theorems (beyond Hilbert spaces). A particular emphasis will be made on the difference between $\ell_2$ regularization (kernel methods) and sparsity-promoting $\ell_1$-regularization (wavelet methods, neural networks) through the concept of adaptivity. For each method/function space, topics such as generalization bounds, metric entropy, and minimax rates will be covered.

## T6: Sparsity and Mixture-of-Experts in the Era of LLMs: A New Odyssey

#### Presenters: Shiwei Liu (Oxford), Tianlong Chen (University of North Carolina, Chapel Hill), Yu Cheng (Chinese University of Hong Kong)


#### Abstract:
Recently, Large Language Models (LLMs) have showcased remarkable generalization capabilities across a plethora of tasks, yielding notable successes. The scale of these models stands out as a pivotal determinant in enhancing LLM performance. However, the escalation in model size significantly amplifies the costs associated with both pre-training and fine-tuning, while simultaneously constraining inference speed. Consequently, there has been a surge in exploration aimed at devising novel techniques for model scaling. Among these, the sparse Mixture-of-Experts (MoE) has garnered considerable attention due to its ability to expedite pre-training and enhance inference speed, especially when compared to dense models with equivalent parameter counts. This tutorial endeavors to offer a comprehensive overview of MoE within the context of LLMs. The discussion commences by revisiting extant research on MoE, elucidating critical challenges encountered within this domain. Subsequent exploration delves into the intricate relationship between MoE and LLMs, encompassing sparse scaling of pre-training models and the conversion of existing dense models into sparse MoE counterparts. Moreover, the tutorial elucidates the broader advantages conferred by MoE beyond mere efficiency. Overall, this tutorial delineates the evolutionary trajectory of MoE within the landscape of LLMs, underscoring its pivotal role in the era of LLMs.

