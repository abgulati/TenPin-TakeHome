
# if i == 10:
# 	print("testing frame 10 as a strike")
# 	frame_scores.update({10:10})
# 	FINAL_STRIKE = True
# 	continue

# if i == 10:
# 	print("testing frame 10 as a spare")
# 	frame_scores.update({10:[7,3]})
# 	FINAL_SPARE = True
# 	continue


###################################################################
################--UNIT TEST 1: Perfect Game!--#####################
###################################################################

def unit_test_1():
	print("Frame scores: ", frame_scores)
	print(" ")

	print("Final scores are: ")
	calculate_gamescore()
	print("CONGRATULATIONS!")

#frame_scores = {1:10,2:10,3:10,4:10,5:10,6:10,7:10,8:10,9:10,10:10,11:10,12:10}
#unit_test_1()
#UNCOMMENT ABOVE TWO LINES FOR UNIT TEST 1

###################################################################
######################--END UNIT TEST 1--##########################
###################################################################


CMD [ "python", "./pseudo.py" ]