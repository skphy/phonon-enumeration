#radix_num_generator.py
#import needed modules

def factorial(num):
#If the number provided is zero then the factorial is 1
	if num == 0:
		fact = 1
#Otherwise set fact to 1 and begin finding the factorial r is used to find each
#num-n for n=0 to n=num each value in r is then used to compute the factorial
	else:
                fact = 1
                r = range(1,num+1)
                for i in r:
                        fact *= i
	return fact

#This method finds a binomial coefficient that is it calculates n choose r
#The method calls for two integer values n and r and the method factorial
#The method returns the binomial factorial as result
def binomial_coefficient(n,r):
#If r is less than zero then the binomial coefficient is zero
	if r < 0:
		result = 0
#Otherwise use the factorial method to calculate the binomial coefficient n!/r!/(n-r)!
	else:
		result = factorial(n) / factorial(r) / factorial(n-r)
	return result

#This method generates the radix numbers for a given aray. It calls for number_of_each_color and
#number_of_slots. number_of_each_color is an array of integers indicating the number of times each
#color is found in the array. number_of_slots is an integer, it should be equal to the sum of the
#number_of_each_color array. It returns an array of radix numbers
def Coefficients(number_of_each_color,number_of_slots):
#renaims variables for convience and creates an empty array
	Coe = []
	for i in range(0,len(number_of_each_color)):
#Uses the binomial_coefficient method to build an array of radix numebrs
		Coe.append(binomial_coefficient(number_of_slots,number_of_each_color[i]))
		number_of_slots -= number_of_each_color[i]
	return Coe

#This method generates numerical labels for each color in the provided array. It calls for 
#listi and number_of_each_color, and returns an array of integers. listi is an array of integers

def hash(listi):
#an empty array for storage
        m = len(listi)
        #this loop goes through this process for each color in number_of_each_color
        y = 0
        k = listi.count(1)
        #for each occurance of the color in the array a counter is increased
        for i in range(0,m):
                #uses the binomial_coefficient method to generate the label using information from the array
                y += binomial_coefficient(m-1-i,k-1)
#appends the lable to the output array
        return(y)


def hash(listi,number_of_each_color):
#an empty array for storage
	X = []
	num = 1
	for j in range(0,len(number_of_each_color)):
#this loop goes through this process for each color in number_of_each_color
		m = len(listi)
		y = 0
		for i in range(0,m):
			k = 0
#finds out if the desired color is in a portion of the array
			if listi[i] != num and num in listi[i:m]:
				for z in range(len(listi[i:m])-1,0,-1):
					if listi[z+i] == num:
#for each occurance of the color in the array a counter is increased
						k += 1
#uses the binomial_coefficient method to generate the label using information from the array
				y += bc.binomial_coefficient(m-i-1,k-1)
#appends the lable to the output array
		X.append(y)
#this code removes the desired color form the array and creates a new shorter 
#array for conitnued computation
		listi[:] = (value for value in listi if value != num)
		num += 1
	return(X)


#This method calls for Coefficients and Xi and returns a unique identification number
#for an array called idh. The Coefficients is an array of integers, it can be generated from the
#Coefficients method above, Xi is also an array of integr labelings which can be generated from
#hash method above. idh is returned as an integer value 
def idnum(Coefficients,X):
#Change variable names for convience
	idh = 0
	for i in range(len(X)-1,-1,-1):
#perfrom computation on elements for both arrays such that
#X1+C1(X2+C2(X3+C3(X4.....))) is computed
		if i == len(X):
			idh = X[i]*Coefficients[i-1]
		elif i == 0:
			idh += X[i]
		else:
			idh += X[i]
			idh *= Coefficients[i-1]
	return(idh)

def binomial(listi):
#this loop goes through this process for each color in number_of_each_color
	m = len(listi)
	y = 0
	for i in range(0,m):
		k = 0
#finds out if the desired color is in a portion of the array
		if listi[i] != 1 and 1 in listi[i:m]:
			for z in range(len(listi[i:m])-1,0,-1):
				if listi[z+i] == 1:
#for each occurance of the color in the array a counter is increased
					k += 1
#uses the binomial_coefficient method to generate the label using information from the array
			y += binomial_coefficient(m-i-1,k-1)
#appends the lable to the output array
	return(y)
#col = [4,2,2]

#print(idnum([210,15,6,1],[18,12,0]))

