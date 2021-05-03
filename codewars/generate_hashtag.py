def generate_hashtag(s):
    word_list = [word.capitalize() for word in s.split()]
    hastag = '#'
    if len(s) != 0 and len(s) < 140:
        for word in word_list:
            hastag += word
        return hastag
    else:
        return False

print(generate_hashtag(""))