def uncommon_words(s1, s2):
    count = {}
    for word in s1.split():
        count[word] = count.get(word, 0) + 1

    for word in s2.split():
        count[word] = count.get(word, 0) + 1

    return [word for word in count if count[word] == 1]

s1="Chandigarh University"
s2="Welcome to Chandigarh University"

print(uncommon_words(s1, s2))