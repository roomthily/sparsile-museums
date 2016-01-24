from colormath.color_objects import sRGBColor


class SentimentColor(object):
    '''
    convert the sentiment array [negative, neutral, positive, compound]
    into a color value

    the sentiment analysis returns a dict of 0-1 floats, we use
    the first three for the RGB values but a) it doesn't map to
    anything like colors associated with moods (that we would recognize)
    and b) currently just in the order provided. so it generates
    RGB and it generates the hex but it's goofy.
    '''
    def __init__(self, sentiment):
        self.sentiment = sentiment

    def to_rgb(self):
        # using the sentiment scores, 0-1, so not upscaled

        # TODO: sort out the ordering for an appropriate
        #       sentiment from the images
        self.rgb = sRGBColor(
            self.sentiment['neg'],
            self.sentiment['neu'],
            self.sentiment['pos'],
            False
        )

    def to_hex(self):
        return self.rgb.get_rgb_hex()
