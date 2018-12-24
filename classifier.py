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
        return activate(sum)

    def train(self, inputs, target):
        #calculate error
        guess = self.guess(inputs)
        error = target - guess

        # update weights by adding the input times the error times the learning rate
        self.weights = [weights[i] + input[i] * error * self.learning_rate for i in range(len(input))]

    def activate(n):
        if n >= 0:
            return 1
        else:
            return -1


# HARVARD, MIT summer courses

#activation function
def sign(n):
    if n >= 0:
        return 1;
    else:
        return -1;



#test
brain = Perceptron(5)
