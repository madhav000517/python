inputList =[]
listElementCount=[]
flag="false"

allowedvalues=['m','z','c','p','s'] 
inp1=raw_input("enter input:")
inputString=str(inp1)
for i in inputString:
    inputList +=i
    
for i in inputString:
    if i in allowedvalues:
        flag="true"
    else:
        flag="false"
        print("The input provided is not acceptable, please re-run with proper input")
        break

if flag == "true"  :
   for i in inputList:
       count=inputList.count(i)
       b=inputList.index(i)
       listElementCount.append(count)
       print i, count
   minCount=min(listElementCount)
   print("No of Unique Teams formed") 
   print(minCount)
