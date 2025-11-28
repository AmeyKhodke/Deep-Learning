Deep Learning: From Perceptrons to Deep Neural Networks

📖 Overview

This repository serves as a comprehensive documentation of my deep learning journey, focusing on the mathematical implementation of core neural network architectures from scratch.
Unlike using high-level APIs blindly, this project emphasizes understanding the calculus and linear algebra governing backpropagation, optimization landscapes, and gradient dynamics. The implementations here demonstrate the transition from single-layer perceptrons to multi-layer deep networks, addressing critical challenges like the vanishing gradient problem.

📂 Repository Architecture
The codebase is organized into modules that progressively increase in complexity:

1. 🧠 Perceptron & Foundations
Directory: /Perceptron
Theory: Implementation of the Rosenblatt Perceptron and the Adaline model.

Key Concepts:
Binary classification and linear separability.
Decision boundary convergence.
Limitations of single-layer networks (e.g., the XOR impossibility).

2. 📉 The Backpropagation Algorithm
Directory: /Backpropagation Algorithm
Theory: Manual derivation and implementation of the backward pass (chain rule).

Key Concepts:
Computation graphs and partial derivatives.
Gradient Descent (GD) and Stochastic Gradient Descent (SGD).
Weight updates $\Delta w = -\eta \cdot \nabla J(w)$.

3. 🚀 Improving Neural Networks
Directory: /Improving Neural Network
Theory: Advanced techniques to accelerate convergence and prevent overfitting.

Key Concepts:
Initialization: He and Xavier (Glorot) initialization to maintain variance.
Optimization: Momentum, RMSprop, and Adam optimizers.
Regularization: Implementation of L2 Regularization and Dropout layers.

4. ⚠️ The Vanishing Gradient Problem

Directory: /Vanishing Gradient Problem
Theory: Analysis of signal decay in deep networks when using saturating activation functions (Sigmoid/Tanh).

Key Concepts:
Mathematical analysis of derivative multiplication in deep layers ($\prod \frac{\partial \sigma}{\partial z} \approx 0$).
Solutions: Implementation of ReLU (Rectified Linear Unit) and Leaky ReLU.\
Impact on training stability and speed.

🛠️ Technical Stack
Primary Language: Python 3.x
Numerical Computing: NumPy (Heavy usage for matrix operations & vectorization)
Data Manipulation: Pandas
Visualization: Matplotlib / Seaborn (For loss curves and decision boundaries)

🚀 Getting Started

To run these implementations locally:

Clone the repository:
git clone [https://github.com/AmeyKhodke/Deep-Learning-.git](https://github.com/AmeyKhodke/Deep-Learning-.git)

Install dependencies:

pip install numpy pandas matplotlib

Navigate and Run:
cd "Backpropagation Algorithm"
python main.py


📬 Contact & Contributions
This project is part of my preparation for advanced roles in AI/ML.

Author: Amey Khodke

Focus: Deep Learning, Computer Vision, and Optimization Theory.

Created with ❤️ and ☕ by Amey Khodke.
