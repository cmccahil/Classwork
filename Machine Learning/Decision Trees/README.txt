Colin McCahill, Shomya Mitra

Research Questions:
1. Seed 750, Training Percentage: 75%
	a. Iris Accuracy: 92.11%
	   Monks1 Accuracy: 96.30%
	   Occupancy Accuracy: 98.87%
	   opticalDigit Accuracy: 59.77%
	b. Iris Confidence Interval: [.8356,1]
	   Monks1 Confidence Interval: [.9274,.9986]
	   Occupancy Confidence Interval: [.9858,.9916]
	   opticalDigit Accuracy: [.5722,.6235]

2a. Rules that the tree learns: Jacket color, head shape, body shape,
    is_smiling, holding
b.  It correctly learns the jacket color and it will predict 1 if the jacket 
    color is red. It does a very good job of predicting 1 if the head shape
    and body shape are the same. The only thing it gets bogged down by for 
    some reason is the "holding" and "is_smiling" variable if the jacket color
    is green. 

3a. Accuracy: 30.53%
b. Confidence Interval: [.2813,.3294]
c. The numeric categorization works nearly twice as well compared to when there is
   no numeric comparisons (or thresholds). The confidence interval is in the high
   50s and low 60s when using thresholds compared to high 20s and low 30s when not. 
   What this implies is that when dealing with numeric or continuous attributes, it 
   is necessary to implement thresholds into trees or other Cart/C4.5 methods because 
   treating the attributes like they are categorical does not work nearly as well. 

README Questions:
3. This assignment was a bit easier to implement than the last one. I enjoyed figuring 
   out the pseudocode and implementing the ID3 algorithm. It was also cool seeing my code
   in action, printing out a tree using the algorithm I implemented, and working well on the
   datasets. We are a bit curious about opticalDigit. It runs differently than the other 
   datasets, takes much longer and the accuracy was not as high as we had hoped for. Maybe there 
   is some small bug in the code that you can find that explains why it does not run as well as 
   the other datasets. 

4. We each spent around 12-15 hours on the assignment.
5. "We affirm that we have adhered to the honor code in this assignment." 


