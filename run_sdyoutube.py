__author__ = 'oliver'

import create_dataset
import get_predictions
import eval_tools.metrics

dataset = 'sdyoutube'
# dataset = 'youtube2text'
algName = '10frames'
total_num_samples = 1000
samples_per_video=10
out_dir = 'data/sdyoutube/results'


create_dataset.sdyoutube(total_num_samples,samples_per_video,dataset,extract_features=True)
get_predictions.run('results_metrics/model_lstm_checkpoint_sdyoutube_oliver-Aurora-R4_baseline_483.67.p',dataset,algName,num_sent=1)
# get_predictions.run('cv/model_checkpoint_youtube2text_oliver-Aurora-R4_baseline_10.49.p',dataset,algName)
# get_predictions.run('cv/model_checkpoint_youtube2text_oliver-Aurora-R4_baseline_37.54.p',dataset,algName)
eval_tools.metrics.run(dataset,algName,out_dir)

# get_predictions.run('results_metrics/model_icoupled_checkpoint_sdyoutube_oliver-Aurora-R4_baseline_1.01.p',dataset,algName,num_sent=1)
# eval_tools.metrics.run(dataset,algName,out_dir)