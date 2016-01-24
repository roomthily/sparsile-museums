from vaderSentiment import sentiment as vader_sentiment
from collections import defaultdict
import statistics


'''
this is the most basic implementation and doesn't
do what we maybe want to do

consider:
    mean sentiment of all messages provided
    most positive score
    most negative score

so you could ask the bot for one of those things
'''


def run_sentiment(inputs):
    '''
    returns mean sentiment scores (mean of each bucket)
    inputs = an array of string inputs, ie sentences
    or paragraphs from a source.

    ex output:
        {'neg': 0.0, 'neu': 0.508, 'pos': 0.492, 'compound': 0.4404}
    '''
    dd = defaultdict(list)
    for i in inputs:
        vs = vader_sentiment(i)
        for k, v in vs.iteritems():
            dd[k].append(v)

    # map the average
    return {k: statistics.mean(v) for k, v in dd.items()}
