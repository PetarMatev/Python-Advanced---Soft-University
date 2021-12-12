# 05. Word Count:
# Write a program that reads a list of words from the file words.txt and finds how many times
# each of the words is contained in another file text.txt. Matching should be case-insensitive.
# The results should be written to another text files. Sort the words by frequency in descending order.

words = open('D:\\03. Python\\03. Python Advanced\\13. File Handling\\words.txt', 'w')
words.write("quick is fault")
words.close()

input = open('D:\\03. Python\\03. Python Advanced\\13. File Handling\\input.txt', 'w')
input.write(f"-I was quick to judge him, but it wasn't his fault."
            f"\n-Is this some kind of joke?! Is it?"
            f"\n-Quick, hide here…It is safer.")
input.close()

words = open('D:\\03. Python\\03. Python Advanced\\13. File Handling\\words.txt', 'r')
input = open('D:\\03. Python\\03. Python Advanced\\13. File Handling\\input.txt', 'r')

searched_words = [i for i in str(*words).split()]
input_list = []
for line in str(*input):
    input_list.append(line)

print(input_list)