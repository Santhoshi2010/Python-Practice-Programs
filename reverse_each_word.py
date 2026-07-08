# Reverse Each Word
# Write a Python program that takes a sentence as input and reverses each word
# individually while keeping the words in the same order.
# Input :
# hello world python
# Output :
# olleh dlrow nohtyp

sentence=input("Enter a sentence: ")
words=sentence.split() 
# print(word) #['hello', 'world', 'python']
result=[]
for word in words:
    result.append(word[::-1])
# print(result)  #['olleh', 'dlrow', 'nohtyp']  
print(" ".join(result))






