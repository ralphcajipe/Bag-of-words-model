# Bag-of-words model in NLP

vocab = {}  # maps word to integer representing it
word_encoding = 1 # start at index 1
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

'''
OUTPUT:
Vocabulary and their index number:
{'this': 1, 'is': 2, 'a': 3, 'test': 4, 'to': 5, 'see': 6, 'if': 7, 'will': 8, 'work.': 9, 'one': 10}

Frequency of words:
{1: 3, 2: 2, 3: 1, 4: 3, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1}

This isn't really the way we would do this in practice, but I hope it gives you an idea of how bag of words works.
Notice that we've lost the order in which words appear. 
*********************************************************************************************************************
In fact, let's look at how this encoding works for our movie reviews:

positive_review = "I thought the movie was going to be bad but it was actually amazing"
negative_review = "I thought the movie was going to be amazing but it was actually bad"

pos_bag = bag_of_words(positive_review)
neg_bag = bag_of_words(negative_review)

print("Positive:", pos_bag)
print("Negative:", neg_bag)

OUTPUT:
Positive: {11: 1, 12: 1, 13: 1, 14: 1, 15: 2, 16: 1, 5: 1, 17: 1, 18: 1, 19: 1, 20: 1, 21: 1, 22: 1}
Negative: {11: 1, 12: 1, 13: 1, 14: 1, 15: 2, 16: 1, 5: 1, 17: 1, 22: 1, 19: 1, 20: 1, 21: 1, 18: 1}

We can see that even though these sentences have a very different meaning they are encoded exaclty the same way. 
Obviously, this isn't going to work well. We have to look at some other methods like "Integer Encoding".
'''
