#!/usr/bin/env python
# -*- coding: utf-8 -*-

# We do data input in this file, essentially.

# imports
import argparse
import csv
import re
from pathlib import Path

import yaml
from event import Event
from program import Calendar
from roles import Organizer, RisingStar, Speaker, Tutorial

# this is the root directory of the jekyll site
# exports will go there
root = Path(__file__).parent.parent.parent

# variables for location strings
day_one_str = "TBD"
day_two_str = "TBD"

# Speaker photos should be close to 1:1 aspect (height : width)

# Organizer photos should be close to 1:1 aspect

# Rising Stars photos should be close to 1:1 aspect


def make_risingstars():
    risingstars = []

    risingstars.append(
        RisingStar(
            name="Bhavya Vasudeva",
            role="Researcher",
            website="",
            affiliation="University of Southern California",
            photo="image1.png",
            session=1,
            order=1,
            talk="How Muon's Spectral Design Benefits Generalization: A Study on Imbalanced Data",
            abstract="The growing adoption of spectrum-aware matrix-valued optimizers such as Muon and Shampoo in deep learning motivates a systematic study of their generalization properties and, in particular, when they might outperform competitive algorithms. We approach this question by introducing appropriate simplifying abstractions as follows: First, we use imbalanced data as a testbed. Second, we study the canonical form of such optimizers, which is Spectral Gradient Descent (SpecGD) -- each update step is UV^T where USV^T is the truncated SVD of the gradient. Third, within this framework we identify a canonical setting for which we precisely quantify when SpecGD outperforms vanilla Euclidean GD. For a Gaussian mixture data model and both linear and bilinear models, we show that unlike GD, which prioritizes learning dominant principal components of the data first, SpecGD learns all principal components of the data at equal rates. We demonstrate how this translates to a growing gap in class balanced loss favoring SpecGD early in training and further show that the gap remains consistent even when the GD counterpart uses adaptive step-sizes via normalization. By extending the analysis to deep linear models, we show that depth amplifies these effects. We empirically verify our theoretical findings on a variety of imbalanced datasets. Our experiments compare practical variants of spectral methods, like Muon and Shampoo, against their Euclidean counterparts and Adam. The results validate our findings that these spectral optimizers achieve superior generalization by promoting a more balanced learning of the data's underlying components.",
        )
    )

    risingstars.append(
        RisingStar(
            name="Can Yaras",
            role="Researcher",
            website="",
            affiliation="University of Michigan",
            photo="image2.png",
            session=1,
            order=2,
            talk="Compressing Activations via Structured Matrices in Transformers",
            abstract="Matrix multiplications between weights and activations dominate the computational cost of Transformers. Prior work primarily reduces this cost by compressing weights, whereas activation compression remains underexplored due to its online, input-dependent nature. We introduce a general framework for approximating activation matrices with structured matrices that admit fast matrix-vector multiplication, using efficient on-the-fly optimization. We demonstrate the effectiveness of this approach in the instance of attention activations with MonarchAttention, which has recently been adapted to speed up state-of-the-art video generation.",
        )
    )

    risingstars.append(
        RisingStar(
            name="Harry Dong",
            role="Researcher",
            website="",
            affiliation="Carnegie Mellon University",
            photo="image3.png",
            session=1,
            order=3,
            talk="Squeezing the Most Out of LLMs: The Interplay Between Efficiency and Performance",
            abstract="Large language models (LLMs) continuously demonstrate surprising capabilities, which drive the spread of their potential to various domains and applications. Yet, inefficiencies in various components of the architecture and inference pipeline limit broader deployment of LLMs. The demanding nature of LLM inference can harm latency, throughput, and memory. Furthermore, underutilization of information can also artificially limit performance. In this talk, we take a close look at the model architecture, data, features, and hardware behavior to reveal emergent patterns and redundancy that provide clues to optimize inference efficiency and performance. Together, our methods push towards the compute-performance Pareto frontier for LLM inference.",
        )
    )

    risingstars.append(
        RisingStar(
            name="Lu Yin",
            role="Researcher",
            website="",
            affiliation="University of Surrey",
            photo="image4.png",
            session=1,
            order=4,
            talk="Sustainable Compute, Smart Reasoning, and Specialized Domain Foundation Models",
            abstract="TBD",
        )
    )

    risingstars.append(
        RisingStar(
            name="Zhenyu Zhang",
            role="Researcher",
            website="",
            affiliation="University of Texas at Austin",
            photo="image5.png",
            session=1,
            order=5,
            talk="Democratizing LLM Training via Low-Rank Methods",
            abstract="As Large Language Models (LLMs) continue to scale in size and capability, the cost and complexity of training -- particularly memory consumption from optimizer states -- have become critical bottlenecks. In this talk, we explore the evolution of low-rank optimization techniques for LLMs, tracing the progression from GaLore to APOLLO. GaLore introduces a memory-efficient training paradigm by applying low-rank projections to gradients and optimizer states, enabling the training of models with up to 7 billion parameters on consumer-grade GPUs such as the NVIDIA RTX 4090. Building on this foundation, APOLLO demonstrates the surprising effectiveness of rank-1 optimizer states with purely random projections, achieving SGD-level memory overhead while maintaining performance comparable to AdamW. This method brings substantial system-level improvements, including a 3x increase in throughput on 8xA100-80G GPUs and enhanced model scalability.",
        )
    )

    risingstars.append(
        RisingStar(
            name="Ang Li",
            role="Researcher",
            website="",
            affiliation="University of Maryland",
            photo="image6.png",
            session=2,
            order=1,
            talk="Parsimony and Efficiency in Foundation Models: A Holistic Framework for Structural Analysis and Resource-Aware Serving",
            abstract='The increasing overparameterization of foundation models necessitates a shift toward parsimonious architectures and resource-aware serving to enable universal deployment. This research establishes a holistic framework for efficiency by identifying structural redundancies and mitigating operational bottlenecks across the AI stack. We introduce a similarity-based metric to quantify module importance, revealing that "Attention Drop" -- the strategic pruning of redundant attention layers -- can streamline Transformers while preserving core functional performance. For Mixture of Experts (MoE) architectures, we propose a unified compression strategy integrating "Expert Trimming" of structured modules with "Expert Slimming" of individual experts. To enhance sparse inference efficiency, we address the "Straggler Effect" caused by imbalanced token routing through Capacity-Aware Inference, which regulates expert workloads via token dropping and rerouting. Finally, we demonstrate system-level parsimony through EdgeLoRA, a multi-tenant serving system that utilizes adaptive adapter selection and heterogeneous memory management to maximize efficiency on edge hardware. Collectively, these contributions provide a scientific foundation for the next generation of sustainable and hardware-aware intelligent systems.',
        )
    )

    risingstars.append(
        RisingStar(
            name="Bowen Song",
            role="Researcher",
            website="",
            affiliation="University of Michigan",
            photo="image7.png",
            session=2,
            order=2,
            talk="Better spatial reasoning and analysis through depth-informed 3D geometry tokens",
            abstract="TBD",
        )
    )

    risingstars.append(
        RisingStar(
            name="Chenyu You",
            role="Researcher",
            website="",
            affiliation="Stony Brook University",
            photo="image8.png",
            session=2,
            order=3,
            talk="Towards Robust, Efficient, and Generalized Medical AI",
            abstract="Artificial intelligence has advanced biomedical image analysis dramatically, yet reliable clinical deployment remains limited. A key reason is that current models do not fully leverage the parsimonious, low-dimensional structure underlying anatomy, physiology, and disease. Scarce labeled data hinder representation learning, distribution shifts break brittle invariances, and the absence of theoretical guarantees reduces trust in high-stakes decisions. My research addresses these challenges by developing robust, efficient, and generalized medical AI methods that extract compact structural representations, unify data-driven learning with mathematical principles, and build medical foundation models that transfer across populations, modalities, and institutions. The central aim of my research is to uncover and exploit intrinsic low-dimensional structure to achieve sample efficiency, computational efficiency, and reliable generalization in real clinical environments.",
        )
    )

    risingstars.append(
        RisingStar(
            name="Lingjiao Chen",
            role="Researcher",
            website="",
            affiliation="Stanford University",
            photo="image9.png",
            session=2,
            order=4,
            talk="Economical AI Marketplaces: From Model Cascading to Compound AI Systems",
            abstract='The paradigm of machine learning has shifted from training individual models to utilizing "AI as a Service" via APIs like GPT-5 and Gemini 3 Pro. While this democratizes access, it introduces significant challenges in cost and performance optimization. With thousands of available models and infinite combinations, how do we efficiently orchestrate these services? In this talk, I will present two frameworks that address this challenge at different levels of complexity. First, I will introduce FrugalGPT, a cascading framework for single-turn queries. By learning to route easy queries to cheaper models and only escalating hard queries to expensive ones, FrugalGPT matches the performance of top-tier models with up to 98% cost reduction. Second, I will discuss LLMSelector, which extends this optimization to compound AI systems. I will show that in these complex workflows, naively using the "best" model for every step is inefficient. LLMSelector uses a data-efficient optimization algorithm to assign the optimal model to each module, achieving substantial accuracy gains over baseline approaches.',
        )
    )

    risingstars.append(
        RisingStar(
            name="Tianjiao Ding",
            role="Researcher",
            website="",
            affiliation="University of Pennsylvania",
            photo="image10.png",
            session=2,
            order=5,
            talk="Parsimonious Concept Engineering",
            abstract="Large Language Models (LLMs) are being used for a wide variety of tasks. While they are capable of generating human-like responses, they can also produce undesirable output including potentially harmful information, racist or sexist language, and hallucinations. Alignment methods are designed to reduce such undesirable output, via techniques such as fine-tuning, prompt engineering, and representation engineering. However, existing methods face several challenges: some require costly fine-tuning for every alignment task; some do not adequately remove undesirable concepts, failing alignment; some remove benign concepts, lowering the linguistic capabilities of LLMs. To address these issues, we propose Parsimonious Concept Engineering (PaCE), a novel activation engineering framework for alignment. First, to sufficiently model the concepts, we construct a large-scale concept dictionary in the activation space, in which each atom corresponds to a semantic concept. Given any alignment task, we instruct a concept partitioner to efficiently annotate the concepts as benign or undesirable. Then, at inference time, we decompose the LLM activations along the concept dictionary via sparse coding, to accurately represent the activations as linear combinations of benign and undesirable components. By removing the latter ones from the activations, we reorient the behavior of the LLM towards the alignment goal. We conduct experiments on tasks such as response detoxification, faithfulness enhancement, and sentiment revising, and show that PaCE achieves state-of-the-art alignment performance while maintaining linguistic capabilities.",
        )
    )

    risingstars.append(
        RisingStar(
            name="Avrajit Ghosh",
            role="Researcher",
            website="",
            affiliation="University of California, Berkeley",
            photo="image11.png",
            session=3,
            order=1,
            talk="A fundamental statistical limitation of Gradient Descent in learning sparse targets from hard labels",
            abstract='The success of gradient descent in deep learning has often been attributed to a property called implicit regularization which enables finding "generalizing" solutions. Contrary to past works, we point out a statistical limitation of learning with gradient descent in the simplest but the most commonly occurring case. We study well-specified sparse logistic regression in the over-constrained regime, where the number of input-label samples (n) exceeds the dimension (d), and the learner has access only to hard discrete labels. In this setting, when gradient descent learns using a standard dot-product model between weights and inputs, it is provably suboptimal and incurs an excess risk that scales with the dimension (d). This limitation holds more broadly for a class of rotation-invariant algorithms, which includes deep neural networks with a fully connected first layer. In contrast, simple non-rotation-invariant parameterizations achieve substantially better statistical performance using early stopping, with only logarithmic dependence on the dimension. Our results highlight a limitation of the commonly celebrated implicit regularization of gradient descent and its failure to efficiently learn sparse targets from hard labels.',
        )
    )

    risingstars.append(
        RisingStar(
            name="Lingjing Kong",
            role="Researcher",
            website="",
            affiliation="Carnegie Mellon University",
            photo="image12.png",
            session=3,
            order=2,
            talk="Parsimony through Causality: Building Trustworthy and Interpretable AI",
            abstract="TBD",
        )
    )

    risingstars.append(
        RisingStar(
            name="Yuko Kuroki",
            role="Researcher",
            website="",
            affiliation="Intesa Sanpaolo AI Research",
            photo="image13.png",
            session=3,
            order=3,
            talk="Sequential Learning under Uncertainty: Structure, Adaptivity, and Efficiency",
            abstract="How can we make reliable decisions when data is limited, feedback is partial, and environments are uncertain? Many real-world decision-making problems involve complex and structured action spaces, yet only limited and noisy feedback is available. In this talk, I present a unified perspective on sequential learning under uncertainty through the lens of multi-armed bandits, achieving both statistical and computational efficiency by exploiting latent structure. First, we show how latent combinatorial structure can dramatically reduce the cost of exploration. We develop query-efficient methods for recovering clustered structures from noisy feedback. Second, we investigate adaptive algorithms for linear contextual bandits that achieve optimal performance in stochastic environments while remaining robust in adversarial settings -- without prior knowledge of the regime. Finally, we connect these foundations to societal systems. We introduce a low-rank matrix bandit framework for optimizing opinion dynamics to mitigate polarization and disagreement in social networks. Looking ahead, my goal is to build a principled theory of adaptive exploration in complex systems and to translate these foundations into tools for data-driven discovery.",
        )
    )

    risingstars.append(
        RisingStar(
            name="Yuqing Wang",
            role="Researcher",
            website="",
            affiliation="Johns Hopkins University",
            photo="image14.png",
            session=3,
            order=4,
            talk="Data Uniformity Improves Training Efficiency and More, with a Convergence Framework Beyond the NTK Regime",
            abstract="Data selection is crucial for data-driven decision-making, including foundation models, but beyond data quality and diversity, it is unclear whether other general quantitative principles can reliably improve complex tasks. In this talk, I will demonstrate that selecting more uniformly distributed data can improve training efficiency while enhancing performance. Specifically, we establish that more uniform (less biased) distribution leads to a larger minimum pairwise distance between data points, denoted by h_min, and prove that a smaller h_min can slow down the training dynamics of gradient descent (GD). Moreover, we theoretically show that the approximation error of neural networks decreases as h_min increases. Our analysis introduces a convergence framework for GD beyond the Neural Tangent Kernel (NTK) regime, applicable to a broad class of architectures, including transformers, without requiring Lipschitz smoothness. This framework further provides theoretical justification for the use of residual connection and function composition in deep neural architectures. In the end, I will show some comprehensive experiments, including supervised fine-tuning across various settings, different optimization strategies, model sizes, and training datasets. The results consistently demonstrate that selecting data by maximizing the minimum pairwise distance significantly accelerates training and achieves comparable or better performance across diverse datasets.",
        )
    )

    risingstars.append(
        RisingStar(
            name="Zhen Tan",
            role="Researcher",
            website="",
            affiliation="Arizona State University",
            photo="image15.png",
            session=3,
            order=5,
            talk="Fathoming the Unfathomable Foundation Models: From Algorithms to Scientific Discovery",
            abstract="As foundation models become central to information systems, cybersecurity, and scientific decision-making, their opacity raises critical challenges for trust, accountability, and governance. While much prior work has focused on post-hoc explainability, my research shows that such approaches are intrinsically limited and can even obscure model failures. In this talk, I present a shift from explaining opaque systems to designing trustworthy and interpretable AI by construction. I will introduce diagnostic frameworks that reveal failures in explanation faithfulness and security, such as explanatory inversion and vulnerability to retrieval and communication attacks. I will then demonstrate how concept-based, human-centered model architectures enable glass-box reasoning, actionable interventions, and self-reflection for large language models (LLMs). I will conclude by demonstrating how these ideas translate into real-world impact across AI-driven cybersecurity, conversational agents, agricultural robotics, and neuroscience, and by outlining a vision for information-centric AI systems that are transparent, reliable, and aligned with human values.",
        )
    )

    return risingstars


def make_speakers():
    speakers = []

    speakers.append(
        Speaker(
            name="Yingyu Liang",
            role="Keynote Speaker",
            website="https://yingyuliang.github.io/",
            affiliation="University of Hong Kong, University of Wisconsin-Madison",
            photo="liang.png",
            talk="TBA",
            abstract="TBA",
            bio="TBA",
            day=2,  # Tuesday March 24th
            start="9:00 AM",
            end="10:00 AM",
            location=day_two_str,
        )
    )

    speakers.append(
        Speaker(
            name="Taiji Suzuki",
            role="Keynote Speaker",
            website="https://ibis.t.u-tokyo.ac.jp/suzuki/",
            affiliation="University of Tokyo / RIKEN AIP",
            photo="suzuki.png",
            talk="TBA",
            abstract="TBA",
            bio="TBA",
            day=2,  # Tuesday March 24th
            start="10:30 AM",
            end="11:30 AM",
            location=day_two_str,
        )
    )

    speakers.append(
        Speaker(
            name="Matthias Bethge",
            role="Keynote Speaker",
            website="https://bethgelab.org/",
            affiliation="University of Tubingen",
            photo="bethge.png",
            talk="TBA",
            abstract="TBA",
            bio="TBA",
            day=3,  # Wednesday March 25th
            start="9:00 AM",
            end="10:00 AM",
            location=day_two_str,
        )
    )

    speakers.append(
        Speaker(
            name="Fanny Yang",
            role="Keynote Speaker",
            website="https://sml.inf.ethz.ch/group/fannyy/",
            affiliation="ETH Zurich",
            photo="yang.png",
            talk="TBA",
            abstract="TBA",
            bio="TBA",
            day=3,  # Wednesday March 25th
            start="10:30 AM",
            end="11:30 AM",
            location=day_two_str,
        )
    )

    speakers.append(
        Speaker(
            name="Jared Tanner",
            role="Keynote Speaker",
            website="https://people.maths.ox.ac.uk/tanner/",
            affiliation="University of Oxford",
            photo="tanner.png",
            talk="TBA",
            abstract="TBA",
            bio="TBA",
            day=2,  # Tuesday March 24th
            start="2:30 PM",
            end="3:30 PM",
            location=day_two_str,
        )
    )

    speakers.append(
        Speaker(
            name="Francis Bach",
            role="Keynote Speaker",
            website="https://www.di.ens.fr/~fbach/",
            affiliation="INRIA - Ecole Normale Superieure",
            photo="bach.png",
            talk="TBA",
            abstract="TBA",
            bio="TBA",
            day=3,  # Wednesday March 25th
            start="2:30 PM",
            end="3:30 PM",
            location=day_two_str,
        )
    )

    speakers.append(
        Speaker(
            name="Niao He",
            role="Keynote Speaker",
            website="https://odi.inf.ethz.ch/niaohe.html",
            affiliation="ETH Zurich",
            photo="he.png",
            talk="TBA",
            abstract="TBA",
            bio="TBA",
            day=4,  # Thursday March 26th
            start="9:00 AM",
            end="10:00 AM",
            location=day_two_str,
        )
    )

    speakers.append(
        Speaker(
            name="Andreas Krause",
            role="Keynote Speaker",
            website="https://las.inf.ethz.ch/krausea",
            affiliation="ETH Zurich",
            photo="krause.png",
            talk="TBA",
            abstract="TBA",
            bio="TBA",
            day=4,  # Thursday March 26th
            start="10:30 AM",
            end="11:30 AM",
            location=day_two_str,
        )
    )

    speakers.append(
        Speaker(
            name="Leena Chennuru Vankadara",
            role="Keynote Speaker",
            website="https://leenacvankadara.com/",
            affiliation="University College London",
            photo="vankadara.png",
            talk="TBA",
            abstract="TBA",
            bio="TBA",
            day=4,  # Thursday March 26th
            start="2:30 PM",
            end="3:30 PM",
            location=day_two_str,
        )
    )

    speakers.append(
        Speaker(
            name="Bernhard Scholkopf",
            role="Keynote Speaker",
            website="https://is.mpg.de/~bs",
            affiliation="Max Planck Institute for Intelligent Systems / ELLIS Institute Tubingen",
            photo="scholkopf.png",
            talk="TBA",
            abstract="TBA",
            bio="TBA",
            day=4,  # Thursday March 26th
            start="4:00 PM",
            end="5:00 PM",
            location=day_two_str,
        )
    )

    return speakers


def make_tutorials():
    tutorials = []

    # Track 1 tutorials

    tutorials.append(
        Tutorial(
            name="Weiyang Liu",
            role="Researcher",
            website="",
            affiliation="CUHK",
            photo="placeholder.png",
            tutorial="Orthogonal Training for Foundation Models: Theory, Algorithm and Application",
            abstract="Orthogonal training offers a principled way to optimize foundation models without disturbing their core spectrum and geometry. This tutorial will present a unified framework of orthogonal training for large-scale neural networks, with a focus on language and text-to-image foundation models. We will start from first principles -- how orthogonal training relates to the inductive bias of minimum description length, and then show how this idea can lead to generalizable inductive bias. Building on this foundation, we will present recent orthogonal training algorithms, including orthogonal finetuning and orthogonal pretraining. We will further analyze their impact on optimization stability, generalization, calibration, and robustness. Special attention will be given to memory- and compute-efficient implementations that enable billion-parameter models to be trained under tight hardware budgets, as well as connections to sparse training and low-rank adaptation. Finally, we will discuss practical recipes, open-source implementations, and case studies on training and fine-tuning LLMs and other foundation models with orthogonal training, highlighting both the current limitations and promising research frontiers. The tutorial targets researchers and practitioners interested in principled ways to scale foundation models more efficiently, reliably, and interpretably.",
            track=1,
            order=1,
        )
    )

    tutorials.append(
        Tutorial(
            name="Zeju Qiu",
            role="Researcher",
            website="",
            affiliation="Max Planck Institute for Intelligent Systems",
            photo="placeholder.png",
            tutorial="Orthogonal Training for Foundation Models: Theory, Algorithm and Application",
            abstract="Orthogonal training offers a principled way to optimize foundation models without disturbing their core spectrum and geometry. This tutorial will present a unified framework of orthogonal training for large-scale neural networks, with a focus on language and text-to-image foundation models.",
            track=1,
            order=2,
        )
    )

    tutorials.append(
        Tutorial(
            name="Kailash Budhathoki",
            role="Researcher",
            website="",
            affiliation="AWS",
            photo="placeholder.png",
            tutorial="Inference Optimization Playbook for Serving LLMs in the Industry: Techniques from Architecture to AI Accelerators",
            abstract="The explosive growth of Large Language Models (LLMs) in production environments has made inference efficiency a critical bottleneck for industrial adoption. This tutorial provides a comprehensive playbook covering the advanced, production-proven techniques used to minimize latency and maximize throughput when serving state-of-the-art LLMs. We will guide attendees through the complete LLM lifecycle, starting by establishing the hardware constraints imposed by modern AI accelerators, detailing the interplay between memory hierarchy and compute units. We will then examine architectural design choices (e.g., Grouped-Query Attention, MoE, Speculative-Decoding Aware Architectures) and progress to post-training optimization (quantization, sparsity, speculative decoding) with a focus on practical guardrails for accuracy preservation. A significant portion of the tutorial will dive into the core of high-performance inference engines, detailing essential concepts such as continuous batching, Paged Attention, KV caching, efficient scheduling, and the use of CUDA Graphs and kernel fusion. Attendees will gain a deep, end-to-end understanding of how to architect, optimize, and serve LLMs efficiently at scale in a real-world setting.",
            track=1,
            order=3,
        )
    )

    tutorials.append(
        Tutorial(
            name="Jonas Kuebler",
            role="Researcher",
            website="",
            affiliation="AWS",
            photo="placeholder.png",
            tutorial="Inference Optimization Playbook for Serving LLMs in the Industry: Techniques from Architecture to AI Accelerators",
            abstract="",
            track=1,
            order=4,
        )
    )

    tutorials.append(
        Tutorial(
            name="Ashish Khetan",
            role="Researcher",
            website="",
            affiliation="AWS",
            photo="placeholder.png",
            tutorial="Inference Optimization Playbook for Serving LLMs in the Industry: Techniques from Architecture to AI Accelerators",
            abstract="",
            track=1,
            order=5,
        )
    )

    tutorials.append(
        Tutorial(
            name="Meng Fang",
            role="Researcher",
            website="",
            affiliation="University of Liverpool",
            photo="placeholder.png",
            tutorial="Reward Modeling in Large Language Models: Principles, Methods, and Challenges",
            abstract="Reward modeling has become a central mechanism for steering large language models (LLMs) toward desired behaviors. Beyond pure next-token prediction, modern systems rely on pre-defined/learned reward signals to encode preferences over outputs, shape reasoning processes, and perform test-time optimization. This tutorial provides a structured overview of how rewards are built and used in contemporary LLM pipelines. We first introduce how LLMs can be viewed as policies and how learned rewards are used both for post-training and for test-time reranking. We then illustrate reward modeling from preferences: how human feedback is collected, how explicit scalar reward models are trained, and how DPO-style methods use the pair-wise data to optimize the policy directly. Next, we compare outcome and process reward modeling, and discuss the training pipeline of process reward models. We then introduce verifiable rewards and how reinforcement learning from such signals is applied in practice. This is followed by LLM-as-reward settings, where judge models provide language-based, holistic feedback that differs from purely numeric rewards. Finally, we present a unifying view of this design space, evaluation metrics for reward models, key challenges such as data quality and reward hacking, and emerging directions including multimodal and online reward learning.",
            track=1,
            order=6,
        )
    )

    tutorials.append(
        Tutorial(
            name="Yudi Zhang",
            role="Researcher",
            website="",
            affiliation="Eindhoven University of Technology",
            photo="placeholder.png",
            tutorial="Reward Modeling in Large Language Models: Principles, Methods, and Challenges",
            abstract="",
            track=1,
            order=7,
        )
    )

    tutorials.append(
        Tutorial(
            name="Mykola Pechenizkiy",
            role="Researcher",
            website="",
            affiliation="Eindhoven University of Technology",
            photo="placeholder.png",
            tutorial="Reward Modeling in Large Language Models: Principles, Methods, and Challenges",
            abstract="",
            track=1,
            order=8,
        )
    )

    # Track 2 tutorials

    tutorials.append(
        Tutorial(
            name="Leena Chennuru Vankadara",
            role="Researcher",
            website="https://leenacvankadara.com/",
            affiliation="University College London",
            photo="placeholder.png",
            tutorial="Training Neural Networks at Any Scale",
            abstract="At the heart of deep learning's transformative impact lies the concept of scale -- encompassing both data and computational resources, as well as their interaction with neural network architectures. Scale, however, presents critical challenges, such as increased instability during training and prohibitively expensive model-specific tuning. Given the substantial resources required to train such models, formulating high-confidence scaling hypotheses backed by a rigorous theoretical research has become paramount. The first part of the tutorial will provide an overview of significant advances in the theory of scaling in deep learning, covering its historical foundations, recent breakthroughs, and practical implications for training large-scale models. To bridge theory and practice, the tutorial explores another key mathematical ingredient of scaling: the numerical solution algorithms commonly employed in deep learning, spanning domains from vision to language models. We unify these algorithms under a common master template, making their foundational principles transparent. In doing so, we reveal the interplay between adaptation to smoothness structures via online learning and the exploitation of optimization geometry through non-Euclidean norms. Our exposition moves beyond simply building larger models -- it emphasizes strategic scaling, offering insights that promise to advance the field while economizing on resources.",
            track=2,
            order=1,
        )
    )

    tutorials.append(
        Tutorial(
            name="Volkan Cevher",
            role="Researcher",
            website="",
            affiliation="EPFL, LIONS",
            photo="placeholder.png",
            tutorial="Training Neural Networks at Any Scale",
            abstract="",
            track=2,
            order=2,
        )
    )

    tutorials.append(
        Tutorial(
            name="Lu Yin",
            role="Researcher",
            website="",
            affiliation="University of Surrey",
            photo="placeholder.png",
            tutorial="Where to Spend Parameters: From Layerwise Efficiency To Federated Architecture Search",
            abstract='Large neural networks -- especially Large Language Models (LLMs) and modern transformers -- deliver strong performance, but their growing scale makes a central question unavoidable: where should we spend parameters to get the best capability per unit compute? This tutorial presents a unified answer across two complementary levels of design: allocation within a fixed model through layerwise efficiency, and allocation across models under distributed constraints through federated architecture search. We begin by showing that layerwise signals reveal substantial depthwise heterogeneity: different layers contribute unequally to model quality. Leveraging this structure enables targeted pruning for efficient inference and compute-aware finetuning by prioritizing updates on the most influential layers. We then examine the origin of layerwise imbalance as a pretraining deficiency and introduce simple training-time remedies that re-balance layer contributions across depth, improving utilization of the model\'s capacity. Moving from "which layers to trust" to "which architectures to deploy," we examine neural architecture search across increasingly complex settings. We begin with multitask scenarios where architectures must balance accuracy and efficiency across heterogeneous tasks and datasets, then extend to federated learning environments where additional constraints -- distributed data, varying compute budgets, and privacy requirements -- demand coordinated architecture discovery across participants. Together, these methods demonstrate that practical efficiency comes from learning to spend parameters deliberately -- across layers within models, across architectures in model families, and across heterogeneous tasks and participants.',
            track=2,
            order=3,
        )
    )

    tutorials.append(
        Tutorial(
            name="Xilu Wang",
            role="Researcher",
            website="",
            affiliation="University of Surrey",
            photo="placeholder.png",
            tutorial="Where to Spend Parameters: From Layerwise Efficiency To Federated Architecture Search",
            abstract="",
            track=2,
            order=4,
        )
    )

    tutorials.append(
        Tutorial(
            name="Jingfeng Wu",
            role="Researcher",
            website="",
            affiliation="University of California, Berkeley",
            photo="placeholder.png",
            tutorial="Theoretical Insights on Training Instability in Deep Learning",
            abstract="The advances in deep learning build on the dark arts of gradient-based optimization. In deep learning, the optimization process is oscillatory, spiky, and unstable. This makes little sense in classical optimization theory, which primarily operates in a well-behaved, stable regime. Yet, the best training configuration in practice constantly operates in an unstable regime. This tutorial introduces recent theoretical progress in understanding the benign nature of training instabilities, providing new insights from both optimization and statistical learning perspectives. Participants will gain a solid understanding of training instabilities in deep learning, their theoretical and practical implications, and future research directions in this critical area.",
            track=2,
            order=5,
        )
    )

    tutorials.append(
        Tutorial(
            name="Yu-Xiang Wang",
            role="Researcher",
            website="",
            affiliation="UC San Diego",
            photo="placeholder.png",
            tutorial="Theoretical Insights on Training Instability in Deep Learning",
            abstract="",
            track=2,
            order=6,
        )
    )

    tutorials.append(
        Tutorial(
            name="Maryam Fazel",
            role="Researcher",
            website="",
            affiliation="University of Washington",
            photo="placeholder.png",
            tutorial="Theoretical Insights on Training Instability in Deep Learning",
            abstract="",
            track=2,
            order=7,
        )
    )

    return tutorials


def make_organizers():
    organizers = []

    # General Chair
    organizers.append(
        Organizer(
            name="Yi Ma",
            role="General Chair",
            website="https://people.eecs.berkeley.edu/~yima/",
            affiliation="University of Hong Kong",
            photo="ma.jpeg",
        )
    )

    organizers.append(
        Organizer(
            name="Misha Belkin",
            role="General Chair",
            website="http://misha.belkin-wang.org/",
            affiliation="UC San Diego",
            photo="belkin.png",
        )
    )

    organizers.append(
        Organizer(
            name="Gitta Kutyniok",
            role="General Chair",
            website="https://www.ai.math.uni-muenchen.de/members/professor/kutyniok/index.html",
            affiliation="LMU Munchen",
            photo="kutyniok.jpg",
        )
    )

    # Program Chairs
    organizers.append(
        Organizer(
            name="Shiwei Liu",
            role="Program Chair",
            website="https://shiweiliuiiiiiii.github.io/",
            affiliation="ELLIS Institute Tubingen and Max Planck Institute for Intelligent Systems",
            photo="sliu.png",
        )
    )

    organizers.append(
        Organizer(
            name="Rebekka Burkholz",
            role="Program Chair",
            website="https://cispa.de/en/people/c01rebu",
            affiliation="CISPA",
            photo="burkholz.png",
        )
    )

    organizers.append(
        Organizer(
            name="Saiprasad Ravishankar",
            role="Program Chair",
            website="https://sites.google.com/site/sairavishankar3/",
            affiliation="Michigan State University",
            photo="ravishankar.jpg",
        )
    )

    organizers.append(
        Organizer(
            name="William T. Redman",
            role="Program Chair",
            website="https://wredman4.wixsite.com/wtredman",
            affiliation="Johns Hopkins University",
            photo="redman.jpeg",
        )
    )

    # Senior Advisor to PCs
    organizers.append(
        Organizer(
            name="Qing Qu",
            role="Senior Advisor to PCs",
            website="https://qingqu.engin.umich.edu/",
            affiliation="University of Michigan",
            photo="qq.jpeg",
        )
    )

    organizers.append(
        Organizer(
            name="Atlas Wang",
            role="Senior Advisor to PCs",
            website="https://vita-group.github.io/",
            affiliation="UT Austin",
            photo="aw.png",
        )
    )

    organizers.append(
        Organizer(
            name="Jere Sulam",
            role="Senior Advisor to PCs",
            website="https://sites.google.com/view/jsulam",
            affiliation="Johns Hopkins University",
            photo="js.png",
        )
    )

    organizers.append(
        Organizer(
            name="Sijia Liu",
            role="Senior Advisor to PCs",
            website="https://lsjxjtu.github.io/",
            affiliation="Michigan State University",
            photo="liu.png",
        )
    )

    organizers.append(
        Organizer(
            name="Yu-Xiang Wang",
            role="Senior Advisor to PCs",
            website="https://cseweb.ucsd.edu/~yuxiangw/",
            affiliation="UCSD",
            photo="wang.jpeg",
        )
    )

    # Local chairs
    organizers.append(
        Organizer(
            name="Jonas Geiping",
            role="Local Chair",
            website="https://jonasgeiping.github.io/",
            affiliation="ELLIS Institute Tubingen and Max Planck Institute for Intelligent Systems",
            photo="geiping.png",
        )
    )

    organizers.append(
        Organizer(
            name="Haotong Qin",
            role="Tutorial Chair",
            website="https://htqin.github.io/",
            affiliation="ETH",
            photo="qin.png",
        )
    )

    organizers.append(
        Organizer(
            name="Decebal Constantin Mocanu",
            role="Local Chair",
            website="https://www.uni.lu/fstm-en/people/decebal-constantin-mocanu/",
            affiliation="University of Luxembourg",
            photo="d_mocanu.png",
        )
    )

    # Publication chairs
    organizers.append(
        Organizer(
            name="Zhihui Zhu",
            role="Publication Chair",
            website="https://zhihuizhu.github.io",
            affiliation="Ohio State University",
            photo="zz.jpeg",
        )
    )

    organizers.append(
        Organizer(
            name="Weijie Su",
            role="Publication Chair",
            website="http://stat.wharton.upenn.edu/~suw/",
            affiliation="University of Pennsylvania",
            photo="su.jpeg",
        )
    )

    organizers.append(
        Organizer(
            name="Wei Huang",
            role="Publication Chair",
            website="https://weihuang05.github.io/",
            affiliation="RIKEN AIP",
            photo="huang.png",
        )
    )

    # Industry Liaison Chairs
    organizers.append(
        Organizer(
            name="Yi (Ethan) Liang",
            role="Industry Liaison Chair",
            affiliation="Google",
            photo="liang_yi.png",
        )
    )

    organizers.append(
        Organizer(
            name="Souvik Kundu",
            role="Industry Liaison Chair",
            website="https://ksouvik52.github.io/",
            affiliation="Intel",
            photo="kundu.jpeg",
        )
    )

    organizers.append(
        Organizer(
            name="Zechun Liu",
            role="Industry Liaison Chair",
            website="https://zechunliu.com/",
            affiliation="Meta",
            photo="liu_zechun.png",
        )
    )

    # Web Chairs
    organizers.append(
        Organizer(
            name="Sam Buchanan",
            role="Web Chair",
            website="https://sdbuchanan.com/",
            affiliation="UC Berkeley",
            photo="sdb.jpg",
        )
    )

    # Rising Stars Award Chairs
    organizers.append(
        Organizer(
            name="Tianlong Chen",
            role="Rising Stars Award Chair",
            website="https://tianlong-chen.github.io/",
            affiliation="UNC Chapel Hill",
            photo="chen_t.jpeg",
        )
    )

    # Publicity Chairs
    organizers.append(
        Organizer(
            name="Liyue Shen",
            role="Publicity Chair",
            website="https://liyueshen.engin.umich.edu/",
            affiliation="University of Michigan",
            photo="shen-liyue.jpeg",
        )
    )

    # Local support
    organizers.append(
        Organizer(
            name="Carmela Rianna",
            role="Local Support",
            website="https://institute-tue.ellis.eu/en/people/crianna",
            affiliation="ELLIS Institute Tubingen",
            photo="rianna.png",
        )
    )

    organizers.append(
        Organizer(
            name="Matthias Troendle",
            role="Local Support",
            website="https://is.mpg.de/person/mtroendl",
            affiliation="MPI-IS",
            photo="troendle.png",
        )
    )

    # Advisory Committee
    organizers.append(
        Organizer(
            name="Alex Dimakis",
            role="Advisory Committee",
            website="https://users.ece.utexas.edu/~dimakis/",
            affiliation="UC Berkeley",
            photo="dimakis.jpeg",
        )
    )

    organizers.append(
        Organizer(
            name="Michael Elad",
            role="Advisory Committee",
            website="https://elad.cs.technion.ac.il/",
            affiliation="Technion",
            photo="elad.jpeg",
        )
    )

    organizers.append(
        Organizer(
            name="Stefano Soatto",
            role="Advisory Committee",
            website="https://web.cs.ucla.edu/~soatto/",
            affiliation="UCLA",
            photo="soatto.jpeg",
        )
    )

    organizers.append(
        Organizer(
            name="Rebecca Willett",
            role="Advisory Committee",
            website="https://willett.psd.uchicago.edu/",
            affiliation="UChicago",
            photo="willett.jpeg",
        )
    )

    organizers.append(
        Organizer(
            name="Eric P. Xing",
            role="Advisory Committee",
            website="https://www.cs.cmu.edu/~epxing/",
            affiliation="MBZUAI / Carnegie Mellon University",
            photo="ex.jpeg",
        )
    )

    organizers.append(
        Organizer(
            name="Tong Zhang",
            role="Advisory Committee",
            website="http://tongzhang-ml.org/",
            affiliation="University of Illinois Urbana-Champaign",
            photo="zhangt.jpeg",
        )
    )

    organizers.append(
        Organizer(
            name="Anima Anandkumar",
            role="Advisory Committee",
            website="http://tensorlab.cms.caltech.edu/users/anima/",
            affiliation="Caltech / NVIDIA",
            photo="anandkumar.jpeg",
        )
    )

    organizers.append(
        Organizer(
            name="Emmanuel Candes",
            role="Advisory Committee",
            website="https://candes.su.domains/",
            affiliation="Stanford",
            photo="ecandes.jpeg",
        )
    )

    organizers.append(
        Organizer(
            name="Peyman Milanfar",
            role="Advisory Committee",
            website="http://www.milanfar.org/",
            affiliation="Google Research",
            photo="milanfar.jpeg",
        )
    )

    organizers.append(
        Organizer(
            name="Yi Ma",
            role="Advisory Committee",
            website="https://people.eecs.berkeley.edu/~yima/",
            affiliation="University of Hong Kong",
            photo="ma.jpeg",
        )
    )

    return organizers


def make_conference_events():
    conference_events = []

    # Day 1: Monday March 23 - Tutorial Day
    conference_events.append(
        Event(
            name="Registration",
            event_class="meta",
            day=1,  # Monday March 23rd
            start="8:30 AM",
            end="9:00 AM",
            location=day_one_str,
        )
    )

    conference_events.append(
        Event(
            name="Tutorial Session 1<br>T1: Orthogonal Training for Foundation Models<br>T2: Training Neural Networks at Any Scale",
            event_class="tutorial",
            day=1,
            start="9:00 AM",
            end="11:30 AM",
            location=day_one_str,
        )
    )

    conference_events.append(
        Event(
            name="Lunch Break",
            event_class="break",
            day=1,
            start="11:30 AM",
            end="12:30 PM",
            location=day_one_str,
        )
    )

    conference_events.append(
        Event(
            name="Tutorial Session 2<br>T1: Inference Optimization Playbook for Serving LLMs in the Industry<br>T2: Where to Spend Parameters: From Layerwise Efficiency To Federated Architecture Search",
            event_class="tutorial",
            day=1,
            start="12:30 PM",
            end="3:00 PM",
            location=day_one_str,
        )
    )

    conference_events.append(
        Event(
            name="Coffee Break",
            event_class="break",
            day=1,
            start="3:00 PM",
            end="3:30 PM",
            location=day_one_str,
        )
    )

    conference_events.append(
        Event(
            name="Tutorial Session 3<br>T1: Reward Modeling in Large Language Models<br>T2: Theoretical Insights on Training Instability in Deep Learning",
            event_class="tutorial",
            day=1,
            start="3:30 PM",
            end="6:00 PM",
            location=day_one_str,
        )
    )

    # Day 2: Tuesday March 24
    conference_events.append(
        Event(
            name="Registration",
            event_class="meta",
            day=2,  # Tuesday March 24th
            start="8:00 AM",
            end="8:30 AM",
            location=day_two_str,
        )
    )

    conference_events.append(
        Event(
            name="Opening Remarks",
            event_class="remarks",
            day=2,
            start="8:30 AM",
            end="9:00 AM",
            location=day_two_str,
        )
    )

    conference_events.append(
        Event(
            name="Coffee Break",
            event_class="break",
            day=2,
            start="10:00 AM",
            end="10:30 AM",
            location=day_two_str,
        )
    )

    conference_events.append(
        Event(
            name="Lunch Break",
            event_class="break",
            day=2,
            start="11:30 AM",
            end="12:30 PM",
            location=day_two_str,
        )
    )

    conference_events.append(
        Event(
            name="Rising Stars Talks I",
            event_class="rising",
            day=2,
            start="12:30 PM",
            end="1:30 PM",
            location=day_two_str,
        )
    )

    conference_events.append(
        Event(
            name="Wellness Session",
            event_class="wellness",
            day=2,
            start="1:30 PM",
            end="2:30 PM",
            location=day_two_str,
        )
    )

    conference_events.append(
        Event(
            name="Highlight Talks I",
            event_class="oral",
            day=2,
            start="3:30 PM",
            end="4:00 PM",
            location=day_two_str,
        )
    )

    conference_events.append(
        Event(
            name="Poster Session I",
            event_class="poster",
            day=2,
            start="4:00 PM",
            end="6:00 PM",
            location=day_two_str,
        )
    )

    conference_events.append(
        Event(
            name="Reception",
            event_class="event",
            day=2,
            start="6:00 PM",
            end="8:00 PM",
            location=day_two_str,
        )
    )

    # Day 3: Wednesday March 25
    conference_events.append(
        Event(
            name="Coffee Break",
            event_class="break",
            day=3,
            start="10:00 AM",
            end="10:30 AM",
            location=day_two_str,
        )
    )

    conference_events.append(
        Event(
            name="Lunch Break",
            event_class="break",
            day=3,
            start="11:30 AM",
            end="12:30 PM",
            location=day_two_str,
        )
    )

    conference_events.append(
        Event(
            name="Rising Stars Talks II",
            event_class="rising",
            day=3,
            start="12:30 PM",
            end="1:30 PM",
            location=day_two_str,
        )
    )

    conference_events.append(
        Event(
            name="Highlight Talks II",
            event_class="oral",
            day=3,
            start="1:30 PM",
            end="2:00 PM",
            location=day_two_str,
        )
    )

    conference_events.append(
        Event(
            name="Coffee Break",
            event_class="break",
            day=3,
            start="2:00 PM",
            end="2:30 PM",
            location=day_two_str,
        )
    )

    conference_events.append(
        Event(
            name="Poster Session II",
            event_class="poster",
            day=3,
            start="3:30 PM",
            end="5:30 PM",
            location=day_two_str,
        )
    )

    # Day 4: Thursday March 26
    conference_events.append(
        Event(
            name="Coffee Break",
            event_class="break",
            day=4,
            start="10:00 AM",
            end="10:30 AM",
            location=day_two_str,
        )
    )

    conference_events.append(
        Event(
            name="Lunch Break",
            event_class="break",
            day=4,
            start="11:30 AM",
            end="12:30 PM",
            location=day_two_str,
        )
    )

    conference_events.append(
        Event(
            name="Rising Stars Talks III",
            event_class="rising",
            day=4,
            start="12:30 PM",
            end="1:30 PM",
            location=day_two_str,
        )
    )

    conference_events.append(
        Event(
            name="Highlight Talks III",
            event_class="oral",
            day=4,
            start="1:30 PM",
            end="2:00 PM",
            location=day_two_str,
        )
    )

    conference_events.append(
        Event(
            name="Coffee Break",
            event_class="break",
            day=4,
            start="2:00 PM",
            end="2:30 PM",
            location=day_two_str,
        )
    )

    conference_events.append(
        Event(
            name="Closing Remarks",
            event_class="remarks",
            day=4,
            start="5:00 PM",
            end="5:30 PM",
            location=day_two_str,
        )
    )

    return conference_events


def make_speaker_events():
    speakers = make_speakers()
    speaker_events = []
    for speaker in speakers:
        speaker_events.append(
            Event(
                name=speaker.name,
                event_class="keynote",
                day=speaker.day,
                start=speaker.start,
                end=speaker.end,
                location=speaker.location,
                talk=speaker.talk,
            )
        )
    return speaker_events


def create_and_export_calendar():
    speaker_events = make_speaker_events()
    conference_events = make_conference_events()
    cpal_calendar = Calendar(
        name="CPAL-2026",
        start_month="Mar",
        start_day=23,
        start_day_of_week="Monday",
        early_time="8:00 AM",
        late_time="8:00 PM",
        events=speaker_events + conference_events,
    )
    cpal_calendar.validate_calendar()
    cpal_calendar.export_calendar(path=root)


def organizers_to_jekyll():
    organizers = make_organizers()
    for organizer in organizers:
        organizer.export_jekyll(path=root)


def speakers_to_jekyll():
    speakers = make_speakers()
    for speaker in speakers:
        speaker.export_jekyll(path=root)


def tutorials_to_jekyll():
    tutorials = make_tutorials()
    for tutorial in tutorials:
        tutorial.export_jekyll(path=root)


def risingstars_to_jekyll():
    risingstars = make_risingstars()
    for risingstar in risingstars:
        risingstar.export_jekyll(path=root)


def _parse_poster_csv():
    csv_path = Path.home() / "Downloads" / "CPAL 2026 Program - Poster Session.csv"
    mapping = {}
    current_session = None

    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if not any(row) or row[2] == "Title":
                continue
            if row[0].startswith("Day One"):
                current_session = 1
            elif row[0].startswith("Day Two"):
                current_session = 2
            if not row[2] or not row[2].strip():
                continue
            if not row[1] or not row[1].strip():
                continue
            try:
                num = int(row[1].strip())
            except ValueError:
                continue
            title = row[2].strip()
            link = row[3].strip() if len(row) > 3 else ""
            track = "spotlight" if "Recent_Spotlight_Track" in link else "proceedings"
            normalized = " ".join(title.lower().split())
            mapping[normalized] = (current_session, num, track)
    return mapping


def _parse_oral_csv():
    csv_path = Path.home() / "Downloads" / "CPAL 2026 Program - Oral Presentation.csv"
    mapping = {}

    date_to_session = {
        "March 24": 1,
        "March 25": 2,
        "March 26": 3,
    }

    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            date_str = row["Date"]
            title = re.sub(r"^\d+\s+", "", row["Title"]).strip()
            oral_session = None
            for date_key, session_num in date_to_session.items():
                if date_key in date_str:
                    oral_session = session_num
                    break
            if oral_session is not None:
                mapping[" ".join(title.lower().split())] = oral_session
    return mapping


def proceedings_to_jekyll():
    import openreview

    poster_map = _parse_poster_csv()
    oral_map = _parse_oral_csv()

    client = openreview.api.OpenReviewClient(baseurl="https://api2.openreview.net")
    papers = client.get_all_notes(content={"venueid": "CPAL.cc/2026/Conference"})

    out_dir = root / "_proceedings"
    out_dir.mkdir(parents=True, exist_ok=True)

    for paper in papers:
        paper = paper.to_json()
        title = paper["content"]["title"]["value"]
        title_lower = " ".join(title.lower().split())

        venue = paper["content"]["venue"]["value"]
        oral_or_poster = venue.split()[-1].lower()

        if title_lower in poster_map:
            session, num, _track = poster_map[title_lower]
        else:
            print(f"WARNING: Proceedings paper not found in poster CSV: {title}")
            session = 0
            num = 0

        oral_session = 0
        if oral_or_poster == "oral" and title_lower in oral_map:
            oral_session = oral_map[title_lower]

        out = {
            "title": title,
            "authors": ", ".join(paper["content"]["authors"]["value"]),
            "link": "https://openreview.net/forum?id=" + paper["id"],
            "keywords": ", ".join(paper["content"]["keywords"]["value"]),
            "type": oral_or_poster,
            "session": session,
            "num": num,
            "oral_session": oral_session,
        }
        out_fn = paper["id"] + ".md"
        out_path = out_dir / out_fn
        with out_path.open(mode="w", encoding="utf-8") as f:
            f.write("---\n")
            f.write(yaml.dump(out, allow_unicode=True))
            f.write("---\n")

    print(f"Wrote {len(papers)} proceedings papers to {out_dir}")


def spotlight_to_jekyll():
    import openreview

    poster_map = _parse_poster_csv()

    client = openreview.api.OpenReviewClient(baseurl="https://api2.openreview.net")

    papers = []
    for vid in [
        "CPAL.cc/2026/Recent_Spotlight_Track",
        "CPAL.cc/2026/Spotlight_Track",
    ]:
        papers = client.get_all_notes(content={"venueid": vid})
        if papers:
            break

    if not papers:
        print("No spotlight papers found via OpenReview API. Using poster CSV data.")
        out_dir = root / "_spotlight"
        out_dir.mkdir(parents=True, exist_ok=True)
        count = 0
        csv_path = Path.home() / "Downloads" / "CPAL 2026 Program - Poster Session.csv"
        current_session = None
        with open(csv_path, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if not any(row) or row[2] == "Title":
                    continue
                if row[0].startswith("Day One"):
                    current_session = 1
                elif row[0].startswith("Day Two"):
                    current_session = 2
                if not row[2] or not row[2].strip():
                    continue
                if not row[1] or not row[1].strip():
                    continue
                try:
                    num = int(row[1].strip())
                except ValueError:
                    continue
                link = row[3].strip() if len(row) > 3 else ""
                if "Recent_Spotlight_Track" not in link:
                    continue
                title = row[2].strip()
                authors = row[4].strip() if len(row) > 4 else ""
                forum_match = re.search(r"forum\?id=([^&#]+)", link)
                forum_id = forum_match.group(1) if forum_match else f"spotlight_{count}"
                out = {
                    "title": title,
                    "authors": authors,
                    "link": f"https://openreview.net/forum?id={forum_id}",
                    "keywords": "",
                    "type": "poster",
                    "session": current_session,
                    "num": num,
                }
                out_fn = forum_id + ".md"
                out_path = out_dir / out_fn
                with out_path.open(mode="w", encoding="utf-8") as fout:
                    fout.write("---\n")
                    fout.write(yaml.dump(out, allow_unicode=True))
                    fout.write("---\n")
                count += 1
        print(f"Wrote {count} spotlight papers to {out_dir}")
        return

    out_dir = root / "_spotlight"
    out_dir.mkdir(parents=True, exist_ok=True)

    for paper in papers:
        paper = paper.to_json()
        title = paper["content"]["title"]["value"]
        title_lower = title.lower()

        if title_lower in poster_map:
            session, num, _track = poster_map[title_lower]
        else:
            print(f"WARNING: Spotlight paper not found in poster CSV: {title}")
            session = 0
            num = 0

        out = {
            "title": title,
            "authors": ", ".join(paper["content"]["authors"]["value"]),
            "link": "https://openreview.net/forum?id=" + paper["id"],
            "keywords": ", ".join(paper["content"]["keywords"]["value"]),
            "type": "poster",
            "session": session,
            "num": num,
        }
        out_fn = paper["id"] + ".md"
        out_path = out_dir / out_fn
        with out_path.open(mode="w", encoding="utf-8") as f:
            f.write("---\n")
            f.write(yaml.dump(out, allow_unicode=True))
            f.write("---\n")

    print(f"Wrote {len(papers)} spotlight papers to {out_dir}")


def organizer_emails():
    organizers = make_organizers()
    emails = []
    for organizer in organizers:
        emails.append(organizer.email)
    return emails


def speaker_emails():
    speakers = make_speakers()
    emails = []
    for speaker in speakers:
        emails.append(speaker.email)
    return emails


# Argparse for usage
parser = argparse.ArgumentParser(
    description="Create and export database properties for CPAL 2026."
)
parser.add_argument(
    "--orgs",
    dest="do_list",
    action="append_const",
    const=organizers_to_jekyll,
    help="Export organizer YAML info",
)
parser.add_argument(
    "--speakers",
    dest="do_list",
    action="append_const",
    const=speakers_to_jekyll,
    help="Export speaker YAML info",
)
parser.add_argument(
    "--tutorials",
    dest="do_list",
    action="append_const",
    const=tutorials_to_jekyll,
    help="Export tutorial YAML info",
)
parser.add_argument(
    "--stars",
    dest="do_list",
    action="append_const",
    const=risingstars_to_jekyll,
    help="Export Rising Star YAML info",
)
parser.add_argument(
    "--calendar",
    dest="do_list",
    action="append_const",
    const=create_and_export_calendar,
    help="Create and export event calendar",
)
parser.add_argument(
    "--proceedings",
    dest="do_list",
    action="append_const",
    const=proceedings_to_jekyll,
    help="Export Accepted Proceedings Track YAML info",
)
parser.add_argument(
    "--spotlight",
    dest="do_list",
    action="append_const",
    const=spotlight_to_jekyll,
    help="Export Spotlight Track YAML info",
)
parser.add_argument(
    "--org-emails",
    dest="do_list",
    action="append_const",
    const=lambda: print(", ".join(map(str, organizer_emails()))),
    help="Print organizer emails to stdout",
)

args = parser.parse_args()
if args.do_list is None:
    raise SyntaxError("Provide at least one argument (see -h)")
for func in args.do_list:
    func()
