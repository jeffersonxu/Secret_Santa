import random, time

def secret_santa(givers, copy):
	pairs = {}

	for i in range(len(givers)):
		choice = random.choice(givers)
		while(choice not in copy or choice == givers[i]):
			choice = random.choice(givers)

		copy.remove(choice)
		pairs[givers[i]] = choice

	return pairs

def main(): 
	original = []

	while True:
		try:
			num_friends = int(input("How many friends do you want to include?\t"))
		except ValueError:
			print("Please enter a valid number of friends")
			continue
		else:
			break

	while len(original) < num_friends:
		f = input("Enter your friend's name:\t")
		original.append(f)

	final_list = secret_santa(original, original[:])
	print("\n----------------------------------------")

	for giver in final_list:
		print(giver, "has", final_list[giver], "as their secret santa")

if __name__ == "__main__":
	start_time = time.time()
	main()
	print("--- %.4f seconds ---" % (time.time() - start_time))