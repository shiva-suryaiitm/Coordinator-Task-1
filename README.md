# Coordinator-Task-1

**Git Tasks:**

- Fork and clone this Github repository.
- Create a folder named "Name" (or Handle) in which you have all the
contents of whatever submission you wanna make (solutions to
question 1 and 2)
- Pull origin & add files, commit and push to fork.
- Create pull request on main repo
- Create Issue

Resources for **Getting Started with Git:**

- Part 1 - [https://www.youtube.com/watch?v=uR6G2v_WsRA&ab_channel=DavidMahler](https://www.youtube.com/watch?v=uR6G2v_WsRA&ab_channel=DavidMahler)
- Part 2 - [https://www.youtube.com/watch?v=FyAAIHHClqI&ab_channel=DavidMahler](https://www.youtube.com/watch?v=FyAAIHHClqI&ab_channel=DavidMahler)
- Part 3 - [https://www.youtube.com/watch?v=Gg4bLk8cGNo&ab_channel=DavidMahler](https://www.youtube.com/watch?v=Gg4bLk8cGNo&ab_channel=DavidMahler)

There’s 2 questions in the task to help you get comfortable with python, do try both of them out.

**Python Tasks:**

- Create two vectors 𝑦 and 𝑦̂ having **the same** dimensions, where 𝑦̂ should
consist of random numbers between [0,1) and 𝑦 should contain 0𝑠 and
1𝑠, for example, 𝑦=[0,1,1,0,1,0,0,1,...,1]. Compute the given expression:
    
    ![loss](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/11165546-89e0-4931-9828-d5fb91d5d5d7/Untitled.png)
    
    Where n = 100, is the total number of elements in y and 𝑦̂
    
    Note: The expression *O*, which you have computed is actually a
    **Cross-Entropy** loss function used in machine learning for classification
    tasks which tells us how bad or good the model is performing, if *O* is large
    then the model is performing worst and vice versa.
    
- Write a Python class to find a pair of elements (indices of the two
numbers) from a given array whose sum equals a specific target
number.
Note: There will be multiple solutions, so create a dictionary where the
keys represent just [S.No](http://S.No) (1,2,3,4.....) and the value corresponding to
the key represents the indices of the two numbers
    
    For example:
    
    Input: numbers= [10,20,10,40,50,60,70], target=50
    
    Output: {1: [0, 3], 2: [2, 3], 3: [3, 0], 4: [3, 2]}
