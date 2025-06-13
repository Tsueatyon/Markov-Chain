import re
import numpy as np
import random
# precondition: accept a opened txt file and a matrix,
# postcondition: return a matrix  and the list stats to represent the trained model.
def train(file,matrix,states):
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    if rows != cols:
        print("error in matrix format")
        return matrix,states
    content = file.read()
    readings = re.findall(r'\w+|[^\w\s]', content) # split contents in to words and punctuations
    curread = None
    for reading in readings:
        reading = reading.lower()
        prevread = curread
        curread = reading
        if curread not in states: # case1 creat a new node
            lenstates = len(states)
            if rows == lenstates:# hits matrix limitation- expand
                matrix = matrixexpand(matrix)
                rows = matrix.shape[0]
            states.append(curread)
        else:# simply modify data
            if prevread is not None:
                matrix[states.index(prevread)][states.index(curread)] += 1
    return matrix, states

# pre-condition : a matrix is passed as argument
# Poste condition: return a matrix expanded with zeros from the original one
def matrixexpand(matrix):
    original = matrix.shape[0]
    newsize = original + 500
    expanded_matrix = np.zeros((newsize, newsize), dtype=matrix.dtype) # Create a new matrix filled with zeros
    expanded_matrix[:matrix.shape[0], :matrix.shape[1]] = matrix # Copy the original matrix to the new one
    return expanded_matrix

# pre-condition: pass a list
# post-condition: sum(row) == 1 returns True
def percentizerow(row):
    total = sum(row)
    if total == 0:
        print("error IN rows")
        return 1
    for i in range (len(row)):
        row[i] = row[i] / total
    return row

# precondition : matrix and states trained
# post condition : return a string generated based on training data
def generate(steps,matrix,states):
    currindex = random.randint(0, len(states)-1)
    while sum(matrix[currindex]) == 0: # starting at a ramdom position
        currindex = random.randint(0, len(states) - 1)

    record = states[currindex] # put the curr word in

    for _ in range(steps):
        if sum(matrix[currindex].copy()) == 0:
            currindex = states.index(".")
            continue # reset if meet a deadend
        percendrow = percentizerow(matrix[currindex].copy())
        nextindex = random.choices(range(len(percendrow)), weights=percendrow)[0]
        currindex = nextindex
        if bool(re.fullmatch(r"[a-zA-Z]+", states[nextindex])): # if is not a word -  don't add space
            record += " " + states[nextindex]
        else:
            record += states[nextindex]
    return record






