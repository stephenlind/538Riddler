# Solution to FiveThirtyEight's Riddler problem:
# http://fivethirtyeight.com/features/can-you-best-the-mysterious-man-in-the-trench-coat/

lowest = 1
highest = 1000
highest_winnings = 0
winningest_guess = 0

# try each starting number
for starting in range(lowest, highest + 1):
	total_winnings = 0 

  # for each starting number, test every possible 'purse'
	for money in range(lowest, highest + 1):
		upper_bound = highest
		lower_bound = lowest
		
		# from the starting number, binary search to find the purse
		num_guesses = 1
		current_guess = starting
		while num_guesses <= 9:
			num_guesses += 1
			
			if current_guess > money:
				upper_bound = current_guess - 1
				current_guess = (upper_bound - lower_bound) / 2
			elif current_guess < money:
				lower_bound = current_guess + 1
				current_guess = (upper_bound - lower_bound) / 2
			elif current_guess == money:
				total_winnings += money
				#print "won", money, "total", total_winnings
				break
				
			if upper_bound == lower_bound:
				current_guess = upper_bound
				
	if total_winnings > highest_winnings:
		highest_winnings = total_winnings
		winningest_guess = starting
		
	print "starting number:", starting, "winnings:", total_winnings
	
print "winningest starting:", winningest_guess, "total:", highest_winnings
			
