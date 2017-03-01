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
	while not gameOver:
		if not p1.dead and not p2.dead:
			print "Player {} choose: (1) Reload, (2) Fire, (3) Shield (4) Bazooka".format(str(playerTurn[i]))
			choice = input("Choice:\n")

			if playerTurn[i] == 1:
				if choice == 1:
					if shotFired:
						p1.take_bullet()
					else:
						p1.reload()
				elif choice == 2 and p1.bullet1 == False and p2.bullet2 == False:
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
				elif choice == 4:
					if shotFired:
						p1.take_bullet()
					else:
						p1.fire_bazooka()
				
				if choice == 1 and shotFired: # player 1 hasn't fired/shielded
					p1.take_bullet()

			elif playerTurn[i] == 2:
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
				elif choice == 4:
					if shotFired:
						p2.take_bullet()
					else:
						p2.fire_bazooka()
				
				if choice == 1 and shotFired: # player 2 hasn't fired/shielded
					p2.take_bullet()

		if p1.dead or p2.win:
			print "Player 2 wins!!"
			break
		elif p2.dead or p1.win:
			print "Player 1 wins!!"
			break

		i = (i+1) % 2


if __name__ == '__main__':
	main()