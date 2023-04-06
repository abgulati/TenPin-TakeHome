def calculate_gamescore():

	frame_scores = {}  #dict_containing roll scores as FRAME_NO:<ROLL_1><ROLL_2>
	GAME_SCORE = 0

	for i in range(1, len(frame_scores)):
		FRAME_SCORE = 0

		#Intuition: The score will only be '10' for strikes, else it'll be a list of roll scores

		if strike:

			#calculate bonus = next two rolls:
			
			if (next frame also strike):

				if (second roll also strike):
					#calculate score

				else:
					bonus = [strike_frame_i+1] + [roll_1_of_frame_i+2]

			else (next frame not strike):
				bonus = [roll_1_of_frame_i+1] + [roll_2_of_frame_i+1]

			calculate FRAME_SCORE

		elif not strike:

			score = [roll_1_of_frame_i] + [roll_2_of_frame_i]

			if score == 10:
				Spare!
				bonus = [next_roll_score]

			calculate FRAME_SCORE

		update GAME_SCORE

	return GAME_SCORE







def gameMode():

	FINAl_STRIKE = False
	FINAL_SPARE = False

	for i in range(1,12):		#Frame 11 (bonus_frame) can hold two bonus rolls

		if bonus_frame and not FINAL_STRIKE and not FINAL_SPARE:
			frame_scores.update({11:[0]})
			continue
		elif bonus_frame and FINAL_STRIKE:
			score = []
			for j in range(2):
				bonus_roll()
				update score
			frame_scores.update({11:score})
			continue
		elif bonus_frame and FINAL_SPARE:
			score = bonus_roll()
			frame_scores.update({11:score})
			continue


		current_framescore = 0
		WAS_STRIKE = False
		WAS_SPARE = False

		for j in range(2):		#two rolls a frame, unless strike

			if roll_2 and WAS_STRIKE:
				continue		#progress to next frame

			user_input = enter_to_roll

			if pocket_hit:		#consider strike
				frame_scores.update({10})
				WAS_STRIKE = True

			elif head-on:		#check if strike or not

				if strike:
					frame_scores.update({10})
					WAS_STRIKE = True

				elif not_strike:

					if roll_1:
						current_framescore += calculate_score_1_to_9

					if roll_2:
						calculate_score = random(total_pins - pins_standing_after_roll_1)
						update current_framescore

						if Spare:
							WAS_SPARE = True

			if final_frame:
				if WAS_STRIKE:
					FINAl_STRIKE = True
				elif WAS_SPARE:
					FINAL_SPARE = True

	calculate_gamescore()
	print("congrats!")





def favorable():
	outcome = random.choice([True, False])
	return outcome


def ascii_art_functions():

	print()
	print()
	print()



frame_scores = {}

def main():

	user_input = gameMode or testMode

	if gameMode:
		user_input = disable_ASCII_Art?
		if disable:
			DISABLE_ASCII = True

		gameMode()

	elif testMode:
		define_input_regex
		print_guidance

		frame_counter = 1
		while True:
			try:
				user_input
				if not regex_match:
					raise ValueError
			except ValueError:
				print("Please re-enter")
				continue

		frame_scores.update({})
		if frame_counter == 12:
			calculate_gamescore()
			break
