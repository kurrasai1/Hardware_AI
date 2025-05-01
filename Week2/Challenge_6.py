import numpy as np

# Sigmoid activation function and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(output):
    return output * (1 - output)

# Perceptron class
class Perceptron:
    def __init__(self, learning_rate=0.1):
        self.weights = np.random.randn(2)
        self.bias = np.random.randn()
        self.lr = learning_rate

    def predict(self, inputs):
        summation = np.dot(inputs, self.weights) + self.bias
        return sigmoid(summation)

    def train(self, X, y, epochs=10000):
        for epoch in range(epochs):
            for xi, target in zip(X, y):
                pred = self.predict(xi)
                error = target - pred
                # Weight update rule
                self.weights += self.lr * error * xi
                self.bias += self.lr * error

# Logic gates as input/output data
def train_gate(gate_name):
    gate = {
        'NAND': {
            'X': np.array([[0,0],[0,1],[1,0],[1,1]]),
            'y': np.array([1, 1, 1, 0])
        },
        'XOR': {
            'X': np.array([[0,0],[0,1],[1,0],[1,1]]),
            'y': np.array([0, 1, 1, 0])
        }
    }

    X, y = gate[gate_name]['X'], gate[gate_name]['y']
    perceptron = Perceptron(learning_rate=0.1)
    perceptron.train(X, y, epochs=10000)

    print(f"\nResults for {gate_name} gate:")
    for xi in X:
        print(f"Input: {xi} => Output: {round(perceptron.predict(xi), 2)}")

train_gate("NAND")
train_gate("XOR")

