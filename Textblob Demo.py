# TextBlob is a beginners natural langauge processing library used to evaluate text...as best as a computer can. It's an interesing
# first step into learning how computers understand language.  

# import the library
from textblob import TextBlob
from textblob import Word 

# convert text to convertable variable
text = TextBlob("I want to be remembered not only as an entertainer but as a person who cared a lot, and I gave the best that I could. I tried to be the best role model that I possibly could.")

#converts text to list of words
print(text.words)

# breaks down stext into seperate sentences 
print(text.sentences)

# list seperate noun phrases
print(text.noun_phrases)

# convert text to convertable variable
test_sent = TextBlob("Data science projects have several steps to follow and for continuity, these steps should flow together. Without a systematic work flow, it is very easy to get lost in one of these steps. In industry, when people think that they finished a project, they often struggle to bring the project to full operational support as they have failed to consider these life cycle steps. This is a common, but serious one resulting from people who do not know or appreciate the meaning of the term, production ready.")

# breaks down text into seperate sentences 
print(test_sent.sentences)

# list seperate noun phrases
print(test_sent.noun_phrases)

# tag words as parts of speech
print(test_sent.tags) 

# show words in base form as given (" ") part of speech
print(text.words[15].lemmatize("a"))

