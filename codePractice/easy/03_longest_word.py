# Have the function LongestWord(sen) take the sen parameter being passed and return the largest word in the string.
# If there are two or more words that are the same length, return the first word from the string with that length.
# Ignore punctuation and assume sen will not be empty.


def LongestWord(sen):
  max_word = ""
  for word in sen.split(" "):
    wo = [True if w in string.punctuation else False for w in word]
    if not all(wo) is True and len(word) > len(max_word):
            max_word = word
  return max_word
  

print(LongestWord(input()))
