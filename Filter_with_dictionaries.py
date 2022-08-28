our_lyrics = ['hey', 'ho', 'let/s', 'go', 'go']
def lyrics_to_frequencies(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict

print(lyrics_to_frequencies(our_lyrics))

def most_common_words(freqs):
    val = freqs.vars()
    best = max(freqs.vars())
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return(words, best)

(w, b) = most_common_words(our_lyrics)

