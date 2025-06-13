import sys

import markovify

def main():

    for i in range(1,len(sys.argv)): # use all inputed text file to train
        filename = sys.argv[i]
        with open(filename, 'r') as file:
            text = markovify.Text(file)
            for j in range(10):
                print(text.make_sentence())

if __name__ == "__main__":
    main()
