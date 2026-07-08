# Secret Word Replacement
# Write a Python program that reads a sentence and replaces specific words according
# to the following rules:
# ● cat → dog
# ● apple → orange
# ● red → blue
# Words not listed above should remain unchanged.
# Input:
# cat likes red apple
# Output:
# dog likes blue orange

# sentence = input("Enter a sentence: ")
# words = sentence.split() 
# for i in range(len(words)):
#     if words[i] == "cat":
#         words[i] = "dog"
#     elif words[i] == "apple":
#         words[i] = "orange"
#     elif words[i] == "red":
#         words[i] = "blue"
# print(" ".join(words))

#another method
sentence = input("Enter a sentence: ")
words=sentence.split()
replace={
    "cat":"dog",
    "apple":"orange",
    "red":"blue"
}
for i in range(len(words)):
    if words[i] in replace:
        # print(words[i])
        words[i]=replace[words[i]]
print(" ".join(words))        

       

