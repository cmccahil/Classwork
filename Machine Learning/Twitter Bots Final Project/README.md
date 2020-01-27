Note: Our Tweet data file was way too big to upload to GitHub because of their file size limits. It is on Google Drive and can be found here:
https://drive.google.com/file/d/1oEF5fQNAML5GSaybnzWE9IFSOVewaQZI/view?usp=sharing

This project contains three programs:

1. neural_network.py
   Usage: python3 neural_network data_file hidden_neurons learning_rate threshold training_percent seed title_of_results_file
   
   This program takes as input account data and classifies them as bots, social spambots, or traditional spambots.
   It writes its results to a results file, including the accuracy of each epoch.
   
2. decision_tree.py
   Usage: python3 decision_tree data_file title_of_results_file training_percent seed
   
   This program also takes as input account data and classifies them as bots, social spambots, or traditional spambots.
   It writes its results to a file, but without epoch data (since there are no epochs)
   
3. naive_bayes.py
   Usage: python3 naive_bayes data_file

   This program takes as input Tweet data and determines whether each Tweet came from a genuine account, social spambot, or traditional spambot.

Original data set found here by clicking on the "cresci-2017" data set: https://botometer.iuni.iu.edu/bot-repository/datasets.html
The assemblers of this data put each category in individual files, which we then had to label and combine into single data files to feed to our algorithms.
This combined data is found in our Tweet data.csv and account data.csv files.