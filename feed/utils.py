from nltk.tokenize import TweetTokenizer

def text_analyzer(text):
    """Analyze the incoming text to separate the
    users that were mentionned and the hashtags
    from the current actual text"""
    tokenizer = TweetTokenizer()
    tokens = tokenizer.tokenize(text)
    mentions = filter(lambda x: x.startswith('@'), tokens)
    hashtags = filter(lambda x: x.startswith('#'), tokens)
    return list(mentions), list(hashtags), tokens
