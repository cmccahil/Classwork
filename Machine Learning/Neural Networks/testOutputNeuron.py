import math

def sigmoid(x): #applies the sigmoid function
    return 1 / (1 + math.exp(-x))

weights = [0.08768039351619761, 0.0031839961177084486, 0.0003889229007292106, 0.0066577182589784125, 0.07690492159270691, 0.04640035625539198, 0.09289548590639991, -0.05595053121979827, -0.03519140062641561, 0.02775422283948122, 0.04569650495957419, 0.06166717615145095, -0.059641496142497204, -0.04344274002504324, -0.042133058146789505, -0.03425122571289065, -0.0949704924405373, -0.030893775363591724, 0.03135390564389008, 0.06162407758247504]
inputs = [0.4579692404592136, 0.5122173757809478, 0.46753281386609413, 0.5162220923595878, 0.47187936588816276, 0.49776517041337026, 0.5305961340663223, 0.5208901751136766, 0.415937141549188, 0.5418419251175046, 0.4848408076270898, 0.5128104292278338, 0.48385954093248645, 0.541186633880114, 0.43668118559347496, 0.4208370263556102, 0.4836348306928165, 0.4727581618467189, 0.48047315584594485, 0.511397509153302]
wZero = 0.0010051878433499932

result = 0 
for i in range(0,len(weights)):
    result += weights[i]*inputs[i]
result += wZero
print(sigmoid(result))