# -*- coding: utf-8 -*-

""" Simple calculator. """

def addition(num1, *args):
    total = num1
    for num in args:
        total = total + num
    return total

def subtraction(num1, *args):
    total = num1
    for num in args:
        total = total - num
    return total

def multiplication(num1, *args):
    total = num1
    for num in args:
        total = total * num
    return total

def division(num1, *args):
    total = num1
    for num in args:
        total = total / num
    return total
