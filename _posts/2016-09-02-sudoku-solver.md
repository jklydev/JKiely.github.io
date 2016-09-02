---
layout: post
---

So as I mentioned in the Haskell post, my first project in the language was a [Sudoku solver](https://github.com/JKiely/Sudo-Ku). I picked this as the only algorithm I knew was the one I learned from Norvig's [blog post](http://norvig.com/sudoku.html) on the subject, and since it involved so much iteration and list modification I wanted to see how the functional approach would differ. 

As it happens I've still not really learned a functional approach to solving the problem. So far I just have a brute force backtracking approach. For each blank cell it picks a currently valid choice and moves to the next one. When it runs out of valid moves it backtracks to the last cell it made a guess in, makes a new guess, and starts again from that point. Despite it's simplicity it's still pretty quick on easy Sudoku boards... and utterly unworkable on hard ones.

Still, even if I've not learned a lot about functional approaches to solving a sudoku board, I have learned a lot about Haskell (again, mostly thanks to pairing Sean Martin). It took me a while but this project really helped me get use to the type system and come to appreciate how many errors it catches before you even run the program. On top of that it really drilled in how to compose Haskell functions, work with lists and use recursion. 

Of course it also exposed the lack of a real random function in Haskell, which is what lead me, Sean, and Taylor to our next project... 
