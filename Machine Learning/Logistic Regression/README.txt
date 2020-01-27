1. Using seed 12345

   monks1.csv: 
	-Accuracy 78.16%
	-Confidence interval = [0.6948,0.8684]
   seismic.csv:
	-Accuracy 93.42%
	-Confidence interval = [0.9128,0.9556]
   banknotes.csv:
	-Accuracy 95.99%
	-Confidence interval = [0.9367,0.9831]
   occupancy.csv:
	-Accuracy 98.91%
	-Confidence interval = [0.9859,0.9923]

2. Using seeds: [1,5,6,10,20,33,554,3,6,59,2,19,4,58,59,62,88,90,95,200,201,202,203,220,
222,223,250,300,340,333]

monks1.csv:
	-Average Accuracy 74.14%
	-This falls within the confidence interval
	-26 out of the 30 seeds fell within the confidence interval. This did not match my expectation.

banknotes.csv:
	-Average Accuracy 95.79%
	-This falls within the confidence interval
	-All 30 seeds were in the confidence interval. This matched my expectation. 

occupancy.csv
	-Average Accuracy 98.87%
	-This falls within the confidence interval
	-One seed was outside the confidence interval. This matched my expectation.

seismic.csv
	-Average Accuracy 93.11%
	-This falls within the confidence interval
	-One seed was outside the confidence interval. This matched my expectation.

3. 
b. In the beginning the algorithm learns very quickly and improves its accuracy rapidly. Once the number of epochs 
reaches about 50, the learning curve slows considerably. All of the seeds produced very similar results, with the
exception with two or three of the seeds which actually did reach 99 percent accuracy, and they stopped learning
producing a slightly different looking graph. 
c. These results imply that a logistic regression algorithm produces a logistic regression looking graph. It implies
that this algorithm produces very good results, especially in the beginning, but once its accuracy reaches a certain
percentage, it can no longer learn anymore and the results stay the same. The graph will flatten out once this happens.

My experience: The hardest part about this assignment was implementing the algorithm. I had one bug which took me about 
two hours to find. The bug ended up being that the weights were changing in the wrong direction because I was feeding the 
change in weights equation the actual weight coefficients instead of the training weights for the given training sample. 
The panda library took me awhile to figure out how to implement and use, but once I started using it, it made things
a bit more simple, especially with the data preprocessing. 

Time spent on assignment: Around 8-9 hours. A 2 or 3 hours was waiting for the data to compute for the README.

Honor Code: "I affirm that I have adhered to the honor code in this assignment." -Colin McCahill


   