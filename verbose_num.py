#!/usr/bin/python3

import sys
#possible to add more nums to this 
names = [ 
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eightteen",
    "nineteen",
    "twenty",
    "thirty",
    "fourty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
    "thousand",
    "million",
    "billion",
    "trillion",
    "quadrillion",
    "quintillion",
    "sextillion",
    "septillion",
    "octillion",
    "nonillion",
    "decillion",
    "undecillion",
    "duodecillion",
    "tredecillion",
    "quattuordecillion",
    "quindecillion",
    "sexdecillion",
    "septendecillion",
    "octodecillion",
    "novemdecillion",
    "vigintillion",
    "centillion"
]


def short_scale(num, i=0):
    """Takes a positive integer and returns the short scale name of it.
    See: 'https://en.wikipedia.org/wiki/Long_and_short_scales'"""
    
    # which set of three numbers leftmost numbers belong to
    # where 0 is hundreds, 1 is thousands, 2 is millions, etc.
    place_pos = ((num_length(num) + 1) // 3) - 1

    # the leftmost place quantifier eg. thousand, million, etc.
    place_quantifier = names[place_pos + 26 ]

    # used to split apart number at left end
    base = 1000 ** place_pos

    if i == 0:
        if num == 0:
            return ["zero"]
        elif (num < 1000) and (num % 100 == 0):
            return short_scale_hundreds(num)
    
    if num >= 1000:
        #works left to right on number
        return short_scale_hundreds(num // base) + [place_quantifier] + short_scale(num % base, i=i+1)
    else:
        #at the end of the number we say and to signify we are done talking
        return short_scale_hundreds(num)

def short_scale_hundreds(num):
    """Takes a number and returns the short scale name of it if it's less than 1000."""
    if (num == 0) or (num >= 1000):
        return [""]
    elif num <= 20:
        return [names[num - 1]]
    elif num < 100:
        return [names[(num // 10) + 17]] + short_scale_hundreds(num % 10)
    else:
        return [names[(num // 100) - 1], "hundred"] + short_scale_hundreds(num % 100)


def num_length(num, base=10):
    """returns the number of digits in a number."""
    length = 1
    while(num > 0):
        length += 1
        num = num // base

    return length


def main(argv):
    if len(argv) != 2:
        print(f"usage: {argv[0]} [number]")
    else:
        
        # we use lists so formatting is done once and spacing isn't terrible
        num = int(argv[1])
        #TODO calculate largest digit based on values in nums
        #larget_num is 1000 centillion
        largest_num = 1000000000000000000000000000000000000000000000000000000000000000000000
        if num >= largest_num:
            print("name unknown, exiting...")
            return


        if(num < 0):
            print(" ".join(["negative"] + short_scale(abs(num))))
        else:
            print(" ".join(short_scale(abs(num))))

if __name__ == "__main__":
    main(sys.argv)
