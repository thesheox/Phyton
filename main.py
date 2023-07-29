# Get three inputs on separate lines
'''''
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# Calculate the sum and divide by three
result = (num1 + num2 + num3) / 3

# Print the result
print("The average is:", result)

number_range1=int(input("from : "))
number_range2=int(input("to : "))
count=0
nc=number_range2
check_num=False
for i in range(number_range1,number_range2):
    copy=i
    copy2=i
    copy3=i
    left=i
    right=0
    length=0
    while(copy>0):
        copy=int(copy/10)
        length+=1

    if(length%2==0):
        f=int(length/2)
        k=pow(10,f)
        left=int(left/k)

    else:
        continue


    j=0
    for i in range(0,f):
        right+=int(copy2%10)*(pow(10,j))
        copy2=int(copy2/10)
        j+=1


    if(left==right):
        count+=1
        print("left : "+str(left)+" right : "+str(right)+" number : "+str(copy3))

print(count)


input=input("enter a number ")
length=len(input)
print(length)
n=int(length/3)
k=3
for i in range(0,n):
    input=input[:k]+","+input[k:]
    k=k+3
    k+=1
print(input)

import random

guess = random.randint(1, 1000000)
count=0
while True:
    user_input = int(input("Enter your guess (enter 0 to exit): "))

    if user_input == 0:
        print("Exiting the game.")
        print("Not Possible"+" number was : ")
        print(guess)
        break
    elif user_input > guess:
        print("Your guess is too high. Try again.")
    elif user_input < guess:
        print("Your guess is too low. Try again.")
    else:
        print("Congratulations! Your guess is correct."+str(guess))
        break

    count+=1
print("number of gusses : "+str(count))


input1=input("enter a ")
input2=input("enter b ")
count=0
for i in range(int(input1),int(input2)):
    #print(str(i) + " : ")
    count=0
    for j in range(1,i+1):
        if(i%j==0):
            # print(j)
            count+=j
    if(count>2*i):

        print("num : "+str(i)+" sum : "+str(count))

import sympy as sympy


from sympy import primerange
count=0
maghsom=[]
couter=[]

num=int(input("enter a number "))
for i in range(1,num+1):
    if num%i==0:
        count+=1
        maghsom.append(i)


primes = list(primerange(1, num))

for i in range(0,len(primes)):
    couter.append(0)
print(primes)
index=0
for i in primes:
    while num%i==0:
        couter[index]+=1
        num=num//i
    index+=1


#print(maghsom)
print(max(couter),count)
#print(couter)



fib = []
avali = 1
dovomi = 1
damane1=1
damane2=2000000
damane = damane2-damane1

fib.append(avali)
index = avali


from itertools import product

def generate_permutations_with_repetitions(numbers, length):
    all_permutations = list(product(numbers, repeat=length))
    return all_permutations

# Example usage:
rangee=int(dovomi-avali+1)
adad=[]
a=avali
for i in range(0,rangee):
    adad.append(a)
    a += 1
counter=0
numbers = adad
length = 2
tedad=pow(dovomi-avali+1,2)
all_permutations = generate_permutations_with_repetitions(numbers, length)
for i in range(0,tedad):
    fib0 = []
    fib0.append(all_permutations[i][0])
    index = all_permutations[i][1]
    for i in range(2, 50):
        fib0.append(index)
        index = fib0[i - 1] + fib0[i - 2]

    print(fib0)

    fib_num=[]
    x = 0
    j = 0
    while  j < len(fib0)-1:
        if x==0:
            x =int(str(fib0[j]) + str(fib0[j+1]))
        else:
            x=int(str(x)+str(fib0[j+1]))
        j += 1
        if damane2 >= x >= damane1:
            fib_num.append(x)
            counter+=1

    print(fib_num)

print("teadad: "+str(counter))



num = []
num.append(12)
adad = str(345678910111213141516171819202122)
index = int((int(len(adad)) - 1) / 2)
j=2
while j<len(adad):
    while True:
        x = int(adad[:j])
        if x > int(num[-1]):
            num.append(x)
            adad = adad[j:]
            j=2
            break
        j += 1


print(num)
k=int(input("enter komin adad you want "))
print(num[k-1])

number = "012345123690"
num_list = []

for i in range(len(number)):
    for j in range(len(number)):
        substring = number[i:j + 1]
        num_list.append(substring)


num_acc=[]
for i in range(len(num_list)):
    num_str = str(num_list[i])
    is_ascending = True
    for i in range(1, len(num_str)):
        if num_str[i] < num_str[i - 1]:
            is_ascending = False
            break

    if is_ascending:
        num_acc.append(num_str)


num_len=[]
for i in range(0,len(num_acc)):
    num_len.append(len(str(num_acc[i])))

print(max(num_len))

amelha = input()
amelha_list = amelha.split()

tavan1 = input()
tavan1_list = tavan1.split()

tavan2 = input()
tavan2_list = tavan2.split()

result=[]

if len(amelha_list) == len(tavan1_list) and len(amelha_list) == len(tavan2_list):
    for i in range(len(amelha_list)):
        num = int(amelha_list[i])
        tavan1 = int(tavan1_list[i])
        tavan2 = int(tavan2_list[i])
        min_exponent = min(tavan1, tavan2)
        result.append(pow(num, min_exponent))

else:
    print("Error: The lengths of the lists do not match.")
nahayi=1
for i in range(len(result)):
    nahayi=nahayi*result[i]
print(nahayi)

'''''
number = input("enter a number")
digit_to_count = "1"


number_str = str(number)


count_ones = number_str.count(digit_to_count)


print(count_ones)
