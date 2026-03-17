def fullJustify(words,maxWidth):
    res=[]
    i=0

    while i<len(words):
        line=[]
        length=0

        while i<len(words) and length+len(words[i])+len(line)<=maxWidth:
            line.append(words[i])
            length+=len(words[i])
            i+=1

        spaces=maxWidth-length

        if i==len(words) or len(line)==1:
            s=" ".join(line)
            s+=" "*(maxWidth-len(s))
        else:
            gaps=len(line)-1
            space=spaces//gaps
            extra=spaces%gaps
            s=""
            for j in range(gaps):
                s+=line[j]+" "*(space+(1 if j<extra else 0))
            s+=line[-1]

        res.append(s)

    return res

words=["This","is","an","example","of","text","justification."]
print(fullJustify(words,16))
