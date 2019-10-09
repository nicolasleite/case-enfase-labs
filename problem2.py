# Problem 2 - Ênfase Labs
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

#return 0 if it's a tie, -1 if its invalid or the winner number
def checkWinner(game):
	firstWins = ['X', 'X', 'X']
	secondWins = ['0','0','0']

	allResults = []
	mainDiag = []
	secDiag = []
	for i in range(0,3):
		newColumn = []
		newLine = []
		for j in range(0,3):
			newColumn.append(game[j][i])
			newLine.append(game[i][j])
		allResults.append(newColumn)
		allResults.append(newLine)
		mainDiag.append(game[i][i])
		secDiag.append(game[i][2-i])

	allResults.append(mainDiag)
	allResults.append(secDiag)

	if secondWins in allResults and firstWins in allResults:
		return -1

	elif secondWins in allResults:
		return 2
	elif firstWins in allResults:
		return 1

	else:
		return 0

#returns number of next player
def checkNextPlayer(first, second):
	if first > second:
		return 2
	else: 
		return 1

def main():
	game = []
	firstPlays = 0
	secondPlays = 0
	fullBoard = True
	invalidGame = False

	for line in range(0,3):
		game.append(list(input()))
		
	#checks input's validity and current state of game
	for line in game:
		if len(line) is not 3:
			invalidGame = True
			break

		for row in line:
			if row is "X":
				firstPlays += 1
			elif row is "0":
				secondPlays += 1
			elif row is "." and fullBoard:
				fullBoard = False
			else:
				invalidGame = True
				break

	if firstPlays > (secondPlays + 1) or secondPlays > firstPlays:
		invalidGame = True


	if invalidGame:
		print("inválido")
	
	else:
		winner = checkWinner(game)
		
		if winner is 1:
			print("primeiro_venceu")
		elif winner is 2:
			print("segundo_venceu")
		elif winner is -1:
			print("inválido")
		
		elif fullBoard:
			print("empate")
		else:
			nextPlayer = checkNextPlayer(firstPlays, secondPlays)
			if nextPlayer is 1:
				print ("primeiro")
			else:
				print ("segundo")

	return

if __name__ == "__main__":
	main()