import random
import time
import re

#state variables:
frame_scores = {}
DISABLE_ASCII = False

def favorable():
	outcome = random.choice([True, False])
	return outcome

def calculate_gamescore():
	global frame_scores
	print(" ")
	print("Final Scores: ", frame_scores)
	print(" ")
	GAME_SCORE = 0

	for i in range (1, len(frame_scores)):
		#print("run: ", i)

		FRAME_SCORE = 0
		temp_score = 0

		#Intuition: The score will only be '10' for strikes, else it'll be a list of roll scores

		#0 - if it's a strike, calculate the total frame score w/ bonus
		if frame_scores[i] == 10:
			temp_score = 10

			#1 - if next frame is also a strike:
			if frame_scores[i+1] == 10:
				temp_score += 10
				
				#2 - same logic here to check if next frame is also a strike...
				if frame_scores[i+2] == 10:
					temp_score += 10
				#2 - ...or not!
				else:
					temp_score += frame_scores[i+2][0]
			
			#1 - if not a strike, check the scores of the two rolls within the next frame
			else:
				for j in range(0, len(frame_scores[i+1])):
					temp_score += frame_scores[i+1][j]

			FRAME_SCORE += temp_score

		#0 - if not a strike, calculate frame score by summing rolls
		else:
			for j in range(0, len(frame_scores[i])):
				temp_score += frame_scores[i][j]

			#3 - It was a Spare! Add next roll score as bonus:
			if temp_score == 10:
				if frame_scores[i+1] == 10:
					temp_score += 10
				else:
					temp_score += frame_scores[i+1][0]

			FRAME_SCORE += temp_score

		print("Frame score for frame ", i, " is: ", FRAME_SCORE)
		GAME_SCORE += FRAME_SCORE

	print("Final Game Score is: ", GAME_SCORE)
	return GAME_SCORE
###############################################END CALCULATE_GAMESCORE()####################################



def roll_ascii():
	if DISABLE_ASCII:
		return
	print("=========================================================================================")
	print("                   >                                                                   | ")
	print("                     >                                                               |   ")
	print("                        >                                                          |   | ")
	print(" O                         >                                                     |   |   ")
	print("                        >                                                          |   | ")
	print("                     >                                                               |   ")
	print("                   >                                                                   | ")
	print("=========================================================================================")
	time.sleep(1)
	print(" ")
	print(" ")
	print(" ")
	print("=========================================================================================")
	print("                   >                                                                   | ")
	print("                     >                                                               |   ")
	print("                        >                                                          |   | ")
	print("                           >    O                                                |   |   ")
	print("                        >                                                          |   | ")
	print("                     >                                                               |   ")
	print("                   >                                                                   | ")
	print("=========================================================================================")
	time.sleep(1)
	print(" ")
	print(" ")
	print(" ")
	print("=========================================================================================")
	print("                   >                                                                   | ")
	print("                     >                                                               |   ")
	print("                        >                                                          |   | ")
	print("                           >                                            O        |   |   ")
	print("                        >                                                          |   | ")
	print("                     >                                                               |   ")
	print("                   >                                                                   | ")
	print("=========================================================================================")
	time.sleep(1)
	print(" ")
	print(" ")
	print(" ")


def split_ascii():
	if DISABLE_ASCII:
		return
	print(" ")
	print(" ")
	print(" ")
	print("=========================================================================================")
	print("                   >                                                                   / ")
	print("                     >                                                               /   ")
	print("                        >                                                          /     ")
	print("                           >                                                     SPLIT!  ")
	print("                        >                                                          /     ")
	print("                     >                                                               /   ")
	print("                   >                                                                   / ")
	print("=========================================================================================")
	time.sleep(1)
	print(" ")
	print(" ")
	print(" ")

def openframe_ascii():
	if DISABLE_ASCII:
		return
	print(" ")
	print(" ")
	print(" ")
	print("=========================================================================================")
	print("                   >                                                                   / ")
	print("                     >                                                               /   ")
	print("                        >                                                          /     ")
	print("                           >                                                OPEN FRAME   ")
	print("                        >                                                          /     ")
	print("                     >                                                               /   ")
	print("                   >                                                                   / ")
	print("=========================================================================================")
	time.sleep(1)
	print(" ")
	print(" ")
	print(" ")

def strike_ascii():
	if DISABLE_ASCII:
		return
	print(" ")
	print(" ")
	print(" ")
	print("=========================================================================================")
	print("                   >                                                                     ")
	print("                     >                                                                   ")
	print("                        >                                                                ")
	print("                           >                                                  STRIKE!!   ")
	print("                        >                                                                ")
	print("                     >                                                                   ")
	print("                   >                                                                     ")
	print("=========================================================================================")
	time.sleep(1)
	print(" ")
	print(" ")
	print(" ")

def spare_ascii():
	if DISABLE_ASCII:
		return
	print(" ")
	print(" ")
	print(" ")
	print("=========================================================================================")
	print("                   >                                                                     ")
	print("                     >                                                                   ")
	print("                        >                                                                ")
	print("                           >                                                  SPARE!!    ")
	print("                        >                                                                ")
	print("                     >                                                                   ")
	print("                   >                                                                     ")
	print("=========================================================================================")
	time.sleep(1)
	print(" ")
	print(" ")
	print(" ")

def gutter_ascii():
	if DISABLE_ASCII:
		return
	print(" ")
	print(" ")
	print(" ")
	print("=========================================================================================")
	print("                   >                                                                   | ")
	print("                     >                                                               |   ")
	print("                        >                                                          |   | ")
	print("                           >                                     GUTTER!!        |   |   ")
	print("                        >                                                          |   | ")
	print("                     >                                                               |   ")
	print("                   >                                                                   | ")
	print("=========================================================================================")
	time.sleep(1)
	print(" ")
	print(" ")
	print(" ")


#########################################END ASCII funcs#####################################################


def gameMode():

	#This function is used for bonus rolls only: 
	def bonusRoll():
		score = 0
		roll_ascii()
		#1 - Does the ball strike the pins?
		if favorable():
			
			#2 - Did it hit the pocket: it's a strike!
			if favorable():
				print("STRIKE!!")
				strike_ascii()
				score += 10

			#2b - Not a pocket-hit	
			else:

				#3 - It hit head-on, is it a split or still a strike?
				if favorable():
					#3b - Strike!
					print("HEAD-ON STRIKE!!")
					strike_ascii()
					score += 10

				else:
					#3b - Split!
					split_score = random.randint(0,9)
					score += split_score
					print("It's a SPLIT!")
					split_ascii()
		
		#1b - It went into the gutter!
		else:
			print("You rolled into the gutter!")
			gutter_ascii()

		print("roll score: ", score)
		return score
			

	FINAL_SPARE = False
	FINAL_STRIKE = False

	for i in range(1,12):

		#10 frames  done, checking if any bonus rolls are applicatble:
		if i == 11 and not FINAL_STRIKE and not FINAL_SPARE:
			frame_scores.update({11:[0]})
			continue
		elif i == 11 and FINAL_STRIKE:
			turn_score = []
			for j in range(2):
				print(" ")
				input("Press Enter to roll...")
				print(" ")
				roll_score = bonusRoll()
				turn_score.append(roll_score)
			frame_scores.update({11:turn_score})
			continue
		elif i == 11 and FINAL_SPARE:
			turn_score = []
			print(" ")
			input("Press Enter to roll...")
			print(" ")
			roll_score = bonusRoll()
			turn_score.append(roll_score)
			frame_scores.update({11:turn_score})
			continue
		
		#initializing basic data for the frame:
		FRAME_SCORE = 0
		print(" ")
		print("FRAME ", i)
		
		WAS_STRIKE = False
		WAS_SPARE = False

		#Time to roll!
		for j in range(2):

			if j == 1 and WAS_STRIKE:
				continue

			print(" ")
			input("Press Enter to roll...")
			print(" ")
			roll_ascii()
			print("ROLL ", j+1)


			# #1 - Does the ball strike the pins?
			# if favorable():
				
			#2 - Did it hit the pocket: it's a strike!
			if j == 0 and favorable():

				print("STRIKE!!")
				strike_ascii()
				print("roll score: 10")
				frame_scores.update({i: 10})
				WAS_STRIKE = True

			#2b - Not a strike	
			else:

				#3 - It hit head-on, is it a split or still a strike?
				if j == 0 and favorable():
					
					#3b - Strike!
					print("HEAD-ON STRIKE!!")
					strike_ascii()
					print("roll score: 10")
					frame_scores.update({i: 10})
					WAS_STRIKE = True

				#3b - Split!
				else:

					if j == 0:
						split_score = random.randint(0,9)
						FRAME_SCORE += split_score
						split_ascii()
						print("It's a SPLIT! Roll score: ", split_score)
					
					elif j == 1:
						split_score = random.randint(0,(10 - FRAME_SCORE))
						print("Roll score: ", split_score)
						frame_scores.update({i: [FRAME_SCORE, split_score]})
						FRAME_SCORE += split_score

						if FRAME_SCORE == 10:
							print("SPARE!!")
							spare_ascii()
							WAS_SPARE = True
						else:
							openframe_ascii()
							#print("Roll score: ", split_score)
			
			# #1b - It went into the gutter!
			# else:
			# 	gutter_ascii()
			# 	print("You rolled into the gutter!")
			# 	if j == 1:
			# 		frame_scores.update({i: [FRAME_SCORE, 0]})

			if i == 10:
				if WAS_STRIKE:
					FINAL_STRIKE = True
				elif WAS_SPARE:
					FINAL_SPARE = True

		print(" ")

	calculate_gamescore()
	print("CONGRATULATIONS!")
###########################################END GAMEMODE()####################################################



def main():

	user_mode_choice = input("Select [t]est mode or [g]ame mode: ")
	user_mode_choice = user_mode_choice.lower()

	if user_mode_choice == 'g':
		user_disable_ascii = input("Disable ASCII Art? [y]es or [n]o: ")
		user_disable_ascii = user_disable_ascii.lower()

		if user_disable_ascii == 'y':
			print("disabling ascii ")
			global DISABLE_ASCII
			DISABLE_ASCII = True

		gameMode()

	elif user_mode_choice == 't':
		global frame_scores
		pattern = re.compile(r'^(10|\d+,\d+)$')

		print("Enter roll scores (not frame scores) in the following format:")
		print("Strike Frame: 10")
		print("Spare Frame: 3, 7")
		print("Open Frame w/ Gutter: 5, 0")
		print("One Bonus roll: 7")
		print("Two Bonus rolls: 10, 10")
		print("No bonus rolls: 0")
		print("")
		print("")		

		frame_counter = 1
		while True:
			print("Frame ", frame_counter, ": ")
			
			try:
				score_str = input("Roll scores: ")
				if not pattern.match(score_str):
					raise ValueError
			except ValueError:
				print("Invalid input: enter 10 for strikes or comma-separated roll-scores without spaces for the frame")
				continue


			score_list = score_str.split(",")
			if len(score_list) == 1:
				frame_scores.update({frame_counter: int(score_list[0])})
			else:
				temp_list = []
				for i in range(0, len(score_list)):
					temp_list.append(int(score_list[i]))
				frame_scores.update({frame_counter: temp_list})
			frame_counter += 1
			
			if frame_counter == 12:
				calculate_gamescore()
				break
#####################################END MAIN()#######################################


def run_program():
	global frame_scores
	while True:
		main()
		user_exit_choice = input("Select to [r]estart or [e]xit: ")
		user_exit_choice = user_exit_choice.lower()

		if user_exit_choice == 'r':
			frame_scores.clear()
			continue
		else:
			break

run_program()