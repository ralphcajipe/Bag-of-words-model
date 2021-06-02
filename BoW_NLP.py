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

text = "This is a test to see if this test will work. This is test A."
bag = bag_of_words(text)
print(bag)
print(vocab)
