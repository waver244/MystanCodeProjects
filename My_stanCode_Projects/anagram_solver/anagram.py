"""
File: anagram.py
Name:Yin Jun (Ingrid) Zeng
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time  # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'  # This is the filename of an English dictionary
EXIT = '-1'  # Controls when to stop the loop

# Global variable
word_list = []


def main():
    """
    This function recursively finds all the anagram(s) for the word input by user
    and terminates when the input string matches the EXIT
    """
    print('Welcome to stanCode \"Anagram Generator\" (or -1 to quit)')
    while True:
        word = input('Find anagrams for: ')
        start = time.time()
        if word == EXIT:
            break
        else:
            print('Searching...')
            find_anagrams(word)
        end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end - start} seconds.')


def read_dictionary():
    global word_list
    with open(FILE, 'r') as f:
        for line in f:
            word = line.split('\n')
            word_list.append(word[0])


def find_anagrams(s):
    """
    :param s: string, inputted word from user
    :return: string, result of all anagrams
    """
    global word_list
    read_dictionary()
    ans = []
    find_anagrams_helper(s, '', [], ans)
    print(str(len(ans)) + ' anagrams: ' + str(ans))


def find_anagrams_helper(s, cur_s, lst, ans):
    """
    :param s: string, inputted word from user
    :param cur_s: string, current s
    :param lst: list, list containing all checked alphabet of s
    :param ans: list, list containing all found anagrams
    :return: string, records of finding anagrams
    """
    global word_list
    if len(cur_s) == len(s):  # Base-case
        if cur_s in word_list:  # Check if exists in word_list
            if cur_s in ans:  # Check if duplicates
                pass
            else:
                print('Found: ' + str(cur_s))
                print('Searching...')
                ans.append(cur_s)  # Add into ans
    else:
        for i in range(len(s)):
            if i in lst:  # Check if duplicates
                pass
            else:
                # Choose
                cur_s += s[i]
                lst.append(i)
                # Early stopping
                if has_prefix(cur_s):  # True
                    # Explore
                    find_anagrams_helper(s, cur_s, lst, ans)
                # Un-choose
                lst.pop()
                cur_s = cur_s[:-1]


def has_prefix(sub_s):
    """
    :param sub_s: string, cur_s from find_anagrams_helper
    :return: True or False, depends on whether there is any word in word_list that starts with sub_s
    """
    global word_list
    for word in word_list:
        if word.startswith(sub_s):
            return True  # Explore
    return False  # Stop


if __name__ == '__main__':
    main()
