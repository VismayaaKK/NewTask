#1. write a python function to find the largest number in a list of numbers.

def find_largest_number(numbers: list):
    if not numbers:
        raise ValueError
    largest_number = numbers[0]
    for number in numbers:
        if number > largest_number:
            largest_number = number
    return largest_number
numbers_list = [4,2,8,-8,6,0,-1,13,-13,24]
print(find_largest_number(numbers_list)) 

#2. write a python function to check  if a given string is a palindrome(reads the same backward as forward) the largest number in a list of numbers
   
def is_palindrome(s: str):
    cleaned_string = ''.join(filter(str.isalnum, s)).lower()
    return cleaned_string == cleaned_string[::-1]
def largest_number(numbers: list) -> int:
    if not numbers:
        raise ValueError("The list is empty")
    return max(numbers)
string_to_check = "A man, a plan, a canal, Panama"
numbers_list = [3, 5, 7, 2, 8, -1, 4, 10, 12]
print(is_palindrome(string_to_check))  
print(largest_number(numbers_list))    


#3. write a function to check if a number is a prime number

def is_prime(n: int):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
number_to_check = 29
print(is_prime(number_to_check))  


#4.write a python function to count the number of vowels in a given string

def count_vowels(s: str):
    vowels = 'AEIOUaeiou'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
input_string = "Beautiful"
print(count_vowels(input_string)) 

#5.write a python function to find the sum of the digits of a given number

def sum_of_digits(number: int):
    sum_digits = 0
    while number > 0:
        sum_digits += number % 10  
        number = number // 10      
    return sum_digits
input_number =555324
print(sum_of_digits(input_number))  
