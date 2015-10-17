__author__ = 'oliver'


import matplotlib
matplotlib.use('Agg') # Or any other X11 back-end


import numpy as np
import matplotlib.pyplot as pyplot
import pickle
import sys
import math
from numpy import genfromtxt

# First arg is file to de-pickle, second arg is "isTest"
work_dir = 'results/'
def main(argv):
    colors = ['#FC474C','#8DE047','#FFDD50','#53A3D7']
    max_x = 0
    max_y = 0
    for i,filename in enumerate(argv):

        data = genfromtxt(work_dir+filename,delimiter=',')


        if i==0:
            fig = pyplot.figure(figsize=(6, 6))
            axes = pyplot.gca()
            pyplot.grid()

            max_y = data[:,4].max()
            max_x = data[:,0].max()

            axes.set_ylim([0, max_y])
            axes.set_xlim([0, max_x])
            pyplot.xlabel('Epochs')
            pyplot.ylabel('Loss')
            pyplot.title('Loss')

        if data[:,4].max() > max_y:
            max_y = data[:,4].max()
            axes.set_ylim([0, max_y])

        if data[:,0].max() > max_x:
            max_x = data[:,0].max()
            axes.set_xlim([0, max_x])

        pyplot.plot(data[:,0], data[:,4], linewidth=2, label=filename, color=colors[i])

    pyplot.legend(loc='upper left', shadow=True, fontsize='medium')
    pyplot.savefig(work_dir+'loss')

if __name__=="__main__":
    work_dir = sys.argv[1]
    main(sys.argv[2:])