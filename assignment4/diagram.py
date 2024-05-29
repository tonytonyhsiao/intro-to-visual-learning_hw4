import matplotlib.pyplot as plt

# Data
models = [
    "Vanilla CNN (No Attention)",
    "Vanilla CNN (Single Attention Block: Early attention)",
    "Vanilla CNN (Single Attention Block: Late attention)",
    "Vanilla CNN (Double Attention Blocks)",
    "ResNet10",
    "ResNet10 with Attention"
]
accuracies = [58.06, 60.48, 59.96, 62.49, 74.44, 76.53]

# Adjusting the plot for better visibility
plt.figure(figsize=(12, 6))
plt.barh(models, accuracies, color='skyblue')
plt.xlabel('Accuracy (%)')
plt.title('Model Accuracy Comparison')
plt.xlim(55, 80)
plt.gca().invert_yaxis()
plt.subplots_adjust(left=0.3)  # Adjust the left margin for better label visibility
for index, value in enumerate(accuracies):
    plt.text(value + 0.5, index, f"{value}%", va='center')

plt.show()
