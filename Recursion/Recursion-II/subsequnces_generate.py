def generateSubsequnces(string,index,current):
    if(index==len(string)):
        if(not current):return []
        return [current]

    include = generateSubsequnces(string,index+1,current+string[index])
    exclude = generateSubsequnces(string,index+1,current)
    print(include,exclude)
    include.extend(exclude)
    return include

def subsequences(str):
    return generateSubsequnces(str,0,"")

# time complexity: O((2^n)*n)  
# space complexity: O(n)(recursion stack)
s = input().strip()
print(subsequences(s))
    
