"""Activity 4: Extend the following program to test accuracy of operations using the assert statement."""


# Python String Operations with Assertions

str1 = 'Hello'
str2 = 'World!'

# using +
concatenation = str1 + str2
print('str1 + str2 = ', concatenation)
assert concatenation == 'HelloWorld!', "Wrong. Expected: 'Hello World!"

# using *
multiplication = str1 * 3
print('str1 * 3 =', multiplication)
assert multiplication == 'HelloHelloHello', "Wrong. Expected: 'HelloHelloHello'"




"""References
W3Schools. (N.D.) Python assert Keyword. Available from:
https://www.w3schools.com/python/ref_keyword_assert.asp [Accessed 23 January 2024]."""
