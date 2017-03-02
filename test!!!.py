import sys

SHOT_FIRED = False

class player(object):

	def __init__(self):
		# stores the state before transition
		# upon shooting from bullet1 => old = b1
		# n - null, b1 - bullet1, b2 - bullet2, bz - bazooka

		self.old = 'n'
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
			self.old = 'n'
		elif self.bullet1:
			self.bullet1 = False
			self.bullet2 = True
			self.old = 'b1'
		elif self.bullet2:
			self.bullet2 = False
			self.bazooka = True
			self.old = 'b2'

	def fire_bullet(self):
		if self.bullet1:
			self.old = 'b1'
			self.bullet1 = False
			self.null = True
			global SHOT_FIRED 
			SHOT_FIRED = not(SHOT_FIRED)
		elif self.bullet2:
			self.old = 'b2'
			self.bullet2 = False
			self.bullet1 = True
			global SHOT_FIRED 
			SHOT_FIRED= not(SHOT_FIRED)
		else:
			return False

	def fire_bazooka(self):
		if self.bazooka:
			self.old = 'bz'
			self.bazooka = False
			self.null = True
			self.win = True

	def take_bullet(self):
		self.dead = True

	def armor(self):
		if SHOT_FIRED:
			SHOT_FIRED = not(SHOT_FIRED)
		else:
			print "Armored for no reason!"
		self.old = self.old


def get_action_from_player_strategy1(player1, player2, playerTurn):
	if playerTurn == 1:
		if player1.null and player2.null:
		# player1.reload()
			return 1
		if player1.null and player2.bullet1:
			# player1.reload()
			return 1
		if player1.null and player2.bullet2:
			# player1.reload()
			return 1
		if player1.bullet1 and player2.null:
			# player1.reload()
			return 1
		if player1.bullet1 and player2.bullet1:
			# player1.reload()
			return 1
		if player1.bullet1 and player2.bullet2:
			# player1.fire_bullet()
			return 2
		if player1.bullet2 and player2.null:
			# player1.reload()
			return 1
		if player1.bullet2 and player2.bullet1:
			# player1.reload()
			return 1
		if player1.bullet2 and player2.bullet2:
			# player1.reload()
			return 1
	elif playerTurn == 2:
		if player1.null and player2.old=='n':
			# player1.reload()
			return 1
		if player1.null and player2.old=='b1':
			# player1.reload()
			return 1
		if player1.null and player2.old=='b2':
			# player1.reload()
			return 1
		if player1.bullet1 and player2.old=='n':
			# player1.reload()
			return 1
		if player1.bullet1 and player2.old=='b1':
			# player1.reload()
			return 1
		if player1.bullet1 and player2.old=='b2':
			# player1.fire_bullet()
			return 2
		if player1.bullet2 and player2.old=='n':
			# player1.reload()
			return 1
		if player1.bullet2 and player2.old=='b1':
			# player1.reload()
			return 1
		if player1.bullet2 and player2.old=='b2':
			# player1.reload()
			return 1


def get_action_from_player_strategy2(player1, player2, playerTurn):
	if playerTurn == 1:
		if player1.null and player2.null:
			# player1.reload()
			return 1
		if player1.null and player2.bullet1:
			# player1.reload()
			return 1
		if player1.null and player2.bullet2:
			# player1.reload()
			return 1
		if player1.bullet1 and player2.null:
			# player1.reload()
			return 1
		if player1.bullet1 and player2.bullet1:
			# player1.fire_bullet()
			return 2
		if player1.bullet1 and player2.bullet2:
			# player1.fire_bullet()
			return 2
		if player1.bullet2 and player2.null:
			# player1.fire_bullet()
			return 2
		if player1.bullet2 and player2.bullet1:
			# player1.reload()
			return 1
		if player1.bullet2 and player2.bullet2:
			# player1.reload()
			return 1
	if playerTurn == 2:
		if player1.null and player2.old=='n':
			# player1.reload()
			return 1
		if player1.null and player2.old=='b1':
			# player1.reload()
			return 1
		if player1.null and player2.old=='b2':
			# player1.reload()
			return 1
		if player1.bullet1 and player2.old=='n':
			# player1.reload()
			return 1
		if player1.bullet1 and player2.old=='b1' or player1.bullet1 and player2.bullet1:
			# player1.fire_bullet()
			return 2
		if player1.bullet1 and player2.old=='b2':
			# player1.fire_bullet()
			return 2
		if player1.bullet2 and player2.old=='n':
			# player1.fire_bullet()
			return 2
		if player1.bullet2 and player2.old=='b1':
			# player1.reload()
			return 1
		if player1.bullet2 and player2.old=='b2':
			# player1.reload()
			return 1


def get_action_from_player_strategy3(player1, player2, playerTurn):
	if playerTurn == 1:
		if player1.null and player2.null:
			# player1.reload()
			return 1
		if player1.null and player2.bullet1:
			# player1.reload()
			return 1
		if player1.null and player2.bullet2:
			# player1.reload()
			return 1
		if player1.bullet1 and player2.null:
			# player1.reload()
			return 1
		if player1.bullet1 and player2.bullet1:
			# player1.fire_bullet()
			return 3
		if player1.bullet1 and player2.bullet2:
			# player1.fire_bullet()
			return 3
		if player1.bullet2 and player2.null:
			# player1.fire_bullet()
			return 1
		if player1.bullet2 and player2.bullet1:
			# player1.reload()
			return 1
		if player1.bullet2 and player2.bullet2:
			# player1.reload()
			return 1
	if playerTurn == 2:
		if player1.null and player2.old=='n':
			# player1.reload()
			return 1
		if player1.null and player2.old=='b1':
			# player1.reload()
			return 1
		if player1.null and player2.old=='b2':
			# player1.reload()
			return 1
		if player1.bullet1 and player2.old=='n':
			# player1.reload()
			return 1
		if player1.bullet1 and player2.old=='b1':
			# player1.fire_bullet()
			return 3
		if player1.bullet1 and player2.old=='b2':
			# player1.fire_bullet()
			return 3
		if player1.bullet2 and player2.old=='n':
			# player1.fire_bullet()
			return 1
		if player1.bullet2 and player2.old=='b1':
			# player1.reload()
			return 1
		if player1.bullet2 and player2.old=='b2':
			# player1.reload()
			return 1

def get_action_from_player_strategy4(player1, player2, playerTurn):
	if playerTurn == 1:
		if player1.null and player2.null:
			# player1.reload()
			return 1
		if player1.null and player2.bullet1:
			# player1.reload()
			return 1
		if player1.null and player2.bullet2:
			# player1.reload()
			return 1
		if player1.bullet1 and player2.null:
			# player1.reload()
			return 1
		if player1.bullet1 and player2.bullet1:
			# player1.fire_bullet()
			return 1
		if player1.bullet1 and player2.bullet2:
			# player1.fire_bullet()
			return 2
		if player1.bullet2 and player2.null:
			# player1.fire_bullet()
			return 1
		if player1.bullet2 and player2.bullet1:
			# player1.reload()
			return 1
		if player1.bullet2 and player2.bullet2:
			# player1.reload()
			return 2
	if playerTurn == 2:
		if player1.null and player2.old=='n':
			# player1.reload()
			return 1
		if player1.null and player2.old=='b1':
			# player1.reload()
			return 1
		if player1.null and player2.old=='b2':
			# player1.reload()
			return 1
		if player1.bullet1 and player2.old=='n':
			# player1.reload()
			return 1
		if player1.bullet1 and player2.old=='b1':
			# player1.fire_bullet()
			return 1
		if player1.bullet1 and player2.old=='b2':
			# player1.fire_bullet()
			return 2
		if player1.bullet2 and player2.old=='n':
			# player1.fire_bullet()
			return 1
		if player1.bullet2 and player2.old=='b1':
			# player1.reload()
			return 1
		if player1.bullet2 and player2.old=='b2':
			# player1.reload()
			return 2


def get_action_from_player_strategy5(player1, player2, playerTurn):
	if playerTurn == 1:
		if player1.null and player2.null:
			# player1.reload()
			return 1
		if player1.null and player2.bullet1:
			# player1.reload()
			return 1
		if player1.null and player2.bullet2:
			# player1.reload()
			return 1
		if player1.bullet1 and player2.null:
			# player1.reload()
			return 1
		if player1.bullet1 and player2.bullet1:
			# player1.fire_bullet()
			return 2
		if player1.bullet1 and player2.bullet2:
			# player1.fire_bullet()
			return 2
		if player1.bullet2 and player2.null:
			# player1.fire_bullet()
			return 2
		if player1.bullet2 and player2.bullet1:
			# player1.reload()
			return 3
		if player1.bullet2 and player2.bullet2:
			# player1.reload()
			return 1
	if playerTurn == 2:
		if player1.null and player2.old=='n':
			# player1.reload()
			return 1
		if player1.null and player2.old=='b1':
			# player1.reload()
			return 1
		if player1.null and player2.old=='b2':
			# player1.reload()
			return 1
		if player1.bullet1 and player2.old=='n':
			# player1.reload()
			return 1
		if player1.bullet1 and player2.old=='b1':
			# player1.fire_bullet()
			return 2
		if player1.bullet1 and player2.old=='b2':
			# player1.fire_bullet()
			return 2
		if player1.bullet2 and player2.old=='n':
			# player1.fire_bullet()
			return 2
		if player1.bullet2 and player2.old=='b1':
			# player1.reload()
			return 3
		if player1.bullet2 and player2.old=='b2':
			# player1.reload()
			return 1


def get_action_from_player_strategy6(player1, player2, playerTurn):
	if playerTurn == 1:
		if player1.null and player2.null:
			# player1.reload()
			return 1
		if player1.null and player2.bullet1:
			# player1.reload()
			return 1
		if player1.null and player2.bullet2:
			# player1.reload()
			return 1
		if player1.bullet1 and player2.null:
			# player1.reload()
			return 2
		if player1.bullet1 and player2.bullet1:
			# player1.fire_bullet()
			return 3
		if player1.bullet1 and player2.bullet2:
			# player1.fire_bullet()
			return 3
		if player1.bullet2 and player2.null:
			# player1.fire_bullet()
			return 1
		if player1.bullet2 and player2.bullet1:
			# player1.reload()
			return 1
		if player1.bullet2 and player2.bullet2:
			# player1.reload()
			return 1
	if playerTurn == 2:
		if player1.null and player2.old=='n':
			# player1.reload()
			return 1
		if player1.null and player2.old=='b1':
			# player1.reload()
			return 1
		if player1.null and player2.old=='b2':
			# player1.reload()
			return 1
		if player1.bullet1 and player2.old=='n':
			# player1.reload()
			return 2
		if player1.bullet1 and player2.old=='b1':
			# player1.fire_bullet()
			return 3
		if player1.bullet1 and player2.old=='b2':
			# player1.fire_bullet()
			return 3
		if player1.bullet2 and player2.old=='n':
			# player1.fire_bullet()
			return 1
		if player1.bullet2 and player2.old=='b1':
			# player1.reload()
			return 1
		if player1.bullet2 and player2.old=='b2':
			# player1.reload()
			return 1


def main():
	gameOver = False
	playerTurn = [1, 2]
	i = 0
	shotFired = False
	p1 = player()
	p2 = player()
	inf_check = 0

	while not gameOver:
		inf_check += 1
		if not p1.dead and not p2.dead:
			# print "Player {} choose: (1) Reload, (2) Shoot, (3) Armor (4) Bazooka".format(str(playerTurn[i]))
			# choice = input("Choice:\n")

			if playerTurn[i] == 1:
				choice = get_action_from_player_strategy3(p1,p2, playerTurn[i])
			else:
			# ///////////////////////
			# (p2,p1) now because you're playing wrt p2
				choice = get_action_from_player_strategy3(p2,p1, playerTurn[i])
			# ///////////////////////
	
			print "Player: " + str(playerTurn[i]) + " Choice: " + str(choice)
			# sys.exit()

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

		if inf_check > 100:
			print "Draw!!"
			gameOver = True
	

if __name__ == '__main__':
	main()