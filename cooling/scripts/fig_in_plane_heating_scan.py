import numpy as np

def read_data(i, j):
    filename = 'heating_run_' + str(i) + '_' + str(j) + '.dat'
    return np.loadtxt(filename, dtype=np.float64, skiprows=2)

for j in range(9):
    data = read_data(0, j)
    print(np.mean(data[50:, 2]))

print('\n\n')

for j in range(1, 10):
    data = read_data(1, j)
    print(np.mean(data[50:, 2]))
