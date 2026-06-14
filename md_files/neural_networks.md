# Neural Networks - Quick Notes

## What is a Neural Network?

A Neural Network is a machine learning model inspired by the human brain. It learns patterns from data using interconnected nodes called neurons.

Applications:
- Image Recognition
- Chatbots
- Speech Recognition
- Recommendation Systems

---

## Structure

Input Layer → Hidden Layer(s) → Output Layer

- Input Layer: Receives data
- Hidden Layers: Learn patterns
- Output Layer: Produces prediction

---

## Neuron Components

### Inputs (x)
Features given to the model.

### Weights (w)
Determine importance of inputs.

### Bias (b)
Helps shift predictions.

### Activation Function
Introduces non-linearity.

---

## Common Activation Functions

### Sigmoid
Output: 0 to 1

Used for binary classification.

### ReLU
Output: max(0, x)

Most commonly used.

### Softmax
Converts outputs into probabilities.

Used for multi-class classification.

---

## Forward Propagation

Data flows through the network:

Input → Hidden Layers → Output

Produces a prediction.

---

## Loss Function

Measures prediction error.

Goal:
Minimize loss.

Examples:
- MSE (Regression)
- Cross Entropy (Classification)

---

## Backpropagation

Training algorithm that:

1. Calculates error
2. Computes gradients
3. Updates weights

---

## Gradient Descent

Optimization algorithm used to reduce loss.

Update Rule:

New Weight = Old Weight − Learning Rate × Gradient

---

## Important Terms

### Epoch
One complete pass through the dataset.

### Batch Size
Number of samples processed before updating weights.

### Learning Rate
Controls how much weights change each update.

---

## Overfitting

Model memorizes training data.

Signs:
- High training accuracy
- Low test accuracy

Solutions:
- More data
- Dropout
- Regularization

---

## Types of Neural Networks

### Feedforward Neural Network (FNN)
Basic neural network.

### CNN
Used for images.

Examples:
- Face Recognition
- Object Detection

### RNN
Used for sequential data.

Examples:
- Text
- Time Series

### LSTM
Improved RNN that remembers long-term information.

### Transformer
Modern architecture behind Generative AI models.

---

## Popular Frameworks

- TensorFlow
- Keras
- PyTorch

---

## Training Workflow

1. Collect Data
2. Preprocess Data
3. Build Network
4. Forward Propagation
5. Calculate Loss
6. Backpropagation
7. Update Weights
8. Repeat

---

## Interview Questions

1. What is a neuron?
2. What are weights and biases?
3. Why are activation functions used?
4. What is backpropagation?
5. What is gradient descent?
6. What is an epoch?
7. What is overfitting?
8. Difference between CNN and RNN?
9. What is an LSTM?
10. What is a Transformer?

---

## Quick Revision

Neural Network =
Inputs → Weights → Bias → Activation → Output

Training =
Forward Propagation → Loss → Backpropagation → Weight Update