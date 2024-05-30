# How Attention affect VanillaCNN and ResNet10 


<!-- ABOUT THE PROJECT -->
## About The Project
For this assignment, in the first part, we're going to add the attention layer to the VanillaCNN model (Early, Late, Double). In the second part, we're going to add the attention layer to the Resnet10.

This project contains two parts.

* VanillaCNN with Attention
* ResNet10 with Attention





We train the network for 10 epochs and rank the accurancy for 
    
    "Vanilla CNN (No Attention)",
    "Vanilla CNN (Single Attention Block: Early attention)",
    "Vanilla CNN (Single Attention Block: Late attention)",
    "Vanilla CNN (Double Attention Blocks)",
    "ResNet10",
    "ResNet10 with Attention"


![accuracy rank](https://github.com/tonytonyhsiao/intro-to-visual-learning_hw4/blob/main/rank%20diagram.png)


the explaination for the rank:(from highest to lowest)
1. **ResNet10 with Attention**
ResNet Architecture: ResNet (Residual Network) is known for its skip connections, which help in training very deep networks by mitigating the vanishing gradient problem.
Attention Mechanism: Attention mechanisms improve model performance by allowing the network to focus on important parts of the input. Combining ResNet with attention mechanisms enhances its ability to learn and generalize from the data.
2. **ResNet10**
ResNet Architecture: Even without attention, the ResNet architecture is very powerful due to its deep layers and skip connections, which facilitate better feature extraction and gradient flow during training.
3. **Vanilla CNN (Double Attention Blocks)**
Double Attention Blocks: Adding two attention blocks to a standard CNN helps the network to focus on important features at multiple stages, significantly improving its accuracy compared to a vanilla CNN without attention.
4. **Vanilla CNN (Single Attention Block: Early Attention)**
Single Attention Block (Early): Placing an attention block early in the network helps to enhance the learning of initial features. This is beneficial, but not as much as having multiple attention blocks.
5. **Vanilla CNN (Single Attention Block: Late Attention)**
Single Attention Block (Late): Placing an attention block later in the network also aids in focusing on important features, but it might not be as effective as early attention because the initial features might not be as well-learned.
6. **Vanilla CNN (No Attention)**
No Attention Mechanism: A vanilla CNN without any attention mechanism relies solely on its convolutional layers to learn features. This makes it the least effective among the listed models as it lacks the ability to dynamically focus on the most relevant parts of the input.