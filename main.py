import sys

import numpy as np

from lib import train, generate

def main():
    states = []
    matrix = np.zeros((50, 50))
    for i in range(1,len(sys.argv)): # use all inputed text file to train
        filename = sys.argv[i]
        with open(filename, 'r') as file:
                matrix, states = train(file, matrix, states) # train the data
    res = generate(150,matrix, states)#generate text
    print(res)
    return res
if __name__ == "__main__":
    main()
