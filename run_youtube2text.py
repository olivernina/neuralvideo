__author__ = 'oliver'

import create_dataset
import get_predictions
import eval_tools.metrics

dataset = 'youtube2text'
algName = '10frames'
total_num_samples = 2000
samples_per_video=10

# create_dataset.youtube2text(total_num_samples,samples_per_video,dataset)
get_predictions.run('cv/model_checkpoint_youtube2text_oliver-Aurora-R4_baseline_15.26.p',dataset,algName)
# get_predictions.run('cv/model_checkpoint_youtube2text_oliver-Aurora-R4_baseline_10.49.p',dataset,algName)
# get_predictions.run('cv/model_checkpoint_youtube2text_oliver-Aurora-R4_baseline_37.54.p',dataset,algName)
eval_tools.metrics.run(dataset,algName)