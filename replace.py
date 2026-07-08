# Replace Every Second Character with *
# Write a Python program that takes a string as input and replaces every second
# character (2nd, 4th, 6th, ...) with an asterisk (*). The first character should remain
# unchanged.
# Input:
# developer
# Output:
# d*v*l*p*r

word=input("Enter a word:")
res=""
for ch in range(len(word)):
    if ch%2==0:
        res=res+word[ch]
    else:
        res=res+"*"    

print(res)       
