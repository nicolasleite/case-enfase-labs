# Problem 1 - Ênfase Labs
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
	x1 = int(input())
	x2 = int(input())

	#calculating the distance each friend will need to walk
	distance = abs(x1-x2)/2
	tiredness = 0

	#if distance is a odd number
	if distance is not int:
		tiredness += int(distance) + 1

	#sum tiredness for each friend at every step
	for step in range(0,int(distance)):
		tiredness += 2 * (step+1)
	
	print(tiredness)
	return

if __name__ == "__main__":
	main()