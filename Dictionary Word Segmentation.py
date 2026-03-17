dictionary={"i","like","sam","sung","samsung","mobile",
            "ice","cream","icecream","man","go","mango"}

def wordBreak(s):
    if len(s)==0:
        return True

    for i in range(1,len(s)+1):
        if s[:i] in dictionary and wordBreak(s[i:]):
            return True
    return False

print("ilike:",wordBreak("ilike"))
print("ilikesamsung:",wordBreak("ilikesamsung"))
