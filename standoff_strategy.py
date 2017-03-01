import sys

class player(object):

	def __init__(self):
		self.null = True
		self.bullet1 = False
		self.bullet2 = False
		self.bazooka = False
		self.win = False
		self.dead = False

	def reload(self):
		if self.null:
			self.null = False
			self.bullet1 = True
		elif self.bullet1:
			self.bullet1 = False
			self.bullet2 = True
		elif self.bullet2:
			self.bullet2 = False
			self.bazooka = True

	def fire_bullet(self):
		if self.bullet1:
			self.bullet1 = False
			self.null = True
		elif self.bullet2:
			self.bullet2 = False
			self.bullet1 = True
		else:
			return False

	def fire_bazooka(self):
		if self.bazooka:
			self.win = True

	def take_bullet(self):
		self.dead = True


def main():
	gameOver = False
	playerTurn = [1, 2]
	i = 0
	shotFired = False
	p1 = player()
	p2 = player()

	p1_strategy = iter([1,1,1])
	p2_strategy = iter([1,2,2])
	playerStrategies = [p1_strategy, p2_strategy]

	while not gameOver:
		if not p1.dead and not p2.dead:
			# print "Player {} choose: (1) Reload, (2) Shoot, (3) Armor (4) Bazooka".format(str(playerTurn[i]))
			# choice = input("Choice:\n")

			choice = next(playerStrategies[playerTurn[i]-1])
			print choice
			print "Player" + str(playerTurn[i])

			if playerTurn[i] == 1:	# player 1's turn
				if choice == 1:
					if shotFired:
						p1.take_bullet()
					else:
						p1.reload()
				elif choice == 2 and p1.bullet1 == False and p1.bullet2 == False:
					print "You have no bullets! Choose again!"
					continue
				elif choice == 2:
					p1.fire_bullet()
					shotFired = not(shotFired)
				elif choice == 3:
					if shotFired:
						print "Shielded"
						shotFired = not(shotFired)
					else:
						print "Shielded for no reason!"
				
				if choice == 1 and shotFired: # player 1 hasn't fired/shielded
					p1.take_bullet()

				if p1.bazooka and not shotFired:
					p1.fire_bazooka()
				
			elif playerTurn[i] == 2:	# player 2's turn
				if choice == 1:
					if shotFired:
						p2.take_bullet()
					else:
						p2.reload()
				elif choice == 2 and p2.bullet1 == False and p2.bullet2 == False:
					print "You have no bullets! Choose again!"
					continue
				elif choice == 2:
					p2.fire_bullet()
					shotFired = not(shotFired)
				elif choice == 3:
					if shotFired:
						print "Shielded"
						shotFired = not(shotFired)
					else:
						print "Shielded for no reason!"
				
				if choice == 1 and shotFired: # player 2 hasn't fired/shielded
					p2.take_bullet()

				if p2.bazooka and not shotFired:
					p2.fire_bazooka()
				
			i = (i+1) % 2

		if p1.dead and p2.dead or p1.win and p2.win:
			continue
			
		if p1.dead or p2.win:
			print "Player 2 wins!!"
			gameOver = True
		elif p2.dead or p1.win:
			print "Player 1 wins!!"
			gameOver = True



if __name__ == '__main__':
	main()