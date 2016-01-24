from vaderSentiment import sentiment as vader_sentiment
from collections import defaultdict
import statistics
from colormath.color_objects import sRGBColor


'''
this is the most basic implementation and doesn't
do what we maybe want to do

consider:
    mean sentiment of all messages provided
    most positive score
    most negative score

so you could ask the bot for one of those things
'''


class SentimentMapper(object):
    '''
    '''
    def __init__(self, inputs, aggregate):
        self.inputs = inputs
        self.aggregate = aggregate
        self.scores = defaultdict(list)

    def analyze(self):
        pass

    def _execute(self):
        for i in self.inputs:
            vs = vader_sentiment(i)
            for k, v in vs.iteritems():
                self.scores[k].append(v)

    def aggregate(self):
        if self.aggregate == 'positive':
            self.agg_scores = {}
        elif self.aggregate == 'negative':
            self.agg_scores = {}
        elif self.aggregate == 'mean':
            self.agg_scores = {
                k: statistics.mean(v) for k, v in self.scores.items()
            }
        else:
            self.agg_scores = {}

    def colorize(self):
        '''
        convert the sentiment array [negative, neutral, positive, compound]
        into a color value

        the sentiment analysis returns a dict of 0-1 floats, we use
        the first three for the RGB values but a) it doesn't map to
        anything like colors associated with moods (that we would recognize)
        and b) currently just in the order provided. so it generates
        RGB and it generates the hex but it's goofy.
        '''
        srgb = sRGBColor(
            self.agg_scores['neg'],
            self.agg_scores['neu'],
            self.agg_scores['pos'],
            False
        )
        return srgb.get_rgb_hex()
