import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
sid = SentimentIntensityAnalyzer()
def get_sentiment(sentence):

    sentiment_score = sid.polarity_scores(sentence)

    positive_meter = round((sentiment_score['pos']), 2) 
    neutral_meter = round((sentiment_score['neu']), 2) 
    negative_meter = round((sentiment_score['neg']), 2)

    return positive_meter, neutral_meter, negative_meter


sentence = "Very, very disappointing. I went here this past weekend for dinner and had a VERY mediocre meal. It was actually one of the worst meals I have had in the 6 years I've lived in Philly. Everything was very bland, like not even seasoned with salt and pepper bland."
# "As a former patron of the Pine Street Dmitris, I had certain expectations. \n\nFirst off, I had no idea that this (and the northern Liberties locations) were BYO. I really wished I knew that ahead of time. It's always nice to have a glass of wine with a nice meal right? I was bummed. \n\nSecondly- the menu at his location was missing the saganaki (fried cheese) that the other now closed location had.\n\nPerhaps my overall disappointment clouds my review but the only thing that stood out was the shrimp pilpil. Outstanding! Everything else was good. But I didn't leave as satisfied as I did at the other Dmitris. \n\nWe ordered the grilled veggies which were good. \nThe meatballs were eh. I had to ask what kind of meat they were and please be aware there is veal in them. I don't eat veal. I am\nbummed once again. \nFried calamari platter: needed salt. What the deuce guys? \n\nOverall the experience was unimpressive. \n\nWhile the ambiance is lovely, the waitstaff is banal, and I wish I had gone there prior to the other location because I would most likely have an entirely different take on the experience. \n\nI miss my Pine Street Dmitri's location. I hear they're putting in a Tria. Eh. Whatever."

# "I love the food, love the owner the lady who waits on you is so lovely and so warm. Chicken Makhani was excellent and Chicken Kashmir was amazing my friend and loved it don't worry about the decor the food is the best Indian around."

# """
# I've been here several times. The price is reasonable, food is quite good, and the service as well. I've always ordered take-out. 
# One time I went, and the guy who normally takes my order wasn't there... Instead there were 2 ladies... 
# I think one was the wife of the owner. Or something along those lines. 
# Anyway they were nice but when I came back to pick up my order they handed me the wrong bag (someone else's order). 
# They should have confirmed the contents, but frankly I should have as well, so I accept at least part of the blame. 
# I ended up going all the way home before I realized the screw-up and came back. I wasn't angry but I was definitely hungry and super-annoyed. 
# The two ladies were gracious and apologetic, and they even threw in a courtesy snack for my trouble.
# """
positive_meter, neutral_meter, negative_meter = get_sentiment(sentence)
print("Positive", positive_meter)
print("Neutral", neutral_meter)
print("Negative", negative_meter)

