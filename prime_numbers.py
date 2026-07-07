#Check whether a number is prime or not
# def is_prime(num):
#     if num>1:
#         for i in range(2,num):
#             if num%i==0:
#                 return f"{num} is not a prime number"
#         return f"{num} is a prime number"
# result=is_prime(int(input("Enter a number:")))        
# print(result)

#print nth prime number and count of prime numbers between 1 and n
# num=int(input("Enter a number:"))
# count=0
# for i in range(2,num):
#     for j in range(2,i):
#         if i%j==0:
#             count+=1
#             break
#     else:
#         print(i)
# print(f'The count of prime numbers between 1 and {num} is {count}')  

#print nth prime number if the given number is prime
num=int(input("Enter a number:"))
for nums in range(2,num+1):
    for i in range(2,int(nums**0.5)+1):
        if nums%i==0:
            break
    else:
        print(nums)