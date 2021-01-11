### https://www.interviewquery.com/questions/last-page-number
input='9910010110299100101103991001011045'
# actual page numbers = [99100101102,99100101103,99100101104,5]
ans=[]
for i in range((len(input)//2),0,-1): # slot for number of digits
    temp_str=input
    curr=temp_str[:i]
    temp_str=temp_str[i:]
    f=0
    # Iterate the string and search for increments
    while(str(int(curr)+1)==temp_str[:len(str(int(curr)+1))]): 
        curr=temp_str[:len(str(int(curr)+1))]
        temp_str=temp_str[len(str(int(curr)+1)):]
        f=1
    if f==1: # if at least one successive page is found, append the result.
        print(curr)
        break
 # ans = [[2, '102'], [11, '99100101104']] -  gives starting length of page number with highest page number associated
