def topngram(file,num):
    textfile = open(file,"r")
    alist = []
    ngram= []
    symb = "?.,;:'!-_&*$+`\"=/|"
    common = ["of","the","i","he","she","a","it","the","is","was","be","not","my"]
    Text = textfile.read()
    Text = Text.lower()
    Text = Text.split()
    dictNgrams = {}
    for word in Text: #Adds words that are not in common in a new list
        for letter in word: #Removes the punctuation
            if letter in symb: 
                word = word.replace(letter,"")
        if word not in common:
            alist.append(word)
    for idx in range(0, len(alist)-(num+1)): #Makes a dictionary of the specified number of ngrams
        ngram = alist[idx:(num+idx)]
        ngram = " ".join(ngram)
        if ngram in dictNgrams:
            dictNgrams[ngram] += 1
        else:        
            dictNgrams[ngram] = 1
        ngram = []
    maxx = sorted(dictNgrams, key=lambda k:dictNgrams[k]) #Sorts the dictionary
    return maxx[-1]
    textfile.close()   





