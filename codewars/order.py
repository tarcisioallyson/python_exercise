def order(sentence):
    if sentence == '':
        return ''
    else:
        words = sentence.split()
        new_sentence = ''
        x = 1
        while x < len(words) + 1:
            for y in words:
                if str(x) in y:
                    new_sentence += y + ' '
            x+=1   
        return new_sentence.rstrip()

sentence = "4of Fo1r pe6ople g3ood th5e the2"
print(order(sentence))