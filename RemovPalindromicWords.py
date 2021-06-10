https://ide.geeksforgeeks.org/BhQsHtfNVk 

def isPalindrome(string) :
    return string==string[::-1]
 
def removePalinWords(string) :
    final_str = ""; word = "";
     
    string = string + " ";
    n = len(string);
     
    # traversing 'str'
    
    for i in range(n) :
        # if not new word add to the existing str 
    
        if (string[i] != ' ') :
            word = word + string[i];
        
        #  when space occurs check if isPalindrome & add to final op
        # else eliminate loop and reinitialise op 
        else :
            if (not (isPalindrome(word))) :
                final_str += word + " ";
            word = "";
     
    return final_str;
     
# Driver Code
if __name__ == "__main__" :
    string = "Text contains malayalam and level words";
    print(removePalinWords(string));
 
 
