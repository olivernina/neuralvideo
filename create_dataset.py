__author__ = 'oliver'
import csv
import json
import os
import process_frames
import subprocess

labels_file = '/media/SSD/projects/datasets/youtube2text/viddesceng.csv'


def youtube2text(total_num_samples,samples_per_video,dataset):
    samples = list()
    counter = 0

    # json_file = open(, 'w')
    # json.dump(samples, json_file)
    # json_file.close()

    json_file = 'data/'+dataset+'/dataset.json'
    frames_file = 'data/'+dataset+'/frames.txt'
    json_ann = 'data/'+dataset+'/captions_val.json'

    create_dataset = True
    img_id = 0
    sent_id = 0
    images = list()
    if create_dataset:
        open(frames_file, 'w').close()
        train_samples = 0
        val_samples = 0
        test_samples = 0

        current_vid = {}
        current_vid['id'] = ''
        annotations = []

        with open(labels_file) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:

                if row['VideoID'].startswith('#'):
                    print 'bad video filename: '+row['VideoID']
                    continue

                print(row['VideoID'], row['Description'])

                # row['Description']=row['Description'].lower()

                if current_vid['id'] == '':

                    current_vid_sentences = []
                    current_vid['id'] = row['VideoID']
                    current_vid['start'] = row['Start']
                    current_vid['end'] = row['End']

                    period_tokenized = row['Description'].replace('.',' .')
                    tokens = period_tokenized.split(' ')
                    current_vid_sentences.append({'tokens': tokens, 'raw': period_tokenized})

                    annotations.append({'image_id':img_id,'id':sent_id,'caption':row['Description']})
                    sent_id = sent_id +1
                    continue

                elif current_vid['id'] == row['VideoID'] :

                    # current_vid_id = row['VideoID']
                    period_tokenized = row['Description'].replace('.',' .')
                    tokens = period_tokenized.split(' ')
                    current_vid_sentences.append({'tokens': tokens, 'raw': period_tokenized})

                    annotations.append({'image_id':img_id,'id':sent_id,'caption':row['Description']})

                else:


                    src_dir = '/media/SSD/projects/datasets/youtube2text/videos'
                    dst_dir = '/media/SSD/projects/datasets/youtube2text/frames'
                    # video_name = row['VideoID']+'_'+row['Start']+'_'+row['End']+'.avi'
                    video_name = current_vid['id']+'_'+current_vid['start']+'_'+current_vid['end']+'.avi'


                    success = process_frames.get_frames(src_dir,dst_dir,video_name)

                    if success:

                        if total_num_samples > 1900: #Total number of videos in the dataset
                            if counter < 1200:
                                split = 'train'
                                train_samples = train_samples +1
                            elif counter < 1300:
                                split = 'val'
                                val_samples = val_samples +1
                            else:
                                split = 'test'
                                test_samples = test_samples + 1
                        else:

                            if counter%2 == 0:
                                split = 'train'
                                train_samples = train_samples +1
                            elif counter%2 == 1 and counter%3==0:
                                split = 'val'
                                val_samples = val_samples +1
                            else:
                                split = 'test'
                                test_samples = test_samples + 1



                        frames_sampled = process_frames.sample_frames(dst_dir,video_name,samples_per_video)

                        local_file_paths = list()
                        for frame_sampled in frames_sampled:
                            local_file_path = os.path.join(dst_dir,video_name,frame_sampled)
                            local_file_paths.append(local_file_path)

                            with open(frames_file, 'a') as textfile: #this is for getting features
                                textfile.write(local_file_path + '\n')


                        sample = {'sentences':current_vid_sentences,'id':img_id,'imgid':counter,'vidid':row['VideoID'],
                                  'split':split,'frames':frames_sampled,'filename':frames_sampled,'local_file_path':local_file_paths}
                        samples.append(sample)



                        counter = counter +1
                        img_id = img_id + 1
                        annotations.append({'image_id':img_id,'id':sent_id,'caption':row['Description']})

                        if counter > total_num_samples:
                            break

                    current_vid_sentences = []
                    current_vid['id'] = row['VideoID']
                    current_vid['start'] = row['Start']
                    current_vid['end'] = row['End']
                    period_tokenized = row['Description'].replace('.',' .')
                    tokens = period_tokenized.split(' ')
                    current_vid_sentences.append({'tokens': tokens, 'raw': period_tokenized})


                sent_id = sent_id +1


        json.dump({'images':samples}, open(json_file, 'w'))
        json.load(open(json_file, 'r'))


        json.dump({'annotations':annotations,'images':samples,'info':'','type':'captions','licenses':''},open(json_ann,'w'))
        json.load(open(json_ann,'r'))

        print 'train: '+str(train_samples)
        print 'val: '+str(val_samples)
        print 'test: '+str(test_samples)

    extract_features = True
    if extract_features:
        command = 'python python_features/extract_features.py --caffe caffe --gpu --model_def python_features/deploy_features.prototxt --model python_features/VGG_ILSVRC_16_layers.caffemodel --files '+frames_file +' --out vgg_feats.mat'+' --spv '+str(samples_per_video)
        print(command)
        proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, universal_newlines=True)
        while proc.poll() is None:
            line = proc.stdout.readline()
            print(line)
