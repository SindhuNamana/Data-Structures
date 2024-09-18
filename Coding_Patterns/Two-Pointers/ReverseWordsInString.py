def reverse_words(sentence):

    # Replace this placeholder return statement with your code
    sen = sentence.strip().split()
    start = 0
    end = len(sen)-1
    while start<=end:
      sen[start], sen[end] = sen[end], sen[start]
      start+=1
      end-=1
    return ' '.join(sen)


#Time-Complexity = O(n)
#Space-Complexity = O(n)
