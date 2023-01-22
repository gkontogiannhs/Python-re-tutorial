import re

phone_regex = r'\d{3}[-]\d{3}[-]\d{3}'
email_regex = r'[A-Za-z0-9\._]+@\w+(\.\w{3,4})'
date_regex = r'([0-2][0-9]|[30?1?])/(0[0-9]|1[0-2])/\d{4}'
az_regex = r'\ba[A-Za-z]*z\b'
cd_regex = r'\w*(cat|dog)\w*'
sentence_regex = r'^[^.!?]*[.!?]$'
swap_regex = r'(\w+,\s+)(\b\w+\s+\b)'


text = '''
The Cat in the hat, sat there with a fat rat. He ate a mat, and a bat came out of nowhere to attack.
He had 2 cats, one was black and one was white. He also had 4 dogs, 2 of them were big and 2 of them were small.
He wanted to buy a new Dog, but he couldn't decide between a Labrador or a Golden Retriever.
In the end, he decided to adopt a stray Cat from the street. He painted his room in #ff0000 color.
His email address is moew@gmail.com and his phone numbers 555-555-5555, 555.555.5555, 555555-5555, 555555.5555.
He was born on 05/12/2018, and he graduated on 01/14/2023. He also has a website https://www.example.com.
He likes to shop online and his favorite store is http://store.com and also likes to shop at www.store2.com.
His favorite color is blue and he likes to buy items that cost $9.99, $19.99, $29.99 and also $39.99.
He also likes to buy items that have a discount of $5.99 and $9.99. He has a dog named Buddy with a collar number #123456.
His best friend's email is bestfriend@example.com and his phone number is 555-555-5556.
They usually meet every 15th of the month at 7:00 pm.
'''

######################### Exercise 1: re.search(pattern, string) ############################################################
######################### Write a regular expression that matches the word "cat"
######################### Use the re.search() method to find the first match of the pattern in the string.

rg = r'\bcat\b'
pattern = re.compile(rg, re.IGNORECASE)
found = pattern.search(text)
if found: print("Fount the cat!")


######################## Exercise 2: re.match(pattern, string): 
######################## Write a regular expression that matches the word "cat"
######################## Use the re.match() method to find the first match of the pattern in the string.
rg = r'\bcat\b'
pattern = re.compile(rg, re.IGNORECASE)
matches = pattern.match(text)
print(matches)


####################### Write a regular expression that matches all the digits ####################################################
####################### Use the re.findall() method to return a list of all the matches of the pattern in the string.

rg = r'\d'
pattern = re.compile(rg)
matches = pattern.findall(text)
print(matches)


######################## Write a regular expression that matches all the words that start with "cat"
######################## Use the re.finditer() method to return an iterator that yields match objects for all the matches of the pattern in the string.

rg = r'\bcat\b'
pattern = re.compile(rg, re.IGNORECASE)
matches = pattern.finditer(text)
for match in matches:
    print(match)


######################## re.sub(pattern, repl, string, count=0)
######################## Write a regular expression that matches all the occurrences of the word "dog"
######################## re.sub() method to replace all the occurrences of the pattern with the word "puppy".

rg = r'\b(dog)\b'
pattern = re.compile(rg, re.IGNORECASE)
new_text = pattern.sub('puppy', text)
print(new_text)



####################### re.split(pattern, string, maxsplit=0): 
####################### Write a regular expression that matches the comma and space characters 

rg = r', '
pattern = re.compile(rg)
matches = pattern.split(text)
print(matches)