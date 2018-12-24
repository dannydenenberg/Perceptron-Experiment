import numpy as nu
import random as rand

# represents a single neuron
class Perceptron():
    def __init__(self, num_inputs):
        # randomly initialize the weights based on the number of inputs
        self.weights = [rand.randint(-1,1) for i in range(num_inputs)]
        self.learning_rate = 0.1

    def feedforward(self, inputs):
        sum = 0
        for i in range(len(inputs)):
            sum += inputs[i] * self.weights[i]
        return self.activate(sum)

    def train(self, inputs, target):
        #calculate error
        guess = self.guess(inputs)
        error = target - guess

        # update weights by adding the input times the error times the learning rate
        self.weights = [weights[i] + input[i] * error * self.learning_rate for i in range(len(input))]

    # activation function
    def activate(self, n):
        if n >= 0:
            return 1
        else:
            return -1

# simple function of x as a line
def line(x):
    return x

# HARVARD, MIT summer courses

# to train the classifier, we need a set of inputs with a known answer
class Trainer:
    def __init__(self, x, y, ans):
        self.inputs = [x, y, 1] # 1 is the bias or y-intercept
        self.answer = ans

data = []
for i in range(20):
    x = rand.randint(0, 20)
    y = rand.randint(0, 20)
    answer = 1 if line(x) - y < 0 else -1

    data.append(Trainer(x, y, answer))

    print ("(", x, ",",y,") => ", answer)
