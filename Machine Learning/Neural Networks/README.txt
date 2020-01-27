3c. All of the learning rates for the training sets cause the accuracies to go up and down. .1 reaches its plateua the fastest, but it's change in accuracy can vary quite a bit 
for each epoch on its ascent. .001 reaches its plateua the slowest, and its changes in accuracy are very minimal epoch to epoch. The best learning rate is 0.01 because its accuracy
does not dip tremendous amounts like the other learning rates, and it has the best overall final accuracy. What this implies about choosing a learning rate is that if you want to
reach an accuracy plateau in the shortest amount of epochs you choose a larger learning rate, but expect more dips and falls in accuracy of your training set. If you want a better
final prediction accuracy of your training set you make the learning rate smaller, but not too small. 

d. The validation set accuracy is ultimately dependent on the training set accuracy, but a couple of differences I noticed: The 0.001 learning rate has a very steady ascent for the
validation set accuracy, the 0.01 learning rate has a quick ascent to a very high validation set accuracy but it ultimately declines to a mediocre validation set accuracy because it 
is dependent on the training set (which has a higher accuracy despite the validation set having a lower accuracy). The .1 learning rate has overall a pretty good final accuracy but in
its ascent the accuracy can rise and fall quite a bit. I don't believe the learning rate has a tremendous effect on the validation set accuracy, the learning rate has more of an effect
on the training set which in turn has an effect on the validation set. The best accuracy came from .1 learning rate, but also .001 also had a pretty good accuracy it just reached this
final accuracy much slower. So if I wanted the best possible accuracy for the validation set (which I would rather have a higher training accuracy since it is a larger set), I would
choose a .1 learning rate because it reaches the highest accuracy the fastest and the accuracy does not decline like the other learning rates. 

4a. Accuracies for
	.05 = 6.18%
	.1 = 91.12%
	.5 = 94.02%
	.9 = 94.02%
b. Recalls for
	.05 Recall1 = 100%
	    Recall0 = 0.21%
	.1 Recall1 = 3.23%
	   Recall0 = 96.71%
	.5 Recall1 = 0%
	   Recall0 = 100%
	.9 Recall1 = 0%
	   Recall0 = 100%
	.95 Recall1 = 0%
	    Recall0 = 100%
c. None of these thresholds are very good at all. None of them really accurately predict a seismic event, however if I were to choose I would choose threshold .1 because if there is a 
prediction of a seismic event at this threshold there is a very small possibility that this prediction may be right.

README questions:
1. Colin McCahill, Shomya Mitra
3. Our experience during the assignment was difficult. Answering all the questions and implementing
the parsing and neural network was fine, but we struggled to debug the algorithm and we were not quite
able to figure out what was wrong with it. We believe it has something to do with the output neuron 
because the output neuron will always give an activation that never varies by more than .001. It probably 
is that or perhaps we implemented the feedbacks incorrectly? We are interested to see what we did wrong 
because we are stumped and will perhaps come in during office hours to figure out what was wrong with the 
implementation. 
4. We spent approximately 15 hours on this assignment each. 
5. "We affirm that we have adhered to the honor code in this assignment"
 
 