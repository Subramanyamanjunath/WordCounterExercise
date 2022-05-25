#this program is about iterating the logic of counting the particular word in a string paragraph.

text_variable = "Microdegree is a learning platform. i learnt programming at Microdegree"

count = 0
word_list = text_variable.split(" ")
print(word_list)

for every_word in word_list:
    if ("Microdegree" == every_word):
        count = count + 1

print(count)

