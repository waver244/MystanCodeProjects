"""
File: boggle.py
Name:Yin Jun (Ingrid) Zeng
----------------------------------------
This functions plays the boggle game.
All words found from the alphabet inputted by the user will be listed out when the game ends.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


# Global variable
word_list = []


def main():
	"""
	This functions plays the boggle game.
	All words found from the alphabet inputted by the user will be listed out when the game ends.
	"""
	start = time.time()
	read_dictionary()

	# Input data
	lst = []
	for i in range(4):
		s_lst = []
		row = input(str(i+1) + ' row of letters: ')
		if len(row) != 7 or row[1] != ' ' or row[3] != ' ' or row[5] != ' ':
			print('Illegal input')
			return
		else:
			for ch in row:
				if ch.isalpha():
					ch = ch.lower()  # case-insensitive
					s_lst.append(ch)
		lst.append(s_lst)

	# Run every ele in lst
	ans = []
	for i in range(len(lst)):  # y
		for j in range(len(lst[i])):  # x
			find_word(lst, '', [], i, j, ans)  # Recursion for finding surrounding
	print('There are ' + str(len(ans)) + ' words in total.')

	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_word(lst, cur_s, index_check, index_y, index_x, ans):
	global word_list
	if len(cur_s) >= 4:
		if cur_s in word_list:  # Base-case
			if cur_s not in ans:  # Check if duplicates
				print('Found \"' + str(cur_s) + '\"')
				ans.append(cur_s)  # Add word into ans
	# Finding index for the surrounding
	for k in range(-1, 2, 1):  # var_y
		for l in range(-1, 2, 1):  # var_x
			y = index_y + k
			x = index_x + l
			# Check the boundaries
			if 0 <= y < 4 and 0 <= x < 4:  # Scope-in
				if (y, x) not in index_check:  # Check if duplicates
					# Choose
					cur_s += lst[y][x]
					index_check.append((y, x))  # Append used index (type: tuple)
					# Early stopping
					if has_prefix(cur_s):  # True
						# Explore
						find_word(lst, cur_s, index_check, y, x, ans)
					# Un-choose
					index_check.pop()
					cur_s = cur_s[:-1]


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global word_list
	with open(FILE, 'r') as f:
		for line in f:
			word = line.split('\n')
			word_list.append(word[0])


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in word_list:
		if word.startswith(sub_s):
			return True  # Explore
	return False  # Stop


if __name__ == '__main__':
	main()
