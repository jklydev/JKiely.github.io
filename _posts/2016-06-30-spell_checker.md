I've always liked Peter Norvig's writing (who doesn't?) and I came across his (spellcheck)[http://norvig.com/spell-correct.html] article at just the right time as I was looking for a small project to keep be busy and sharpen my python before RC starts.

So my first step was to go though and build it as it was in the article, which was relatively straight forward. I was expecting there to be some problems with using python 3, but it all went smoothly. While the code was a little less explicit at some points than I like to be, I read through the article as I wrote it and it was all simple enough. Since I knew I wanted to modify and extend it I also took the time to add unit tests with pytest.

The next step was to convert it into a class. Which, again, went simple enough. All the tests passed and it continued to work perfectly well in the interpreter. I did this in order to make it easier to use on a flask page. So once I had it done I put together a simple site in flask that displays a text box and corrects any text you type in. It's pretty clunky for now but it seems to work.

Once I had that the site up I wanted to focus on improving the spell checker, so I built the evaluator from Norvig's article and the results were... not good. About 49%. I'm not sure why my results would be so different from his? I would assume that I didn't copy over the corpus correctly, as I had some trouble downloading it.

So my next steps for this project are as follows, on the back end:
1. Improve the size and variety of the corpus
2. Incorporate bigrams into the model

And on the front end:
1. Let the user select their replacement word, since I returning a list of probable candidates anyway.
2. Use javascript to make the corrections rather than reloading the whole page.