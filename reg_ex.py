'''
Objective: The aim of this assignment is to deepen your practical skills in Python's regular expressions, 
enhancing your ability to process and manipulate text data. You will tackle a variety of real-world scenarios, 
applying regex to extract, validate, and transform text effectively.

Task 1: Email Extraction Enhancement

Problem Statement: You have a script that extracts email addresses from a text but needs to be refined to exclude certain domains 
(e.g., '[exclude.com](http://exclude.com/)'). Modify the script to extract all email addresses except those from the specified domain.

'''

import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com, dennis@yahoo.com, dennis@gmail.com"

emails = re.findall(r"\b[A-Za-z0-9._%+-]+@(?!exclude\.com\b)[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b", text)
print(emails)