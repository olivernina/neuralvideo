__author__ = 'oliver'


import matplotlib
matplotlib.use('Agg') # Or any other X11 back-end


import numpy as np
import matplotlib.pyplot as pyplot
import pickle
import sys
import math
from numpy import genfromtxt
import os

# First arg is file to de-pickle, second arg is "isTest"
work_dir = 'results/'
def loss_plot(argv):
    colors = ['#FC474C','#8DE047','#FFDD50','#53A3D7']
    max_x = 0
    max_y = 0

    column_num = 4
    for i,filename in enumerate(argv):

        if os.path.exists(work_dir+filename):
            data = genfromtxt(work_dir+filename,delimiter=',')


            if i==0:
                fig = pyplot.figure(figsize=(6, 6))
                axes = pyplot.gca()
                pyplot.grid()

                max_y = data[:,column_num].max()
                max_x = data[:,0].max()

                axes.set_ylim([0, max_y])
                axes.set_xlim([0, max_x])
                pyplot.xlabel('Epochs')
                pyplot.ylabel('Loss')
                pyplot.title('Loss')

            if data[:,column_num].max() > max_y:
                max_y = data[:,column_num].max()
                axes.set_ylim([0, max_y])

            if data[:,0].max() > max_x:
                max_x = data[:,0].max()
                axes.set_xlim([0, max_x])

            pyplot.plot(data[:,0], data[:,column_num], linewidth=2, label=filename, color=colors[i])
        else:
            print "file: "+work_dir+filename+" not found"

    pyplot.legend(loc='upper left', shadow=True, fontsize='medium')
    pyplot.savefig(work_dir+'loss')


def ppl2_plot(argv):
    colors = ['#FC474C','#8DE047','#FFDD50','#53A3D7']
    max_x = 0
    max_y = 0

    column_num = 6
    for i,filename in enumerate(argv):

        if os.path.exists(work_dir+filename):
            data = genfromtxt(work_dir+filename,delimiter=',')

            init_val = 10
            if i==0:
                fig = pyplot.figure(figsize=(6, 6))
                axes = pyplot.gca()
                pyplot.grid()

                max_y = data[init_val:,column_num].max()
                max_x = data[init_val:,0].max()

                axes.set_ylim([0, max_y])
                axes.set_xlim([0, max_x])
                pyplot.xlabel('Epochs')
                pyplot.ylabel('ppl2')
                pyplot.title('Perplexity')

            if data[init_val:,column_num].max() > max_y:
                max_y = data[init_val:,column_num].max()
                axes.set_ylim([0, max_y])

            if data[init_val:,0].max() > max_x:
                max_x = data[init_val:,0].max()
                axes.set_xlim([0, max_x])

            pyplot.plot(data[init_val:,0], data[init_val:,column_num], linewidth=2, label=filename, color=colors[i])
        else:
            print "file: "+work_dir+filename+" not found"

    pyplot.legend(loc='upper left', shadow=True, fontsize='medium')
    pyplot.savefig(work_dir+'loss')

def val_plot(argv):
    colors = ['#FC474C','#8DE047','#FFDD50','#53A3D7']
    max_x = 0
    max_y = 0

    column_num = 4
    for i,filename in enumerate(argv):
        file_path = os.path.join(work_dir,filename)
        if os.path.exists(file_path):
            data = genfromtxt(file_path,delimiter=',')

            init_val = 0
            if i==0:
                fig = pyplot.figure(figsize=(6, 6))
                axes = pyplot.gca()
                pyplot.grid()

                max_y = data[init_val:,column_num].max()
                max_x = data[init_val:,0].max()

                axes.set_ylim([0, max_y])
                axes.set_xlim([0, max_x])
                pyplot.xlabel('Epochs')
                pyplot.ylabel('ppl2')
                pyplot.title('Perplexity')

            if data[init_val:,column_num].max() > max_y:
                max_y = data[init_val:,column_num].max()
                axes.set_ylim([0, max_y])

            if data[init_val:,0].max() > max_x:
                max_x = data[init_val:,0].max()
                axes.set_xlim([0, max_x])

            pyplot.plot(data[init_val:,0], data[init_val:,column_num], linewidth=2, label=filename, color=colors[i])
        else:
            print "file: "+work_dir+filename+" not found"

    pyplot.legend(loc='upper left', shadow=True, fontsize='medium')
    pyplot.savefig(os.path.join(work_dir,'val.png'))
    # pyplot.show()


if __name__=="__main__":
    work_dir = sys.argv[1]
    plot_type = sys.argv[2]

    if plot_type == 'loss':
        loss_plot(sys.argv[3:])
    if plot_type == 'ppl2':
        ppl2_plot(sys.argv[3:])
    if plot_type == 'val':
        val_plot(sys.argv[3:])
