
# Python program to display all the prime numbers within an interval

#Limits of the interval
lower = 1
upper = 100

print("Prime numbers between", lower, "and", upper, "are:")

# Iterate through all numbers of the interval
for num in range(lower, upper + 1):
   # All prime numbers are greater than 1
   if num > 1:
       #Check if the numbers is divisible by any number less than itself
       for i in range(2, num):
           if (num % i) == 0: #If it is divisible it is not prime
               break
       else:#If it is not divisible is prime
           print(num)
