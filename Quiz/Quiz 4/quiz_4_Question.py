# Uses National Data on the relative frequency of given names
# in the population of U.S. births,
# stored in a directory "names", in files named "yobxxxx.txt
# with xxxx (the year of birth)
# ranging from 1880 to2013.
# Prompts the user for a first name, and finds out the first year
# when this name was most popular in terms of frequency of names being given,
# as a female name and as a male name.
#
# Written by *** and Eric Martin for COMP9021


import os
from sys import exit

first_name = input('Enter a first name: ')
directory = 'names'
min_male_frequency = 0
male_first_year = None
min_female_frequency = 0
female_first_year = None



# Replace this comment with your code

if not female_first_year:
    print('In all years, {:} was never given as a female name.'.
                                      format(first_name))
else:
    print('In terms of frequency, {:} was the most popular '
          'as a female name first in the year {:}.\n'
          '  It then accounted for {:.2f}% of all female names'.
          format(first_name,
                 female_first_year,
                 min_female_frequency))
if not male_first_year:
    print('In all years, {:} was never given as a male name.'
                                               .format(first_name))
else:
    print('In terms of frequency, {:} was the most popular '
          'as a male name first in the year {:}.\n'
          '  It then accounted for {:.2f}% of all male names'.
          format(first_name,
                 male_first_year,
                 min_male_frequency))
