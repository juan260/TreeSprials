import numpy as np
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure

figure(figsize=(6,6), dpi = 200)
#x, y = [1.0, 0.0], [0.0, 0.0]
repetitions = 1000

params = {'x' : [1.0, 0.0], 'y' : [0.0, 0.0], 'angle' : - np.pi, 'length' : 1.0, 'angularGrowth' : np.pi * 2.0 / 3.09, 'proportionalGrowth' : 1.08, 'growth' : 0.2}

for i in range(repetitions):
    #length = np.sqrt(np.square(np.abs(x[1]-x[0]))+np.square(np.abs(y[1]-y[0])))
    #angle = np.arcsin(np.abs(y[1]-y[0])/length)
    #print(angle)
    params['length'] += params['growth']
    params['angle'] += params['angularGrowth']
    params['growth'] *= params['proportionalGrowth']
    params['x'], params['y'] = [params['x'][1], params['x'][1] + params['length'] * np.cos(params['angle'])], [params['y'][1], params['y'][1] + params['length'] * np.sin(params['angle'])]
    plt.plot(params['x'], params['y'], color='black')
plt.axis('off')
plt.show()