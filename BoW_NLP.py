# Bag-of-words model in NLP

vocab = {}  # maps word to integer representing it
word_encoding = 0 # start at index 0
def bag_of_words(text):
  global word_encoding

  words = text.lower().split(" ")  # create a list of all of the words in the text, we'll assume there is no grammar in our text for this example
  bag = {}  # stores all of the encodings and their frequency

  for word in words:
    if word in vocab:
      encoding = vocab[word]  # get encoding from vocab
    else:
      vocab[word] = word_encoding
      encoding = word_encoding
      word_encoding += 1
    
    if encoding in bag:
      bag[encoding] += 1
    else:
      bag[encoding] = 1
  
  return bag

text = "This is a test to see if this test will work. This is test one"
bag = bag_of_words(text)
print("Vocabulary and their index number:")
print(vocab)
print("\nFrequency of words:")
print(bag)

# OUTPUT
# Vocabulary and their index number:
# {'this': 0, 'is': 1, 'a': 2, 'test': 3, 'to': 4, 'see': 5, 'if': 6, 'will': 7, 'work.': 8, 'one': 9}

# Frequency of words:
# {0: 3, 1: 2, 2: 1, 3: 3, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}

# This isn't really the way we would do this in practice, but I hope it gives you an idea of how bag of words works. Notice that we've lost the order in which words appear.
