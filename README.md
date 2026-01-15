# Data Science Lab

### Lab 1 - Python Basics
Fundamental Python programming exercises covering control structures, functions, and basic algorithms.

1. [qn.py](lab1/qn.py) - Addition of two numbers (handles int and float)
2. [qn2.py](lab1/qn2.py) - Palindrome string checker
3. [qn3.py](lab1/qn3.py) - Prime numbers up to n
4. [qn4.py](lab1/qn4.py) - Fibonacci series generator
5. [qn5.py](lab1/qn5.py) - Greatest Common Divisor (GCD) calculator
6. [qn6.py](lab1/qn6.py) - Even or odd number checker
7. [qn7.py](lab1/qn7.py) - Largest number in a list
8. [qn8.py](lab1/qn8.py) - Leap year checker
9. [qn9.py](lab1/qn9.py) - Temperature converter (Celsius to Fahrenheit/Kelvin)
10. **Question 10 - Multi-file project:**
    - [age.py](lab1/qn10/age.py) - Birth year calculator with leap year check
    - [bmi.py](lab1/qn10/bmi.py) - BMI calculator with category classification
    - [army.py](lab1/qn10/army.py) - Army eligibility checker based on age and BMI

### Lab 2 - Data Structures & Collections
Working with Python dictionaries, lists, tuples, and sets for data manipulation.

1. [movie_rating.py](lab2/movie_rating.py) - Movie ratings analyzer (average, highest-rated, above-average movies)
2. [marks.py](lab2/marks.py) - Student marks manager with grade computation and top performers
3. [inventory.py](lab2/inventory.py) - Store inventory tracker (add, sell, low-stock alerts)
4. [uniqueWord.py](lab2/uniqueWord.py) - Unique words collector from paragraph with frequency count
5. [wordreverse.py](lab2/wordreverse.py) - Word reverser (reverses words with even length)
6. [pathvalidator.py](lab2/pathvalidator.py) - Simple path validator using graph representation

### Lab 3 - File Handling & Exception Management
File I/O operations with text, CSV, and JSON files, implementing robust error handling.

1. [basicFile.py](lab3/basicFile.py) - Basic file read and write operations with exception handling
2. [csvFile.py](lab3/csvFile.py) - CSV file handling for student records
3. [fileWithException.py](lab3/fileWithException.py) - Number processing from file with error handling
4. [jsonFile.py](lab3/jsonFile.py) - JSON data writing and reading with exception handling
5. [menuFileOps.py](lab3/menuFileOps.py) - Menu-driven file operations (write, read, append)

### Lab 4 - Advanced Python Features

1. [sortMarks.py](lab4/sortMarks.py) - Write a Python script that takes a list of student marks and sorts them in descending order (highest to lowest) using either the `sorted()` function or the `.sort()` method.
2. [calculateSum.py](lab4/calculateSum.py) - Given a list of student names and a list of their corresponding scores, use the `zip()` function to pair them together and then apply the `reduce()` function from the `functools` module to calculate the total sum of all scores.
3. [generator.py](lab4/generator.py) - Create a generator function using the `yield` keyword that produces numbers from 1 to 5 one by one to illustrate how lazy evaluation can save memory when dealing with large datasets.
4. [randomSelect.py](lab4/randomSelect.py) - Write a Python script that takes a list of six student names and uses the `random.sample()` function to randomly select exactly three "Volunteers" for a presentation, ensuring that no student is picked more than once in the selection.
5. [reModule.py](lab4/reModule.py) - Use the `re` module to write a script that searches through a paragraph and extracts all words that start with an uppercase letter (e.g., "London", "Python") to identify proper nouns or sentence starters.
6. [listComprehension.py](lab4/listComprehension.py) - Use a list comprehension to create a new list containing only the even numbers between 1 and 20, demonstrating a more concise and readable alternative to traditional loops.