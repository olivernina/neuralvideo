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
xmin = 20000
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

                #axes.set_ylim([0, max_y])
                # axes.set_xlim([xmin, max_x])
                axes.set_ylim([0, 50])
                axes.set_xlim([15, 2000])
                pyplot.xlabel('Iterations')
                pyplot.ylabel('Loss')
                pyplot.title('Training')

            #if data[:,column_num].max() > max_y:
             #   max_y = data[:,column_num].max()
              #  axes.set_ylim([0, max_y])

            #if data[:,0].max() > max_x:
             #   max_x = data[:,0].max()
              #  axes.set_xlim([0, max_x])

            pyplot.plot(data[:,0], data[:,column_num], linewidth=2, label=filename.split('.')[0], color=colors[i])
        else:
            print "file: "+work_dir+filename+" not found"

    pyplot.legend(loc='upper right', shadow=True, fontsize='medium')
    pyplot.savefig(os.path.join(work_dir,'loss.eps'))


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

                # axes.set_ylim([15, max_y])
                #axes.set_xlim([xmin, max_x])
                axes.set_ylim([0, 70])
                axes.set_xlim([15, 1000])
                pyplot.xlabel('Iterations')
                pyplot.ylabel('Perplexity')
                pyplot.title('Training')

           # if data[init_val:,column_num].max() > max_y:
            #    max_y = data[init_val:,column_num].max()
             #   axes.set_ylim([0, max_y])

           # if data[init_val:,0].max() > max_x:
            #    max_x = data[init_val:,0].max()
             #   axes.set_xlim([0, max_x])

            pyplot.plot(data[init_val:,0], data[init_val:,column_num], linewidth=2, label=filename.split('.')[0], color=colors[i])
        else:
            print "file: "+work_dir+filename+" not found"

    pyplot.legend(loc='upper right', shadow=True, fontsize='medium')
    pyplot.savefig(os.path.join(work_dir,'ppl2.eps'))

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

                #axes.set_ylim([0, max_y])
                axes.set_ylim([14, 19])
                axes.set_xlim([xmin, max_x])
                axes.set_xlim([0, 24500])
                pyplot.xlabel('Iterations')
                pyplot.ylabel('Perplexity')
                pyplot.title('Validation')

            if data[init_val:,column_num].max() > max_y:
                max_y = data[init_val:,column_num].max()
                #axes.set_ylim([0, max_y])

            if data[init_val:,0].max() > max_x:
                max_x = data[init_val:,0].max()
                axes.set_xlim([0, max_x])
            from scipy.interpolate import spline
            x_smooth = np.linspace(0, max_x, 100)
	    y_smooth = spline(data[init_val:,0],data[init_val:,column_num],x_smooth)

            pyplot.plot(data[init_val:,0], data[init_val:,column_num], linewidth=2, label=filename.split('.')[0].split('_')[0], color=colors[i])


           #pyplot.plot(x_smooth, y_smooth, linewidth=2, label=filename.split('.')[0].split('_')[0], color=colors[i])
        else:
            print "file: "+work_dir+filename+" not found"

    pyplot.legend(loc='upper right', shadow=True, fontsize='medium')
    pyplot.savefig(os.path.join(work_dir,'val.eps'))
    # pyplot.show()



#cider = 5, blue4=6, ..., ROUGE= 10,METEOR=11

def bleu_plot(argv):
    colors = ['#FC474C','#8DE047','#FFDD50','#53A3D7']
    max_x = 0
    max_y = 0

    column_num = 6 #cider = 5, blue4=6, ..., ROUGE= 10,METEOR=11
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

                # axes.set_ylim([0, max_y])
                axes.set_ylim([.30,.45])
                # axes.set_xlim([xmin, max_x])
                axes.set_xlim([0, 24500])
                pyplot.xlabel('Iterations')
                pyplot.ylabel('BLEU')
                pyplot.title('Validation')

            # if data[init_val:,column_num].max() > max_y:
            #     max_y = data[init_val:,column_num].max()
            #     axes.set_ylim([0, max_y])
            #
            # if data[init_val:,0].max() > max_x:
            #     max_x = data[init_val:,0].max()
            #     axes.set_xlim([0, max_x])

            pyplot.plot(data[init_val:,0], data[init_val:,column_num], linewidth=2, label=filename.split('.')[0].split('_')[0], color=colors[i])
        else:
            print "file: "+work_dir+filename+" not found"

    pyplot.legend(loc='upper right', shadow=True, fontsize='medium')
    pyplot.savefig(os.path.join(work_dir,'blue.eps'))


def cider_plot(argv):
    colors = ['#FC474C','#8DE047','#FFDD50','#53A3D7']
    max_x = 0
    max_y = 0

    column_num = 5 #cider = 5, blue4=6, ..., ROUGE= 10,METEOR=11
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
                axes.set_xlim([xmin, max_x])
                pyplot.xlabel('Iter')
                pyplot.ylabel('CIDEr')
                pyplot.title('')

            if data[init_val:,column_num].max() > max_y:
                max_y = data[init_val:,column_num].max()
                axes.set_ylim([0, max_y])

            if data[init_val:,0].max() > max_x:
                max_x = data[init_val:,0].max()
                axes.set_xlim([0, max_x])

            pyplot.plot(data[init_val:,0], data[init_val:,column_num], linewidth=2, label=filename, color=colors[i])
        else:
            print "file: "+work_dir+filename+" not found"

    pyplot.legend(loc='lower right', shadow=True, fontsize='medium')
    pyplot.savefig(os.path.join(work_dir,'cider.eps'))

def rouge_plot(argv):
    colors = ['#FC474C','#8DE047','#FFDD50','#53A3D7']
    max_x = 0
    max_y = 0

    column_num = 10 #cider = 5, blue4=6, ..., ROUGE= 10,METEOR=11
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
                axes.set_xlim([xmin, max_x])
                pyplot.xlabel('Iter')
                pyplot.ylabel('ROUGE')
                pyplot.title('')

            if data[init_val:,column_num].max() > max_y:
                max_y = data[init_val:,column_num].max()
                axes.set_ylim([0, max_y])

            if data[init_val:,0].max() > max_x:
                max_x = data[init_val:,0].max()
                axes.set_xlim([0, max_x])

            pyplot.plot(data[init_val:,0], data[init_val:,column_num], linewidth=2, label=filename, color=colors[i])
        else:
            print "file: "+work_dir+filename+" not found"

    pyplot.legend(loc='lower right', shadow=True, fontsize='medium')
    pyplot.savefig(os.path.join(work_dir,'rouge.eps'))

def meteor_plot(argv):
    colors = ['#FC474C','#8DE047','#FFDD50','#53A3D7']
    max_x = 0
    max_y = 0

    column_num = 11 #cider = 5, blue4=6, ..., ROUGE= 10,METEOR=11
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
                axes.set_xlim([xmin, max_x])
                pyplot.xlabel('Iter')
                pyplot.ylabel('METEOR')
                pyplot.title('')

            if data[init_val:,column_num].max() > max_y:
                max_y = data[init_val:,column_num].max()
                axes.set_ylim([0, max_y])

            if data[init_val:,0].max() > max_x:
                max_x = data[init_val:,0].max()
                axes.set_xlim([0, max_x])

            pyplot.plot(data[init_val:,0], data[init_val:,column_num], linewidth=2, label=filename, color=colors[i])
        else:
            print "file: "+work_dir+filename+" not found"

    pyplot.legend(loc='lower right', shadow=True, fontsize='medium')
    pyplot.savefig(os.path.join(work_dir,'meteor.eps'))

def time_plot(argv):
    colors = ['#FC474C','#8DE047','#FFDD50','#53A3D7']
    max_x = 0
    max_y = 0

    column_num = 2
    for i,filename in enumerate(argv):
        file_path = os.path.join(work_dir,filename)
        if os.path.exists(file_path):
            data = genfromtxt(file_path,delimiter=',')

            # init_val = 0
            # if i==0:
            #     fig = pyplot.figure(figsize=(6, 6))
            #     axes = pyplot.gca()
            #     pyplot.grid()
            #
            #     max_y = data[init_val:,column_num].max()
            #     max_x = data[init_val:,0].max()
            #
            #     axes.set_ylim([0, max_y])
            #     axes.set_xlim([xmin, max_x])
            pyplot.xlabel('Iter')
            pyplot.ylabel('TIME')
            pyplot.title('')
            #
            # if data[init_val:,column_num].max() > max_y:
            #     max_y = data[init_val:,column_num].max()
            #     axes.set_ylim([0, max_y])
            #
            # if data[init_val:,0].max() > max_x:
            #     max_x = data[init_val:,0].max()
            #     axes.set_xlim([0, max_x])

            values, base = np.histogram(data[:,column_num], bins=40)
            cumulative = np.cumsum(data[:,2])
            pyplot.plot(data[:,0],cumulative , linewidth=2, label=filename, color=colors[i])
            print filename+' '+str(cumulative[-1])

            # pyplot.plot(base[:-1], cumulative, c='green')
            # pyplot.plot(data[init_val:,0], data[init_val:,column_num], linewidth=2, label=filename, color=colors[i])
        else:
            print "file: "+work_dir+filename+" not found"

    pyplot.legend(loc='upper left', shadow=True, fontsize='medium')
    pyplot.savefig(os.path.join(work_dir,'time.eps'))

if __name__=="__main__":
    work_dir = sys.argv[1]
    plot_type = sys.argv[2]

    if plot_type == 'loss': #training loss
        loss_plot(sys.argv[3:])
    if plot_type == 'ppl2': #training ppl2
        ppl2_plot(sys.argv[3:])
    if plot_type == 'val': #val ppl2
        val_plot(sys.argv[3:])
    if plot_type == 'bleu':
        bleu_plot(sys.argv[3:])
    if plot_type == 'cider':
        cider_plot(sys.argv[3:])
    if plot_type == 'rouge':
        rouge_plot(sys.argv[3:])
    if plot_type == 'meteor':
        meteor_plot(sys.argv[3:])
    if plot_type == 'time':
        time_plot(sys.argv[3:])
