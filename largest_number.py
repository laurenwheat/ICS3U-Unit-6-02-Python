#!/usr/bin/env python3

# Created by: Lauren Wheatley
# Created on: June 2021
# This program determines the average of 10 random numbers


import random


def largest_number(ten_numbers):

    largest_int = ten_numbers[0]

    for loop_counter in range(0, len(ten_numbers)):
        if largest_int >= ten_numbers[loop_counter]:
            continue
        elif largest_int < ten_numbers[loop_counter]:
            largest_int = ten_numbers[loop_counter]

    return largest_int


def main():

    ten_numbers = []
    print("Here are 10 numbers:")

    for loop_counter in range(1, 10):
        random_numbers = random.randint(1, 100)
        ten_numbers.append(random_numbers)
        print(random_numbers)

    biggest_num = largest_number(ten_numbers)

    print("The largest number is {0}".format(biggest_num))


if __name__ == "__main__":
    main()
