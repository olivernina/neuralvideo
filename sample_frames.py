__author__ = 'oliver'

import os
src_dir = '/media/SSD/projects/datasets/youtube2text/frames'
dirs = os.listdir(src_dir)
frames_sampled = []
for dir in dirs[1:10]:
    frames = os.listdir(os.path.join(src_dir,dir))
    frames.sort()
    frame_sampled = os.path.join(src_dir,dir,frames[len(frames)/2])
    frames_sampled.append(frame_sampled)


open('./frames.txt', 'w').close()
for frame in frames_sampled:
    if frame.endswith('.jpg') or frame.endswith('.png'):
        # if counter >= frameFreq:
        print frame
        with open('./frames.txt', 'a') as textfile:
            textfile.write(frame + '\n')
        # counter = 0
        # counter += 1

