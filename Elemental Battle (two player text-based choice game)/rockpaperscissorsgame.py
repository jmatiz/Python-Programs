import random

class player_choices:
    def __init__(self,name, element, weapon, skill, score=0):
        self.name = name
        self.element = element
        self.weapon = weapon
        self.skill = skill
        self.score = score
    def add_score(self):
        self.score += 1
    def add_tiebreaker(self):
        self.score += 0.25
    def get_score(self):
        return self.score

def find_winner(p1,p2,part): #this returns 1 if player1 wins or 2 if player2 wins
    if p1 == p2:
        if part == "element":
            if p1 == 1:
                print("Bursts of air are blown away by gusting winds. The players are equally matched elementally.")
            elif p1 == 2:
                print("Jet streams of water crash against defensive waves. The players are equally matched elementally.")
            elif p1 == 3:
                print("Fireballs explode violently against furious walls of flames. The players are equally matched elementally.")
        elif part == "weapon":
            if p1 ==1:
                print("The ground shakes as heavy axes smash into the floor, narrowly missing their target with each telegraphed swing.")
            elif p1 == 2:
                print("Shield shoves against shield, neither wanting to give up their defenses for an effective attack.")
            elif p1 == 3:
                print("The clanging of sharpened steel rings out as two swords swiftly strike, parrying each other's every move.")
        elif part == "skill":
            if p1 ==1:
                print("Every quick move met with a quick counter, neither player can outpace the other.")
            elif p1 == 2:
                print("Every prediction is foreseen and every calculation is accounted for, neither player can outsmart the other.")
            elif p1 == 3:
                print("Every unstoppable force is met with an immovable object, neither player can outwork the other.")
        return 0 #tie
    else:
        if p1 == 1:
            if p2 == 2:
                if part == "element":
                    print(str(player1.name) + " sends large gusts of wind that slice through " +  str(player2.name) + "'s powerful jet streams.")
                    print("Forceful winds dissolve away huge defensive waves, " + str(player1.name) + " blasts " +str(player2.name) + " with pulverizing bursts of air.")
                elif part == "weapon":
                    print(str(player1.name) + " swings their powerful axe down at " + str(player2.name) + ", who raises their shield to block the blow.")
                    print("The axe fractures the shield on impact, crushing the shieldbearer under its force.")
                elif part == "skill":
                    print(str(player1.name) + " moves with blinding speed, operating before " + str(player2.name) +" has a chance to come up with a plan.")
                return 1
            elif p2 == 3:
                if part == "element":
                    print(str(player1.name) + " sends blasts of air towards " +  str(player2.name) + "'s furious wall of flames. The forceful wind only fans the flames, spreading the blaze.")
                    print(str(player2.name) + " launches explosive fireballs towards " + str(player1.name) + ", detonating them in a fiery inferno.")
                elif part == "weapon":
                    print(str(player1.name) + " begins to swing their powerful axe down at " + str(player2.name) + ", who quickly strikes with the much lighter weapon of the sword.")
                    print("Before the axe can complete its deliberate swing, "+ str(player2.name) + " lands multiple critical slashes, crippling " + str(player1.name) + ".")
                elif part == "skill":
                    print(str(player1.name) + " makes their move in a flash, but " + str(player2.name) +" just waits for the speedster to approach, easily overpowering with their strength")
                return 2
        if p1 == 2:
            if p2 == 1:
                if part == "element":
                    print(str(player1.name) + " pumps powerful jet streams of water at " + str(player2.name) + ", who slices through them with large gusts of wind.")
                    print(str(player1.name) + " pulls huge defensive waves around themself, but " + str(player2.name) + " blasts through the waves, pulverizing " + str(player1.name) + " with bursts of air")
                elif part == "weapon":
                    print(str(player1.name) + " shoves their shield forward, ready to buffer the incoming blow as " + str(player2.name) + " begins to swing their powerful axe.")
                    print("The axe fractures the shield on impact, crushing the shieldbearer under its force.")
                elif part == "skill":
                    print(str(player1.name) + " can accurately predict their opponent's next move, and prepare a calculated counter. ")
                    print("However, " + str(player2.name) + " moves with such blinding speed that they give " + str(player1.name) + " no chance to prepare.")          
                return 2
            elif p2 == 3:
                if part == "element":
                    print(str(player1.name) + " pumps powerful jet streams of water at " + str(player2.name) + "'s ferocious wall of flames. Dissolving powerful fire into useless steam.")
                    print(str(player1.name) + " calls upon huge waves to send crashing down on " + str(player2.name) + ", whose power drowns away.")
                elif part == "weapon":
                    print(str(player1.name) + " shoves their shield forward, ready to buffer all incoming blows as " + str(player2.name) + " fragments their sword thrashing it helplessly against the unyielding shield")
                    print(str(player1.name) + " uses the mighty shield to bash their now weapon-less opponent")
                elif part == "skill":
                    print(str(player1.name) + " can accurately predict their opponent's next move, and prepare a calculated counter.")
                    print(str(player2.name) + "'s powerful might is worthless against their prepared opponent who outsmarts them with traps and counters.")  
                return 1
        if p1 == 3:
            if p2 == 1:
                if part == "element":
                    print(str(player1.name) + " launches explosive fireballs, easily propelled through gusts of wind. " + str(player2.name) + "'s blasts of air only fan the flames of the fiery attacks.")
                    print("Engulfed in a violent inferno, " + str(player2.name) + " has no answer to the oppresive heat.")
                elif part == "weapon":
                    print(str(player1.name) + " quickly strikes with their agile sword as  " + str(player2.name) + " has only just begun the slow and deliberate swing of their powerful axe.")
                    print(str(player1.name) + " lands multiple critical slashes, crippling " + str(player2.name) + ".")
                elif part == "skill":
                    print(str(player1.name) + " has mighty strength and power. Even though " + str(player2.name) + " moves with blinding speed, they pose no threat.")
                    print(str(player1.name) + " simply waits for the speedster to approach, then crushes " + str(player2.name) + " with overpowering strength.")  
                return 1
            elif p2 == 2:
                if part == "element":
                    print(str(player1.name) + " launches explosive fireballs towards huge defensive waves. The fireballs dissolve uselessly against the powerful waves.")
                    print(str(player2.name) + " pumps jet streams of water that drown out even the largest flames, pummeling into " + str(player1.name) + ".")
                elif part == "weapon":
                    print(str(player1.name) + " quickly strikes with their agile sword as  " + str(player2.name) + " absorbs every blow with their unyielding shield.")
                    print(str(player1.name) + " begins to thrash their sword helplessly, fragmenting it against the shield's surface. " + str(player2.name) + " uses the mighty shield to bash their unarmed opponent.")
                elif part == "skill":
                    print(str(player1.name) + " has incredible strength and power. However, " + str(player2.name) + " prepares for this using their sharp intellect.")
                    print(str(player2.name) + " uses calculated predictions to set traps for " + str(player1.name) + ", effectively countering their overpowering strength.")  
                return 2
            
def winner_score(winner):
    if winner == 1:
        player1.add_score()
    elif winner == 2:
        player2.add_score()
    elif winner == 0:
        random_winner = random.randint(1,2)
        if random_winner == 1:
            player1.add_tiebreaker()
        elif random_winner == 2:
            player2.add_tiebreaker()
 


while True: #game on, this is the master game loop that is broken or repeated after a completed game

    p1_name = input("Player 1, what is your name?\n")


    while True:
        p1_element = input("What is your element? Please select a number\n 1.AIR\n 2.WATER\n 3.FIRE\n")
        if p1_element == '1' or p1_element == '2' or p1_element == '3':
            p1_element = int(p1_element)
            break
    
        else:
            print("Invalid input. Please make sure to type in the number seen in front of the option as your input.")

    while True:
        p1_weapon = input("What is your weapon of choice? Please select a number\n 1.AXE\n 2.SHIELD\n 3.SWORD\n")
        if p1_weapon == '1' or p1_weapon == '2' or p1_weapon == '3':
            p1_weapon = int(p1_weapon)
            break
    
        else:
            print("Invalid input. Please make sure to type in the number seen in front of the option as your input.")

    while True:
        p1_skill = input("What is your skill? Please select a number\n 1.SPEED\n 2.INTELLECT\n 3.STRENGTH\n")
        if p1_skill == '1' or p1_skill == '2' or p1_skill == '3':
            p1_skill= int(p1_skill)
            break
    
        else:
            print("Invalid input. Please make sure to type in the number seen in front of the option as your input.")

    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    p2_name = input("Player 2, what is your name?\n")

    while True:
        p2_element = input("What is your element? Please select a number\n 1.AIR\n 2.WATER\n 3.FIRE\n")
        if p2_element == '1' or p2_element == '2' or p2_element == '3':
            p2_element = int(p2_element)
            break
    
        else:
            print("Invalid input. Please make sure to type in the number seen in front of the option as your input.")

    while True:
        p2_weapon = input("What is your weapon of choice? Please select a number\n 1.AXE\n 2.SHIELD\n 3.SWORD\n")
        if p2_weapon == '1' or p2_weapon == '2' or p2_weapon == '3':
            p2_weapon = int(p2_weapon)
            break
    
        else:
            print("Invalid input. Please make sure to type in the number seen in front of the option as your input.")

    while True:
        p2_skill = input("What is your skill? Please select a number\n 1.SPEED\n 2.INTELLECT\n 3.STRENGTH\n")
        if p2_skill == '1' or p2_skill == '2' or p2_skill == '3':
            p2_skill= int(p2_skill)
            break
    
        else:
            print("Invalid input. Please make sure to type in the number seen in front of the option as your input.")


    player1 = player_choices(p1_name,p1_element,p1_weapon,p1_skill)
    player2 = player_choices(p2_name,p2_element,p2_weapon,p2_skill)




    skill_winner = find_winner(player1.skill,player2.skill,"skill")

    winner_score(skill_winner)


    element_winner = find_winner(player1.element,player2.element,"element")

    winner_score(element_winner)
    
    weapon_winner = find_winner(player1.weapon,player2.weapon,"weapon")

    winner_score(weapon_winner)


#calculate score, if score difference is less than 1 then the winner was determined by a tiebreaker (the black cat).

    if player1.score > player2.score:
        if (player1.score - player2.score) < 1:
            print("A black cat wanders across the battlefield, distracting " + str(player2.name) + ", allowing their opponent to land a fatal strike.")
        print(str(player1.name) + " wins!")
    elif player2.score > player1.score:
        if (player2.score - player1.score) < 1:
            print("A black cat wanders across the battlefield, distracting " + str(player1.name) + ", allowing their opponent to land a fatal strike.")
        print(str(player2.name) + " wins")
    else:
        print("A stand off occurs...")

#game loop: play again or hit x to break loop.

    if input("Enter x to quit, anything else to keep going!\n") == 'x':
        print("Thanks for playing! Goodbye!")
        break

    else:
        print("Time to play again!\n\n\n")
        

