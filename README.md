Objective:

Produce the score for one single-lane game of American ten-pin bowling

↳ Not checking if rolls are valid or invalid

↳ Not checking for the correct number of rolls and frames

↳ Not scoring intermediate frames (?)




Game Rules:

Ten-pin bowling:

↳ Game consists of 10 “frames”

↳ Each frame provides players two opportunities to knock down all ten pins

↳ The score for a frame is the total number of pins knocked down, and any bonuses

↳ A “spare” is when all 10 pins are knocked down in those two attempts, thus completing the frame
	↳ Bonus: the first roll of the next frame; that score will therefore count twice!
	
↳ A “strike” is when all 10 pins are knocked down in the very first roll of a frame, essentially completing the frame
	↳ Bonus: the score of the next two rolls!
	
↳ This way, the max score for a frame is 30, including bonuses
	↳ Thus for a game of 10 frames, it’s 300
	
↳ Additionally, if a player scores a strike or a spare in the final (10th) frame, they do get to roll the extra balls but no more    than three rolls are allowed in the final frame, this way a game can have a maximum of 12 strikes


Approach:

1.	The core-nature:
	A roll can be valid or invalid, but since that’s out of scope, let’s assume all rolls are valid
	A valid roll may make contact with the pins, or it may go to the gutter
	If it does strike the pins, some or all may fall over:
↳ Precisely calculating which pins fall will require a physics engine, this brings us to an important fork in our design approach!
	The game can be designed to be luck-based or skill-based:
↳ A skill-based game will require physics calculation determining the roll-path of the ball and the pin-impact
↳ A luck-based game will simply proceed by randomly picking outcomes, we start with this approach!

2.	A luck-based approach:
	Central to this approach would be a random Boolean: TRUE(1) for a favorable outcome, FALSE(0) otherwise
	A roll strikes the pins (Boolean: TRUE (1)) or misses and goes to the gutter (Boolean: FALSE(0))
	Since this is luck-based and not skill/physics-based, let’s assume that if the pins are struck by our ball, they collide either head-on or in the pockets:
↳ Statistically, the pockets are more favorable for a strike, so let’s assume that hitting the pocket gets us a strike
↳ Conversely, hitting head-on is more unpredictable, so let’s assume a head-on hit can lead to either a strike where all the pins fall or we end up with a split where some are still left standing
↳ If it’s a split, the remaining roll will either knock down the remaining pins or we’re left with an open frame!



Pseudo-Code


Calculate GameScore():

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



GameMode():

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



Main() and misc. functions:


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



Execution Instructions


Simply execute “python ten_pin.py” on CLI: python .\ten_pin.py


Docker Deployment:


Makefile:

FROM python:3.9-slim-buster
RUN useradd --create-home --shell /bin/bash app_user
WORKDIR /home/app_user
USER app_user
COPY . .
CMD ["bash"]
CMD [ "python", "./ten_pin.py" ]


Build & Run the Container:
docker build -t tenpin_container .
docker run -it --name tenpin tenpin_container


