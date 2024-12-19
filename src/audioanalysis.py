#todo fill in and implement
#import model

def getStreamSentiment(stream: audioStream):
    analysis = model.analyse_sentiment(stream)
    return analysis.sentiment