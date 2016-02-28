# -- coding: utf-8 --
#!/usr/bin/python
#------------------------------------------------------------
# how short can we make paper scissors rock lizzard spock?
# version 0.8
#------------------------------------------------------------
import random
ans = raw_input('scissors, paper, rock, lizard or spock?').title()
print random.choice([s for s in ['Scissors cuts Paper','Paper covers Rock','Rock crushes Lizard','Lizard poisons Spock','Spock smashes Scissors','Scissors decapitates Lizard','Lizard eats Paper','Paper disproves Spock','Spock vaporizes Rock','Rock crushes Scissors'] if ans in s]+['Draw!']if ans in ['Scissors','Paper','Rock','Lizard','Spock'] else ['Incorrect input.'])