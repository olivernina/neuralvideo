# neuralvideo


Generators options are: lstm,  icoupled, noinput, gru.

For instance for using clstm use:

python driver.py --dataset youtube2text --generator lstm --outdir results

To get the numbers use:

python eval_sentence_predictions.py results/model_checkpoint
