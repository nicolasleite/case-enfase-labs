# Problem 3 - Ênfase Labs
# Copyright (C) 2019  Nícolas Bassetto Leite

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

def main():
	lenght = int(input())
	seq = []
	positives = 0
	negatives = 0

	temp = input().split()
	for item in temp:
		seq.append(int(item))
		if int(item) > 0:
			positives += 1
		elif int (item) < 0:
			negatives += 1

	# sorting input, so it's easier to find the fibonaccian function
	# if most numbers are positive, the function will be crescent
	# if most numbers are negative, the function will be decrescent
	if positives > negatives:
		seq.sort()
	else:
		seq.sort(reverse = True)


	# looking for the first three elements of the function
	fib = []
	for i in range(0, lenght):
		for j in range(0, lenght):
			for k in range(0, lenght):
				if seq[k] is seq[j]+seq[i] and i is not j and j is not k:
					fib.append(seq[i])
					fib.append(seq[j])
					fib.append(seq[k])
					for item in fib:
						seq.remove(item)
					break
			if len(fib) is not 0:
				break
		if len(fib) is not 0:
			break

	while seq is not []:
		nextElement = fib[len(fib)-1] + fib[len(fib)-2]
		prevElement = fib[1] - fib[0]
		altPrev = fib[0] - fib[1]
		if nextElement in seq:
			fib.append(nextElement)
			seq.remove(nextElement)
		elif prevElement in seq:
			newFib = [prevElement]
			fib = newFib + fib
			seq.remove(prevElement)
		elif altPrev in seq:
			valid = True
			if len(fib) > 3:
				if fib[0] + fib[2] is not fib[3]:
					valid = False
			if valid:
				newFib = [altPrev, fib[1], fib[0]]
				fib.pop(0)
				fib.pop(0)
				fib = newFib + fib
		else:
			break

	print (len(fib))

	return

if __name__ == "__main__":
	main()