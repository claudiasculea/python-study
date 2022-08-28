our_lyrics = ['hey', 'ho', 'let/s', 'go', 'go']
def lyrics_to_frequencies(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict

beatles = lyrics_to_frequencies(our_lyrics)
print(beatles) #first we create a dictionary

def most_common_words(freqs):
    value = freqs.values() 
    best = max(freqs.values())
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return(words, best)

(w, b) = most_common_words(beatles)
print(w)
print(b)

def words_often(freqs, minTimes):
    result = []
    done = False
    while not done:
        temp = most_common_words(freqs)
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del(freqs[w])
        else:
            done = True
    return result
print(words_often(beatles, 2))