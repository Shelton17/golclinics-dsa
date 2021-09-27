def reverseSentence(sen):
    wordsInSentence = sen.split()
    reverseWords = wordsInSentence[::-1]
    print(" ".join(reverseWords))


sen = input("Enter a sentence: ")
reverseSentence(sen)
