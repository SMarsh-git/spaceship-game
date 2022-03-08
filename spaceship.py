import random
import sys
import time

def slowprintart(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.003)

def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.095)

def top_down_doors_closed():
    print(f"""\n\n\n     ##############################                                                                                                          ###
     ##############################                                                     Science bay                                          ###
     ################################################################################____________________#######################################
     ################################################################################                    #######################################
     ###                                                                                                                               ###
      |                                                                                                                                 |
      |                                                                                                                                 |
      |         Security Chief {name2}                                                                                                  |
      |                   |                                                                                                             |
      |                   |                                                                                                             |
      |                   |                                                                                                             |
      |                   |                                                                                                             |
     ###                  |                                                                                                            ###
     ####                 |    #####################################################                      ######################################
     ####                 |    #####################################################                      ######################################
     ####                 |    ####                                              ###                      ######################################
     ####                 |    ####                                              ###                      ######################################
     ####                 V    |###                                              ###                      ######################################
     ####                 X    |###                                              ###                      ######################################
     ####                      |###                                               |                        |####################################
     ####                      ####                                               |                        |####################################
     ####                      ####                                               |                        |####################################
     ####                      ####                                               |                        |####################################
     ####                      ####                                               |                        |####################################
     ####                      ####               Maintenance bay                 |                        |####################################
     ####                      ####                                               |                        |####################################
     ####                      ####                                              ###                      ######################################
     ####                      ####                                              ###                      ######################################
     ####                      ####                                              ###                      ######################################
     ####                      ####                                              ###                      ######################################
     ####                      ####                                              ###                      ######################################
     #####____________________#####                                              ####____________________#######################################
     #####                    #####                                              ####                    #######################################
     ####                      ####                                              ###                      ######################################
     ####                      ####                                              ###                      ######################################
     ####                      #####################################################                      ######################################
     ####                      #####################################################                      ######################################\n\n\n""")

def top_down_sci():
    slowprintart("""\n\n\n \033[1;31;37m    ############################################################################################################################################
     ###########################################################################################################################################
     ##############################                 \033[1;31;34m  .       .  . ,\033[1;31;37m           __________________      __________________                    ###
     |                           |              \033[1;31;34m  .  .     ≋   , .\033[1;31;37m            |                  |    |     ♨     ࿄      |                   ###
     |          Air Lock         |            \033[1;31;34m       .   ≋≋≋≋  ⚗ \033[1;31;37m             |   ⚗   ♨  ࿄   ⚗   |    |       ⚗      ⚗   |                   ###
     |                           |            \033[1;31;34m    .,    ≋≋≋≋≋   , \033[1;31;37m            |__________________|    |__________________|                   ###
     ##############################         \033[1;31;34m       .   ≋≋≋≋  ,  \033[1;31;37m                  П        П              П        П                         ###
     ##############################            \033[1;31;34m         .  ,    \033[1;31;37m                                                                             ###
     ##############################    _______                                                                                               ###
     ##############################   |⊟ ⌨    |                                                                                              ###
     ##############################    ‾‾‾‾‾‾‾                                                                                               ###
     ##############################     П                                                                                                    ###
     ##############################    Computer                                         Science bay                                          ###
     ################################################################################____________________#######################################\n\n\n""")

def top_down1():
    slowprintart(f"""\n\n\n     ###########################################################################################################################################
     ###########################################################################################################################################
     ###                                                                                                                                  ###

                                         Scene of struggle                                                                                 To comms ----->              


                                        X <---Security Chief {name2}

     ###                                                                                                                                  ###
     ####______________________#################################______________________##########################################################
     ####                      #################################                      ##########################################################\n\n\n""")

def top_down2():
    slowprintart(f"""\n\n\n     ##############################                                                                                                          ###
     ##############################                                                     Science Bay                                          ###
     ################################################################################____________________#######################################
     ################################################################################                    #######################################
     ###                                                                                                                               ###
     <----- To Investigate                                                                                                              |
                                                                                                                                        |
        X <---Security Chief {name2}                                                                                                    |
                                                                                                                                        |
                                                                                                                                        |
                 Fix comms                                                                                                              |
                      \                                                                                                                 |
     ###               \                                                                                                               ###
     ####               \      #####################################################                      ######################################
     ####                \     #####################################################                      ######################################
     ####                 \    ####                                              ###                      ######################################
     ####                  \   ####                                              ###                      ######################################
     ####                   \  |###                                              ###                      ######################################
     ####                    ->|###                                              ###                      ######################################
     ####                      |###                                               |                        |####################################
     ####                      ####                                               |                        |####################################
     ####                      ####                                               |                        |####################################
     ####                      ####                                               |                        |####################################
     ####                      ####                                               |                        |####################################
     ####                      ####               Maintenance bay                 |                        |####################################
     ####                      ####                                               |                        |####################################
     ####                      ####                                              ###                      ######################################
     ####                      ####                                              ###                      ######################################
     ####                      ####                                              ###                      ######################################
     ####                      ####                                              ###                      ######################################
     ####                      ####                                              ###                      ######################################
     #####                    #####                                              ####                    #######################################
     #####                    #####                                              ####                    #######################################
     ####                      ####                                              ###                      ######################################
     ####                      ####                                              ###                      ######################################
     ####                      #####################################################                      ######################################
     ####                      #####################################################                      ######################################\n\n\n""")

def corridor():
    time.sleep(1)
    print("""\n\n\n         ###%#%/               ,%                      %%%%%%%%%%%%%&&*//////%%%%%%&&&/////&%%%%%%%%%%%%%   #.....#     %%(#//,           / (#                                  
         ###%#%/                  ,%        , (       /                                                  \  #.....#     %%(#//,           / (#                                    
        /#%%%%%/                    .%      / #      /   /%%%%%%%%&&&//////&&%%%%%&#/////%&%%&%%%%%%%%\   \ #.....#     %%##//*.          ./####((((((((%###%%((((#(#########(((((
        .#%%%%%                        #    * #     /   /%%%%%%%%%%%&##%#%%%%&%%%&%&&&&&&&%%%%%%%%%%   \   \#.. %%#     %%##/,*           .(##     ________                       
         %%%%%%                          #(  /%    #    #                                    #%%##      #   #%%#  #     #%.(#*.           ,//#    |\       |                      
       .%%%%%%%/                            % *    #   .#   /(%%%%%%%%###%%%%%%%%###%%(*%#  \ *         #   #     #     #%*(((,          * (##.   | access |'                     
        #%%%%%%                              ./    #   .#  / .........................    \  \      ,#%%#   #.    #     #%##(// ,         .//##   | panel  | ' ,                  
       .#%%%%%/                               #    #    # #  %%%%%%%%*&&%%%%&&*/&%%%%%     \  # ,#%%    #   #.    #     #%%#/,/.          ./(##   |/\/\/\/\| ,                    
       .#%%%%%,                               */   #   *# #  /######################\ \   , # #%.       #   #.    #     #%%##/*/           /(#(//(((((//((#((((((((((####(##(#####
       .#%%%%%/                               **   #   ## # /|######################|\ \.'  # #.        #   #%%#..#     #%&(/*.           *(/##                                   
        %%%%%%%%%##* .                        **   #   ## #| |####      |      #####| |'    # #*   ,/(%%#   #.....#     #%%(#//           ../##                                   
       #%%%%%%#%%%%%%%%%%%%%/                 #    #   ##  # |####      |      #####| #     # #%%(%     #   #.....#     (%%(/(/           ,*(##                                   
      ,#%%%%%%.        /%#%#%%%%%%%%%*/.     .#    #   ##--# |####      |      #####| #---- # #         #   #.....#     (%%##***,          /(##                                   
      ,%#%%%%#                      /#%%%%%%%#*    #   ##  # |####      |      #  ##| #     # #         #   #. ...#     /%%##//..          ./##                                   
      .%%%%%%*                                #    #  ,##  # |####      |      #####| #     # #,,,#(#%%%#   #%%%%%%     *%%#(/**.           ((# ((/(/////////////((/((((((((((((((
       #%%%%%.                               .#.   #   ##--# |####      |      #####| #---- # #         #   #.....#     *%%#((/*,          /(##                                   
      ,%%%%%%.                                /    #   (#  # |####      |      #####| #     # #         #   #.....#     *%%#/(, ,         . (##                                   
      ,%%%%%%                                 *    #   ##  # |####______|______#####| #    /  /......   #   #.....#     *%%#(#*           ,*,##//  ../.      ..         ..,   .   
      (##%%%#                                 *    #  ,#\  .\/                      \/.   / ./@@@@@&&**/    /.....#     *#%(**/             /,## . /,./*. /.*///** ,../.,//..,   /
      #####%(                                 /     \    \'                             ',|   #%%&&@@@@/    &@@&%%/      *#%##/             /(###(##(###(##########################
     .######.                             .. ./      \    |                                  *((((###|    &@@@@@/       *##(.             (#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
     .######                         .....&&@@%#,     \ ,/                                          (/(//(#((###/        %###(#///.       (#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
     ######(                      ...(&@@@@@@@@@%(    ,/                                                    /(((.(..*.,.*/./ ,.*,* ,  , ,.(#####%#######################(/....    
     #######                   ..%&@@@@@@@@@@@@%##/                                                                                                                               
     (######              . (%&@@@@@@@@@@@@@%###                                                               ###                                                                   
     ###(###           (#&&@@@@@@@@@@@@@@%###(                                                                # #                                                                  
     #(#/##        #%%&@@@@@@@@@@@@@@@&%##(                                                                  ###                                                                    
     _____________________________________________________________________________________________________________________________________________________________________________\n\n\n""")
    time.sleep(1)

def door_art():
        slowprintart("""\n\n\n
                                                                ######################################################################################################
                                          ████████████████████████████████████████████████############################################################################
                                      ████████████████████████████████████████████████████████########################################################################
                                    ████                      ██############################████######################################################################
                                    ██                          ████##########################██######################################################################
                                    ██                            ██##########################██######################################################################
                                    ██                            ██##########################██######################################################################
                                    ██                          ██############################██######################################################################
                                    ██                          ██############################██######################################################################
                                    ██                          ██############################██######################################################################
                                    ██                          ████##########################██#############≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣ #####################################
                                    ██                            ██##########################██#############≣     ≣     ≣     ≣ #####################################
                                    ██                            ██##########################██#############≣  1  ≣  2  ≣  3  ≣ #####################################
                                    ██                            ██##########################██#############≣     ≣     ≣     ≣ #####################################
                                    ██                          ▓▓██##########################██#############≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣ #####################################
                                    ██                          ████]#########################██#############≣     ≣     ≣     ≣ #####################################
                                    ██                          ██############################██#############≣  4  ≣  5  ≣  6  ≣ #####################################
                                    ██                          ██############################██#############≣     ≣     ≣     ≣ #####################################
                                    ██                          ██############################██#############≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣ #####################################
                                    ██                          ████##########################██#############≣     ≣     ≣     ≣ #####################################
                                    ██                            ██##########################██#############≣  7  ≣  8  ≣  9  ≣ #####################################
                                    ██                            ██##########################██#############≣     ≣     ≣     ≣ #####################################
                                    ██                            ██##########################██#############≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣ #####################################
                                    ██                            ██##########################██######################################################################
                                    ████████████████████████████████████████████████████████████######################################################################
\n\n\n""")

def riddle_door():
    slowprintart("""\n
                                                                #######################################################################################################
                                          ████████████████████████████████████████████████#############################################################################
                                      ████████████████████████████████████████████████████████#########################################################################
                                    ████                      ██############################████#######################################################################
                                    ██                          ████##########################██#######################################################################
                                    ██                            ██##########################██#######################################################################
                                    ██                            ██##########################██#######################################################################
                                    ██                          ██############################██#######################################################################
                                    ██                          ██############################██#######################################################################
                                    ██                          ██############################██#######################################################################
                                    ██                          ████##########################██#############≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣ ################
                                    ██                            ██##########################██#############≣ A ≣ B ≣ C ≣ D ≣ E ≣ F ≣ G ≣ H ≣ I ≣ J ≣ ################
                                    ██                            ██##########################██#############≣ K ≣ L ≣ M ≣ N ≣ O ≣ P ≣ Q ≣ R ≣ S ≣ T ≣ ################
                                    ██                            ██##########################██#############≣ U ≣ V ≣ W ≣ X ≣ Y ≣ Z ≣    ENTER      ≣ ################
                                    ██                          ▓▓██##########################██#############≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣≣ ################
                                    ██                          ████]#########################██#######################################################################
                                    ██                          ██############################██#######################################################################
                                    ██                          ██############################██#######################################################################
                                    ██                          ██############################██#######################################################################
                                    ██                          ████##########################██#######################################################################
                                    ██                            ██##########################██#######################################################################
                                    ██                            ██##########################██#######################################################################
                                    ██                            ██##########################██#######################################################################
                                    ██                            ██##########################██#######################################################################
                                    ████████████████████████████████████████████████████████████#######################################################################
\n""")

def loop():  
    
    ans=None 
    while ans not in ("y", "n"): 
        ans=input("\nWould you like to play again? y/n\n\n").lower()
        if ans=="y": 
            main()    
        elif ans=="n": 
            slowprint("\nGood bye!\n\nThank you for playing!")
            exit()
        else: 
    	    print("Please type [Y] or [N]...")

def start():

    slowprint(f"""\nNot long after departing Alpha5 a crew member seems to have disappeared, and reports are coming in that 
a new science officer is also missing. Since you're by the science bay you decide to check things out.""")
    slowprint("""\nDuring your inspections you have noticed signs of a struggle. You try to communicate to the rest of the 
crew but your personal communicator is not working.""")
    ans=None 
    while ans not in ("a", "b"): 
        ans = input("\nWould you like to: \n\n[A] Investigate  \n\n[B] Contact the security team?\n\n").lower()
        
        if ans=="a": 
        
            ans=None 
            while ans not in ("a", "b"): 
                slowprint("\nYou can't really notice anything right now...")

                ans=input("\nWould you like to: \n\n[A] Stay and investigate further? \n\n[B] Contact the security team?\n\n").lower()
               
                if ans=="a": 
                    slowprint("\nYou stuck around this area for too long!")
                    time.sleep(1)
                    attack()

                elif ans=="b":

                    top_down1()

                    time.sleep(1)
                    
                    slowprint("""\nYou walk down the long dimly lit corridor to the comms panel. You notice 
the panel has been tampered with.\n\nOut of the corner of your eye you 
notice a crew ID card catching the light.""")

                    ans=None 
                    while ans not in ("a", "b"): 
                        ans=input("Do you: \n\n[A] Fix comms?\n\n[B] Go to inspect the ID card?\n\n").lower()
                        if ans=="a": 
                            door_code()
                        elif ans=="b": 
                            science_path()
                        
        elif ans=="b": 

            top_down1()

            time.sleep(1)
        
            slowprint("""\nYou walk down the long dimly lit corridor to the comms panel. You notice 
the panel has been tampered with. Out of the corner of your eye you 
notice a crew ID card catching the light.\n""")

            corridor()
            time.sleep(1)

            ans=None 
            while ans not in ("a", "b"): 
                ans=input("Do you: \n\n[A] Head to the maintenance bay?\n\n[B] Go to inspect the ID card?\n\n").lower()
                if ans=="a": 
                    door_code()

                elif ans=="b":
                    science_path() 

def door_code():

    top_down2()
    time.sleep(1)
    slowprint("\nYou make your way around the corner to the maintenance bay")
    time.sleep(1)
    door_art()
     
    slowprint("""The doors to the ship have been acting strangely recently. 
To your suprise the door is hard locked... Not even the master code of the 
Chief Security Officer can unlock the door. 

You use your security officer skills to open the failsafe to open the door. 
The panel says in a robotic voice "The value of x is the backup access code, 
please solve for x.\n (6000+262)/2=x\n""")

    pin="6262"
    user_pin="3131"
    attempts=3
    while attempts != 0:
        pin=(input("Please enter the access code.\n\n"))
        if pin != user_pin:
            attempts-=1
            slowprint(f"Incorrect access code, you have {attempts} attempts left.")
            if attempts==0:
                slowprint ("""Sorry you have run out of attempts, you are unable to 
access the tool box to fix the communications panel.\n""")
                attack()
        elif pin==user_pin:
            attempts=0
            slowprint("That is the correct accesscode.\n")
            slowprint("""The door opens to the maintence bay. You quickly grab the 
toolbox so that you can fix the panel at communications.""")
            if attempts==0:
                slowprint ("""You approach the communications area with intent to call for 
backup. With the tools you have gained from the maintenance 
bay you begin fixing the broken communications panel.\n""")
                slowprint ("""To finish fixing the panel you must cut one of two wires, 
there is a red and a purple wire. The red wire leads 
towards the door. The purple wire leads towards a box 
labelled 'ALARMS'.""")
                comms_fix()

def comms_fix():
    wire=None
    wire=input("\nWhat colour wire would you like to cut? Red or purple?\n\n").lower()
    if wire == "red":
        slowprint ("""\nThe access panel fizzles and shoots sparks before coming back to life. 
You use your security code to  unlock the panel and then to send out a 
message to your security team.""")
        
        slowprint (f"""You speak into the panel's microphone "This is Security Chief {name1} {name2}. 
Send a security team to deck 4 sector 7 immediately.""")
        slowprint ("""\nYour backup are on their way. Unfortunately you realise that the deck has
been sealed off and your backup are trapped on the other side of the door.\n""")
        time.sleep(1)
        riddle()
    elif wire == "purple":
        slowprint ("""\nSparks fly from the panel as you fall back on to the ground. Deafening sirens 
begin to sound alerting to your mishap. You notice a figure behind you as you 
are attacked\n""")
        time.sleep(1)
        attack()
    
    else:
        slowprint ("\nThat is not a valid wire, please enter the colours purple or red.\n")
        comms_fix()

def riddle():
    slowprint ("The deck doors require an answer to a word game to unlock.")
    riddle_door()
    time.sleep(1)
    slowprint ("""I'm blue and green and a little brown. I'm a small planet with life 
all around. They call me the third rock from the sun. I don't have 
many moons - just one.\n""")
    planet_ans="none"
    planet_ans=input("\nWhat planet am I? YOU WILL ONLY HAVE ONE ATTEMPT! \n\n").lower()
    if planet_ans=="earth":
        slowprint("""\nThe deck doors swing open allowing your comrades through 
the doors. You and your comrades split up to inspect the 
area. You hear a scuffle as your comrades are holding 
down a suspicious charcter.\n""")
        slowprint("""\nAfter searching him you find a fake ID card and an 
advanced hacking tool. You have successfully found the 
perpetrator!\n""")
        slowprint("You win!")
        end()
    if planet_ans!="earth":
        slowprint("""\nThe deck doors permanently seal shut. All this commotion
has attracted the perpetrator to your location and they approach you 
to attack.""")
        attack()

def science_path():
    slowprint("""\nYou check out the ID card at the scene. The card belongs to 
one of two missing crew members. This one belongs to the 
missing science officer.""")

    slowprint("""\nYou're confused as to what is happening... You look for a 
few more clues but you're unsure about any of it.""")

    slowprint("""\nYou get a feeling to head to the science bay but you're 
weary about the whole situation.""")

    ans=None 
    while ans not in ("a", "b"): 
        
        ans=input("\n\nDo you: \n\n[A] Head to the science bay? \n\n[B] Investigate further? \n\n").lower() 
        
        if ans=="a": 
            
            slowprint("\nYou arrive at the science bay.\n")
            science_door()

        elif ans=="b":
            slowprint("""\nYou're looking around and you can see a few things out of place. Dents in a few panels,
some scraping on the walls leading to the science bay... You can't make sense of any of it.""")

        ans=None 
        while ans not in ("a", "b"):

            ans=input("Do you: \n\n[A] Go to the science bay? \n\n[B] Stick around to investigate further?\n\n").lower()
                
            if ans=="a": 
                slowprint("\nYou arrive at the science bay door.")
                slowprint("""\n'beep beep' The doors have been acting strange all over the ship for the past 18 hours...
It is not unusual for the science doors to be locked. But not even the master code of the Chief security officer 
can unlock the door.

You use your security officer skills and remember a hack for the security panel.""")
                science_door()

            elif ans=="b": 
                attack()    

def science_door():
    slowprint("""The doors to the ship have been acting strangely recently. 
To your suprise the door is hard locked... Not even the master code 
of the Chief Security Officer can't unlock the door. 

You use your security officer skills to open the failsafe 
to open the door. 

The panel says in a robotic voice "The value of x is the 
backup access code, please solve for x.\n (6000+262)/2=x\n""")
    pin="6262"
    user_pin="3131"
    attempts=3
    while attempts != 0:
        pin=input("\nPlease enter the access code.\n\n")
        if pin != user_pin:
            attempts-=1
            slowprint(f"\nIncorrect access code, you have {attempts} attempts left.")
            if attempts==0:
                slowprint ("\nSorry you have run out of attempts, you are unable to access the tool box to fix the panel at communications.")
                time.sleep(1)
                attack()
        elif pin==user_pin:
            attempts=0
            
            science_test()

def science_test():

    slowprint("""\nOn your way in to the science bay you notice a smashed beaker 
surrounded by a clear liquid. There is clear evidence of a struggle 
heading towards the science bay airlock.""")

    top_down_sci()
    
    slowprint("""As you get closer to the airlock you spot a piece of fabric trapped 
in the seal of the door. The door and surrounding areas are covered
in scuff marks. 

You think 'What happened here?'""")

    slowprint("""\nYou open the inner door of the airlock to free the fabric. You put 
it straight into a sample bag from the science bay. This could be 
serious evidence...""")

    slowprint("""\nYou turn your attention back to the smashed beaker. The liquid 
surrounding it seems like water... But this is the science bay.
it could be anything and it could help you work out what is 
happening...""") 

    slowprint("""\nYou use your brief training in forensics to analyse the liquid.
It turns out to be water... But as chief of security, you need 
to log it anyway...""")

    slowprint("""\n\nAs your personal device isn't working you need log this down in 
the science bay computer...""")

    science_question()

def science_question():
    answer="h2o"     
    attempts=2 
    slowprint("The computer asks \n\n'What is the molecular formular for The compound you analysed?'...")      
    ans=input("\nyou think to yourself 'Hmmm... What is the molecule formula for water?...'\n\n").lower()   
    while ans!=answer:   
        attempts -=1      
        if attempts >0:   
            slowprint("\nNot recognised...")
            slowprint("\nYou think to yourself 'Damn... Is it H something o?")
            ans=input("\nWhat is the molecular formula for The compound you analysed?\n\n").lower()
        elif attempts <=0: 
            slowprint("""\nFeeling defeated by a question you got right in high school,
you step towards the airlock to try and gain clarity. 
                       
You pick up the piece of fabric you found to look at it 
a bit closer. You hold it up in the cold sterile glow 
of the airlock working lights. 

You notice it is the same colour as a science officers
uniform... You ask yourself 

'did someone...? No, it can't be...'""")

            time.sleep(1)

            science_attack()
    else:
        slowprint("\nsuccess")
        slowprint("""\nHappy with yourself that you still remember high school chemistry,
you step towards the airlock to soak everything in. 
                       
You pick up the piece of fabric you found to look at it 
a bit closer. You hold it up in the cold sterile glow 
of the airlock working lights. 

You notice it is the same colour as a science officers
uniform... You ask yourself 

'did someone...? No, it can't be...'""") 
    

    science_win()

def science_win():
    time.sleep(2)
    print("\n\nATTACKED!")

    sce=random.randint(0,101)

    if sce<51:

        ans=None 
        while ans not in ("a", "b"): 
            
                print("""\nYou suddenly get tackled to the ground! You and the attacker slide fully 
into the airlock. There is a struggle to gain control as the attacker 
has the advantage of surprise.\n""")
                
                ans=input("\nDo you: \n\n[A] Try to flip the attacker off you and close him in the airlock till backup arrives? \n\n[B] Try to reach for your weapon?\n\n").lower()

                if ans=="a":
                    print("\nYou flip the attacker over and he hits his head.\n")
                    print("Dayzed and disorientated, the attacker staggers toward you.\n")
                    print("You quickly back out of the airlock and decide to lock him in till help arrives.\n")
                    slowprint("\nYou win!\n\n")
                    time.sleep(1)
                    comms_fix2() 
                
                elif ans=="b":
                    print("\nThe attacket is fighting you. You try to get up but you can't get your footing.")
                    print("\nFrom the ground you fire your weapon and hit the attacker in the arm.")
                    print("\nYou quickly scramble out of the airlock and decide to lock him in till help arrives.")
                    slowprint("""\n'beep beep beep loss of pressure' You look through the window and notice your weapon
has damaged the airlock controls. You try to open the airlock quickly to save and 
arrest the attacker, but the damaged computer control unit wont let you override. 
before the pressure is even to low to breathe, the outer airlock door blasts open 
sucking the attacker out into space...""")
                    slowprint("\n\nYou win... But now you have to try and retrieve the attacker...")
                    time.sleep(1)
                    comms_fix2()
    elif sce >51:
        print("""\nYou suddenly get tackled to the ground! You and the attacker slide fully into the airlock. 
There is a struggle to gain control as the attacker has the advantage of surprise.""")

        print("\nYou flip the attacker over and he hits his head.\n")
        print("Dayzed and disorientated, the attacker staggers toward you.\n")
        print("You quickly back out of the airlock and decide to lock him in till help arrives.\n")
        print("\nYou win!\n\n")
        time.sleep(1)
        comms_fix2()

def comms_fix2():
    wire=None

    slowprint("""\nYou've came out on top! Now it is time to fix the comms and alert the 
security team to scene.""")

    time.sleep(1)

    top_down_doors_closed()

    time.sleep(1)

    slowprint("""\nThe doors on this deck have all been sealed... 
Must have been sabotaged by the perpetrator!""")

    slowprint("""\nAfter a visit to the maintenance bay, you arrive at the 
comms panel with tools in hand, ready to take on the challenge. 
You need to get a security team there soon!

You notice there is a complete diversion of power to comms
and door systems... Luckily, one wire should sort it.""")

    slowprint("""\nYou notice there are two wires that have been tampered with and 
redirected... Red and purple...""")

    slowprint("\nYou need to cut and redirect one of them in order to contact the crew.")
     
    while wire not in ("red", "purple"): 
         wire=input("\nWhat colour wire would you like to cut? Red or purple?\n\n").lower()
    if wire=="red":
        slowprint ("""\nThe access panel fizzles and shoots sparks before coming back to life. You use 
your security code to unlock the panel and then to send out a message to your 
security team.""")
        slowprint (f"""\nYou speak into the panel's microphone "This is Security Chief {name1} {name2}. 
Send a security team to deck 4 sector 7 immediately.""")

        time.sleep(1)

        top_down2()

        time.sleep(1)

        slowprint("""\nThe doors open and your team rushes in. You point them in the direction of the 
incident and sit in the corridor with your back against the wall.""")
        slowprint("""\nYou take a minute for yourself and process what happened. 
You take a deep breath and rest. 

You've won!""")
        end()
    elif wire == "purple":
        print ("\nSparks fly from the panel as you fall back on to the ground. Deafening sirens begin to sound. That was not the right wire.\n")
        wire=None 
        while wire not in ("red", "purple"): 
            wire=input("Maybe try the red wire? Red or purple? \n\n").lower()
            if wire=="red":
                slowprint("""\nThe doors open and your team rushes in. You point them in the 
direction of the incident and sit in the corridor with your 
back against the wall.""")
                slowprint("""\nYou take a minute for yourself and process what happened. 
You take a deep breath and rest. 
                           
You've won!""")
                end()
        
            elif wire=="purple":
                print("\nThere is a giant power surge that kills you instantly")
                slowprint("\n\nDespite dealing with the perpetrator... Your poor electrical knowledge and incorrect choices have handed you the ultimate loss...\n")
                loop()

def attack():
    ans=None
    print("\nYou are being ATTACKED!!!")

    while ans not in ("a", "b", "c"): 
        ans=input("\nDo you: \n\n[A] Reach for your weapon? \n\n[B] Push the attacker away? \n\n[C] Pin the attacker? \n\n").lower()

        if ans=="a":
            print("\nYou reach for your weapon but the attacker knocks it out of your hand.\n")
            print("\nHe runs for your weapon. You both intercept it at the same time and \nthere is a struggle.\n")
            
            ans=None 
            while ans not in ("a", "b"): 
                
                ans=input("\nDo you: \n\n[A] Try and point the weapon at the attacker and fire? \n\n[B] Try to throw the weapon out of range and restrain the attacker?\n\n").lower()
                
                if ans=="a":

                    sce=random.randint(0,51)
                    if sce <24:            
                        print("\nYou were able to use your weapon before the attacker could react!")
                        print("\nHe is now wounded and in need of medical attention.")
                        print("\nYou win!\n")
                        time.sleep(1)
                        comms_fix2()
                    elif sce >25:
                        print("\nThe attacker pre-emptes your movements and takes your weapon from you.")
                        print("\nHe uses it against you, killing you where you stand.")
                        print("\nYou lose...\n")
                        loop()


                elif ans=="b":

                    sce=random.randint(0,51)
                    if sce <24:
                        print("\nYou throw the weapon out of range to gain some distance. This proves advantageous.")
                        print("\nWith the extra distance between yourselves and the weapon you are better able to \npredict his movements.")
                        print("\nAs he runs for the weapon you jump at him, bringing him down out of reach of \nthe weapon.")
                        print("\nYou hold him down and quickly move to restrain him.")           
                        print("\nYou win!\n")
                        time.sleep(1)
                        comms_fix2()
                    elif sce >25:
                        print("\nAs you throw the weapon out of range the attacker takes advantage of your brief \nlack of attention.")
                        print("\nHe knocks you down and runs for the weapon. Having a hold of the weapon he now \nfull control of the situation.")
                        print("\nAs you try to fake to the left, the attacker preempts your moves and \nopens fire...")
                        print("\nYou lose...\n")
                        loop() 


        
        elif ans=="b":
            sce=random.randint(0,51)
            if sce <24:
                print("\nYou push the attacker away to gain some distance. This proves advantageous.")
                print("\nWith the extra distance between you, you are better able to predict \nhis movements.")
                print("\nAs he comes running at you, you fake to jump at him but swoop to the side.")
                print("\nWith his full momentum he stumbles over your extended leg. You let him \nfall and quickly move to restrain him.")           
                print("\nYou win!\n")
                time.sleep(1)
                comms_fix2()
            elif sce >25:
                print("\nAs you push the attacker away you fail to notice he has a hold of \nyour weapon.")
                print("\nThere is no way you can close the distance in that time. You think about \nyour next move...")
                print("\nAs you try to fake to the left, the attacker preempts your moves and \nopens fire...")
                print("\nYou lose...\n")
                
                loop() 
         
        elif ans=="c":
            
            print("\nYou pin the attacker but he pushes you away and you fall.")
            print("\nAs you fall he tries to grab your weapon.")

            sce=random.randint(0,51)

            if sce<24:
                
                print("\nIn the chaos of the struggle you accidentally discharge your weapon. But you're in luck... \nWith the angle of your weapon you hit the attacker right in the shoulder and imobilises him. \nYou arrest him and find out whats going on.\n\n")
                print("\nYou win!\n")
                time.sleep(1)
                comms_fix2()

            elif sce>25:
                
                sce=random.randint(0,51)
                if sce <24:
                    
                    print("\nYou fire your weapon killing the attacker. Not the ideal outcome...\nBut you're safe now...")
                    print("\nYou win!\n")
                    time.sleep(1)
                    comms_fix2()

                elif sce>25:
                    
                    sce=random.randint(0,51)
                    if sce<24:
                        
                        print("\nThe attacker grabs your weapon and uses it against you. He hits you in the \nlower shoulder and you are briefly knocked unconscious.")
                        print("\nThe attacker walks away thinking you are dead... You quickly come back \naround, full of adrenaline!")
                        print("\nYou think fast and in your injured state slowly creep up on the attacker...")
                        print("\nWith your good arm, you swing at the back of his head with all \nof your force")
                        print("\nThe attacker stumbles forwards hitting his head on the corner \nof the bulkhead.")
                        print("\nWhile the attacker is unconscious you restrain him while you try \nto call for backup.")
                        print("\nYou are both in serios need of medical attention...")
                        print("\nYou win!")
                        time.sleep(1)
                        comms_fix2()
                    
                    elif sce>25:
                        
                        print("\nThe attacker grabs your weapon and uses it against you.")
                        print("\nYou lose...\n")
                        
                        loop()

def science_attack():
    ans=None
    print("\nYou suddenly get tackled to the ground! Your back was turned too long.\n\nYou and the attacker slide fully into the airlock. \n\nThere is a struggle to gain control as the attacker has the advantage of surprise.\n\n")

    while ans not in ("a", "b"): 
        ans=input("\nDo you: [A] Try to flip the attacker off you and close him in the airlock till backup arrives? \n\n[B] Try to reach for your weapon?\n\n").lower()

        if ans=="a":
            
            print("\nThe attacker falls and hits his head, knocking him unconscious.\n")
            time.sleep(0.1)
            print("\nYou notice your restraints have fallen on the floor in the science bay. \nAs you turn your back, the attacker jumps at you, knocking you to \nthe ground.\n")

            ans=None 
            while ans not in ("a", "b"): 
                
                ans=input("\nDo you: \n\n[A] Reach for your weapon? \n\n[B] Try yo keep the attacker in the airlock till backup arrives?\n\n").lower()
                
                if ans=="a":

                    sce=random.randint(0,51)
                    if sce <24:            
                        print("\nYou were able to use your weapon before the attacker could react!")
                        print("\nHe is now wounded and in need of medical attention.")
                        print("\nYou move quickly and proceed to lock him in the airlock.")
                        print("\nYou win!\n")
                        time.sleep(1)
                        comms_fix2()
                    elif sce >25:
                        print("\nThe attacker pre-empts your movements and uses your momentum against you....")
                        print("\nYou fall into the airlock and he closes the door!")
                        print("\nWithout hesitation he vents you out into space...")
                        print("\nYou lose...\n")
                        
                        loop()


                elif ans=="b":

                    sce=random.randint(1,51)
                    if sce <24:
                        print("\nWhile fighting on the floor, you grab the attacker and roll closer \nto the airlock.")
                        print("\nWith all of your strength you manage to slide the attacker into \nthe airlock and press the 'emergency door close' button.")
                        print("\nHe is locked in with no chance of escape.")           
                        print("\nYou win!\n")
                        time.sleep(1)
                        comms_fix2()

                    elif sce >25:
                        print("\nThe attacker pre-empts your movements and uses your momentum against you....")
                        print("\nYou fall into the airlock and he press the 'emergency door close' button!")
                        print("\nWithout hesitation he vents you out into space...")
                        print("\nYou lose...\n")
                        
                        loop() 


        
        elif ans=="b":

            print("\nYou reach for your weapon but the attacker knocks it out of your hand.\n")
            print("\nHe runs for your weapon. You both intercept it at the same time and \nthere is a struggle.\n")

            sce=random.randint(0,51)
            if sce <24:
                print("\nYou push the attacker away to gain some distance. This proves advantageous.")
                print("\nWith the extra distance between you, you make it to your weapon first.")
                print("\nAs he comes running at you, you roll onto your back and fire multiple shots.")
                print("\nThe beam hits him in the shoulder knocking him back into the airlock.")
                print("\nYou quickly scramble out of the airlock and decide to lock him in till help arrives.")
                print("""\n'beep beep beep loss of pressure' You look through the window and notice your weapon
has damaged the airlock controls. You try to open the airlock quickly to save and 
arrest the attacker, but the damaged computer control unit wont let you override
the process. Before the pressure is even to low to breathe, the outer airlock 
door blasts open, sucking the attacker out into space...""")
                print("\n\nYou win... But now you have to try and retrieve the attacker...")
                time.sleep(1)
                comms_fix2()

                
            elif sce >25:
                print("\nAs you push the attacker away, he falls ahead of you and grabs your weapon.")
                print("\nThere is no way you can close the distance in that time. You think about \nyour next move...")
                print("\nAs you try to fake to the left, the attacker preempts your moves and \nopens fire...")
                print("\n He fires twice... The beams hit you once in the arm and once in \nthe stomach.")
                print("\nYou fall backwards into the airlock...")
                print("\n\nThe attacker vents you out into space without hesitation...")
                print("\nYou lose...\n")
                
                loop()

def end():
    slowprint(f"""After extensive investigation, you find that the perpetrator was 
the missing prisoner from the Alpha5 station. He had managed 
to live on Alpha5 for months undetected, spending his time 
in maintenance corridors and air vents.

The perpetrator managed to kill a new crew member and steal his 
identity. After boarding the {name3}, the perpetrator tried to lay 
low and decided hide. His goal was to hold on for two more days 
till the {name3} arrived at the next science outpost, where he 
would escape and contact his friends for an easy escape.
                 
And it worked... Untill the new science officer recognised the 
prisoner from the look out alerts posted around the Alpha 5 
station. after seeing the science officers reaction, the 
perpetrator knew he had to deal with the situation there and 
then.
                 
After a violent altercation in the corridor near the science 
bay, the perpetrator vented the science officer out of the 
airlock. But in his desperation the perpetrator left too 
many clues.
                 
you followed the clues and solved the mystery...""")

    slowprint("\n\n\nGame produced by Team Orange!!")
    loop()

slowprintart("""\n\n\n\033[1;31;31m
    ▄████████    ▄███████▄    ▄████████  ▄████████    ▄████████    ▄████████    ▄█    █▄     ▄█     ▄███████▄ 
   ███    ███   ███    ███   ███    ███ ███    ███   ███    ███   ███    ███   ███    ███   ███    ███    ███ 
   ███    █▀    ███    ███   ███    ███ ███    █▀    ███    █▀    ███    █▀    ███    ███   ███▌   ███    ███ 
   ███          ███    ███   ███    ███ ███         ▄███▄▄▄       ███         ▄███▄▄▄▄███▄▄ ███▌   ███    ███ 
 ▀███████████ ▀█████████▀  ▀███████████ ███        ▀▀███▀▀▀     ▀███████████ ▀▀███▀▀▀▀███▀  ███▌ ▀█████████▀  
          ███   ███          ███    ███ ███    █▄    ███    █▄           ███   ███    ███   ███    ███        
    ▄█    ███   ███          ███    ███ ███    ███   ███    ███    ▄█    ███   ███    ███   ███    ███        
  ▄████████▀   ▄████▀        ███    █▀  ████████▀    ██████████  ▄████████▀    ███    █▀    █▀    ▄████▀ \n""")

slowprintart("""\033[1;31;34m  
             .        ,MMM8&&&.    . . . .  .   .  + .        . .   .  + .    
                 _...MMMMM88&&&&..._    .   .     .  .   . 
     .        .::'''MMMMM88&&&&&&'''::..  .   .   *  .       .   *  .       .   .  *  
             ::     MMMMM88&&&&&&     ::  .    +  .  *  .       . 
             '::....MMMMM88&&&&&&....::'  *  .  . .      ☄
     *          `''''MMMMM88&&&&''''`  *  .       .             .   *  .       . 
     .   .            'MMM8&&&'.       .  .       .  . .     
                     .              +   .                .   . .     .  .
                             .                    .                       .     *
             .       *                        . . . .  .   .  + .  .  *    .  *  
                         "You Are Here"            .   .  +  . . . . * 
             .                 |             .  .   .    .       . .             . * 
 *  .                          |           .     .     . +.    +  .
         .                    \|/            .                .   . .  .  *   .         .  *   . 
                     . .       V          .      * . . .  .  +   . *   . 
         *           .     . ⁆          ...           .  .*                  * *
          *          ~ >>>>■■■■■■■■―           .   .            +  .           .         
                             ⁆         .             . +    .                   +    .   *   .          .
     .     .                      .     . + .  . .     .      .  +     *   .         .
                     .      .    .     . .      . . .          ! /    +   .    .            +
                 *             .    . .      +    .  .       - O -s
                     .     .    .  +   . .      *  .       . / |
      .                   . + .  .  .  .. +  .
             .      .  .  .  *   .  *  . +..  .            *
 *      .                +
             \n\n\n""")

name1=input("\033[1;31;37mFirst name:\n\n")

name2=input("\nSurname: \n\n")

name3=input("\nShip name: \n\n")

slowprintart(f"""\n\033[1;31;34m
 * .     .            *,,         ..          .       .. ,. ..  .  .   ,    .    
             .                   .                 , .                           
                      ,  .        ,                                    .         
  .              .            "    \033[1;31;37m{name3}\033[1;31;34m.  .  .     .    .      .                          
   .               .  .          .  | .               /              /#**(       
                  .     . ,        .| "                *   .     ,/&#/*/          
                                    |  .               .    (*#@&/*/..,  .       
    .   .          .        ,..     |              /    ,//&@@#(**...*           
                                    |   .     . .    (//#@%((/**..,&         .   
 ..       .                        \|/     .  .   (/*&@&%(/#(,..*(.            , 
 .               .               .  V      .  .,/*%%%&#/(@/...*,,         . .    
 .             .                             **/%@&(//(#,....,.     ,            
                     . ..               / //*#%&(/*//,,.....                     
 .           .        *%@/         (%@((.,/(#(***/*.,,....                       
      .           ,*&***.       ,#@/*,..*(/***/,,... ..,                   #     
               ****/*,,%%&(@@,//*/*.....&***(*/*......                   .        
  .  *.      ,,,***,///((/*,,,,(,..,.,.////*....,.  *    ,                       
          ,,,,*%,*  /***,,*,*,. , .. ,*(/,.*...,  .               ,             .
         /(@/*        ..*,,..,.,..*,*(,.../.*                          ,  .      
       ..            /((**/.**&.(*(,..*..((#& (                     .   .   .    
    .               .    *.**,***..,..*//(#**(,  .                            .  
     ..  .              .(/#&((.,.,*,**//////(*,    *.  . .          . /    .    
  .                     (##((#/&%,(,.******/*///@%#@%., . .                    .  
           .          *(/, */,,/*,     ,****/*,%/*,..  ,    /  / .         ,,  . 
                       . *(%(*..   .     .*,,*/(,..               ...            
  .                      *@(..            ,,**#,..                 (.         .   
  .      .             .(/               /***. .     .                            
           .                . .       **,,.       .                  *    .    , 
        /            .        .      ((/                    ,            .       
   .             .          ,       ..                 .  .    ./         .      
  . .           ,                .    .           ,            .       ,.      ,  
                            .  .         .                           .     ,..   \033[1;31;37m\n\n""")

def main():

    skip=input("\nDo you want to skip the story? y/n\n\n").lower()

    if skip == "n":
        slowprint(f"""\n\n{name1}, you are the chief security officer of the {name3}. Your ship has recently
docked at space station Alpha5 for maintenance and crew rotation.""")
        slowprintart("""\n\n\033[1;31;34m
                 *  .      .        /**  (((/ &#**///( (*       *           .      .     .
         *.   *             &@, (,*,*,/, /***/******/*//*(***#***#//(        .    .    .    
             .            #*,.%*/,,,.*#**,*,,,*********,,,*,*/#*..*//,,**((@%             
                 /**//**.//***,**                          .****,...**.***( &.*         "Alpha5"
             (@@(%(*/*,/*,/,*....           .,         .    *..*,,  *,*# *(%*//,       
             , *,,*%,(**        *,*,..*     ,.   . .,   *..,*,           **/,/((((*@@%  
         *,@,#/#/*(*   .            /,,*.,*/ .**..*,,./,*                 ,*/#**//     
         ,(&*////**                      **/*..,***,*              .         (,%(//.@@@(
         ,,@ (.**/*        .              /..*.,.* **...                     /#(///.    
         *,.#./#(#*                .,..****.,***,..,*,** .,        .      ,*/,,//*@@@@ 
         **,.*(/,*/*(.         ,..***     ,,.    .        ***...,      *#/((.*#,      
             #.@ ,/*****.**,.**/          .                     ,**.#//,*,/(*@,,(     
                     *,#*. /,****/((                           ,(///**,**#*/,*           .
                     ,#,,***(/%(./,*****(((.**#*//#****/*#,/,*,**(.,**,,                
         *                    @,,*,,*#/(/*(*,,*,//**,***/,%#,,***  ,,,            .   .   
             .*        .                ,,,       ,*,                                     
                     .                                        .                 .      *.
                                     \033[1;31;37m\n""") 
        
        slowprint("""\nThe station is orbiting a moon that is used as a prison colony. Several months ago a prisoner 
being transferred to the colony escaped at the station but was never found.""") 
        
        slowprint(f"""\nAfter the station was locked down and searched thoroughly, it was assumed that the prisoner 
had escaped on another visiting vessel. But since then all visiting ships 
have been inspected before departure. And the {name3} is no different...""")

        slowprint(f"""\nThe {name3} departed Alpha5 two days ago after a week long stay to undergo crew rotation and maintenance. 
There are a lot of new crew members and it has been your job to oversee their integration.""")

        start()

    elif skip == "y":

        start()

    else:
        slowprint("\nYou must enter y/n.\n")
        main()
        

main()
exit()