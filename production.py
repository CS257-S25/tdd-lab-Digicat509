def reverse_word(word):
    ans = ""
    for i in range(1, len(word)+1):
        ans += word[-i]
    return ans

def reverse_all_words(phrase):
    ans = ""
    for s in phrase.split(" "):
        ans += reverse_word(s)+" "
    ans = ans.strip()
    return ans
