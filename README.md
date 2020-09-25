# LeetSol
LeetCode solutions

Problem 1) Inverting a binary tree

Greetings, 
are you getting that annoying ad on Youtube that starts off with "you know what's the scariest thing in the world 
.... #Dramatic Tension# .... not knowing how to invert a binary tree" like that measures up at all to the barren
hellscape that is 2020. 

If you're like me, you got slightly annoyed but then was like "wtf is inverting a bin tree" and then after googling 
it you see that it's just mirroring the elements in the binary tree and then immediately became more frustrasted 
as you realize the fact you had to google the terms means you're still insecure as a coder and now you've spend time that could've 
been spent on watching Among Us clips being spent hating yourself.

Now if that run-on sentence is applicable to you, here's a refresher

Solution 1 to the problem: Recursion
In this solution, we recursively switch the left and right child with depth first traversal.
File-PATH in this repository : InvertingBinTree/invertBinTreeSol1.py

Solution 2: Iterative
In this solution, we have to get creative and use a queue to "remember" the nodes on the 
shallower or same level/depth when we go into it to mirror it's chld node. 

