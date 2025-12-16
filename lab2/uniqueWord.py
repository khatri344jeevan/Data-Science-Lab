# Unique Words Collector 
# Take a paragraph input from the user. Split it into words, remove duplicates, sort them 
# alphabetically, and count the total number of unique words. 
para =input("Enter the paragraph:")
para = para.lower()
words =para.split()

# unique_words =set(words)
# unique_words =sorted(unique_words)
# count_unique =len(unique_words)

# print("sorted:",unique_words)
# print("Total number of unique words:",count_unique)
unique_words=set(words)
unique_list=list(unique_words)
for i in range(len(unique_list)):
    for j in range(len(unique_list) - 1):
        if unique_list[j] > unique_list[j + 1]:
            temp = unique_list[j]
            unique_list[j] = unique_list[j + 1]
            unique_list[j + 1] = temp
print("Sorted:",unique_list)