# hw5-authors
HW5: Colin McCahill and Shomya Mitra

This assignment was interesting--it required us to think about the details of implementation more than previous ones because the pseudocode was much more general than neural networks, for example. However, this also meant we were unsure if we were implementing it correctly, which may be why our accuracies were low.

We each spent a few hours on this assignment.

We adhered to the Honor Code on this assignment.

1. a. Our accuracy was 46%. The confidence interval is [0.322, 0.598]  
   b. The hypothetical program would have an accuracy of 10%, and its interval would be [0.017, 0.183]  
   c. Our program is statistically significantly better. This implies the learning made the program more accurate, even though it wasn't as accurate as other models we've implemented.  
   d. To make it better, the program could consider not just the overall proportions of how often each author uses each word, but also which words tend to follow other words. Other possibilities include length of sentences, paragraphs, and chapters, and use of certain tenses or punctuation.  
2. a. Recalls:  
    Carroll: 40%  
    Tolstoy: 40%  
    Dickens: 40%  
    Austen: 60%  
    Shakespeare: 40%  
    Doyle: 40%  
    Homer: 40%  
    Plato: 60%  
    Kafka: 80%  
    Wells: 80%  
   b. It best identified Kafka and Wells and the rest were mostly uniform.  
3. a. Precisions:  
    Carroll: 25%  
    Tolstoy: 50%  
    Dickens: 25%  
    Austen: 43%  
    Shakespeare: 67%  
    Doyle: 33%  
    Homer: 50%  
    Plato: 60%  
    Kafka: 80%  
    Wells: 44%  
    b. Our program most often predicted Wells and Austen and least frequently predicted Tolstoy and Shakespeare. However the most authors it predicted the most when it shouldn't have were Dickens and Carroll.  
    c. There weren't too many trends between recall and precision. Kafka had the best recall and precision but between the other authors it wasn't too consistent.  
4.  Our program often predicted Austen for books by Dickens or Austin, which makes sense because they were both English authors writing realistic fiction within 80 years of each other, so their books probably read slightly similarly. Another result I find makes sense is the fact that it did was accurate when predicting Wells. Since our implementation only accounts for the words used, and Wells was writing science-fiction, he would have used many words that no one else on the list would have. I was also not surprised by the accuracy on Plato because he was writing philosophy and the rest of the authors were writing fiction, so his word usage would also have been different.  
HW5: Predict the Author (Text Classification)

In this assignment, your goal is to write a program capable of competing in a simplified game of Jeopardy!® where the only category asks for the author of a given passage originally written by a famous author.  For your program, you will train and test Naïve Bayes as a text classifier using text downloaded from Project Gutenberg.  In particular, you will download popular, famous books from 10 authors, train Naïve Bayes to learn the writing styles (indicated by word choices) of each author from those texts, then predict which author wrote 50 short passages (taken from different texts than those you used for training).

We will be using texts freely available on Project Gutenberg (https://www.gutenberg.org/wiki/Main_Page).  The passages from the test set are taken from the following books: Sense and Sensibility by Jane Austen, Through the Looking-Glass by Lewis Carroll, A Tale of Two Cities by Charles Dickens, The Return of Sherlock Holmes by Arthur C. Doyle, The Iliad by Homer, Metamorphosis by Franz Kafka, Apology by Plato, War and Peace by Leo Tolstoy, and The Time Machine by H. G. Wells.

The Java helper code makes use of the open source Lucene project (https://lucene.apache.org/, version 6.2.1) by Apache (), which is released under the Apache 2.0 license.  The Python helper code makes use of the open source NLTK project (http://www.nltk.org/, version 3.2.1), which is also released under the Apache 2.0 license.  The Python helper code also makes use of the english.pickle tokenizer by punkt (which is included, but can be alternatively downloaded using NLTK’s downloading function nltk.download(“punkt”)).  All credit to Apache, NLTK, and punkt for their code and libraries. 
