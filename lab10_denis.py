"""
Lab 10 - Exam Preparation Exercises

(100 marks in total, including:
8 code tracing exercises (5 marks each, 40 marks in total);
3 coding quetions (20 marks each, 60 marks in total))

Your Name: Denis
Due date: Apr. 5, 2024, 11am

Objective:
1. Review the function 
2. Review the conditionals (if-else)
3. Review the program flow (for/while - continue, break)
4. Practice when to use and how to operate on the collection data types: 
tuple, list, string, set, dictionary.
6. Review the accumulator algorithm pattern (Initialize-Loop-Return):
   Initialize a variable (accumulator) that is assigned to an integer, a list, etc. 
   Loop (for or while) to update the variable based on requirements; 
   Return the variable.
"""


"""
Exercise 1 - Code tracing (5 marks)

First read and understand the following function.

Then answer the question below:
What will it print if we call this function by running 
practice_if(80, 80)?

Your answer is: 

Nicely done!

"""


def practice_if(score, average):
    if score < average:
        print("Do better next time!")
    else:
        if score >= 90:
            print("Woot woot!")
        elif score > 80:
            print("Great job!")
        else:
            print("Nicely done!")


"""
Exercise 2 - Code tracing (5 marks)

First read and understand the following function.

Then answer the question below:
What will it print if we call this function by running 
print(practice_for_if([5, 5, 2, 9], 3))?

Your answer is: 

[3, 3, 3]

"""


def practice_for_if(nums, target):
    list = []
    for num in nums:
        if num > target:
            list.append(num)
    return list


"""
Exercise 3 - Code tracing (5 marks)

First read and understand the following function.

Then answer the question below:
What will it print if we call this function by running 
print(practice_function([5, 5, 2, 9, 6]))?

Your answer is: 

None

"""


def practice_function(nums):
    even_list = []
    for num in nums:
        if num % 2 == 0:
            even_list.append(num)


#print(practice_function([5, 5, 2, 9, 6]))
"""
Exercise 4, 5, 6 - Code tracing (15 marks in total)

First read and understand the following function.
Then answer the questions below:

Question 1: What will it print if we call this function by running 
print(practice_for_index_1([5, 5, 2, 9, 9, 6], 9))? (5 marks)
Your answer is: 

3
4

Question 2: Are the function practice_for_index_1(nums, target) and 
the function practice_for_index_2(nums, target) have the same 
functionality? Why? (5 marks)
Your answer is: 

no they don't, since there is a break in the code

Question 3: Are the function 
practice_for_index_2(nums, target) and the function 
practice_for_index_3(nums, target) have the same 
functionality? Why? (5 marks)
Your answer is: 

no they do not, because the only difference is the break function, 
which is at the end of the for loop. When the target number is found,
then the loop in the second function cutts of, while the loop in the
last one does not. 

"""


def practice_for_index_1(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1


def practice_for_index_2(nums, target):
    index = -1
    for i in range(len(nums)):
        if nums[i] == target:
            index = i
            break
    return index


def practice_for_index_3(nums, target):
    index = -1
    for i in range(len(nums)):
        if nums[i] == target:
            index = i
    return index


"""
Exercise 7 - Code tracing (5 marks)

First read and understand the following function.

Then answer the question below:
What will it print if we call this function by running 
practice_for_continue([5, 5, 2, 9, 6], 2)?

Your answer is: 

5
5
2
9
6



"""


def practice_for_continue(nums, target):
    for num in nums:
        if num == target:
            continue
        print(num)


"""
Exercise 8 - Code tracing (5 marks)

First read and understand the following function.

Then answer the question below:
What will it print if we call this function by running 
print(practice_while(30))?

Your answer is: 6

"""


def practice_while(n):
    count = 0
    while n > 4:
        n -= 5
        count += 1
    return count

#print(practice_while(30))





"""
Exercise 9 - Coding question

Write a function named "exist_in_both" that takes two strings as input 
and returns the number of characters that occur in both strings.
You can assume that all characters within a string are unique (no repeats).

For example, 
if the function is passed "lap" and "help", 
the function exist_in_both("lap","help") will return 2,
because the characters "l" and "p" occur in both strings.

For example,
exist_in_both("computer","mute") wil return 4.

Function implementation. (15 marks) 
Pass your own unit tests. (5 marks) 

"""


def exist_in_both(str1, str2):
    count = 0
    list1 = [] # for already used values
    for i in str1:
        if i in str2 and i not in list1:
            count += 1
            list1.append(i)
        else:
            pass
    return count

# Write your unit tests below
assert exist_in_both("telephone","phone") == 5
assert exist_in_both("10221","999876321") == 2
assert exist_in_both("qwertyuiopgfds","hjklamnbvcxz") == 0
assert exist_in_both("same_word", "same_word") == 9



"""
Exercise 10 - Coding question

If both adjacent letters in a word are the same, 
we call the two adjacent letters are "good neighbors".

E.g.1, there are one pair of good neighbors inside the word "apple",
since word[1] == word[2], and they are both 'p'.

E.g.2, there are two pairs of good neighbors inside the word "occurrence",
since word[1] == word[2], and they are both 'c'; 
word[4] == word[5], and they are both 'r'.

E.g.3, there are two pairs of good neighbors inside the word "hmmm",
since word[1] == word[2], and they are both 'm'; 
word[2] == word[3], and they are both 'm'.


Write a function called "good_neighbors" that accepts a word as input, 
and return the number of pairs of good_neighbors. 
Assume that all the letters in the word are lowercase letters, 
and there are at least two letters in the word.

For example, good_neighbors("happy") will return 1, 
since there is one pair of adjacent letters 'p'.

good_neighbors("occurrence") will return 2, 
since there are twp pairs of adjacent letters, 'c' and 'r'.

word_example = "arrrrhhh"
good_neighbors(word_example) will return 5, since
word_example[1] == word_example[2], both 'r'
word_example[2] == word_example[3], both 'r'
word_example[3] == word_example[4], both 'r'
word_example[5] == word_example[6], both 'h'
word_example[6] == word_example[7], both 'h'


Hint:

We may compare each letter word[i] with its neighbor word[i + 1], 
while traversing the word using index i. Use the accumulator algorithm pattern.


Function implementation. (15 marks)
Pass your own unit tests. (5 marks) 
"""


def good_neighbors(word):
    count = 0
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            count += 1
        else:
            pass
    return count


# Write your unit tests below
assert good_neighbors("assert") == 1
assert good_neighbors("aabbccdd") == 4
assert good_neighbors("nothing") == 0
assert good_neighbors("1234456789") == 1


"""
Exercise 11 - Coding question

Implement a function called "more_than_2" that accepts a list of strings as input. 
The function identifies strings that occur more than two times in the list,
and return these strings as a list. 

Eg.1, fruits = ["apple", "banana", "apple", "apple", "apple", "pear", "orange",
"banana", "banana", "watermelon"] 
more_than_2(fruits) will return ["apple","banana"]. 

Eg.2, colors = ["red", "red", "yellow", "green", "red", "yellow", "orange",
"green", "banana", "yellow"] 
more_than_2(colors) will return ["red", "yellow"]. 

Hint: Utilize dict data type to count the occurrences for each string, 
then traverse all the keys in the dict and compares its value to 3. 
Use the accumulator algorithm pattern.

Function implementation. (15 marks)
Pass your own unit tests. (5 marks) 
"""

def more_than_2(words):
    list1 = []
    for i in words:
        words.remove(i)
        if i in words and i not in list1:
            list1.append(i)
    return(list1)


# Write your unit tests below
assert more_than_2(["red", "red", "yellow", "green", "red", "yellow", "orange", "green", "banana", "yellow"]) == ["red", "yellow"]
assert more_than_2(["123", "123", "132", "123"]) == ["123"]
assert more_than_2([1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10, 1]) == [1, 8]
assert more_than_2(["target", "targa"]) == []


# Congratulations on your lab10! Please upload it to your github lab repository.