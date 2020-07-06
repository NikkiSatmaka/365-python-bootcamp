#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: nikkisatmaka
"""

# Ask the user for the radius of a circle and then print the area

# radius = float(input('Please enter the circle radius:\n>>> '))
# pi = 3.14159
# area = pi * radius**2
# print('You entered', radius, 'the area of the circle is', area)

# Convert fahrenheit to celsius

# fah = float(input('Please enter the fahrenheit value: '))
# cel = (fah - 32) * 5 / 9
# print(fah, 'Fahrenheit in Celcius is', cel)

# Obtain the product of two integers

# num1 = int(input('Please enter the first number: '))
# num2 = int(input('Please enter the second number: '))
# result = num1 * num2
# print('The product of', num1, 'and', num2, 'is', result)

# Bob, Ann, Jane and Ashwin want to order pizza - they know they will each eat
# 4 slices of pizza. The local pizza shop sells pizzas of only 6 slices
# What is the minimum number of pizzas needed - Use floor division

total_slices = 4 * 4
pizza_needed = total_slices // 6 + 1
slices_left = pizza_needed * 6 % total_slices
print(pizza_needed, slices_left)
