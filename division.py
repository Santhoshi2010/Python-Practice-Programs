def check_divisibility(num):
    res=[]

    if num%3==0:
        res.append("jugs")
    if num%6==0:
        res.append("mugs")
    if num%9==0:
        res.append("pugs")
    
    if res:
        return " ".join(res)
    else:
        return "None"    

num=int(input("Enter a number: "))
result=check_divisibility(num)           
print(result)

