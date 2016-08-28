---
layout: post
---

So when I last left off with the spell checker it was functioning on a web page and I was planning on improving the correction rate. So firstly, the site is currently broken. I have however made quite a lot of progress on improving the correction rate, and I'm generally in the process of restructuring how the site works in order to make it far more useful.

So before my 'correct' percentage was ~30%, which sucked. This was done by looking at all known words within an edit distance of two from the error word, and returning the closest one (with ties being broken by looking at how frequently each correction appeared in the text). In the Norvig [article]() from which I got the algorithm, he was managing ~70% and I was unsure why I was doing so much worse. My first hunch was that I didn't have the complete version of his corpus. Since the corpus was a tad outdated anyway (it does not contain the word 'hello', not even once) I decided that I needed to get a new one before I moved to the final version. However finding a good corpus of modern English proved harder than I thought, and so I decided to see what I could squeeze out of this corpus by improving my algorithm.

Firstly I modified the trainer class to keep track of bigram and trigram counts as well as individual word counts in the corpus, so that it could calculates the probability of a word appearing in that particular context as well as in the text in general. The new algorithm looked like this:

```py
probability = ((a * unigram_probability) + (b * left_bigram_probability) + (c * right_bigram_probability) + (d * trigram_probability) + (e * error_probability))/(a + b + c + d + e)
```

So for example given the sentence `"How arr you?"` you might get the hypothetical probabilities:

```py 
unigram_probability('are') # => 0.9
left_bigram_probability('how are') # => 0.7
right_bigram_probability('are you') # => 0.9
trigram_probability('how are you') # => 0.6
error_probability('are', 'arr') # => 1
```

And thus:

```py
probability= ((1 * 0.9) + (2 * 0.7) + (2 * 0.9) + (1 * 0.6) + (4 * 1))/(1 + 2 + 2 + 2 + 4) # => ~0.79
```

For a total probability of `0.79`, which would almost certainly make it the top correction.

Each of the gram probabilities are generated by looking at how many times that particular gram appeared in the text and normalizing between 0 and 1. The error model is only slightly more complicated. Right now, for simplicities sake, I'm naively assuming that the edit distance is all that matters. But edit distance just returns a natural number, and while it's obvious that the lower the number the more likely the error, it's up to me to decided how that should be turned into a number between 0 and 1 (with 1 now indicating more likely). After trying a few different models I eventually settled on `4/(4 + ((distance -1)^2))`. There's no real mathematical formalism behind this, I don't have the training to reason about this any way other than what works in practice. It maps an edit distance of 1 to a probability of one, 2 to ~0.8,  3 to ~0.5 and keeps decreasing in an exponential fashion from there. I'd like to try some others functions, perhaps get an S shaped curve that drops off more sharply after 2, but I'm happy with this for now.

You may be wondering about the seemingly arbitrary `a, b, c, d, e` in there. I use these as I don't want all the inputs to be treated equally. Unigram probability is less important than bigram or trigram probability, which is less important than error probability. However actually deciding how much more important has created a bit of difficulty. I have some intuitions about this, but I've been having a hard time finding data on which to test them. It was easily enough to find commonly spelled words with corrections in order to test it on unigrams, but finding sentences, or sentence fragments that are suitable for testing has been impossible so far. I went so far as to using my existing unigram data to manually construct some test trigram test cases, but this was extremely time consuming. Right now I'm considering making a program that goes though a document and replaces correct words with common spelling mistakes, but I'd much rather get hold of some naturally occurring data.

So, after all that, my current algorithm has improved my results from 30% to 75% using the previous standard of checking if the correct word was returned as the most probable. However given that I plan on letting a user select a word from the most probable corrections, I think it's more useful to ask if the correct word was returned in the top five. This is still an arbitrary cut off, but it reflects the intended application while still holding myself to a rigorous standard. By this new measure I'm scoring 88% correct. While this is certainly an improvement, and I'm proud to have come this far, these are only the most common spelling errors in English and thus I see no reason not to aim for 100%.

Right now the only way I'm going to make that kind of progress is with more data. My current corpus has gotten me quite far, but I need a larger and more modern one if I'm to catch the few remaining errors. And further tuning of the algorithm is going to require a more robust set of test cases in order that I know I'm making progress.