#!/usr/bin/env python
# -*- coding: utf-8 -*-

# We do data input in this file, essentially.

# imports
import argparse
from pathlib import Path

import yaml

from event import Event
from papers import get_accepted_papers
from program import Calendar
from roles import Organizer, RisingStar, Speaker, Tutorial

# this is the root directory of the jekyll site
# exports will go there
root = Path(__file__).parent.parent.parent

# variables for location strings
day_one_str = '<a href="/venue/#day-1-venue-rayson-huang-theatre-hku">Rayson Huang Theatre</a>'
day_two_str = '<a href="/venue/#days-24-venue-lecture-hall-ii-cpd-lg07-10-lg-centennial-campus-hku">Lee Shau Kee Lecture Ctr.</a>'
banquet_str = '<a href="/social/#dinner-banquet-january-4th-2024">Maxim’s Palace Chinese Restaurant, 2/F, City Hall, 5-7 Edinburgh Place, Central</a>'
tram_str = '<a href="/social/#tram-party-january-5th-2024">Whitty Street Tram Depot</a>'

# Speaker photos should close to 1.33 : 1 aspect (height : width)

# Organizer photos should be close to 1:1 aspect

# Rising Stars photos should be close to 1:1 aspect


def make_risingstars():
    risingstars = []

    risingstars.append(
        RisingStar(
            name="Rahul Parhi",
            role="Postdoctoral Researcher",
            website="https://rahul.sh/",
            affiliation="École Polytechnique Fédérale de Lausanne",
            photo="parhi.jpg",
            session=2,
            order=2,
            talk="On the Sparsity-Promoting Effect of Weight Decay in Deep Learning",
            abstract="Deep learning has been wildly successful in practice and most state-of-the-art artificial intelligence systems are based on neural networks. Lacking, however, is a rigorous mathematical theory that adequately explains the amazing performance of deep neural networks. In this talk, I present a new mathematical framework that provides the beginning of a deeper understanding of deep learning. This framework precisely characterizes the functional properties of trained neural networks through the lens of sparsity. The key mathematical tools which support this framework include transform-domain sparse regularization, the Radon transform of computed tomography, and approximation theory. This framework explains the effect of weight decay regularization in neural network training, the importance of skip connections and low-rank weight matrices in network architectures, the role of sparsity in neural networks, and explains why neural networks can perform well in high-dimensional problems.",
        )
    )

    risingstars.append(
        RisingStar(
            name="Daniel Paul Kunin",
            role="Ph.D. Student",
            website="https://daniel-kunin.com/",
            affiliation="Stanford University",
            photo="kunin.png",
            session=1,
            order=1,
            talk='"Stochastic Collapse: How Gradient Noise Attracts SGD Dynamics Towards Simpler Subnetworks"',
            abstract='"In this work, we reveal a strong implicit bias of stochastic gradient descent (SGD) that drives overly expressive networks to much simpler subnetworks, thereby dramatically reducing the number of independent parameters, and improving generalization. To reveal this bias, we identify invariant sets, or subsets of parameter space that remain unmodified by SGD. We focus on two classes of invariant sets that correspond to simpler (sparse or low-rank) subnetworks and commonly appear in modern architectures. Our analysis uncovers that SGD exhibits a property of stochastic attractivity towards these simpler invariant sets. We establish a sufficient condition for stochastic attractivity based on a competition between the loss landscape’s curvature around the invariant set and the noise introduced by stochastic gradients. Remarkably, we find that an increased level of noise strengthens attractivity, leading to the emergence of attractive invariant sets associated with saddle-points or local maxima of the train loss. We observe empirically the existence of attractive invariant sets in trained deep neural networks, implying that SGD dynamics often collapses to simple subnetworks with either vanishing or redundant neurons. We further demonstrate how this simplifying process of stochastic collapse benefits generalization in a linear teacher-student framework. Finally, through this analysis, we mechanistically explain why early training with large learning rates for extended periods benefits subsequent generalization."',
        )
    )

    risingstars.append(
        RisingStar(
            name="Bahareh Tolooshams",
            role="Postdoctoral Researcher",
            website="https://btolooshams.github.io/",
            affiliation="California Institute of Technology",
            photo="tolooshams.png",
            session=3,
            order=3,
            talk='"Deep Interpretable Generative Learning for Science and Engineering"',
            abstract='"Discriminative and generative AI are two deep learning paradigms that revolutionized prediction and generation of high-quality images from text prompts. Nonetheless, discriminative learning is unable to generate data, and deep generative models struggle with decoding capabilities. Moreover, both approaches are data-hungry and have low interpretability. These drawbacks have posed significant barriers to the adoption of deep learning in applications where a) acquiring supervised data is expensive or infeasible, and b) goals extend beyond data fitting to attain scientific insights. Furthermore, deep learning applications are fairly unexplored in fields with rich mathematical and optimization frameworks such as inverse problems, or those in which interpretability matters. This talk discusses the theory and applications of deep learning in data-limited or unsupervised inverse problems. These include applications in radar sensing, Poisson image denoising, and computational neuroscience."',
        )
    )

    risingstars.append(
        RisingStar(
            name="Ravid Shwartz Ziv",
            role="CDS Faculty Fellow",
            website="https://www.ravid-shwartz-ziv.com/",
            affiliation="New York University",
            photo="ziv.png",
            session=3,
            order=4,
            talk='"Decoding the Information Bottleneck in Self-Supervised Learning: Pathway to Optimal Representation"',
            abstract='"Deep Neural Networks (DNNs) have excelled in many fields, largely due to their proficiency in supervised learning tasks. However, the dependence on vast labeled data becomes a constraint when such data is scarce. Self-Supervised Learning (SSL), a promising approach, harnesses unlabeled data to derive meaningful representations. Yet, how SSL filters irrelevant information without explicit labels remains unclear. In this talk, we aim to unravel the enigma of SSL using the lens of Information Theory, with a spotlight on the Information Bottleneck principle. This principle, while providing a sound understanding of the balance between compressing and preserving relevant features in supervised learning, presents a puzzle when applied to SSL due to the absence of labels during training. We will delve into the concept of ‘optimal representation’ in SSL, its relationship with data augmentations, optimization methods, and downstream tasks, and how SSL training learns and achieves optimal representations. Our discussion unveils our pioneering discoveries, demonstrating how SSL training naturally leads to the creation of optimal, compact representations that correlate with semantic labels. Remarkably, SSL seems to orchestrate an alignment of learned representations with semantic classes across multiple hierarchical levels, an alignment that intensifies during training and grows more defined deeper into the network. Considering these insights and their implications for class set performance, we conclude our talk by applying our analysis to devise more robust SSL-based information algorithms. These enhancements in transfer learning could lead to more efficient learning systems, particularly in data-scarce environments."',
        )
    )

    risingstars.append(
        RisingStar(
            name="Peng Wang",
            role="Postdoctoral Researcher",
            website="https://peng8wang.github.io/",
            affiliation="University of Michigan",
            photo="wangp.jpeg",
            session=1,
            order=3,
            talk='"Understanding Hierarchical Representations in Deep Networks via Intermediate Features"',
            abstract='"Over the past decade, deep learning has proven to be a highly effective method for learning meaningful features from raw data. This work attempts to unveil the mystery of hierarchical feature learning in deep networks. Specifically, in the context of multi-class classification problems, we explore how deep networks transform input data by investigating the output (i.e., features) of each layer after training. Towards this goal, we first define metrics for within-class compression and between-class discrimination of intermediate features, respectively. Through an analysis of these two metrics, we show that the evolution of features follows a simple and quantitative law from shallow to deep layers: Each layer of linear networks progressively compresses within-class features at a linear rate and discriminates between-class features at a sublinear rate. To the best of our knowledge, this is the first quantitative characterization of feature evolution in hierarchical representations of deep networks. Moreover, our extensive experiments validate our theoretical findings numerically."',
        )
    )

    risingstars.append(
        RisingStar(
            name="Lijun Ding",
            role="IFDS Postdoctoral Researcher",
            website="https://www.lijunding.net/",
            affiliation="University of Wisconsin / University of Washington",
            photo="ding.jpg",
            session=3,
            order=1,
            talk='"Optimization for statistical learning with low dimensional structure:  regularity and conditioning"',
            abstract='"Many statistical machine learning problems, where one aims to recover an underlying low-dimensional signal, are based on optimization. Existing work often overlooked the computational complexity in solving the optimization problem, or required case-specific algorithm and analysis -- especially for nonconvex problems. This talk addresses the above two issues from a unified perspective of conditioning. In particular, we show that once the sample size exceeds the intrinsic dimension, (1) a broad class of convex and nonsmooth nonconvex problems are well-conditioned, (2) well conditioning in turn ensures the efficiency of out-of-box optimization methods and inspires new algorithms. Lastly, we show that a conditioning notion called flatness leads to accurate recovery in overparametrized models."',
        )
    )

    risingstars.append(
        RisingStar(
            name="Shuang Li",
            role="Assistant Professor",
            website="https://www.ece.iastate.edu/~lishuang/",
            affiliation="Iowa State University",
            photo="li.jpg",
            session=3,
            order=2,
            talk='"The Future Geometric Analysis of Optimization Problems in Signal Processing and Machine Learning"',
            abstract='"High-dimensional data analysis and estimation appear in many signal processing and machine learning applications. The underlying low-dimensional structure in these high-dimensional data inspires us to develop optimality guarantees as well as optimization-based techniques for the fundamental problems in signal processing and machine learning. In recent years, non-convex optimization widely appears in engineering and is solved by many heuristic local algorithms, but lacks global guarantees. The recent geometric/landscape analysis provides a way to determine whether an iterative algorithm can reach global optimality. The landscape of empirical risk has been widely studied in a series of machine learning problems, including low-rank matrix factorization, matrix sensing, matrix completion, and phase retrieval. A favorable geometry guarantees that many algorithms can avoid saddle points and converge to local minima. In this presentation, I will discuss potential directions for the future geometric analysis of optimization problems in signal processing and machine learning."',
        )
    )

    risingstars.append(
        RisingStar(
            name="Daniel LeJeune",
            role="Postdoctoral Researcher",
            website="https://dlej.net/",
            affiliation="Stanford University",
            photo="lejeune.png",
            session=1,
            order=4,
            talk='"Emergent properties of heuristics in machine learning"',
            abstract='"Successful methods in modern machine learning practice are built on solid intuition and theoretical insight by their designers, but are often ultimately heuristic and exhibit unintended emergent behaviors. Sometimes these emergent behaviors are detrimental, but surprisingly, many provide unexpected desirable benefits. By theoretically characterizing these emergent behaviors, we can develop a more robust methods development process, where more and more of these desirable behaviors can be included by design and leveraged in powerful ways. I will discuss several examples of heuristics and emergent behavior: subsampling and sketching in linear regression and their equivalence to ridge regularization; empirical risk minimization and the universality of relative performances under distribution shifts; and adaptivity in dropout and feature learning models which are equivalent to parsimony-promoting sparse or low-rank regularization."',
        )
    )

    risingstars.append(
        RisingStar(
            name="Shiwei Liu",
            role="IFML Postdoctoral Researcher",
            website="https://shiweiliuiiiiiii.github.io/",
            affiliation="University of Texas at Austin / Eindhoven University of Technology / University of Oxford",
            photo="liu.png",
            session=2,
            order=3,
            talk='"Sparsity in Neural Networks: Science and Practice"',
            abstract='"Sparsity has demonstrated its remarkable performance in the realm of model compression through the selectively eliminating a large portion of model parameters. Nevertheless, conventional methods to discover strong sparse neural networks often necessitate the training of an over-parameterized dense model, followed by iterative cycles of pruning and re-training. As the size of modern neural networks exponentially increases, the costs of dense pre-training and updates have become increasingly prohibitive. In this talk, I will introduce an approach that enables the training of sparse neural networks from scratch, without the need for any pre-training steps or dense updates. By achieving the property of over-parameterization in time, our approach demonstrates the capacity to achieve performance levels equivalent to fully dense networks while utilizing only a very small fraction of weights. Beyond the advantages in model compression, I will also elucidate a broader spectrum of benefits of sparsity in neural networks including scalability, robustness, and fairness, and great potentials build large-scale responsible AI."',
        )
    )

    risingstars.append(
        RisingStar(
            name="Yaodong Yu",
            role="Ph.D. Student",
            website="https://yaodongyu.github.io/",
            affiliation="University of California, Berkeley",
            photo="yu.jpg",
            session=1,
            order=2,
            talk='"White-Box Transformers via Sparse Rate Reduction"',
            abstract='"In this talk, I will present the white-box transformer --- CRATE (i.e., Coding RAte reduction TransformEr). We contend that the objective of representation learning is to compress and transform the distribution of the data, say sets of tokens, towards a mixture of low-dimensional Gaussian distributions supported on incoherent subspaces. The quality of the final representation can be measured by a unified objective function called sparse rate reduction. From this perspective, popular deep networks such as transformers can be naturally viewed as realizing iterative schemes to optimize this objective incrementally. Particularly, we show that the standard transformer block can be derived from alternating optimization on complementary parts of this objective: the multi-head self-attention operator can be viewed as a gradient descent step to compress the token sets by minimizing lossy coding rate. This leads to a family of white-box transformer architectures which are mathematically interpretable. Our experiments show that these networks indeed learn to optimize the designed objective: they compress and sparsify representations of large-scale real-world vision datasets such as ImageNet, and achieve performance very close to thoroughly engineered transformers (ViTs). I will also present some recent theoretical and empirical results of CRATE on emergence behavior, language modeling, and auto-encoding."',
        )
    )

    risingstars.append(
        RisingStar(
            name="Ambar Pal",
            role="Ph.D. Student",
            website="https://www.cis.jhu.edu/~ambar/",
            affiliation="Johns Hopkins University",
            photo="pal.png",
            session=1,
            order=5,
            talk='"The Role of Parsimonious Structures in Data for Trustworthy Machine Learning"',
            abstract='"This talk overviews recent theoretical results in the geometric foundations of adversarially robust machine learning. Modern ML classifiers can fail spectacularly when subject to specially crafted input-perturbations, called adversarial examples. On the other hand, we humans are quite robust for several tasks involving vision. Motivated by this disconnect, in the first part of this talk we will take a deeper dive into the question of when exactly we can avoid adversarial examples. We will see that a key geometric property of the data-distribution — concentration on small-volume subsets of the input space — characterizes whether any robust classifier exists. In particular, this suggests that natural image distributions are concentrated. In the second part of this talk, we will empirically instantiate these results for a few concentrated data-distributions, and discover that utilizing such structure in data leads to classifiers that enjoy better provable robustness guarantees in several regimes. This talk is based on work at NeurIPS ’23, ’20 and TMLR ’23."',
        )
    )

    risingstars.append(
        RisingStar(
            name="Hongyi Wang",
            role="Senior Project Scientist",
            website="https://hwang595.github.io/",
            affiliation="Carnegie Mellon University",
            photo="wangh.png",
            session=3,
            order=5,
            talk='"Speeding up Large-Scale Machine Learning Model Development Using Low-Rank Models and Gradients"',
            abstract='"Large-scale machine learning (ML) models, such as GPT-4 and Llama2, are at the forefront of advances in the field of AI. Nonetheless, developing these large-scale ML models demands substantial computational resources and a deep understanding of distributed ML and systems. In this presentation, I will introduce three frameworks, namely ATOMO, Pufferfish, and Cuttlefish, which use low-rank approximations on model gradients and model weights to significantly expedite ML model training. ATOMO is a general compression framework that has experimentally established that using low-rank gradients, as opposed to sparse ones, can lead to substantially faster distributed training. Pufferfish further bypasses the cost of compression by directly training low-rank models. However, directly training low-rank models usually leads to a loss in accuracy. Pufferfish mitigates this issue by training a full-rank model and then converting to a low-rank model early in the training process. Nonetheless, Pufferfish necessitates extra hyperparameter tuning, such as determining the optimal transition time from full-rank to low-rank. Cuttlefish addresses this issue by automatically estimating and adjusting these hyperparameters during training. I will present extensive experimental results on the distributed training of large-scale ML models, including LLMs, to demonstrate the efficacy of these frameworks."',
        )
    )

    risingstars.append(
        RisingStar(
            name="Yiping Lu",
            role="Courant Instructor",
            website="https://2prime.github.io/",
            affiliation="New York University",
            photo="lu.png",
            session=3,
            order=6,
            talk='"Simulation-Calibrated Scientific Machine Learning"',
            abstract='"Machine learning (ML) has achieved great success in a variety of applications suggesting a new way to build flexible, universal, and efficient approximators for complex high-dimensional data.  These successes have inspired many researchers to apply ML to other scientific applications such as industrial engineering, scientific computing, and operational research, where similar challenges often occur. However, the luminous success of ML is overshadowed by persistent concerns that the mathematical theory of large-scale machine learning, especially deep learning, is still lacking and the trained ML predictor is always biased. In this talk, I’ll introduce a novel framework of (S)imulation-(Ca)librated (S)cientific (M)achine (L)earning (SCaSML), which can leverage the structure of physical models to achieve the following goals: 1) make unbiased predictions even based on biased machine learning predictors; 2) beat the curse of dimensionality with an estimator suffers from it. The SCASML paradigm combines a (possibly) biased machine learning algorithm with a de-biasing step design using rigorous numerical analysis and stochastic simulation. Theoretically, I’ll try to understand whether the SCaSML algorithms are optimal and what factors (e.g., smoothness, dimension, and boundness) determine the improvement of the convergence rate. Empirically, I’ll introduce different estimators that enable unbiased and trustworthy estimation for physical quantities with a biased machine learning estimator. Applications include but are not limited to estimating the moment of a function, simulating high-dimensional stochastic processes, uncertainty quantification using bootstrap methods, and randomized linear algebra."',
        )
    )

    risingstars.append(
        RisingStar(
            name="Ramchandran Muthukumar",
            role="Ph.D. Student",
            website="https://ramcha24.github.io/",
            affiliation="Johns Hopkins University",
            photo="muthukumar.png",
            session=2,
            order=1,
            talk='"Sparsity-aware generalization theory for deep neural networks"',
            abstract='"Deep artificial neural networks achieve surprising generalization abilities that remain poorly understood. In this paper, we present a new approach to analyzing generalization for deep feed-forward ReLU networks that takes advantage of the degree of sparsity that is achieved in the hidden layer activations. By developing a framework that accounts for this reduced effective model size for each input sample, we are able to show fundamental trade-offs between sparsity and generalization. Importantly, our results make no strong assumptions about the degree of sparsity achieved by the model, and it improves over recent norm-based approaches. We illustrate our results numerically, demonstrating non-vacuous bounds when coupled with data-dependent priors in specific settings, even in over-parametrized models."',
        )
    )

    risingstars.append(
        RisingStar(
            name="Ningyuan Huang",
            role="Ph.D. Student",
            website="https://nhuang37.github.io/",
            affiliation="Johns Hopkins University",
            photo="huang.png",
            session=2,
            order=5,
            talk='"Approximately Equivariant Graph Networks"',
            abstract='"Graph neural networks (GNNs) are commonly described as being permutation equivariant with respect to node relabeling in the graph. This symmetry of GNNs is often compared to the translation equivariance of Euclidean convolution neural networks (CNNs). However, these two symmetries are fundamentally different: The translation equivariance of CNNs corresponds to active symmetries, whereas the permutation equivariance of GNNs corresponds to passive symmetries. In this talk, we focus on the active symmetries of GNNs, by considering a learning setting where signals are supported on a fixed graph. In this case, the natural symmetries of GNNs are the automorphisms of the graph. Since real-world graphs tend to be asymmetric, we relax the notion of symmetries by formalizing approximate symmetries via graph coarsening. We propose approximately equivariant graph networks to implement these symmetries and investigate the symmetry model selection problem. We theoretically and empirically show a bias-variance tradeoff between the loss in expressivity and the gain in the regularity of the learned estimator, depending on the chosen symmetry group."',
        )
    )

    risingstars.append(
        RisingStar(
            name="Omar Montasser",
            role="FODSI-Simons Postdoctoral Researcher",
            website="https://home.ttic.edu/~omar/",
            affiliation="University of California, Berkeley",
            photo="montasser.png",
            session=2,
            order=4,
            talk='"Theoretical Foundations of Adversarially Robust Learning"',
            abstract='"Despite extraordinary progress, current machine learning systems have been shown to be brittle against adversarial examples: seemingly innocuous but carefully crafted perturbations of test examples that cause machine learning predictors to misclassify. Can we learn predictors robust to adversarial examples? and how? There has been much empirical interest in this major challenge in machine learning, and in this talk, we will present a theoretical perspective. We will illustrate the need to go beyond traditional approaches and principles, such as empirical (robust) risk minimization, and present new algorithmic ideas with stronger robust learning guarantees."',
        )
    )

    return risingstars


def make_speakers():
    speakers = []

    speakers.append(
        Speaker(
            name="Dan Alistarh",
            role="Speaker",
            website="https://people.csail.mit.edu/alistarh/",
            affiliation="Institute of Science and Technology Austria / Neural Magic",
            photo="alistarh.jpeg",
            talk='"Accurate Model Compression at GPT Scale"',
            abstract='"A key barrier to the wide deployment of highly-accurate machine learning models, whether for language or vision, is their high computational and memory overhead. Although we possess the mathematical tools for highly-accurate compression of such models, these theoretically-elegant techniques require second-order information of the model’s loss function, which is hard to even approximate efficiently at the scale of billion-parameter models.In this talk, I will describe our work on bridging this computational divide, which enables the accurate second-order pruning and quantization of models at truly massive scale. Compressed using our techniques, models with billions and even trillions of parameters can be executed efficiently on a few GPUs, with significant speedups, and negligible accuracy loss. Based in part on our work, the community has been able to run accurate billion or even trillion-parameter models on computationally-limited devices."',
            bio='"Dan Alistarh is a Professor at IST Austria, in Vienna. Previously, he was a Researcher with Microsoft, a Postdoc at MIT CSAIL, and received his PhD from the EPFL. His research is on algorithms for efficient machine learning and high-performance computing, with a focus on scalable DNN inference and training, for which he was awarded an ERC Starting Grant in 2018. In his spare time, he works with the ML research team at Neural Magic, a startup based in Boston, on making compression faster, more accurate and accessible to practitioners."',
            day=1,
            start="4:00 PM",
            end="5:00 PM",
            location=day_one_str,
        )
    )

    speakers.append(
        Speaker(
            name="Tom Goldstein",
            role="Speaker",
            website="https://www.cs.umd.edu/~tomg/",
            affiliation="University of Maryland",
            photo="goldstein.jpeg",
            talk='"Statistical methods for addressing safety and security issues of generative models"',
            abstract='"This talk will have two parts.  In the first part, I’ll talk about mathematical perspectives on how to watermark generative models to prevent parameter theft,  ways to watermark generative model outputs to enable detection, and ways to perform post-hoc detection of language models without relying on watermarks.  I’ll emphasize the important idea of using statistical hypothesis testing and p-values to provide rigorous control of the false-positive rate of detection. In the second part of the talk, I’ll present methods for constructing neural networks that exhibit “slow” thinking abilities akin to human logical reasoning.  Rather than learning simple pattern matching rules, these networks have the ability to synthesize algorithmic reasoning processes and solve difficult discrete search and planning problems that cannot be solved by conventional AI systems.  Interestingly, these reasoning systems naturally exhibit error correction and robustness properties that make them more difficult to break than their fast thinking counterparts."',
            bio='"Tom Goldstein is the Volpi-Cupal Professor of Computer Science at the University of Maryland, and director of the Maryland Center for Machine Learning.  His research lies at the intersection of machine learning and optimization, and targets applications in computer vision and signal processing. Professor Goldstein has been the recipient of several awards, including SIAM’s DiPrima Prize, a DARPA Young Faculty Award, a JP Morgan Faculty award, an Amazon Research Award, and a Sloan Fellowship."',
            day=4,
            start="9:00 AM",
            end="10:00 AM",
            location=day_two_str,
        )
    )

    speakers.append(
        Speaker(
            name="Yingbin Liang",
            role="Speaker",
            website="https://sites.google.com/view/yingbinliang/home",
            affiliation="Ohio State University",
            photo="liang.jpeg",
            talk='"In-Context Convergence of Transformers"',
            abstract='"Transformers have recently revolutionized many machine learning domains and one salient discovery is their remarkable in-context learning capability, where models can capture an unseen task by utilizing task-specific prompts without further parameters fine-tuning. In this talk, I will present our recent work that aims at understanding the in-context learning mechanism of transformers. Our focus is on the learning dynamics of a one-layer transformer with softmax attention trained via gradient descent in order to in-context learn linear function classes. I will first present our characterization of the training convergence of in-context learning for data with balanced and imbalanced features, respectively. I will then discuss the insights that we obtain about attention models and training processes. I will also talk about the analysis techniques that we develop which may be useful for a broader set of problems. I will finally conclude my talk with comments on a few future directions.<br>This is a joint work with Yu Huang (UPenn) and Yuan Cheng (NUS)."',
            bio='"Dr. Yingbin Liang is currently a Professor at the Department of Electrical and Computer Engineering at the Ohio State University (OSU), and a core faculty of the Ohio State Translational Data Analytics Institute (TDAI). She also serves as the Deputy Director of the AI-EDGE Institute at OSU. Dr. Liang received the Ph.D. degree in Electrical Engineering from the University of Illinois at Urbana-Champaign in 2005, and served on the faculty of University of Hawaii and Syracuse University before she joined OSU. Dr. Liang’s research interests include machine learning, optimization, information theory, and statistical signal processing. Dr. Liang received the National Science Foundation CAREER Award and the State of Hawaii Governor Innovation Award in 2009. She also received EURASIP Best Paper Award in 2014. She is an IEEE fellow."',
            day=2,
            start="9:00 AM",
            end="10:00 AM",
            location=day_two_str,
        )
    )

    # speakers.append(
    #     Speaker(
    #         name='Robert D. Nowak',
    #         role='Speaker',
    #         website='https://nowak.ece.wisc.edu/',
    #         affiliation='University of Wisconsin-Madison',
    #         photo='nowak.jpeg'
    #     )
    # )

    speakers.append(
        Speaker(
            name="Stefano Soatto",
            role="Speaker",
            website="https://web.cs.ucla.edu/~soatto/",
            affiliation="University of California, Los Angeles",
            photo="soatto.jpeg",
            talk='"Representation and Control of Meanings in Large Language Models and Multimodal Foundation Models"',
            abstract='"Large Language Models and Multimodal Foundation Models, despite the simple predictive learning criterion and absence of explicit complexity bias, have shown the ability to capture the structure and “meaning” of data. I will introduce a notion of “meaning” for large language models as equivalence classes of sentences, and describe methods to establish a geometry and topology in the space of meanings, as well as an algebra so meanings can be composed and asymmetric relations such as entailment and implication can be quantified. Meanings as equivalence classes of sentences determined by the trained embedings can be defined, computed and quantified for pre-trained models, without the need for instruction tuning, reinforcement learning, or prompt engineering. Meanings as trajectories can be shown to align with human assessment through manually annotated benchmarks and can, as the outputs of dynamical systems, be controlled. I will show illustrative examples using both text and imaging modalities."',
            bio='"Professor Soatto received his Ph.D. in Control and Dynamical Systems from the California Institute of Technology in 1996; he joined UCLA in 2000 after being Assistant and then Associate Professor of Electrical and Biomedical Engineering at Washington University, and Research Associate in Applied Sciences at Harvard University. Between 1995 and 1998 he was also Ricercatore in the Department of Mathematics and Computer Science at the University of Udine - Italy. He received his D.Ing. degree (highest honors) from the University of Padova- Italy in 1992. His general research interests are in Computer Vision and Nonlinear Estimation and Control Theory. In particular, he is interested in ways for computers to use sensory information (e.g. vision, sound, touch) to interact with humans and the environment.  Dr. Soatto is the recipient of the David Marr Prize (with Y. Ma, J. Kosecka and S. Sastry of U.C. Berkeley) for work on Euclidean reconstruction and reprojection up to subgroups. He also received the Siemens Prize with the Outstanding Paper Award from the IEEE Computer Society for his work on optimal structure from motion (with R. Brockett of Harvard). He received the National Science Foundation Career Award and the Okawa Foundation Grant. He is Associate Editor of the IEEE Transactions on Pattern Analysis and Machine Intelligence (PAMI) and a Member of the Editorial Board of the International Journal of Computer Vision (IJCV) and Foundations and Trends in Computer Graphics and Vision."',
            day=1,
            start="10:00 AM",
            end="11:00 AM",
            location=day_one_str,
        )
    )

    speakers.append(
        Speaker(
            name="Dimitris Papailiopoulos",
            role="Speaker",
            website="https://papail.io/",
            affiliation="University of Wisconsin-Madison",
            photo="papailiopoulos.jpeg",
            talk='"Teaching arithmetic to small language models"',
            abstract='"Can a language model truly “understand” arithmetic? We explore this by trying to teach small transformers from scratch to perform elementary arithmetic operations, using the next-token prediction objective. We first demonstrate that conventional training data (i.e., “A+B=C”) is not effective for arithmetic learning, and simple formatting changes can significantly improve accuracy. This leads to sharp phase transitions which, in some cases, can be explained through connections to low-rank matrix completion. We then train these small models on chain-of-thought data that includes intermediate steps. Even in the complete absence of pretraining, this approach significantly and simultaneously improves accuracy, sample complexity, and convergence speed. We finally discuss the issue of length generalization: can a model trained on n digits add n+1 digit numbers? Humans don’t need to be taught every digit length of addition to be able to perform it. It turns out that language models aren’t great at length generalization, but we catch glimpses of it in “unstable” scenarios. Surprisingly, the infamous U-shaped overfitting curve makes an appearance!"',
            bio='"Dimitris Papailiopoulos is the Jay & Cynthia Ihlenfeld Associate Professor of Electrical and Computer Engineering at the University of Wisconsin-Madison. His research interests span machine learning, information theory, and distributed systems, with a current focus on understanding the intricacies of large-language models. Before coming to Madison, Dimitris was a postdoctoral researcher at UC Berkeley and a member of the AMPLab. He earned his Ph.D. in ECE from UT Austin, under the supervision of Alex Dimakis. He received his ECE Diploma M.Sc. degree from the Technical University of Crete, in Greece. Dimitris is a recipient of the NSF CAREER Award (2019), three years of Sony Faculty Innovation Awards (2018, 2019 and 2020), a joint IEEE ComSoc/ITSoc Best Paper Award (2020), an IEEE Signal Processing Society, Young Author Best Paper Award (2015), the Vilas Associate Award (2021), the Emil Steiger Distinguished Teaching Award (2021), and the Benjamin Smith Reynolds Award for Excellence in Teaching (2019). In 2018, he co-founded MLSys, a new conference that targets research at the intersection of machine learning and systems."',
            day=3,
            start="1:30 PM",
            end="2:30 PM",
            location=day_two_str,
        )
    )

    speakers.append(
        Speaker(
            name="Jong Chul Ye",
            role="Speaker",
            website="https://bispl.weebly.com/professor.html",
            affiliation="Korea Advanced Institute of Science and Technology (KAIST)",
            photo="jongchulye.png",
            talk="Enlarging the Capability of Diffusion Inverse Solvers by Guidance",
            abstract="The recent advent of diffusion models has led to significant progress in solving inverse problems, leveraging these models as effective generative priors. Nonetheless, challenges related to the ill-posed nature of such problems remain, such as 3D extension and overcoming inherent ambiguities in measurements. In this talk, we introduce  strategies to address these issues. First, to enable 3D extension using only 2D diffusion models, we propose a novel approach using two perpendicular pre-trained 2D diffusion models which guides each solver to solve the 3D inverse problem. Specifically, by modeling the 3D data distribution as a product of 2D distributions sliced in different directions, our method effectively addresses the curse of dimensionality from the image guidance from the perpendicular direction. Second, drawing inspiration from the human ability to resolve visual ambiguities through perceptual biases, we introduce a novel latent diffusion inverse solver by incorporating guidance by text prompts. Specifically, our method applies the textual description of the preconception of the solution during the reverse sampling phase, of which description is dynamically reinforced through null-text optimization for adaptive negation. Our comprehensive experimental results show that our method successfully mitigates ambiguity in latent diffusion inverse solvers, enhancing their effectiveness and accuracy.",
            bio="Jong Chul Ye is a Professor at the Kim Jaechul Graduate School of Artificial Intelligence (AI) of Korea Advanced Institute of Science and Technology (KAIST), Korea. He received his B.Sc. and M.Sc. degrees from Seoul National University, Korea, and his PhD from Purdue University. Before joining KAIST, he worked at Philips Research and GE Global Research in New York. He has served as an associate editor of IEEE Trans. on Image Processing and an editorial board member for Magnetic Resonance in Medicine. He is currently an associate editor for IEEE Trans. on Medical Imaging and a Senior Editor of IEEE Signal Processing Magazine. He is an IEEE Fellow, was the Chair of IEEE SPS Computational Imaging TC, and IEEE EMBS Distinguished Lecturer. He was a General co-chair (with Mathews Jacob) for IEEE Symposium on Biomedical Imaging (ISBI) 2020. His research interest is in machine learning for biomedical imaging and computer vision.",
            day=3,
            start="9:00 AM",
            end="10:00 AM",
            location=day_two_str,
        )
    )

    speakers.append(
        Speaker(
            name="SueYeon Chung",
            role="Speaker",
            website="https://sites.google.com/site/sueyeonchung/",
            affiliation="New York University / Flatiron Institute",
            photo="sueyeon.jpeg",
            talk='"Multi-level theory of neural representations: Capacity of neural manifolds in biological and artificial neural networks"',
            abstract='"A central goal in neuroscience is to understand how orchestrated computations in the brain arise from the properties of single neurons and networks of such neurons. Answering this question requires theoretical advances that shine a light on the ‘black box’ of representations in neural circuits. In this talk, we will demonstrate theoretical approaches that help describe how cognitive task implementations emerge from the structure in neural populations and from biologically plausible neural networks. <br> We will introduce a new theory that connects geometric structures that arise from neural population responses (i.e., neural manifolds) to the neural representation’s efficiency in implementing a task. In particular, this theory describes how many neural manifolds can be represented (or ‘packed’) in the neural activity space while they can be linearly decoded by a downstream readout neuron. The intuition from this theory is remarkably simple: like a sphere packing problem in physical space, we can encode many “neural manifolds” into the neural activity space if these manifolds are small and low-dimensional, and vice versa. <br> Next, we will describe how such an approach can, in fact, open the ‘black box’ of distributed neuronal circuits in a range of settings, such as experimental neural datasets and artificial neural networks. In particular, our method overcomes the limitations of traditional dimensionality reduction techniques, as it operates directly on the high-dimensional representations. Furthermore, this method allows for simultaneous multi-level analysis, by measuring geometric properties in neural population data and estimating the amount of task information embedded in the same population. <br> Finally, we will discuss our recent efforts to fully extend this multi-level description of neural populations by (1) understanding how task-implementing neural manifolds emerge across brain regions and during learning, (2) investigating how neural tuning properties shape the representation geometry in early sensory areas, and (3) demonstrating the impressive task performance and neural predictivity achieved by optimizing a deep network to maximize the capacity of neural manifolds. By expanding our mathematical toolkit for analyzing representations underlying complex neuronal networks, we hope to contribute to the long-term challenge of understanding the neuronal basis of tasks and behaviors."',
            bio='"SueYeon Chung is an Assistant Professor in the Center for Neural Science at NYU, with a joint appointment in the Center for Computational Neuroscience at the Flatiron Institute, an internal research division of the Simons Foundation. She is also an affiliated faculty member at the Center for Data Science and Cognition and Perception Program at NYU. Prior to joining NYU, she was a Postdoctoral Fellow in the Center for Theoretical Neuroscience at Columbia University, and BCS Fellow in Computation at MIT. Before that, she received a Ph.D. in applied physics at Harvard University, and a B.A. in mathematics and physics at Cornell University. She received the Klingenstein-Simons Fellowship Award in Neuroscience in 2023. Her main research interests lie at the intersection between computational neuroscience and deep learning, with a particular focus on understanding and interpreting neural computation in biological and artificial neural networks by employing methods from neural network theory, statistical physics, and high-dimensional statistics."',
            day=4,
            start="10:00 AM",
            end="11:00 AM",
            location=day_two_str,
        )
    )

    speakers.append(
        Speaker(
            name="Maryam Fazel",
            role="Speaker",
            website="https://people.ece.uw.edu/fazel_maryam/",
            affiliation="University of Washington",
            photo="mfazel.jpeg",
            talk='"Flat Minima and Generalization in Learning: The Case of Low-rank Matrix Recovery"',
            abstract='"Many behaviors observed in deep neural networks still lack satisfactory explanation; e.g., how does an overparameterized neural network avoid overfitting and generalize to unseen data? Empirical evidence suggests that generalization depends on which zero-loss local minimum is attained during training. The shape of the training loss around a local minimum affects the model’s performance: “Flat” minima---around which the loss grows slowly—appear to generalize well. Clarifying this phenomenon helps explain generalization properties, which still largely remain a mystery.<br> In this talk we focus on a simple class of overparameterized nonlinear models, those arising in low-rank matrix recovery. We study several key models: matrix sensing, phase retrieval, robust Principal Component Analysis, covariance matrix estimation, and single hidden layer neural networks with quadratic activation. We prove that in these models, flat minima (measured by average curvature) exactly recover the ground truth under standard statistical assumptions, and we prove weak recovery for matrix completion. These results suggest (i) a theoretical basis for favoring methods that bias iterates towards flat solutions, (ii) use of Hessian trace as a good regularizer. Since the landscape properties we prove are algorithm-agnostic, a future direction is to pair these findings with the analysis of common training algorithms to better understand the interplay between the loss landscape and algorithmic implicit bias."',
            bio='"Maryam Fazel is the Moorthy Family Professor of Electrical and Computer Engineering at the University of Washington, with adjunct appointments in Computer Science and Engineering, Mathematics, and Statistics. Maryam received her MS and PhD from Stanford University, her BS from Sharif University of Technology in Iran, and was a postdoctoral scholar at Caltech before joining UW. She is a recipient of the NSF Career Award, UWEE Outstanding Teaching Award, and UAI conference Best Student Paper Award with her student. She directs the Institute for Foundations of Data Science (IFDS), a multi-site NSF TRIPODS Institute. She serves on the Editorial board of the MOS-SIAM Book Series on Optimization, is an Associate Editor of the SIAM Journal on Mathematics of Data Science and an Action Editor of Journal of Machine Learning Research. Her current research interests are in the area of optimization in machine learning and control."',
            day=1,
            start="1:30 PM",
            end="2:30 PM",
            location=day_one_str,
        )
    )

    speakers.append(
        Speaker(
            name="Kostas Daniilidis",
            role="Speaker",
            website="https://www.cis.upenn.edu/~kostas/",
            affiliation="University of Pennsylvania",
            photo="kostas.jpeg",
            talk="Parsimony through Equivariance",
            abstract="Equivariant representations are crucial in various scientific and engineering domains because they encode the inherent symmetries present in physical and biological systems, thereby providing a more natural and efficient way to model them. In the context of machine learning and perception, equivariant representations ensure that the output of a model changes in a predictable way in response to transformations of its input, such as 2D or 3D rotation or scaling. In this talk, we will show a systematic way of how to achieve equivariance by design and how such an approach can yield parsimony in training data and model capacity.",
            bio="Kostas Daniilidis is the Ruth Yalom Stone Professor of Computer and Information Science at the University of Pennsylvania where he has been faculty since 1998. He is an IEEE Fellow. He was the director of the GRASP laboratory from 2008 to 2013, Associate Dean for Graduate Education from 2012-2016, and Faculty Director of Online Learning from 2013- 2017. He obtained his undergraduate degree in Electrical Engineering from the National Technical University of Athens, 1986, and his PhD (Dr.rer.nat.) in Computer Science from the University of Karlsruhe, 1992, under the supervision of Hans-Hellmut Nagel. He received the Best Conference Paper Award at ICRA 2017. He co-chaired ECCV 2010 and 3DPVT 2006. His most cited works have been on event-based vision, equivariant learning, 3D human pose, and hand-eye calibration.",
            day=2,
            start="1:30 PM",
            end="2:30 PM",
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
            abstract='',
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
            tutorial='',
            abstract='',
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
            tutorial='',
            abstract='',
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
            tutorial='',
            abstract='"We will introduce modern deep learning-based methods for image reconstruction, particularly in medical imaging, including image-domain or sensor-domain neural network denoisers, and hybrid-domain deep learning schemes that combine physics-based forward models together with neural networks. Hybrid methods, both supervised and unsupervised or self-supervised, will be a key focus and amongst them, we will review plug and play (PnP) priors, consensus equilibrium, regularization by denoising (RED), deep unrolling methods, deep equilibrium models, and bilevel optimization based methods. Then, generative models for image reconstruction will be presented including generative adversarial networks (GANs), deep image prior, and diffusion models (DMs). We will provide a brief introduction to score-based DMs and introduce Diffusion Posterior Sampling ReSample algorithms. Other recent trends in image reconstruction will also be covered including exploiting deep reinforcement learning, unifying deep learning and sparse modeling, and methods focused on improving robustness of deep learning based image reconstruction (to various perturbations, train-test disparities, etc.) via randomized smoothing, diffusion models, etc. Other topics will also be covered briefly including learning sparse neural networks and joint or end-to-end training of sensing and image reconstruction setups. The session will conclude with brief discussion of future directions for the field.<br><br> Lecture 3 will involve multiple speakers covering different themes. Avrajit Ghosh will present many of the hybrid or physics-based deep learning methods. Dr. Ismail Alkhouri will speak on key ideas involving diffusion models. Gabriel Maliakal will discuss GANs and deep reinforcement learning and Dr. Saiprasad Ravishankar will speak on the key other topics.<br><br><em>Time: 140--150 minutes (coffee break in between)</em>"',
            track=2,
            order=6,
        )
    )

    return tutorials


def make_organizers():
    organizers = []

    organizers.append(
        Organizer(
            name="Dan Alistarh",
            role="Industry Liaison Chair",
            website="https://people.csail.mit.edu/alistarh/",
            affiliation="IST Austria / Neural Magic",
            photo="alistarh.jpeg",
        )
    )

    organizers.append(
        Organizer(
            name="Chenglong Bao",
            role="Area Chair",
            website="https://matbc.github.io/",
            affiliation="Tsinghua University",
            photo="bao.jpeg",
        )
    )

    organizers.append(
        Organizer(
            name="Babak Ehteshami Bejnordi",
            role="Area Chair",
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
            role="Area Chair",
            website="https://www.andrew.cmu.edu/user/beidic/",
            affiliation="Meta / Carnegie Mellon University",
            photo="chen0.jpeg",
        )
    )

    organizers.append(
        Organizer(
            name="Tianlong Chen",
            role="Area Chair",
            website="https://tianlong-chen.github.io/",
            affiliation="UT Austin / MIT",
            photo="chen_t.jpeg",
        )
    )

    organizers.append(
        Organizer(
            name="Yubei Chen",
            role="Area Chair",
            website="https://yubeichen.com",
            affiliation="UC Davis",
            photo="chen_yubei.jpeg",
        )
    )

    organizers.append(
        Organizer(
            name="Yubei Chen",
            role="Rising Stars Award Chair",
            website="https://yubeichen.com",
            affiliation="UC Davis",
            photo="chen_yubei.jpeg",
        )
    )

    organizers.append(
        Organizer(
            name="Yuxin Chen",
            role="Area Chair",
            website="https://yuxinchen2020.github.io/",
            affiliation="UPenn",
            photo="chen_yuxin.jpeg",
        )
    )

    organizers.append(
        Organizer(
            name="Yuejie Chi",
            role="Program Chair",
            website="https://users.ece.cmu.edu/~yuejiec/",
            affiliation="Carnegie Mellon University",
            photo="yc.jpeg",
        )
    )

    organizers.append(
        Organizer(
            name="Alex Dimakis",
            role="Advisory Committee",
            website="https://users.ece.utexas.edu/~dimakis/",
            affiliation="UT Austin",
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

    organizers.append(
        Organizer(
            name="Simon Du",
            role="Area Chair",
            website="https://simonshaoleidu.com/",
            affiliation="University of Washington",
            photo="du.jpeg",
        )
    )

    organizers.append(
        Organizer(
            name="Gintare Karolina Dziugaite",
            role="Program Chair",
            website="https://gkdz.org/",
            affiliation="Google DeepMind",
            photo="gintare.jpeg",
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
            name="Utku Evci",
            role="Area Chair",
            website="https://research.google/people/UtkuEvci/",
            affiliation="Google DeepMind",
            photo="evci.jpeg",
        )
    )

    organizers.append(
        Organizer(
            name="Yani Ioannou",
            role="Publicity Chair",
            website="https://yani.ai/",
            affiliation="University of Calgary",
            photo="ioannou.jpeg",
        )
    )

    organizers.append(
        Organizer(
            name="Souvik Kundu",
            role="Area Chair",
            website="https://ksouvik52.github.io/",
            affiliation="Intel Labs, USA",
            photo="kundu.jpeg",
        )
    )

    organizers.append(
        Organizer(
            name="Gitta Kutyniok",
            role="General Chair",
            website="https://www.ai.math.uni-muenchen.de/members/professor/kutyniok/index.html",
            affiliation="LMU Munich",
            photo="kutyniok.jpg",
        )
    )

    organizers.append(
        Organizer(
            name="Qi Lei",
            role="Area Chair",
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
            role="Panel Chair",
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

    organizers.append(
        Organizer(
            name="Elena Mocanu",
            role="Area Chair",
            website="https://people.utwente.nl/e.mocanu",
            affiliation="University of Twente",
            photo="mocanu.jpeg",
        )
    )

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
            role="Program Chair",
            website="https://qingqu.engin.umich.edu/",
            affiliation="University of Michigan",
            photo="qq.jpeg",
        )
    )

    organizers.append(
        Organizer(
            name="Saiprasad Ravishankar",
            role="Tutorial Chair",
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
            affiliation="UCSB",
            photo="redman.jpeg",
        )
    )

    organizers.append(
        Organizer(
            name="Liyue Shen",
            role="Publicity Chair",
            website="https://liyueshen.engin.umich.edu/",
            affiliation="University of Michigan",
            photo="shen-liyue.jpeg",
        )
    )

    organizers.append(
        Organizer(
            name="Harry Shum",
            role="General Chair",
            affiliation="HKUST / IDEA",
            photo="shum.jpeg",
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
            name="Mahdi Soltanolkotabi",
            role="Area Chair",
            website="https://viterbi-web.usc.edu/~soltanol/",
            affiliation="USC",
            photo="soltanolkotabi.jpeg",
        )
    )

    organizers.append(
        Organizer(
            name="Jeremias Sulam",
            role="Panel Chair",
            website="https://sites.google.com/view/jsulam",
            affiliation="Johns Hopkins University",
            photo="js.png",
        )
    )

    organizers.append(
        Organizer(
            name="René Vidal",
            role="General Chair",
            website="http://vision.jhu.edu/rvidal.html",
            affiliation="UPenn",
            photo="vidal.jpeg",
        )
    )

    organizers.append(
        Organizer(
            name="Atlas Wang",
            role="Program Chair",
            website="https://vita-group.github.io/",
            affiliation="UT Austin",
            photo="aw.png",
        )
    )

    organizers.append(
        Organizer(
            name="Dilin Wang",
            role="Industry Liaison Chair",
            website="https://research.facebook.com/people/wang-dilin/",
            affiliation="Meta",
            photo="wangd.jpeg",
        )
    )

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
            role="Area Chair",
            website="https://sites.cs.ucsb.edu/~yuxiangw/",
            affiliation="UC Santa Barbara",
            photo="wang.jpeg",
        )
    )

    organizers.append(
        Organizer(
            name="Bihan Wen",
            role="Area Chair",
            website="https://personal.ntu.edu.sg/bihan.wen/",
            affiliation="Nanyang Technological University",
            photo="wen.jpeg",
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
            name="John Wright",
            role="Tutorial Chair",
            website="http://www.columbia.edu/~jw2966/",
            affiliation="Columbia University",
            photo="jw.jpg",
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
            name="Yanchao Yang",
            role="Local Chair",
            website="https://yanchaoyang.github.io/",
            affiliation="HKU",
            photo="yyang.jpeg",
        )
    )

    organizers.append(
        Organizer(
            name="Fanny Yang",
            role="Area Chair",
            website="https://sml.inf.ethz.ch/group/fannyy/",
            affiliation="ETH Zurich",
            photo="yang.png",
        )
    )

    organizers.append(
        Organizer(
            name="Chong You",
            role="Industry Liaison Chair",
            website="https://sites.google.com/view/cyou",
            affiliation="Google Research",
            photo="cy.jpeg",
        )
    )

    organizers.append(
        Organizer(
            name="Man-Chung Yue",
            role="Local Chair",
            website="https://manchungyue.com/",
            affiliation="HKU",
            photo="ymc.jpeg",
        )
    )

    organizers.append(
        Organizer(
            name="Yuqian Zhang",
            role="Area Chair",
            website="https://sites.google.com/view/yuqianzhang",
            affiliation="Rutgers University",
            photo="yz.jpg",
        )
    )

    organizers.append(
        Organizer(
            name="Tong Zhang",
            role="Advisory Committee",
            website="http://tongzhang-ml.org/",
            affiliation="HKUST",
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

    organizers.append(
        Organizer(
            name="Tianbao Yang",
            role="Area Chair",
            website="https://people.tamu.edu/~tianbao-yang/",
            affiliation="Texas A&M",
            photo="tianbao_yang.jpeg",
        )
    )

    organizers.append(
        Organizer(
            name="Jiaqi Ma",
            role="Area Chair",
            website="https://www.jiaqima.com/",
            affiliation="Harvard / UIUC",
            photo="jiaqi-ma.jpeg",
        )
    )

    organizers.append(
        Organizer(
            name="Paris Giampouras",
            role="Area Chair",
            website="https://parisgiampouras.github.io/",
            affiliation="Johns Hopkins University",
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
            name="Weijie Su",
            role="Area Chair",
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

    organizers.append(
        Organizer(
            name="Wei Hu",
            role="Area Chair",
            website="https://weihu.me/",
            affiliation="University of Michigan",
            photo="huwei.jpeg",
        )
    )

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
            website="https://www.andrew.cmu.edu/user/laixis/",
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

    organizers.append(
        Organizer(
            name="Sarah Dean",
            role="Area Chair",
            website="https://sdean.website/",
            affiliation="Cornell University",
            photo="dean.jpeg",
        )
    )

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

    return organizers


def make_conference_events():
    conference_events = []

    # Populate 'meta' events
    conference_events.append(
        Event(
            name="Registration",
            event_class="meta",
            day=1,
            start="8:00 AM",
            end="9:15 AM",
            location=day_one_str,
        )
    )
    conference_events.append(
        Event(
            name="Opening Remarks",
            event_class="meta",
            day=1,
            start="9:15 AM",
            end="10:00 AM",
            location=day_one_str,
        )
    )
    conference_events.append(
        Event(
            name="Panel Discussion",
            event_class="meta",
            day=2,
            start="4:00 PM",
            end="5:00 PM",
            location=day_two_str,
        )
    )
    conference_events.append(
        Event(
            name="Open-Door Roundtable (Organization Committee)",
            event_class="meta",
            day=4,
            start="11:20 AM",
            end="12:30 PM",
            location="TBA",
        )
    )
    conference_events.append(
        Event(
            name='OPEN TO PUBLIC: Half-Day Tutorials, Part I<br>(Two Parallel Tracks: <a href="/tutorials/#track-learning-deep-low-dimensional-models-from-high-dimensional-data-from-theory-to-practice">Low-Dimensional Structure in Deep Networks</a>; <a href="/tutorials/#track-advances-in-machine-learning-for-image-reconstruction-sparse-models-to-deep-networks">Learning for Image Reconstruction</a>)',
            event_class="meta",
            day=4,
            start="1:30 PM",
            end="3:30 PM",
            location=day_two_str + ', LG.17 and LG.18',
        )
    )
    conference_events.append(
        Event(
            name='OPEN TO PUBLIC: Half-Day Tutorials, Part II<br>(Two Parallel Tracks: <a href="/tutorials/#track-learning-deep-low-dimensional-models-from-high-dimensional-data-from-theory-to-practice">Low-Dimensional Structure in Deep Networks</a>; <a href="/tutorials/#track-advances-in-machine-learning-for-image-reconstruction-sparse-models-to-deep-networks">Learning for Image Reconstruction</a>)',
            event_class="meta",
            day=4,
            start="4:00 PM",
            end="6:30 PM",
            location=day_two_str + ', LG.17 and LG.18',
        )
    )

    # Populate 'fun' events
    conference_events.append(
        Event(
            name="Reception",
            event_class="event",
            day=1,
            start="5:00 PM",
            end="6:30 PM",
            location=day_one_str,
        )
    )
    yoga_str = '<a href="/wellness/">Tailored Wellness Session</a>'
    conference_events.append(
        Event(
            name=yoga_str,
            event_class="event",
            day=2,
            start="8:00 AM",
            end="8:40 AM",
            location=day_two_str,
        )
    )
    conference_events.append(
        Event(
            name=yoga_str,
            event_class="event",
            day=3,
            start="8:00 AM",
            end="8:40 AM",
            location=day_two_str,
        )
    )
    conference_events.append(
        Event(
            name=yoga_str,
            event_class="event",
            day=4,
            start="8:00 AM",
            end="8:40 AM",
            location=day_two_str,
        )
    )
    conference_events.append(
        Event(
            name="Banquet",
            event_class="event",
            day=2,
            start="7:00 PM",
            end="9:00 PM",
            location=banquet_str,
        )
    )
    conference_events.append(
        Event(
            name="Tram Tour",
            event_class="event",
            day=3,
            start="7:00 PM",
            end="9:00 PM",
            location=tram_str,
        )
    )
    # conference_events.append(
    #     Event(
    #         name="Social Event / Tour / Etc. (TBA)",
    #         event_class="event",
    #         day=5,
    #         start="10:00 AM",
    #         end="2:00 PM",
    #         location="TBA",
    #     )
    # )

    # Populate 'break' events
    conference_events.append(
        Event(
            name="Coffee Break",
            event_class="break",
            day=1,
            start="11:00 AM",
            end="11:20 AM",
            location=day_one_str
        )
    )
    conference_events.append(
        Event(
            name="Coffee Break",
            event_class="break",
            day=2,
            start="11:00 AM",
            end="11:20 AM",
            location=day_two_str,
        )
    )
    conference_events.append(
        Event(
            name="Coffee Break",
            event_class="break",
            day=3,
            start="11:00 AM",
            end="11:20 AM",
            location=day_two_str,
        )
    )
    conference_events.append(
        Event(
            name="Coffee Break",
            event_class="break",
            day=4,
            start="11:00 AM",
            end="11:20 AM",
            location=day_two_str,
        )
    )
    conference_events.append(
        Event(
            name="Coffee Break",
            event_class="break",
            day=1,
            start="3:30 PM",
            end="4:00 PM",
            location=day_one_str,
        )
    )
    conference_events.append(
        Event(
            name="Coffee Break",
            event_class="break",
            day=2,
            start="3:30 PM",
            end="4:00 PM",
            location=day_two_str,
        )
    )
    conference_events.append(
        Event(
            name="Coffee Break",
            event_class="break",
            day=3,
            start="3:30 PM",
            end="4:00 PM",
            location=day_two_str,
        )
    )
    conference_events.append(
        Event(
            name="Coffee Break",
            event_class="break",
            day=4,
            start="3:30 PM",
            end="4:00 PM",
            location=day_two_str,
        )
    )
    conference_events.append(
        Event(
            name="Lunch Break",
            event_class="break",
            day=1,
            start="12:20 PM",
            end="1:30 PM",
            location=day_one_str,
        )
    )
    conference_events.append(
        Event(
            name="Lunch Break",
            event_class="break",
            day=2,
            start="12:20 PM",
            end="1:30 PM",
            location=day_two_str,
        )
    )
    conference_events.append(
        Event(
            name="Lunch Break",
            event_class="break",
            day=3,
            start="12:20 PM",
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

    # Poster sessions
    # conference_events.append(
    #         Event(name='Oral Session 1',
    #               event_class='poster',
    #               day=1,
    #               start='11:20 AM',
    #               end='12:30 PM',
    #               location='TBA'
    #               )
    #         )
    conference_events.append(
        Event(
            name="Oral Session 1",
            event_class="oral",
            day=1,
            start="2:30 PM",
            end="3:30 PM",
            location=day_one_str,
        )
    )
    conference_events.append(
        Event(
            name="Oral Session 2",
            event_class="oral",
            day=2,
            start="11:20 AM",
            end="12:20 PM",
            location=day_two_str,
        )
    )
    conference_events.append(
        Event(
            name="Oral Session 3",
            event_class="oral",
            day=2,
            start="2:30 PM",
            end="3:30 PM",
            location=day_two_str,
        )
    )
    conference_events.append(
        Event(
            name="Oral Session 4",
            event_class="oral",
            day=3,
            start="11:20 AM",
            end="12:20 PM",
            location=day_two_str,
        )
    )
    conference_events.append(
        Event(
            name="Oral Session 5",
            event_class="oral",
            day=3,
            start="2:30 PM",
            end="3:30 PM",
            location=day_two_str,
        )
    )
    conference_events.append(
        Event(
            name="Oral Session 6",
            event_class="oral",
            day=3,
            start="4:00 PM",
            end="5:00 PM",
            location=day_two_str,
        )
    )
    conference_events.append(
        Event(
            name="Spotlight Poster Session 1",
            event_class="poster",
            day=2,
            start="5:00 PM",
            end="6:30 PM",
            location=day_two_str,
        )
    )
    conference_events.append(
        Event(
            name="Spotlight Poster Session 2",
            event_class="poster",
            day=3,
            start="5:00 PM",
            end="6:30 PM",
            location=day_two_str,
        )
    )

    # Rising stars sessinos
    conference_events.append(
        Event(
            name="Rising Stars Session 1",
            event_class="rising",
            day=1,
            start="11:20 AM",
            end="12:20 PM",
            location=day_one_str,
        )
    )
    conference_events.append(
        Event(
            name="Rising Stars Session 2",
            event_class="rising",
            day=2,
            start="10:00 AM",
            end="11:00 AM",
            location=day_two_str,
        )
    )
    conference_events.append(
        Event(
            name="Rising Stars Session 3",
            event_class="rising",
            day=3,
            start="10:00 AM",
            end="11:00 AM",
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
        name="CPAL-2024",
        start_month="Jan",
        start_day=3,
        start_day_of_week="Wednesday",
        early_time="8:00 AM",
        late_time="9:00 PM",
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
    papers = get_accepted_papers(venue_str="CPAL.cc/2024/Conference")
    # Loop over papers, write yaml files
    out_dir = root / "_proceedings"
    for paper in papers:
        paper = paper.to_json()
        out = {
            "title": paper["content"]["title"]["value"],
            "authors": ", ".join(paper["content"]["authors"]["value"]),
            "link": "https://openreview.net/forum?id=" + paper["id"],
            "keywords": ", ".join(paper["content"]["keywords"]["value"]),
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
    papers = get_accepted_papers(venue_str="CPAL.cc/2024/Recent_Spotlight_Track")
    # Loop over papers, write yaml files
    out_dir = root / "_spotlight"
    for paper in papers:
        paper = paper.to_json()
        out = {
            "title": paper["content"]["title"]["value"],
            "authors": ", ".join(paper["content"]["authors"]["value"]),
            "link": "https://openreview.net/forum?id=" + paper["id"],
            "keywords": ", ".join(paper["content"]["keywords"]["value"]),
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
    description="Create and export database properties for CPAL 2024."
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
