1. Using seed 12345, and training set percentage 75%, 
the accuracy of:
monks1.csv = 73%
iris.csv = 97%
mnist_100 = 87% 
mnist_1000 = 94%

2. The lower end of the confidence interval for monks1 is .73 - .08686
= 64%. The upper end of the confidence interval is 82%. 

The lower end of the confidence interval for iris is 
.97 - .0509 = 92%. The upper end of the confidence interval is
100%. 

The lower end of the confidence interval for mnist_100 is 
.872 - .0414 = 83%. The upper end of the confidence interval is 
.872 + .0414 = 91%. 

The lower end of the confidence interval for mnist_1000 is .9436 - .0452
= 90%. The upper end of the confidence interval is .9436 + .0452 = 99%

3. mnist_1000 definetly had the higher accuracy/average. I believe the higher 
accuracy resulted from a much larger sample size, and that k-nearest 
neighbor has a pretty high accuracy with larger sample sizes on this 
type of data set. The overlapping confidence intervals suggests that it
is possible that the two statistics are not significantly different, or that
the difference is not statistically significant.

4. Using Iris.cv, and k values of 1,5, and 7: changing k around did not change
the value of the accuracy much. When k was 7, it miscalculated one prediction,
thus the accuracy went down 2 percent to 95%. My theory for the decrease in
accuracy is because when you increase k, the areas predicting each class will be
more "smoothed" because the majority of k-nearest neighbors decide the class of
any point. Thus areas on a graph with higher complexity when smoothed out into 
less complex boundaries will result in lower accuracy. 

5. Using seeds 7, 25, 9, 54, 100, 59, 420, 69, 10, and 4 I came up with the
following accuracies respectively:
92%, 95%, 97%, 100%, 97%, 95%, 97%, 92%, 100%, and 97%

Sepallength and sepalwidth: 76%, 76%, 67%,84%,74%,71%,63%,76%,63%,71%
Sepallength and petallength: 92%, 84%,87%, 95%, 95%,95%,100%,89%,95%,89%
Sepallength and petalwidth: 89%, 95%,95%, 87%, 95%,95%,97%,95%,97%,97%
Sepalwidth and petallength: 92%, 89%,79%,97%,87%,84%,95%,89%,89%,97%
Seaplwidth and petalwidth: 95%,95%,92%,97%,95%,95%,92%,89%,97%,95%
Petallength and petalwidth: 97%,92%,97%,100%,97%,95%,100%,97%,100%,97%

The best pair of attributes when determining the flower species is Petallength and 
petalwidth, showing that the petal is more of a defined attribute between the species
than the sepal. 

OTHER README QUESTIONS

Paragraph: I really enjoyed the coding portion of this assignment. There was a bit of
confusion for me on how to start this project, and I didn't immediatly realize that 
hamming distance was there specifically for monks1.csv until I actually figured out
what hamming was. The readme was a bit tedious but important for my understanding of 
knn. 

Time Spent: Around 9-10 hours

Honor Code: "I affirm that I have adhered to the honor code in this assignment."