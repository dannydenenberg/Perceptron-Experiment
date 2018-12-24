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
        guess = self.feedforward(inputs)
        error = target - guess

        # update weights by adding the input times the error times the learning rate
        self.weights = [self.weights[i] + inputs[i] * error * self.learning_rate for i in range(len(inputs))]

    # activation function
    def activate(self, n):
        if n >= 0:
            return 1
        else:
            return -1

# simple function of x as a line
def line(x):
    return x +8

# HARVARD, MIT summer courses

# to train the classifier, we need a set of inputs with a known answer
class Trainer:
    def __init__(self, x, y, ans):
        self.inputs = [x, y, 1] # 1 is the bias or y-intercept
        self.answer = ans

# initialize the data
data = []
for i in range(2000):
    # create random x, y pairs
    x = rand.randint(0, 1000)
    y = rand.randint(0, 1000)

    # see if the point is above or the below the `line`
     # by comparing the signs of the y values
    answer = 1 if line(x) - y < 0 else -1

    data.append(Trainer(x, y, answer))

    #print ("(", x, ",",y,") => ", answer)


# create the classifier
# this is a Perceptron that takes 3 inputs (one of which is the bias) to
    # produce a single output (-1 or 1)
brain = Perceptron(3)


# train the classifier (Perceptron)
for point in data:
    brain.train(point.inputs, point.answer)


# testing....
print("Have the model predict a value.")
while True:
    pair = [int(i) for i in input("Enter an x,y pair:").split(",")]
    pair.append(1) # 1 for the bias

    prediction = brain.feedforward(pair)
    print ("The models prediction is ", prediction)
