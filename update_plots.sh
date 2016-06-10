#python plot_graphs.py results_metrics/ time lstm.csv clstm.csv noinput.csv iorem.csv
#display results_metrics/time.png

python plot_graphs.py results_metrics/ loss LSTM.csv CLSTM.csv NI.csv NIO.csv
display results_metrics/loss.eps

python plot_graphs.py results_metrics/ ppl2 LSTM.csv CLSTM.csv NI.csv NIO.csv
display results_metrics/ppl2.eps

python plot_graphs.py results_metrics/ val LSTM_val.csv CLSTM_val.csv NI_val.csv NIO_val.csv
display results_metrics/val.eps

python plot_graphs.py results_metrics/ bleu LSTM_val.csv CLSTM_val.csv NI_val.csv NIO_val.csv
display results_metrics/blue.eps

#python plot_graphs.py results_metrics/ cider lstm_val.csv icoupled_val.csv 
#display results_metrics/cider.png

#python plot_graphs.py results_metrics/ rouge lstm_val.csv icoupled_val.csv 
#display results_metrics/rouge.png

#python plot_graphs.py results_metrics/ meteor lstm_val.csv icoupled_val.csv 
#display results_metrics/meteor.png
