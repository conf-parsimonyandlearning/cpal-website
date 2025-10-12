#!/usr/bin/env python
# -*- coding: utf-8 -*-

# We do data input in this file, essentially.

# imports
import argparse
from pathlib import Path

import yaml
from cpal_2025_session_dict import create_session_paper_mapping
from event import Event
from papers import get_accepted_papers
from program import Calendar
from roles import Organizer, RisingStar, Speaker, Tutorial

# this is the root directory of the jekyll site
# exports will go there
root = Path(__file__).parent.parent.parent

# variables for location strings
# day_one_str = '<a href="/venue/#day-1-venue-rayson-huang-theatre-hku">Rayson Huang Theatre</a>'
# day_two_str = '<a href="/venue/#days-24-venue-lecture-hall-ii-cpd-lg07-10-lg-centennial-campus-hku">Lee Shau Kee Lecture Ctr.</a>'
# banquet_str = '<a href="/social/#dinner-banquet-january-4th-2024">Maxim’s Palace Chinese Restaurant, 2/F, City Hall, 5-7 Edinburgh Place, Central</a>'
# tram_str = '<a href="/social/#tram-party-january-5th-2024">Whitty Street Tram Depot</a>'
day_one_str = "Fortinet Seminar Room, E160"  # Assuming this for Tuesday
day_two_str = "Simonyi Conference Center"  # Assuming this for Wednesday and Thursday

# Speaker photos should close to 1.33 : 1 aspect (height : width)

# Organizer photos should be close to 1:1 aspect

# Rising Stars photos should be close to 1:1 aspect


def make_risingstars():
    risingstars = []

    risingstars.append(
        RisingStar(
            name="Tianlong Chen",
            role="Assistant Professor",
            website="https://tianlong-chen.github.io/",
            affiliation="The University of North Carolina at Chapel Hill",
            photo="image1.png",
            session=1,
            order=1,
            talk="Breaking the Resource Monopoly from Industries: Sustainable and Reliable LLM Serving By Recycling Outdated and Resource-Constrained GPUs",
            abstract="In recent years, Large Language Model (LLM) agents, exemplified by models like ChatGPT, and PaLM, have showcased remarkable prowess in various tasks, owing to their vast number of parameters and emergent in-context learning capabilities. To serve these gigantic models with billions of parameters, it is a trend and becomes a must to explore how to use the existing hardware, especially outdated hardware, to collectively improve environmental sustainability, efficiency, and reliability for LLM serving. A few pioneering examples include Microsoft's Project Natick, Google's TPU Pod Optimization, Alibaba's Cloud Server Repurposing, and Facebook's Network Hardware Reuse. In this talk, I will traverse my series of contributions with promising new directions, particularly emphasizing modularized LLM architecture (Part 1), in-storage sustainable computing (Part 2), and reliable serving against software and hardware attacks (Part 3).",
        )
    )

    risingstars.append(
        RisingStar(
            name="Grigorios Chrysos",
            role="Assistant Professor",
            website="https://grigoris.ece.wisc.edu/. ",
            affiliation="University of Wisconsin-Madison",
            photo="image2.png",
            session=1,
            order=2,
            talk="Stairway to Specialization: The Path of Scalable Experts",
            abstract="The Mixture of Experts (MoE) paradigm utilized in large (language or multimodal) models facilitates tackling diverse tasks without specific training. MoE facilitates specialization, simplifies debugging and model steerability. However, scaling the number of experts to achieve fine-grained specialization presents a significant computational challenge, unless low-rank structures are assumed. To that end, we will then introduce the μMoE layer, which employs tensor algebra to perform implicit computations on large weight tensors in a factorized form. This enables using thousands of experts at once, without increasing the computational cost over single MLP layers. I will showcase how the μMoE layer enhances specialization in both image and text applications, including GPT-2 models. This approach allows for on-demand model tailoring by selectively deactivating experts or posing counterfactual questions.",
        )
    )

    risingstars.append(
        RisingStar(
            name="Yihua Zhang",
            role="Ph.D. Candidate",
            website="https://www.yihua-zhang.com/",
            affiliation="Michigan State University",
            photo="image3.png",
            session=1,
            order=3,
            talk="Authenticity and Resilience: New Frontiers in Machine Unlearning for Large Language Models",
            abstract="Machine unlearning has emerged as a powerful approach for selectively removing harmful or undesirable knowledge from large language models (LLMs) while preserving their general capabilities. However, recent findings reveal significant pitfalls in existing unlearning methods, including 'fake unlearning'—where knowledge is merely hidden rather than truly removed. Such incomplete removal can render models highly vulnerable to malicious attacks or unintentional downstream fine-tunings. In this talk, we will explore how authenticity—the genuine erasure of targeted knowledge—and resilience—robustness to relearning and finetuning—can jointly serve as guiding principles for more effective machine unlearning. Drawing on both theoretical insights and empirical findings, we discuss novel strategies such as second-order optimization, weight attribution analysis, invariance-regularized training, and sharpness-aware unlearning. We show how these approaches not only address 'fake unlearning' but also provide even more benefits. By mapping out these new frontiers, our work contributes practical insights and foundational ideas to help researchers and practitioners develop robust, efficient, and truly trustworthy unlearning solutions for the next generation of large language models.",
        )
    )

    risingstars.append(
        RisingStar(
            name="Congyue Deng",
            role="Ph.D. Candidate",
            website="https://cs.stanford.edu/~congyue/ ",
            affiliation="Stanford University",
            photo="image4.png",
            session=1,
            order=4,
            talk="Denoising Hamiltonian Network for Physical Reasoning",
            abstract="Machine learning frameworks for physical problems are expected not only to model the data distributions, but also to understand and enforce the physical constraints that preserve the key structures of the physical systems. Many existing works address these problems by constructing physical operators in neural networks. Despite their theoretically guaranteed physical properties, these methods face two key limitations: (i) They mainly focus on local temporal relations between adjacent time steps, omitting longer-range or abstract-level physical relations; and (ii) they primarily emphasize forward simulation and overlook other physical reasoning tasks in broader scopes. To address these problems, we propose the Denoising Hamiltonian Network (DHN), a novel framework that generalizes the physical concepts in Hamiltonian mechanics with flexible neural network designs. By incorporating a denoising mechanism into the network, it also circumvents the inherent challenges of numerical integration. Moreover, we also introduce global conditioning to facilitate multi-system modeling. We demonstrate its effectiveness on multiple different physical reasoning tasks.",
        )
    )

    risingstars.append(
        RisingStar(
            name="Nived Rajaraman",
            role="Ph.D. Candidate",
            website="https://nivedr.github.io/ ",
            affiliation="University of California, Berkeley",
            photo="image5.png",
            session=1,
            order=5,
            talk="New data-centric frameworks for sequential-decision making",
            abstract="As machine learning systems grow increasingly general-purpose and data-centric, there is a pressing need to develop approaches which mitigate the significant cost of collecting high-quality data. This challenge is exacerbated when agents are deployed in settings involving settings involving sequential decision making. In such changing environments, unseen situations are encountered frequently and undesirable behavior can be catastrophic. For problems involving sequential decision making, a hybrid pipeline (1. pre-training a base policy from offline datasets, which is then 2. fine-tuned by online exploration) has emerged as one of the most effective ways to train performant agents. But how do we carry out pre-training and fine-tuning efficiently and robustly, when access to high-quality data forms one of the major bottlenecks? In this talk, I will discuss new approaches for this problem, which build upon insights derived from principled mathematical frameworks. I will present, (i) [Pre-training] A statistical framework for Imitation Learning, resulting in provably optimal algorithms which have small data footprints in practice. (ii) [Fine-tuning] A study of how verifier-based approaches (such as RL) appear to scale more favorably than verifier-free approaches with fixed data budgets I will conclude with a discussion of future research directions and the longer-term goal of exploring the interplay of RL and modern approaches to sequence-modeling.",
        )
    )

    risingstars.append(
        RisingStar(
            name="Ming Yin",
            role="Postdoctoral Associate",
            website="https://mingyin0312.github.io/",
            affiliation="Princeton University",
            photo="image6.png",
            session=2,
            order=1,
            talk="On the role of reinforcement learning in the era of generative AI",
            abstract="The rise of generative AI has transformed the landscape of artificial intelligence, enabling unprecedented capabilities in creative problem-solving, content generation, and novel scientific discovery. However, as these models continue to scale, challenges related to alignment, safety, and decision-making in dynamic, real-world environments become increasingly prominent. Reinforcement learning (RL) offers a powerful framework to address these challenges by enabling agents to learn from feedback, optimize long-term outcomes, and adapt to complex scenarios. This talk explores the intersection of reinforcement learning and generative AI, highlighting how RL can enhance generative models in areas such as fine-tuning for user preferences, faster inference, and safe deployment. We also discuss the evaluation front for the current generative AI.",
        )
    )

    risingstars.append(
        RisingStar(
            name="Wei Huang",
            role="Research Scientist",
            website="https://weihuang05.github.io/",
            affiliation="RIKEN",
            photo="image7.png",
            session=2,
            order=2,
            talk="Advancing Feature Learning Theory: Optimization and Generalization for Foundation Models",
            abstract="Foundation models, particularly Transformers, have revolutionized modern machine learning, showcasing remarkable capabilities such as in-context learning (ICL), multi-modal representation learning, and vision-specific applications. However, a deep theoretical understanding of their optimization dynamics, generalization mechanisms, and emergent behaviors remains incomplete. My recent research addresses these challenges, developing principled frameworks to unravel the intricate mechanisms of foundation models. This talk will explore three key contributions: (1) Optimization and Generalization in Transformers, where I analyze training dynamics and characterize the transition between effective and poor generalization in noisy data settings; (2) In-Context Learning, with a novel mathematical framework explaining how Transformers leverage multi-concept word semantics for efficient task adaptation; and (3) Multi-Modal Contrastive Learning, establishing a unified feature learning theory to explain why multi-modal learning outperforms single-modal approaches in both optimization and downstream generalization. These contributions bridge the gap between theoretical advancements and practical implementations, paving the way for the design of scalable, trustworthy, and efficient foundation model.",
        )
    )

    risingstars.append(
        RisingStar(
            name="Hadi Daneshmand",
            role="Assistant Professor",
            website="https://www.mit.edu/~hdanesh/index.html ",
            affiliation="University of Virginia",
            photo="image8.png",
            session=2,
            order=3,
            talk="Learning to Compute",
            abstract="Understanding the mechanisms of deep learning models with billions of parameters is a fundamental challenge in AI research. Recent findings reveal that feature extraction in these models progresses incrementally, step-by-step, across network layers. We will review these experimental observations and present theoretical studies that explain the incremental process. We show how this process enables models to implement iterative algorithms capable of solving several problems, including linear regression, optimal transport, and policy evaluation for reinforcement learning, with theoretical guarantees. This computational view provides insights into effective practices like prompt engineering for language models. These findings are steps towards learning from data to implement algorithms, a lasting quest in neural computing research.",
        )
    )

    risingstars.append(
        RisingStar(
            name="Souvik Kundu",
            role="Lead Research Scientist",
            website="https://ksouvik52.github.io/ ",
            affiliation="Intel AI Lab",
            photo="image9.png",
            session=2,
            order=4,
            talk="AI Assisted Automation at Scale: Enabling Large Model Intelligence at Small Scale Devices",
            abstract="With the emergence of large foundation models (LFMs), artificial intelligence (AI) has found its use-cases in various automation tasks across multiple modalities. With this increasing surge of AI assistance, there has been increasing demand for deployment of these models at the edge including AI personal computers (AIPCs) and mobile devices. However, these deployments at scale face a fundamental challenge of deploying large models on a small computation and memory budget. Additionally, various AI assisted tasks like long context reasoning require additional memory overhead of long prefix storage. The problem further intensifies with the emergence of agents where critical thinking may often require assistance from multiple LFMs. Towards mitigating these roadblocks this talk will focus on two major classes of solutions: (1) efficient and scalable optimizations for LFMs: to reduce their latency and improve operation throughput during autoregressive inference while maintaining their down-stream task performance; and (2) enable improved capabilities via post-training optimizations: to improve a model's long context understanding beyond its training effective receptive field. In specific, we empirically demonstrate the long context understanding improvement for the Mamba state space models (SSMs) by up to orders of magnitude, that too without any training requirements of the pre-trained weights.",
        )
    )

    risingstars.append(
        RisingStar(
            name="Denny Wu",
            affiliation="New York University & Flatiron Institute",
            website="https://dennywu1.github.io/",
            role="CDS-Flatiron Faculty Fellow",
            photo="image10.png",
            session=2,
            order=5,
            talk="Learning Single-Index Models with Neural Networks and Gradient Descent",
            abstract="Single-index models (SIMs) are characterized by a univariate link function applied to a one-dimensional projection of the input. This framework has been extensively studied in the deep learning theory literature to investigate neural networks' adaptivity to low-dimensional targets and the advantages of feature learning. In this talk, we will present recent advances in understanding the optimization dynamics of gradient-based feature learning for SIMs, drawing on analytical tools from high-dimensional statistics.",
        )
    )

    risingstars.append(
        RisingStar(
            name="Yu Sun",
            role="Assistant Professor",
            website="https://sunyumark.github.io/",
            affiliation="Johns Hopkins University",
            photo="image11.png",
            session=3,
            order=1,
            talk="Provable Probabilistic Imaging using Score-based Generative Models",
            abstract="Inverse problems in imaging often suffer from ill-posedness, where the task of recovering an unknown signal from incomplete and noisy measurements lacks a unique solution. Posterior sampling offers a principled approach to tackle this challenge by estimating the full posterior distribution of the unknown signal, providing both reconstructions and uncertainty quantification. In this talk, I will introduce two complementary methods for provable posterior sampling in computational imaging by using score-based diffusion models. The first method is plug-and-play Monte Carlo (PnP-MC), which can be viewed as the sampling extension of the proximal gradient method; the other one is plug-and-play Diffusion Model (PnP-DM), which mimics the dynamics of alternating direction method of multipliers. Theoretical guarantees on the convergence of the two methods will be also discussed. Our results on various imaging tasks, including nonlinear black hole imaging, demonstrate the superior performance of PnP-MC/PnP-DM in image reconstruction, as well as their high-fidelity uncertainty quantification.",
        )
    )

    risingstars.append(
        RisingStar(
            name="Ismail Alkhouri",
            role="Research Scientist; Visiting Scholar",
            website="https://sites.google.com/view/ismailalkhouri/about",
            affiliation="DARPA; University of Michigan at Ann Arbor, Michigan State University",
            photo="image12.png",
            session=3,
            order=2,
            talk="Dataless Quadratic Differentiable Combinatorial Optimization",
            abstract="Combinatorial Optimization (CO) addresses many important problems, including the Maximum Independent Set (MIS) problem and the Maximum Cut (MaxCut) Problem. Alongside exact and heuristic solvers, differentiable approaches have emerged, often using training data. Here, we propose a new dataless quadratic formulation for MIS and MaxCut. We characterize local minimizers and stationary points and derive conditions with respect to the solution. To tackle the non-convexity of the objectives, we propose optimizing several initializations in parallel using momentum-based gradient descent. Our experimental results demonstrate the effectiveness of the proposed method compared to exact, heuristic, sampling, and data-centric approaches. Notably, our method avoids the out-of-distribution tuning and reliance on (un)labeled data required by data-centric methods. Additionally, a key advantage of our approach is that, unlike exact and heuristic solvers, the runtime scales only with the number of nodes in the graph, not the number of edges.",
        )
    )

    risingstars.append(
        RisingStar(
            name="Yingcong Li",
            role="Ph.D. Student",
            website="https://yingcong-li.github.io/",
            affiliation="University of Michigan, Ann Arbor",
            photo="image13.png",
            session=3,
            order=3,
            talk="Transformers as Support Vector Machines",
            abstract="The remarkable success of large language models (LLMs) has drawn significant interest, but their underlying mechanisms remain underexplored. This is due to the complexity of their architectures and how their predictions depend heavily on the data. My research focuses on uncovering the fundamental reasons behind the effectiveness of LLMs. One key insight comes from analyzing attention mechanisms, and our work shows that optimized attention acts like a support vector machine, highlighting relevant elements in the input sequence while suppressing irrelevant ones.",
        )
    )

    risingstars.append(
        RisingStar(
            name="Soufiane Hayou",
            role="Researcher",
            website="https://www.soufianehayou.com/",
            affiliation="Simons Institute, UC Berkeley",
            photo="image14.png",
            session=3,
            order=4,
            talk="A Theoretical Framework for Efficient Learning at Scale",
            abstract="State-of-the-art performance is usually achieved via a series of modifications to existing neural architectures and their training procedures. A common feature of these networks is their large-scale nature: modern neural networks usually have billions -- if not hundreds of billions -- of trainable parameters. While empirical evaluations generally support the claim that increasing the scale of neural networks (width, depth, etc) boosts model performance if done correctly, optimizing the training process across different scales remains a significant challenge, and practitioners tend to follow empirical scaling laws from the literature. In this talk, I will present a unified framework for efficient learning at large scale. The framework allows us to derive efficient learning rules that automatically adjust to model scale, ensuring stability and optimal performance. By analyzing the interplay between network architecture, optimization dynamics, and scale, we demonstrate how these theoretically-grounded learning rules can be applied to both pretraining and finetuning. The results offer new insights into the fundamental principles governing neural network scaling and provide practical guidelines for training large-scale models efficiently.",
        )
    )

    risingstars.append(
        RisingStar(
            name="Yanchao Yang",
            role="Assistant Professor",
            website="https://yanchaoyang.github.io/",
            affiliation="The University of Hong Kong",
            photo="image15.png",
            session=3,
            order=5,
            talk="InfoBodied AI: Learning Mutual Information for Embodied AI",
            abstract="Embodied AI strives to create agents capable of learning and tackling complex tasks involving physical interactions, with potential applications in many areas, such as housekeeping, caregiving, and logistics. Such agents must be able to perceive their environment, construct scene representations, and carry out reasoning and actions to accomplish task-specific goals. However, existing learning approaches rely on human annotations or unrealistic simulations, leading to generalization problems in the real world. Thus, it is crucial to equip embodied agents with the ability to autonomously learn from real-world data, minimizing reliance on human supervision and enabling adaptability to new tasks. We propose that the key to autonomous learning of embodied agents is the mutual correlations in the unlabeled data. In this presentation, we will talk about how we can efficiently compute mutual information of data by developing novel neural estimators. We will also show how these freely available mutual correlations can help reduce human annotation effort in learning label-efficient perception, scene representation, and manipulation concepts for generalizable policies. Finally, we show a potential framework to build embodied agents that can learn in unseen environments and automatically acquire novel interaction skills by leveraging mutual information in unlabeled observational data.",
        )
    )

    return risingstars


def make_speakers():
    speakers = []

    # speakers.append(
    #     Speaker(
    #         name="Andrea Montanari",
    #         role="Speaker",
    #         website="https://web.stanford.edu/~montanar/",
    #         affiliation="Stanford University",
    #         photo="montanari.jpeg",
    #         talk="Plenary Talk 1",  # As shown in schedule
    #         abstract="TBA",
    #         bio="TBA",
    #         day=4,  # Thursday March 27th
    #         start="9:00 AM",
    #         end="10:00 AM",
    #         location=day_two_str,
    #     )
    # )

    speakers.append(
        Speaker(
            name="Michael Unser",
            role="Speaker",
            website="https://bigwww.epfl.ch/unser/",
            affiliation="École Polytechnique Fédérale de Lausanne (EPFL)",
            photo="unser.jpeg",
            talk="Are the Methods of Convex Analysis Competitive with Deep Neural Networks?",
            abstract="Computational imaging is currently dominated by two paradigms. Traditional variational methods, supported by well-established theory, provide guarantees for convergence, stability, and signal recovery from limited measurements, as in compressed sensing. In contrast, deep neural network methods generally achieve superior image reconstruction but suffer from a lack of robustness (tendency to hallucinate) and theoretical understanding. This raises a fundamental question: Can variational methods be improved by learning the regularizer while maintaining their theoretical guarantees? To address this, we introduce a general framework for image reconstruction under the constraints of amplitude-equivariance and convexity. We demonstrate that polyhedral norms enable universality, allowing for the design of trainable regularization architectures. These architectures outperform traditional sparsity-based methods, and help us bridge the gap between theoretical rigor and practical performance in computational imaging.",
            bio="Michael Unser is Full Professor at the EPFL and the academic director of EPFL's Center for Imaging, Lausanne, Switzerland. His primary areas of investigation are biomedical imaging and applied functional analysis. He is internationally recognized for his research contributions to sampling theory, wavelets, the use of splines for image processing, and computational bioimaging. He has published over 400 journal papers on those topics. Prof. Unser is a fellow of the IEEE (1999), an EURASIP fellow (2009), and a member of the Swiss Academy of Engineering Sciences. He is the recipient of several international prizes including five IEEE-SPS Best Paper Awards, two Technical Achievement Awards from the IEEE (2008 SPS and EMBS 2010), the Technical Achievement Award from EURASIP (2018), and the IEEE-EMBS Career Achievement Award (2020). He was awarded three ERC AdG grants: FUNSP (2011-2016), GlobalBioIm (2016-2021), and FunLearn (2021-2026) in succession, with the ERC funding scheme being the most competitive one in Europe.",
            day=3,  # Wednesday March 26th
            start="11:30 AM",
            end="12:30 PM",
            location=day_two_str,
        )
    )

    speakers.append(
        Speaker(
            name="Alison Gopnik",
            role="Speaker",
            website="https://psychology.berkeley.edu/people/alison-gopnik",
            affiliation="University of California, Berkeley",
            photo="gopnik.jpeg",
            talk="Empowerment Gain and Causal Model Construction",  # As shown in schedule
            abstract="Learning about the causal structure of the world is a fundamental problem for human cognition. Causal models and especially causal learning have proved to be difficult for Large Models using standard techniques of deep learning. In contrast, cognitive scientists have applied advances in our formal understanding of causation in computer science, particularly within the Causal Bayes Net formalism, to understand human causal learning. In the very different tradition of reinforcement learning, researchers have described an intrinsic reward signal called “empowerment” which maximizes mutual information between actions and their outcomes. “Empowerment” may be an important bridge between classical Bayesian causal learning and reinforcement learning and may help to characterize causal learning in humans and enable it in machines.  If an agent learns an accurate causal world model they will necessarily increase their empowerment, and increasing empowerment will lead to a more accurate causal world model. Empowerment may also explain distinctive empirical features of children’s causal learning, as well as providing a more tractable computational account of how that learning is possible.",
            bio="TBA",
            day=2,  # Tuesday March 25th
            start="11:00 AM",
            end="12:00 PM",
            location=day_two_str,
        )
    )

    speakers.append(
        Speaker(
            name="Fredrik Kjolstad",
            role="Speaker",
            website="https://fredrikbk.com/",
            affiliation="Stanford University",
            photo="kjolstad.jpeg",
            talk="Domain-Specific Software for ML, Hardware, and their Composition",  # As shown in schedule
            abstract="Computer scientists have always built languages and libraries to make it easier to write software for different domains. In the last decade, the demand for performance has dramatically increased due to more expensive uses of more data in machine learning. To deliver this performance, we are increasingly turning to specialized hardware. Such hardware places a large burden on the software stack and increases the need for compilers and programming models to be portable. I will share my thoughts on designing programming systems for machine learning applications that permit portable compilation across disparate hardware. These programming systems must raise the level of abstraction to diverse operations on four abstract collections: tensors, graphs, relations, and space. By raising the level of abstraction and by introducing new compiler techniques, we can make programs portable across different machines and different data structures. To manage complexity, compilers should target hardware-facing abstract machines that separate the software and hardware implementations. Finally, intermediate languages can also help us describe hardware to the compiler, so that we can target it without rewriting large parts of the compiler.",
            bio="Fredrik Kjolstad is an Assistant Professor in Computer Science at Stanford University. He works on topics in compilers, programming models, and systems, with an emphasis on compiler techniques that make high-level languages portable. He has received the NSF CAREER Award, the MIT EECS Sprowls PhD Thesis Award in Computer Science, the Tau Beta Phi 2024 Teaching Honor Roll, the Rosing Award, an Adobe Fellowship, a Google Research Scholarship, and several distinguished paper awards.",
            day=3,  # Wednesday March 26th
            start="9:00 AM",
            end="10:00 AM",
            location=day_two_str,
        )
    )

    speakers.append(
        Speaker(
            name="Yingyu Liang",
            role="Speaker",
            website="https://yingyuliang.github.io/",
            affiliation="University of Hong Kong, University of Wisconsin-Madison",
            photo="liang.jpg",
            talk="Towards Better Understanding of Deep Learning via Investigations of the Learning Dynamics",  # As shown in schedule
            abstract="Compared to the unprecedented empirical success of deep learning, theoretical understanding largely lags behind. In particular, traditional tools are inadequate for analyzing the optimization and generalization in deep learning. This talk will discuss the unique and novel challenges in this direction, via a few case studies: the neural tangent kernel (NTK) approach, feature learning beyond NTK, and different in-context learning behavior of larger language models.",
            bio="TBA",
            day=4,  # Thursday March 27th
            start="9:00 AM",
            end="10:00 AM",
            location=day_two_str,
        )
    )

    speakers.append(
        Speaker(
            name="Konrad Kording",
            role="Speaker",
            website="https://kordinglab.com/people/konrad_kording/index.html",
            affiliation="University of Pennsylvania",
            photo="kording.jpeg",
            talk="How Can We Succeed With Parsimonious Models in a World that is Not So Parsimonious",  # As shown in schedule
            abstract="Many interesting parts of the world, such as ecosystems, economies, psychology, cells and brains are, deep down, very much not explainable in a parsimonious way. And yet, humans, quite successfully, describe the world around them as it it were, and machine learning models are apparently internally quite parsimonious. I will comment on the statistical nature of the world around us and why we may succeed well assuming parsimony.",
            bio="TBA",
            day=4,  # Thursday March 27th
            start="1:30 PM",
            end="2:30 PM",
            location=day_two_str,
        )
    )

    speakers.append(
        Speaker(
            name="Yuandong Tian",
            role="Speaker",
            website="https://yuandong-tian.com/",
            affiliation="Meta AI Research",
            photo="tian.png",
            talk="Emergence of Various Structures During Transformer Training via the Lens of Training Dynamics",  # As shown in schedule
            abstract="Large Language Models (LLMs) have demonstrated remarkable performance across diverse applications. However, most empirical works treat the underlying architecture as black boxes, and it remains a mystery what representation the model learns and how it learns. I will cover two aspects of our theoretical analysis, including the training dynamics of self-attention layers when learning Transformers (i.e. how it learns), as well as intriguing structure of the resulting representations (i.e. what it learns), which includes not only basic structure of sparsity and low rankness, but also more complicated ones such as algebraic, hierarchical and spectral structures. Our analysis provides insights into the complicated nonlinear learning process beyond the scope of traditional learning theory, leads to development of novel empirical approaches and shed light on a possible unification of neural and symbolic representations.",
            bio="TBA",
            day=4,  # Thursday March 27th
            start="4:00 PM",
            end="5:00 PM",
            location=day_two_str,
        )
    )

    speakers.append(
        Speaker(
            name="Jason Lee",
            role="Speaker",
            website="https://jasondlee88.github.io/",
            affiliation="Princeton University",
            photo="lee.jpeg",
            talk="Emergence and Scaling Laws for SGD Learning and Learning Compositional Functions with Transformers",  # As shown in schedule
            abstract="This is a two part talk. (1) We study the sample and time complexity of online stochastic gradient descent (SGD) for learning a two-layer neural network with $P$ orthogonal neurons on isotropic Gaussian data. We focus on the challenging regime $$P\\\\gg 1$$ and allow for large condition number in the second-layer, covering the power-law scaling $$a_p= p^{-\\\\beta}$$ as a special case. We characterize the SGD dynamics for the training of a student two-layer network to minimize the squared loss, and identify sharp transition times for the recovery of each signal direction. In the power-law setting, our analysis entails that while the learning of individual teacher neurons exhibits abrupt phase transitions, the juxtaposition of $$P\\\\gg 1$$ emergent learning curves at different timescales leads to a smooth scaling law in the cumulative squared loss. (2) Transformer-based language models have demonstrated impressive capabilities across a range of complex reasoning tasks. Prior theoretical work exploring the expressive power of transformers has shown that they can efficiently perform multi-step reasoning tasks. However, the learnability of such constructions, particularly the conditions on the data distribution that enable efficient learning via SGD, remains an open question. Towards answering this question, we study the learnability of a task called $$k$$-fold composition, which requires computing an interleaved composition of $$k$$ input permutations and $$k$$ hidden permutations, and can be expressed by a transformer with $$O(\\\\log k)$$ layers. We show that this function class can be efficiently learned, with runtime and sample complexity polynomial in $$k$$, by gradient descent on an $$O(\\\\log k)$$-depth transformer via mixed training: one in which data consists of $$k'$$-fold composition functions with $$k' \\\\le k$$ trained on simultaneously. Our work sheds light on the necessity and sufficiency of having both easy and hard examples in the data distribution for transformers to learn complex compositional tasks. A corresponding statistical query lower bound shows that without mixed training requires $$\\\\exp(k)$$ samples and time.",
            bio="TBA",
            day=2,  # Tuesday March 25th
            start="3:00 PM",
            end="4:00 PM",
            location=day_two_str,
        )
    )

    speakers.append(
        Speaker(
            name="Surya Ganguli",
            role="Speaker",
            website="https://ganguli-gang.stanford.edu/surya.html",
            affiliation="Stanford University",
            photo="ganguli.png",
            talk="On learning and imagination: of mice and machines",
            abstract="Three remarkable abilities of brains and machines are to: (1) learn behaviors from a single example, (2) imagine new possibilities, and (3) perform mathematical reasoning. I will discuss completely mechanistically interpretable and predictive models of how mice perform (1) during navigation, and how diffusion models imagine new images in (2). Then I will consider how LLM training protocols can be modified so that they can better perform mathematical reasoning in (3). Together this will cover a subset of how mice and machines learn, imagine and reason.<br><br>References:<br>Mouse navigation: <a href=\'https://www.nature.com/articles/s41586-024-08034-3\'>https://www.nature.com/articles/s41586-024-08034-3</a><br>Theory of creativity in diffusion models: <a href=\'https://arxiv.org/abs/2412.20292\'>https://arxiv.org/abs/2412.20292</a><br>Mathematical reasoning: <a href=\'https://arxiv.org/abs/2502.07154\'>https://arxiv.org/abs/2502.07154</a>",
            bio="TBA",
            day=3,  # Wednesday March 26th
            start="3:00 PM",
            end="4:00 PM",
            location=day_two_str,
        )
    )

    speakers.append(
        Speaker(
            name="Richard Baraniuk",
            role="Speaker",
            website="https://richb.rice.edu/",
            affiliation="Rice University",
            photo="baraniuk.jpeg",
            talk="Parsimony in the Geometry of Deep Learning",  # As shown in schedule
            abstract="We study the geometry of deep learning through the lens of approximation theory via splines. The enabling insight is that a large class of deep networks can be written as a composition of continuous piecewise affine spline operators, which provides a powerful portal through which to interpret and analyze their inner workings. Our particular focus is the local geometry of the spline partition of the network’s input space, which opens up new avenues to study how deep networks parsimoniously organize signals in a hierarchical, multiscale fashion.",
            bio="Richard G. Baraniuk is the C. Sidney Burrus Professor of Electrical and Computer Engineering at Rice University and the Founding Director of OpenStax and SafeInsights. His research interests lie in new theory, algorithms, and hardware for machine learning, signal processing, and sensing. He is a Member of the National Academy of Engineering and American Academy of Arts and Sciences and a Fellow of the National Academy of Inventors, AAAS, and IEEE. He has received the DOD Vannevar Bush Faculty Fellow Award, the IEEE Jack S. Kilby Signal Processing Medal, the IEEE Signal Processing Society Technical Achievement and Society Awards, the Harold W. McGraw, Jr. Prize in Education, and the IEEE James H. Mulligan, Jr. Education Medal, among others.",
            day=2,  # Tuesday March 25th
            start="9:00 AM",
            end="10:00 AM",
            location=day_two_str,
        )
    )

    return speakers


def make_tutorials():
    tutorials = []

    tutorials.append(
        Tutorial(
            name="Yi Ma",
            role="Professor",
            website="https://people.eecs.berkeley.edu/~yima/",
            affiliation="UC Berkeley / HKU IDS",
            photo="ma.jpeg",
            tutorial='"ReduNet: A White-box Deep Network from the Principle of Maximizing Rate Reduction"',
            abstract='"To begin, we will focus on the special yet highly useful case of learning the data distribution and transforming it to an <em>linear discriminative representation</em> (LDR). We will discuss the information theoretic and statistical principles behind such a representation, and design a loss function, called the <em>coding rate reduction</em>, which is optimized at such a representation. By unrolling the gradient ascent on the coding rate reduction, we will construct a deep network architecture, called the ReduNet, where each operator in the network has a mathematically precise (hence white-box and interpretable) function in the transformation of the data distribution towards an LDR. Also, the ReduNet may be constructed layer-wise in a forward-propagation manner, that is, without <em>any</em> back-propagation required."',
            track=1,
            order=1,
        )
    )

    tutorials.append(
        Tutorial(
            name="Sam Buchanan",
            role="Research Assistant Professor",
            website="https://sdbuchanan.com",
            affiliation="TTIC",
            photo="sdb.jpg",
            tutorial='"White-Box Transformers via Sparse Rate Reduction"',
            abstract='"We demonstrate how combining sparse coding and rate reduction yields sparse linear discriminative representations using an objective named “sparse rate reduction”. We develop CRATE, a deep network architecture, by unrolling the optimization of this objective and parameterizing feature distribution in each layer. CRATE’s operators are mathematically interpretable, with each layer representing an optimization step, making the network a transparent “white box”. Although CRATE’s design significantly differs from ReduNet, both aim for a similar goal, showcasing the versatility of the unrolled optimization approach. Remarkably, CRATE closely resembles the transformer architecture, suggesting that the interpretability gains from such networks might also improve our understanding of current, practical deep architectures."',
            track=1,
            order=2,
        )
    )

    tutorials.append(
        Tutorial(
            name="Zhihui Zhu",
            role="Assistant Professor",
            website="https://zhihuizhu.github.io",
            affiliation="Ohio State University",
            photo="zz.jpeg",
            tutorial='"Understanding Deep Representation Learning via Neural Collapse"',
            abstract='"The session focuses on the strong conceptual connections between low-dimensional structures and deep models in terms of learned representation. We start with the introduction of an intriguing Neural Collapse phenomenon in the last-layer representation and its universality in deep network, and lays out the mathematical foundations of understanding its cause by studying its optimization landscapes. We then generalize and explain this phenomenon and its implications under data imbalanceness. Furthermore, we demonstrate the practical algorithmic implications of Neural Collapse on training deep neural networks."',
            track=1,
            order=3,
        )
    )

    tutorials.append(
        Tutorial(
            name="Qing Qu",
            role="Assistant Professor",
            website="https://qingqu.engin.umich.edu/",
            affiliation="University of Michigan",
            photo="qq.jpeg",
            tutorial='"Invariant Low-Dimensional Subspaces in Gradient Descent for Learning Deep Networks"',
            abstract='"To conclude, we show that low-dimensional structures also emerge in training dynamics of deep networks. Specifically, we show that the evolution of gradient descent only affects a minimal portion of singular vector spaces across all weight matrices. The analysis enables us to considerably improve training efficiency by taking advantage of the low-dimensional structure in learning dynamics. We can construct smaller, equivalent deep linear networks without sacrificing the benefits associated with the wider counterparts. Moreover, it allows us to better understand deep representation learning by elucidating the progressive feature compression and discrimination from shallow to deep layers."',
            track=1,
            order=4,
        )
    )

    # Track 2
    tutorials.append(
        Tutorial(
            name="Saiprasad Ravishankar",
            role="Assistant Professor",
            website="https://sites.google.com/site/sairavishankar3/",
            affiliation="Michigan State University",
            photo="ravishankar.jpg",
            tutorial='"Sparse Modeling for Image Reconstruction"',
            abstract='"Data-driven and machine learning techniques have received increasing attention in recent years for solving various problems in computational imaging. First, we will introduce basics of image reconstruction and sparse modeling before discussing the learning of various classical sparse signal models, particularly synthesis dictionaries and sparsifying transforms. The application of dictionary and transform learning to primarily medical image reconstruction will be discussed. We will also briefly discuss the combination of sparsity with other priors (e.g., low-rank) and variants such as convolutional dictionary learning and multi-layer sparse models used in image reconstruction.<br><em>Time: 50 minutes</em>"',
            track=2,
            order=1,
        )
    )

    tutorials.append(
        Tutorial(
            name="Bihan Wen",
            role="Nanyang Assistant Professor",
            website="https://personal.ntu.edu.sg/bihan.wen/",
            affiliation="Nanyang Technological University",
            photo="wen.jpeg",
            tutorial='"Sparse Modeling to Deep Learning for Image Restoration"',
            abstract='"The second talk will focus more on integration of learned sparsity and nonlocal image modeling via group sparsity, low-rank structures, etc. Applications will be shown for image restoration and medical imaging. This part will also transition to aspects of deep learning for image restoration and offer several examples. How deep learning can be combined with conventional model-based approaches will also be touched upon.<br><em>Time: 50 minutes</em>"',
            track=2,
            order=2,
        )
    )

    tutorials.append(
        Tutorial(
            name="Saiprasad Ravishankar",
            role="Assistant Professor",
            website="https://sites.google.com/site/sairavishankar3/",
            affiliation="Michigan State University",
            photo="ravishankar.jpg",
            tutorial='"Deep Learning for Imaging"',
            abstract="",
            track=2,
            order=3,
        )
    )

    tutorials.append(
        Tutorial(
            name="Ismail Alkhouri",
            role="Postdoc / Visiting Scholar",
            website="https://sites.google.com/view/ismailalkhouri/about",
            affiliation="Michigan State University / University of Michigan, Ann Arbor",
            photo="ismail.jpg",
            tutorial="",
            abstract="",
            track=2,
            order=4,
        )
    )

    tutorials.append(
        Tutorial(
            name="Avrajit Ghosh",
            role="Ph.D. Student",
            website="https://sites.google.com/view/avrajitghosh",
            affiliation="Michigan State University",
            photo="ghosh.png",
            tutorial="",
            abstract="",
            track=2,
            order=5,
        )
    )

    tutorials.append(
        Tutorial(
            name="Gabriel Maliakal",
            role="Ph.D. Student",
            affiliation="Michigan State University",
            photo="maliakal.png",
            tutorial="",
            abstract='"We will introduce modern deep learning-based methods for image reconstruction, particularly in medical imaging, including image-domain or sensor-domain neural network denoisers, and hybrid-domain deep learning schemes that combine physics-based forward models together with neural networks. Hybrid methods, both supervised and unsupervised or self-supervised, will be a key focus and amongst them, we will review plug and play (PnP) priors, consensus equilibrium, regularization by denoising (RED), deep unrolling methods, deep equilibrium models, and bilevel optimization based methods. Then, generative models for image reconstruction will be presented including generative adversarial networks (GANs), deep image prior, and diffusion models (DMs). We will provide a brief introduction to score-based DMs and introduce Diffusion Posterior Sampling ReSample algorithms. Other recent trends in image reconstruction will also be covered including exploiting deep reinforcement learning, unifying deep learning and sparse modeling, and methods focused on improving robustness of deep learning based image reconstruction (to various perturbations, train-test disparities, etc.) via randomized smoothing, diffusion models, etc. Other topics will also be covered briefly including learning sparse neural networks and joint or end-to-end training of sensing and image reconstruction setups. The session will conclude with brief discussion of future directions for the field.<br><br> Lecture 3 will involve multiple speakers covering different themes. Avrajit Ghosh will present many of the hybrid or physics-based deep learning methods. Dr. Ismail Alkhouri will speak on key ideas involving diffusion models. Gabriel Maliakal will discuss GANs and deep reinforcement learning and Dr. Saiprasad Ravishankar will speak on the key other topics.<br><br><em>Time: 140--150 minutes (coffee break in between)</em>"',
            track=2,
            order=6,
        )
    )

    return tutorials


def make_organizers():
    organizers = []

    # organizers.append(
    #     Organizer(
    #         name="Dan Alistarh",
    #         role="Industry Liaison Chair",
    #         website="https://people.csail.mit.edu/alistarh/",
    #         affiliation="IST Austria / Neural Magic",
    #         photo="alistarh.jpeg",
    #     )
    # )

    # organizers.append(
    #     Organizer(
    #         name="Chenglong Bao",
    #         role="Area Chair",
    #         website="https://matbc.github.io/",
    #         affiliation="Tsinghua University",
    #         photo="bao.jpeg",
    #     )
    # )

    organizers.append(
        Organizer(
            name="Babak Ehteshami Bejnordi",
            role="Industry Liaison Chair",
            website="http://babakint.com/",
            affiliation="Qualcomm",
            photo="bejnordi.jpeg",
        )
    )

    organizers.append(
        Organizer(
            name="Sam Buchanan",
            role="Web Chair",
            website="https://sdbuchanan.com/",
            affiliation="TTIC",
            photo="sdb.jpg",
        )
    )

    organizers.append(
        Organizer(
            name="Beidi Chen",
            role="Program Chair",
            website="https://www.andrew.cmu.edu/user/beidic/",
            affiliation="Carnegie Mellon University",
            photo="chen0.jpeg",
        )
    )

    organizers.append(
        Organizer(
            name="Tianlong Chen",
            role="Area Chair",
            website="https://tianlong-chen.github.io/",
            affiliation="UNC Chapel Hill",
            photo="chen_t.jpeg",
        )
    )

    # organizers.append(
    #     Organizer(
    #         name="Yubei Chen",
    #         role="Area Chair",
    #         website="https://yubeichen.com",
    #         affiliation="UC Davis",
    #         photo="chen_yubei.jpeg",
    #     )
    # )

    organizers.append(
        Organizer(
            name="Yubei Chen",
            role="Local Chair",
            website="https://yubeichen.com",
            affiliation="UC Davis",
            photo="chen_yubei.jpeg",
        )
    )

    organizers.append(
        Organizer(
            name="Sara Fridovich-Keil",
            role="Local Chair",
            website="https://sarafridov.github.io/",
            affiliation="Stanford / Georgia Tech",
            photo="sarafk.jpeg",
        )
    )

    organizers.append(
        Organizer(
            name="Sheng Liu",
            role="Local Chair",
            website="https://shengliu66.github.io/",
            affiliation="Stanford",
            photo="shliu.png",
        )
    )

    # organizers.append(
    #     Organizer(
    #         name="Yuxin Chen",
    #         role="Area Chair",
    #         website="https://yuxinchen2020.github.io/",
    #         affiliation="UPenn",
    #         photo="chen_yuxin.jpeg",
    #     )
    # )

    # organizers.append(
    #     Organizer(
    #         name="Yuejie Chi",
    #         role="Program Chair",
    #         website="https://users.ece.cmu.edu/~yuejiec/",
    #         affiliation="Carnegie Mellon University",
    #         photo="yc.jpeg",
    #     )
    # )

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
            name="Ivan Dokmanić",
            role="Area Chair",
            website="https://dmi.unibas.ch/en/persons/dokmanic-ivan/",
            affiliation="University of Basel",
            photo="dokmanic.jpeg",
        )
    )

    # organizers.append(
    #     Organizer(
    #         name="Simon Du",
    #         role="Area Chair",
    #         website="https://simonshaoleidu.com/",
    #         affiliation="University of Washington",
    #         photo="du.jpeg",
    #     )
    # )

    # organizers.append(
    #     Organizer(
    #         name="Gintare Karolina Dziugaite",
    #         role="Program Chair",
    #         website="https://gkdz.org/",
    #         affiliation="Google DeepMind",
    #         photo="gintare.jpeg",
    #     )
    # )

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
            name="Utku Evci",
            role="Industry Liaison Chair",
            website="https://research.google/people/utkuevci/",
            affiliation="Google DeepMind",
            photo="evci.jpeg",
        )
    )

    # organizers.append(
    #     Organizer(
    #         name="Yani Ioannou",
    #         role="Publicity Chair",
    #         website="https://yani.ai/",
    #         affiliation="University of Calgary",
    #         photo="ioannou.jpeg",
    #     )
    # )

    organizers.append(
        Organizer(
            name="Souvik Kundu",
            role="Industry Liaison Chair",
            website="https://ksouvik52.github.io/",
            affiliation="Intel Labs, USA",
            photo="kundu.jpeg",
        )
    )

    # organizers.append(
    #     Organizer(
    #         name="Gitta Kutyniok",
    #         role="General Chair",
    #         website="https://www.ai.math.uni-muenchen.de/members/professor/kutyniok/index.html",
    #         affiliation="LMU Munich",
    #         photo="kutyniok.jpg",
    #     )
    # )

    # organizers.append(
    #     Organizer(
    #         name="Qi Lei",
    #         role="Area Chair",
    #         website="https://cecilialeiqi.github.io/",
    #         affiliation="NYU",
    #         photo="lei0.jpeg",
    #     )
    # )

    organizers.append(
        Organizer(
            name="Qi Lei",
            role="Publicity Chair",
            website="https://cecilialeiqi.github.io/",
            affiliation="NYU",
            photo="lei0.jpeg",
        )
    )

    organizers.append(
        Organizer(
            name="Xiao Li",
            role="Area Chair",
            website="https://www.xiao-li.org/",
            affiliation="CUHK Shenzhen",
            photo="li.png",
        )
    )

    organizers.append(
        Organizer(
            name="Sijia Liu",
            role="Program Chair",
            website="https://lsjxjtu.github.io/",
            affiliation="Michigan State University",
            photo="liu.png",
        )
    )

    organizers.append(
        Organizer(
            name="Yi Ma",
            role="General Chair",
            website="https://people.eecs.berkeley.edu/~yima/",
            affiliation="UC Berkeley / HKU IDS",
            photo="ma.jpeg",
        )
    )

    organizers.append(
        Organizer(
            name="Yi Ma",
            role="Advisory Committee",
            website="https://people.eecs.berkeley.edu/~yima/",
            affiliation="UC Berkeley / HKU IDS",
            photo="ma.jpeg",
        )
    )

    # organizers.append(
    #     Organizer(
    #         name="Elena Mocanu",
    #         role="Area Chair",
    #         website="https://people.utwente.nl/e.mocanu",
    #         affiliation="University of Twente",
    #         photo="mocanu.jpeg",
    #     )
    # )

    organizers.append(
        Organizer(
            name="Greg Ongie",
            role="Area Chair",
            website="https://gregongie.github.io/",
            affiliation="Marquette University",
            photo="ongie.png",
        )
    )

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
            name="Saiprasad Ravishankar",
            role="Panel Chair",
            website="https://sites.google.com/site/sairavishankar3/",
            affiliation="Michigan State University",
            photo="ravishankar.jpg",
        )
    )

    organizers.append(
        Organizer(
            name="William T. Redman",
            role="Publicity Chair",
            website="https://wredman4.wixsite.com/wtredman",
            affiliation="Johns Hopkins APL",
            photo="redman.jpeg",
        )
    )

    organizers.append(
        Organizer(
            name="Shiwei Liu",
            role="Publicity Chair",
            website="https://shiweiliuiiiiiii.github.io/",
            affiliation="University of Oxford",
            photo="sliu.png",
        )
    )

    organizers.append(
        Organizer(
            name="Liyue Shen",
            role="Rising Stars Award Chair",
            website="https://liyueshen.engin.umich.edu/",
            affiliation="University of Michigan",
            photo="shen-liyue.jpeg",
        )
    )

    # organizers.append(
    #     Organizer(
    #         name="Harry Shum",
    #         role="General Chair",
    #         affiliation="HKUST / IDEA",
    #         photo="shum.jpeg",
    #     )
    # )

    organizers.append(
        Organizer(
            name="Stefano Soatto",
            role="Advisory Committee",
            website="https://web.cs.ucla.edu/~soatto/",
            affiliation="UCLA",
            photo="soatto.jpeg",
        )
    )

    # organizers.append(
    #     Organizer(
    #         name="Mahdi Soltanolkotabi",
    #         role="Area Chair",
    #         website="https://viterbi-web.usc.edu/~soltanol/",
    #         affiliation="USC",
    #         photo="soltanolkotabi.jpeg",
    #     )
    # )

    organizers.append(
        Organizer(
            name="Jeremias Sulam",
            role="Program Chair",
            website="https://sites.google.com/view/jsulam",
            affiliation="Johns Hopkins University",
            photo="js.png",
        )
    )

    organizers.append(
        Organizer(
            name="Mert Pilanci",
            role="Program Chair",
            website="https://sites.google.com/view/jsulam",
            affiliation="Stanford",
            photo="mp.jpeg",
        )
    )

    # organizers.append(
    #     Organizer(
    #         name="René Vidal",
    #         role="General Chair",
    #         website="http://vision.jhu.edu/rvidal.html",
    #         affiliation="UPenn",
    #         photo="vidal.jpeg",
    #     )
    # )

    organizers.append(
        Organizer(
            name="Atlas Wang",
            role="Senior Advisor to PCs",
            website="https://vita-group.github.io/",
            affiliation="UT Austin",
            photo="aw.png",
        )
    )

    # organizers.append(
    #     Organizer(
    #         name="Dilin Wang",
    #         role="Industry Liaison Chair",
    #         website="https://research.facebook.com/people/wang-dilin/",
    #         affiliation="Meta",
    #         photo="wangd.jpeg",
    #     )
    # )

    organizers.append(
        Organizer(
            name="Peng Wang",
            role="Area Chair",
            website="https://peng8wang.github.io/",
            affiliation="University of Michigan",
            photo="wangp.jpeg",
        )
    )

    organizers.append(
        Organizer(
            name="Yu-Xiang Wang",
            role="Program Chair",
            website="https://cseweb.ucsd.edu/~yuxiangw/",
            affiliation="UC San Diego",
            photo="wang.jpeg",
        )
    )

    # organizers.append(
    #     Organizer(
    #         name="Bihan Wen",
    #         role="Area Chair",
    #         website="https://personal.ntu.edu.sg/bihan.wen/",
    #         affiliation="Nanyang Technological University",
    #         photo="wen.jpeg",
    #     )
    # )

    organizers.append(
        Organizer(
            name="Rebecca Willett",
            role="Advisory Committee",
            website="https://willett.psd.uchicago.edu/",
            affiliation="UChicago",
            photo="willett.jpeg",
        )
    )

    # organizers.append(
    #     Organizer(
    #         name="John Wright",
    #         role="Tutorial Chair",
    #         website="http://www.columbia.edu/~jw2966/",
    #         affiliation="Columbia University",
    #         photo="jw.jpg",
    #     )
    # )

    organizers.append(
        Organizer(
            name="Eric P. Xing",
            role="Advisory Committee",
            website="https://www.cs.cmu.edu/~epxing/",
            affiliation="MBZUAI / Carnegie Mellon University",
            photo="ex.jpeg",
        )
    )

    # organizers.append(
    #     Organizer(
    #         name="Yanchao Yang",
    #         role="Local Chair",
    #         website="https://yanchaoyang.github.io/",
    #         affiliation="HKU",
    #         photo="yyang.jpeg",
    #     )
    # )

    # organizers.append(
    #     Organizer(
    #         name="Fanny Yang",
    #         role="Area Chair",
    #         website="https://sml.inf.ethz.ch/group/fannyy/",
    #         affiliation="ETH Zurich",
    #         photo="yang.png",
    #     )
    # )

    organizers.append(
        Organizer(
            name="Chong You",
            role="Tutorial Chair",
            website="https://sites.google.com/view/cyou",
            affiliation="Google Research",
            photo="cy.jpeg",
        )
    )

    # organizers.append(
    #     Organizer(
    #         name="Man-Chung Yue",
    #         role="Local Chair",
    #         website="https://manchungyue.com/",
    #         affiliation="HKU",
    #         photo="ymc.jpeg",
    #     )
    # )

    # organizers.append(
    #     Organizer(
    #         name="Yuqian Zhang",
    #         role="Area Chair",
    #         website="https://sites.google.com/view/yuqianzhang",
    #         affiliation="Rutgers University",
    #         photo="yz.jpg",
    #     )
    # )

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
            name="Zhihui Zhu",
            role="Publication Chair",
            website="https://zhihuizhu.github.io",
            affiliation="Ohio State University",
            photo="zz.jpeg",
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

    # organizers.append(
    #     Organizer(
    #         name="Tianbao Yang",
    #         role="Area Chair",
    #         website="https://people.tamu.edu/~tianbao-yang/",
    #         affiliation="Texas A&M",
    #         photo="tianbao_yang.jpeg",
    #     )
    # )

    # organizers.append(
    #     Organizer(
    #         name="Jiaqi Ma",
    #         role="Area Chair",
    #         website="https://www.jiaqima.com/",
    #         affiliation="Harvard / UIUC",
    #         photo="jiaqi-ma.jpeg",
    #     )
    # )

    organizers.append(
        Organizer(
            name="Paris Giampouras",
            role="Area Chair",
            website="https://parisgiampouras.github.io/",
            affiliation="University of Warwick",
            photo="giampouras.jpeg",
        )
    )

    organizers.append(
        Organizer(
            name="Emmanuel Candès",
            role="Advisory Committee",
            website="https://candes.su.domains/",
            affiliation="Stanford",
            photo="ecandes.jpeg",
        )
    )

    organizers.append(
        Organizer(
            name="Emmanuel Candès",
            role="General Chair",
            website="https://candes.su.domains/",
            affiliation="Stanford",
            photo="ecandes.jpeg",
        )
    )

    # organizers.append(
    #     Organizer(
    #         name="Weijie Su",
    #         role="Area Chair",
    #         website="http://stat.wharton.upenn.edu/~suw/",
    #         affiliation="UPenn",
    #         photo="su.jpeg",
    #     )
    # )

    organizers.append(
        Organizer(
            name="Weijie Su",
            role="Publication Chair",
            website="http://stat.wharton.upenn.edu/~suw/",
            affiliation="UPenn",
            photo="su.jpeg",
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
            name="Tianyi Chen",
            role="Area Chair",
            website="https://chentianyi1991.github.io/",
            affiliation="RPI",
            photo="tianyi_chen.jpeg",
        )
    )

    # organizers.append(
    #     Organizer(
    #         name="Wei Hu",
    #         role="Area Chair",
    #         website="https://weihu.me/",
    #         affiliation="University of Michigan",
    #         photo="huwei.jpeg",
    #     )
    # )

    organizers.append(
        Organizer(
            name="Navid Azizan",
            role="Area Chair",
            website="https://azizan.mit.edu",
            affiliation="MIT",
            photo="NavidAzizan_c.jpg",
        )
    )

    organizers.append(
        Organizer(
            name="Laixi Shi",
            role="Area Chair",
            website="https://laixishi.github.io/",
            affiliation="Caltech",
            photo="shi.jpeg",
        )
    )

    organizers.append(
        Organizer(
            name="Soledad Villar",
            role="Area Chair",
            website="https://www.ams.jhu.edu/villar/",
            affiliation="Johns Hopkins University",
            photo="villar.jpeg",
        )
    )

    # organizers.append(
    #     Organizer(
    #         name="Sarah Dean",
    #         role="Area Chair",
    #         website="https://sdean.website/",
    #         affiliation="Cornell University",
    #         photo="dean.jpeg",
    #     )
    # )

    organizers.append(
        Organizer(
            name="Wenjing Liao",
            role="Area Chair",
            website="https://wliao60.math.gatech.edu/",
            affiliation="Georgia Institute of Technology",
            photo="liao.jpeg",
        )
    )

    organizers.append(
        Organizer(
            name="Vidya K. Muthukumar",
            role="Area Chair",
            website="https://vmuthukumar.ece.gatech.edu/",
            affiliation="Georgia Institute of Technology",
            photo="muthukumar.jpeg",
        )
    )

    organizers.append(
        Organizer(
            name="Akshay Rangamani",
            role="Area Chair",
            website="https://akshay-r.github.io/",
            affiliation="New Jersey Institute of Technology",
            photo="rangamani.jpeg",
        )
    )

    organizers.append(
        Organizer(
            name="Tomer Galanti",
            role="Area Chair",
            website="https://tomergalanti.github.io/",
            affiliation="Texas A&M University",
            photo="galanti.jpeg",
        )
    )

    return organizers


def make_conference_events():
    conference_events = []

    # # Welcome and Opening Remarks events
    # conference_events.append(
    #     Event(
    #         name="Opening Remarks",
    #         event_class="meta",
    #         day=1,  # Monday March 24th
    #         start="9:00 AM",
    #         end="9:15 AM",
    #         location=day_one_str,
    #     )
    # )

    conference_events.append(
        Event(
            name="Registration and Breakfast",
            event_class="meta",
            day=1,  # Tuesday March 25th
            start="8:00 AM",
            end="9:00 AM",
            location=day_two_str,
        )
    )

    conference_events.append(
        Event(
            name="Registration",
            event_class="meta",
            day=2,  # Tuesday March 25th
            start="8:15 AM",
            end="8:40 AM",
            location=day_two_str,
        )
    )

    conference_events.append(
        Event(
            name="Registration and Breakfast",
            event_class="meta",
            day=3,  # Tuesday March 25th
            start="8:15 AM",
            end="9:00 AM",
            location=day_two_str,
        )
    )

    conference_events.append(
        Event(
            name="Registration and Breakfast",
            event_class="meta",
            day=4,  # Tuesday March 25th
            start="8:15 AM",
            end="9:00 AM",
            location=day_two_str,
        )
    )

    conference_events.append(
        Event(
            name="Opening Remarks",
            event_class="remarks",
            day=2,  # Tuesday March 25th
            start="8:40 AM",
            end="9:00 AM",
            location=day_two_str,
        )
    )

    # Tutorial Sessions
    conference_events.append(
        Event(
            name="Tutorial Session 1<br>T1: Deep Representation Learning: from Knowledge to Intelligence<br>T2: Foundations on Interpretable AI",
            event_class="meta",
            day=1,
            start="9:15 AM",
            end="11:45 AM",
            location="T1 - " + day_two_str + "<br>" + "T2 - " + day_one_str,
        )
    )

    conference_events.append(
        Event(
            name="Tutorial Session 2<br>T3: Methods, Analysis, and Insights from Multimodal LLM Pre-training and Post-training<br>T4: Harnessing Low Dimensionality in Diffusion Models: From Theory to Practice",
            event_class="meta",
            day=1,
            start="1:15 PM",
            end="3:45 PM",
            location="T3 - " + day_two_str + "<br>" + "T4 - " + day_one_str,
        )
    )

    conference_events.append(
        Event(
            name="Tutorial Session 3<br>T5: A Function-Space Tour of Data Science<br>T6: Sparsity and Mixture-of-Experts in the Era of LLMs: A New Odyssey",
            event_class="meta",
            day=1,
            start="4:15 PM",
            end="6:45 PM",
            location="T5 - " + day_two_str + "<br>" + "T6 - " + day_one_str,
        )
    )

    # Highlight Talks
    conference_events.append(
        Event(
            name="Highlight Talks 1",
            event_class="oral",
            day=2,
            start="10:00 AM",
            end="10:30 AM",
            location=day_two_str,
        )
    )

    conference_events.append(
        Event(
            name="Highlight Talks 2",
            event_class="oral",
            day=2,
            start="12:00 PM",
            end="12:30 PM",
            location=day_two_str,
        )
    )

    conference_events.append(
        Event(
            name="Rising Stars Talks 1",
            event_class="rising",
            day=2,
            start="1:30 PM",
            end="2:30 PM",
            location=day_two_str,
        )
    )

    conference_events.append(
        Event(
            name="Rising Stars Talks 2",
            event_class="rising",
            day=3,
            start="1:30 PM",
            end="2:30 PM",
            location=day_two_str,
        )
    )

    conference_events.append(
        Event(
            name="Highlight Talks 4",
            event_class="oral",
            day=4,
            start="10:00 AM",
            end="11:00 AM",
            location=day_two_str,
        )
    )

    conference_events.append(
        Event(
            name="Highlight Talks 3",
            event_class="oral",
            day=2,
            start="4:00 PM",
            end="5:00 PM",
            location=day_two_str,
        )
    )

    conference_events.append(
        Event(
            name="Rising Stars Talks 3",
            event_class="rising",
            day=4,
            start="3:00 PM",
            end="4:00 PM",
            location=day_two_str,
        )
    )

    # Panel event
    conference_events.append(
        Event(
            name="Panel Discussion",
            event_class="meta",
            day=3,
            start="4:00 PM",
            end="4:45 PM",
            location=day_two_str,
        )
    )

    # Wellness Session (replacement for Yoga)
    conference_events.append(
        Event(
            name="Wellness Session",
            event_class="event",
            day=3,
            start="10:00 AM",
            end="11:00 AM",
            location=day_two_str,
        )
    )

    # Closing event
    conference_events.append(
        Event(
            name="Closing Remarks",
            event_class="remarks",
            day=4,
            start="5:00 PM",
            end="5:20 PM",
            location=day_two_str,
        )
    )

    # Poster Sessions
    conference_events.append(
        Event(
            name="Reception + Poster Session 1",
            event_class="poster",
            day=2,
            start="5:00 PM",
            end="6:15 PM",
            location=day_two_str,
        )
    )

    conference_events.append(
        Event(
            name="Poster Session 2",
            event_class="poster",
            day=3,
            start="4:45 PM",
            end="6:15 PM",
            location=day_two_str,
        )
    )

    conference_events.append(
        Event(
            name="Coffee Break + Poster Session 3",
            event_class="poster",
            day=4,
            start="11:00 AM",
            end="12:30 PM",
            location=day_two_str,
        )
    )

    # Coffee Breaks
    conference_events.append(
        Event(
            name="Coffee Break",
            event_class="break",
            day=1,
            start="3:45 PM",
            end="4:15 PM",
            location=day_two_str,
        )
    )

    conference_events.append(
        Event(
            name="Coffee Break",
            event_class="break",
            day=2,
            start="10:30 AM",
            end="11:00 AM",
            location=day_two_str,
        )
    )

    conference_events.append(
        Event(
            name="Coffee Break",
            event_class="break",
            day=2,
            start="2:30 PM",
            end="3:00 PM",
            location=day_two_str,
        )
    )

    conference_events.append(
        Event(
            name="Coffee Break",
            event_class="break",
            day=3,
            start="11:00 AM",
            end="11:30 AM",
            location=day_two_str,
        )
    )

    conference_events.append(
        Event(
            name="Coffee Break",
            event_class="break",
            day=3,
            start="2:30 PM",
            end="3:00 PM",  # Note: This appears to be "3:00 AM" in the PDF but likely means "3:00 PM"
            location=day_two_str,
        )
    )

    conference_events.append(
        Event(
            name="Coffee Break",
            event_class="break",
            day=4,
            start="2:30 PM",
            end="3:00 PM",  # Note: This appears to be "3:00 AM" in the PDF but likely means "3:00 PM"
            location=day_two_str,
        )
    )

    # Lunch Breaks
    conference_events.append(
        Event(
            name="Lunch Break",
            event_class="break",
            day=1,
            start="11:45 AM",
            end="1:15 PM",
            location=day_two_str,
        )
    )

    conference_events.append(
        Event(
            name="Lunch Break",
            event_class="break",
            day=2,
            start="12:30 PM",
            end="1:30 PM",
            location=day_two_str,
        )
    )

    conference_events.append(
        Event(
            name="Lunch Break",
            event_class="break",
            day=3,
            start="12:30 PM",
            end="1:30 PM",
            location=day_two_str,
        )
    )

    conference_events.append(
        Event(
            name="Lunch Break",
            event_class="break",
            day=4,
            start="12:30 PM",
            end="1:30 PM",
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
        name="CPAL-2025",
        start_month="Mar",
        start_day=24,
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


# TODO: For this and the next, we should convert the output dictionaries
# into a 'paper' dataclass (so that we can assign papers to sessions, etc)
def proceedings_to_jekyll():
    """
    Convert dict of accepted proceedings papers (openreview-py) to jekyll YAML
    """
    papers = get_accepted_papers(venue_str="CPAL.cc/2025/Proceedings_Track")
    session_paper_dict = create_session_paper_mapping()
    paper_session_dict = {v.lower(): k for (k, v) in session_paper_dict.items()}
    # Loop over papers, write yaml files
    out_dir = root / "_proceedings"
    out_dir.mkdir(parents=True, exist_ok=True)

    oral_counter = -1
    for paper in papers:
        paper = paper.to_json()
        oral_or_poster = paper["content"]["venue"]["value"].split(" ")[-1].lower()
        title = paper["content"]["title"]["value"]
        assert title.lower() in paper_session_dict.keys()
        if oral_or_poster == "oral":
            oral_counter += 1
        out = {
            "title": title,
            "authors": ", ".join(paper["content"]["authors"]["value"]),
            "link": "https://openreview.net/forum?id=" + paper["id"],
            "keywords": ", ".join(paper["content"]["keywords"]["value"]),
            "type": oral_or_poster,
            "session": paper_session_dict[title.lower()][0],
            "num": paper_session_dict[title.lower()][1],
            "oral_session": (oral_counter % 3) + 1,
        }
        out_fn = paper["id"] + ".md"
        out_path = out_dir / out_fn
        # Dump output
        with out_path.open(mode="w", encoding="utf-8") as f:
            f.write("---\n")
            f.write(yaml.dump(out))
            f.write("---\n")


def spotlight_to_jekyll():
    """
    Convert dict of accepted spotlight papers (openreview-py) to jekyll YAML
    """
    papers = get_accepted_papers(venue_str="CPAL.cc/2025/Recent_Spotlight_Track")
    session_paper_dict = create_session_paper_mapping()
    paper_session_dict = {v.lower(): k for (k, v) in session_paper_dict.items()}
    # Loop over papers, write yaml files
    out_dir = root / "_spotlight"
    out_dir.mkdir(parents=True, exist_ok=True)
    for paper in papers:
        paper = paper.to_json()
        title = paper["content"]["title"]["value"]
        # assert title.lower() in paper_session_dict.keys()
        if title.lower() not in paper_session_dict.keys():
            breakpoint()
        out = {
            "title": title,
            "authors": ", ".join(paper["content"]["authors"]["value"]),
            "link": "https://openreview.net/forum?id=" + paper["id"],
            "keywords": ", ".join(paper["content"]["keywords"]["value"]),
            "type": "poster",
            "session": paper_session_dict[title.lower()][0],
            "num": paper_session_dict[title.lower()][1],
        }
        out_fn = paper["id"] + ".md"
        out_path = out_dir / out_fn
        # Dump output
        with out_path.open(mode="w", encoding="utf-8") as f:
            f.write("---\n")
            f.write(yaml.dump(out))
            f.write("---\n")


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
    description="Create and export database properties for CPAL 2025."
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
    help="Export Spotlight Proceedings Track YAML info",
)
parser.add_argument(
    "--calendar",
    dest="do_list",
    action="append_const",
    const=create_and_export_calendar,
    help="Create and export event calendar",
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
