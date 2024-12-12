# Loops -> while ,for

# count=5
# while(count>0):
#     print("hello")
#     count=count-1
    
# Q-> [1,4,7,9,12,15,23]  -> find a element in an list ->15

list=[1,4,7,9,12,15,23]
# count=len(list)-1
# key=15
# flag=0

# while(count>=0):
#     if((list[count])==key):
#         print("key mil gayi : ",count)
#         flag=flag+1
#         break
#     count=count-1
    
    
# if(flag==0):
#     print("element not found")

val=list.index(15)

if(val):
    print("element found at : ",val)