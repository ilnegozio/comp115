"""
Lab 6 - Strings and Tuples 
(100 marks in total, including 5 exercises - each 20 marks)

Author:  Denis
Due Date: This Friday (Mar. 1) 11am.
Submission: Upload your lab python file to your GitHub repository.

Objective:
1. Learn how to write a good python docstring for documenting functions'
purpose, parameters, return values. A good docstring helps other developers 
understand how to use the function and serves as documentation that can be 
displayed in tools like IDEs. A sample docstring has been written for exercise 1 and 2,
students need to write good docstrings for all the other exercises.
2. Review how to code simple Python functions and write unit tests using assert
3. Practice how to operate on strings and tuples (similar to lists, but strings and tuples are immutable)
4. Review iterations using loop
5. Review the boolean expression and conditionals
6. Review the accumulator algorithm pattern (Initialize-Loop-Return):
   Initialize a variable that is assigned to an integer, a list, a string, etc.; 
   Loop (for or while) to update the variable based on requirements; 
   Return the variable or a value related to this variable.
"""

"""
Exercise 1 (20 marks: function implementation: 10 marks, unit tests: 10 marks)

Complete the function below to reverse a string.

For example, 
reverse_str("Abd") should return "dbA".
reverse_str("COMP115") should return "511PMOC".

Hint: the accumulator algorithm and the string concatenation using the operator '+'
"""
def reverse_str(s):
    s_rev = "" # create empty string for reversed values of s
    for i in range(1, len(s)+1):
        s_rev += s[-i] # start from the end of the string
    return s_rev
    
# Your unit tests
assert reverse_str("Abd") == "dbA"
assert reverse_str("COMP115") == "511PMOC"
assert reverse_str("nohtyp") == "python"
assert reverse_str("12345") == "54321"

"""
Exercise 2 (20 marks: function implementation: 10 marks, unit tests: 10 marks)

Complete the function below to count how many vowels ('a', 'e', 'i', 'o', 'u') in a string.

For example, 
count_vowels("Apple") should return 2, since 'A' and 'e' are vowels.
count_vowels("Hmmm") should return 0, since there are no vowels.

Hint: you may want to convert the input string to its lowercase version using s.lower() first.
"""
def count_vowels(s):
    vowels = ('a', 'e', 'i', 'o', 'u')
    num = 0 # define num of vowels
    for i in range(len(s)):
        if s[i] in vowels:
            num += 1
    return num
    

# Your unit tests
assert count_vowels("vowels") == 2
assert count_vowels("visual studio code") == 8
assert count_vowels("2024") == 0
assert count_vowels("random_word") == 3

"""
Exercise 3 (20 marks - doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

Complete the following function to remove the duplicate characters in a string.

E.g.,
remove_duplicates("apple") == "aple"
remove_duplicates("Popsipple") == "Popsile" (Notice: 'P' and 'p' are different chars)
remove_duplicates("pear") == "pear"

Hint: We have implemented a function removing duplicates for a list in week 6. Similar.
"""
def remove_duplicates(s):
    list1 = []
    str1 = ""
    for i in range(len(s)):
        if s[i] in list1:
            pass
        else:
            list1.append(s[i])
            str1 += s[i]
    return str1

# Your unit tests
assert remove_duplicates("apple") == "aple"
assert remove_duplicates("long live") == "long ive"
assert remove_duplicates("assert") == "asert"
assert remove_duplicates("comp115") == "comp15"

"""
Exercise 4 (20 marks - doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

Complete the following function to return the lowerest index of a charactor t found in a string s, 
to return -1 if the character is not in the string.

E.g.,
find_index("Abd", 'b') == 1
find_index("Abdccc", 'c') == 3
find_index("Abd", 'w') == -1

Note: we should implement our own algorithm, not using the built-in function find().
"""
def find_index(s, t):
    index = -1
    for i in range(len(s)):
        if t == s[i]:
            index = i
        if index > -1:
            return index
            exit()
    return index


# Your unit tests
assert find_index("Abd", "b") == 1
assert find_index("ccdccCaCcec", "c") == 0
assert find_index("dead", "d") == 0
assert find_index("qwertyuiopasdfghjklzxcvbnm", "m") == 25

"""
Exercise 5 (20 marks - doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

Complete the following function to return the project completion day, 
given the current day in a week and estimated time of days to completion.

E.g.,
project_completion_day('Monday', 4) returns 'Friday'.
project_completion_day('Monday', 7) returns 'Monday'.
project_completion_day('Saturday', 2) returns 'Monday'.
project_completion_day('Saturday', 1) returns 'Sunday'.

Hint:
days_week.index(day) will return the index of the day in the tuple days_week.

"""

days_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
             'Saturday', 'Sunday')
# Notice that days_week is a tuple, and it works the same if it's a list,
# since the index operation is the same for tuple and list.


def project_completion_day(day, days_to_completion):
    day_index = days_week.index(day)
    finish_day = (day_index + days_to_completion) % 7
    return days_week[finish_day]

# Your unit tests
assert project_completion_day("Monday", 4) == "Friday"
assert project_completion_day("Sunday", 7) == "Sunday"
assert project_completion_day("Wednesday", 10) == "Saturday"
assert project_completion_day("Friday", 4) == "Tuesday"

"""
Congratulations on finishing your lab6. Hope you feel more confident on function implementation.

Now you just need to upload it to your GitHub repository. That's all.
"""