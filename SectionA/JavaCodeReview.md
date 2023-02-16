# Code Review for Buso

## Summary

This code is designed to reverse a string and print the Fibonacci series of 10 numbers. However, there are a few issues with the implementation.

## Correctness

**Naming conventions:**

1. The reverse_string function is correctly implemented to reverse the input string. However, the function name and the recursive function call inside the method do not match. The function name is reverse_string, but it is called as reverseString. This will cause a compile-time error.

- Getting user input:

- Printing output: The output of the 'reverse_string' method is being printed within the method. It would be better to return the reversed string and print it outside the method.

2. The upper level class name (line 1) should start with a capital letter ie follow the **Pascal case** naming convention to be consistent with Java standards.

3. The function name "function" (line 24) should be named better, try to always use more descriptive variable names such as findFibonacciNumbers() as generic words such as function could be **reserved words** in other programing languages, and confusing to fellow developers.

4. The variable 'maxNumber' (lines 24 and 26) has been declared twice, which is causing a compilation error. The signature of this function is also wrong in that you gave it a generic type <T> unecessarily (line 24) in order to be able to initialize this maxNumber variable again as an int. It would be better to remove the generic type on the function and pass in a variable maxNumber of type int to the function on line 24 then remove the maxNumber initialization in the function.

5. The Fibonacci series is hardcoded (line 8), and the output statement does not match the series being printed. The output statement mentions 10 numbers, but the series printed has only 9 numbers. You also have not used recursion to come to your solution this also needs some work.

**Efficiency**

The efficiency of the code is decent, as the reverse_string method recursively reverses the given string in an elegant way. However:

1. You have made use of built in method substring() to get to your solution (line 26). Built in methods aren't always the best choice if you're working towards a solution with efficiency in mind as you don't have full control over the time and space complexity of the method unlike when you work to a manual solution yourself. So always look up the time and space complexity of inbuilt functions before you use them (in rare cases where it is of concern) and see whether you can work with your peers to write your own more efficient method.

2. There's no reason to print out the new string at every recursive run in your reverse_string method as this also affects efficiency especially if you're calculating a substring with every call (line 24-25). the function method for printing Fibonacci series could be improved by using memoization to store the previously calculated Fibonacci numbers instead of calculating them again and again.

**Style**

The code mostly follows Java's standard naming conventions relatively readable, however the indentation isn't consistent and the code isn't properly commented in some cases. Class name should be changed to Recursion and some function signatures should be changed to follow Java naming conventions.

[See Java Code Conventions](https://www.oracle.com/technetwork/java/codeconventions-150003.pdf)

Documentation
The code is adequately documented with inline comments explaining the purpose of each method and variable. However, there is no Javadoc style documentation to explain the overall purpose and functionality of the class and some of the comments are unnecessary.

## Recommendation Summary

**Naming conventions:** Update the class name to start with a capital letter, and rename the variable 'maxNumber' to 'numberOfFibonacciNumbers' to be more descriptive.

**Code logic:** Change the parameter of the 'function' method to an integer type and remove the generic type '<T>'. Call the 'function' method in the main function to print the Fibonacci series.
Method signature: Change the name of the 'reverse_string' method to 'reverseString' to match the function call, and remove the generic type '<T>'. Use recurion for both solutions, don't forget to ask for help from your peers as this is an important part of being a Software Engineer.

**Printing output:** Remove the print statement in the 'reverseString' method, return it's result and then store the reversed string in a variable and print it out in the main function.

**Documentation:** Update the comments to follow proper formatting and remove any unnecessary comments.
Corrected Code

**Conclusion:** Hi Buso, I hope you're well. Well done on staying focused on your learning so far, and not being afraid to ask for help when need be. These traits will take you far when you're in Industry.

Overall your code is not far from being correct, efficient and well-written with proper documentation. However, there are a few minor issues that need to be fixed to make the code more readable, maintainable and for it to compile and run.

You're more then welcome to work on what I've pointed out in this code review and send it to me to review again. All the best and may the code be with you!
