#shortening way too long words
n=int(input())#this takes no:of lines or number word inputs
for _ in range(n): #loop
    word=input() #takes no:of words as input
    if len(word)>10: #the minimum word length should be of 10 characters, if it is greater than that entrs the condition 
        first=word[0] #stores first character of the the word
        last=word[-1]  #stores the last character of the word
        size=len(word)-2 #stores the size no:of words in between first and last character
        print(first+str(size)+last) #concates into single word
    else:
        print(word) #if the word is less than 10 characters it displays as it is
#mistakes i had overcome: use () for functions such as range not []
#the size of the characters in between is stored as integer type so convert it into string for concatenation here: str(size)
