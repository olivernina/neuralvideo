# neuralvideo


Generators options are: lstm,  icoupled, noinput, gru.

For instance for using clstm use:

python driver.py --dataset youtube2text --generator lstm --outdir results

To get the numbers use:

python eval_sentence_predictions.py results/model_checkpoint

#Installation

run the create_dataset.py script and modify the path to the videos and the videdesceng.csv which is the video description corpus that comes with the dataset and should be downloaded separate from the videos themselves at 
http://research.microsoft.com/en-us/downloads/38cf15fd-b8df-477e-a4e4-a4680caa75af/default.aspx
The link to the dataset is http://www.cs.utexas.edu/users/ml/clamp/videoDescription/
