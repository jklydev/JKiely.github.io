So when I last left off with the spell checker it was functioning on a webpage and I was planning on improving the correction rate. Well I'm pleased to report that the site it broken! And for all I know the correction rate is even worse, since the evaluator is broken as well!

This is mostly due to me restructuring the project.

But I haven't *just* been ruining the hard work of past John, I've also been working on implimenting a new algorithm which has the potential to be a lot better that the old one. I now, rather than just returning the word with the most occurances and the lowest edit distance, I take a weighted average of the unigram, bigram, trigram and probibilities, and edit distance.

'''
Block showing formula
'''

I've also altered it such that it returns a ranked list of the five most likely corrections, in order to better hook in with the site when I upgrade it.
