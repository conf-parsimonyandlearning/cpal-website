---
name: "Yuqing Wang"
role: "Researcher"
affiliation: "Johns Hopkins University"
website: "https://yzwangyuqing.github.io/"
photo: "image14.png"
talk: "Data Uniformity Improves Training Efficiency and More, with a Convergence Framework Beyond the NTK Regime"
abstract: "Data selection is crucial for data-driven decision-making, including foundation models, but beyond data quality and diversity, it is unclear whether other general quantitative principles can reliably improve complex tasks. In this talk, I will demonstrate that selecting more uniformly distributed data can improve training efficiency while enhancing performance. Specifically, we establish that more uniform (less biased) distribution leads to a larger minimum pairwise distance between data points, denoted by h_min, and prove that a smaller h_min can slow down the training dynamics of gradient descent (GD). Moreover, we theoretically show that the approximation error of neural networks decreases as h_min increases. Our analysis introduces a convergence framework for GD beyond the Neural Tangent Kernel (NTK) regime, applicable to a broad class of architectures, including transformers, without requiring Lipschitz smoothness. This framework further provides theoretical justification for the use of residual connection and function composition in deep neural architectures. In the end, I will show some comprehensive experiments, including supervised fine-tuning across various settings, different optimization strategies, model sizes, and training datasets. The results consistently demonstrate that selecting data by maximizing the minimum pairwise distance significantly accelerates training and achieves comparable or better performance across diverse datasets."
session: "3"
order: "4"
---
