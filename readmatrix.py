import numpy as np

def readmatrix(filename):
    f = open(filename, 'r')
    matrixstrings = f.readlines()
    f.close
    tomatrix = []
    for line in matrixstrings:
        linelist = line.split(',')
        for num in range (0, len(linelist)):
            linelist[num] = float(linelist[num])
        tomatrix.append(linelist)
    return np.array(tomatrix)

def updatematrix(matrix, filename)
    f = open(filename, 'w')
    output_string = ''
    # doesn't raise an error if the two aren't of same dimensions, because that way I can add users
    x, y = matrix.shape
    for i in range x:
        current_string = ''
        for j in range y:
            current_string += str(matrix.item(i, j)) + ','
        output_string += current_string + '/n'
    f.write(output_string)
    f.close
    return


