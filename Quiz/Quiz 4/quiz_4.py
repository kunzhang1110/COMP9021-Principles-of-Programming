# Uses National Data on the relative frequency of given names
# in the population of U.S. births,
# stored in a directory "names", in files named "yobxxxx.txt
# with xxxx (the year of birth)
# ranging from 1880 t o2013.
# Prompts the user for a first name, and finds out the first year
# when this name was most popular in terms of frequency of names being given,
# as a female name and as a male name.
#
# Written by Kun Zhang and Eric Martin for COMP9021


import os
import re
from sys import exit

first_name = input('Enter a first name: ')
directory = 'names'
min_male_frequency = 0
male_first_year = None
min_female_frequency = 0
female_first_year = None

# Open Files
folder = os.listdir(directory)
folder.sort()

for filename in folder:
    m_count = 0    # all male names in a file
    f_count = 0     # all female names in a file

    if not filename.endswith('txt'):
        continue
    match = re.search(r'\d{4}', filename)
    year = match.group()
    path = './' + directory + '/' + filename
    fh = open(path, 'r')
    year_data = [0, 0]  #[Male Number, Female Number]
    for line in fh:
        given_name, sex, count = line.split(",")
        count = int(count)
        if sex == 'M':
            m_count += count
            if given_name == first_name:
                year_data[0] = count        # record Male number
        elif sex == 'F':
            f_count += count
            if given_name == first_name:
                year_data[1] = count        # record Female number

    m_freq = year_data[0]/m_count * 100
    if m_freq> min_male_frequency:
        min_male_frequency = m_freq
        male_first_year = year

    f_freq = year_data[1]/f_count * 100
    if f_freq> min_female_frequency:
        female_first_year = year
        min_female_frequency = f_freq


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
