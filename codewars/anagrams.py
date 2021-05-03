def anagrams(word, words):
    letters = list(set([lt for lt in word]))
    
    def count_letter(letter,word):
        count = []
        i = 0
        while i < len(letter):
            count.append((letter[i], word.count(letter[i])))
            i+=1
        return count  
    
    word_list = []
    for item in words:
        if len(word) == len(item):
            if count_letter(letters,word) == count_letter(letters,item):
                word_list.append(item)
    
    return word_list

print(anagrams('laser', ['lazing', 'lazy',  'lacer']))