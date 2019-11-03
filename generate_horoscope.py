import random


def generate_horoscope():
    welcome = "Welcome to your UB hacking horoscope. Here is what the stars have to say to you: "
    prefix_list = ["Today is a great day to ", "It may not be the best time to ", "The stars think you are ready to ", "It is your time to ", "Ruin would befall you if you were to ", "There has never been a better time to "]
    action_list = ["not sleep for 24 hours. ", "embrace your caffeine addiction with twenty red bulls. ", "throw away all your code at midnight and start over. ", "start a meme contest in the slack channel. ", "make a Tim Hortons run. ", "take nothing seriously and goof off the whole time. ", "eat so much sugar that you see behind your eyeballs. ", "drop your laptop down the stairs.", "attempt to win every prize. ", "sleep under a table with no pillow. "]
    sponser_tie_in = "The best sponser for you to connect with tonight is "
    sponser_list = ["M and T Bank. ", "Centene Corporation. ", "A C V Auctions. ", "Wegmans. ", "I B M. ", "Verison Media. ", "Moog. ", "Value Centric. ", "Facebook. ", "Twilio. ", "Stark and Wayne. ", "Synacor. "]
    forcast_prefix_list = ["Today, ", "It is highly unlikely that ", "It is almost certain that ", "You may be surprised to find out that ", "In the very near future, "]
    forcast_feeling_list = ["you will wake up feeling well-rested, ", "you will be sick, ", "your project will win, ", "you will meet your new best friend ", "you will experience rapid heart beat from all that red bull, ", "you will crash your laptop by running thirty processes at once, ", "you will wake up still feeling confident about your code, ", "you will not catch a cold or the flu from someone here, "]
    but = ["but the stars will smile on you when "]
    second_forecast_list = ["your teammates love you forever. ", "a mentor saves your failing project. ", "you feel better after nine cups of coffee. ", "you learn lots of new things. ", "you demo something fun, even you don't think it's very good. ", "you find out about some cool new job opportunities. ", "you get some awesome swag."]
    lucky_numbers_are = "Lucky numbers are "
    retval = welcome
    retval = retval + prefix_list[random.randint(1,len(prefix_list))]
    retval = retval + action_list[random.randint(1,len(action_list))]
    retval = retval + sponser_tie_in
    retval = retval + sponser_list[random.randint(1,len(sponser_list))]
    retval = retval + forcast_prefix_list[random.randint(1,len(forecast_prefix_list))]
    retval = retval + forcast_feeling_list[random.randint(1,len(forecast_feeling_list))]
    retval = retval + but
    retval = retval + second_forecast_list[random.randint(1,len(second_forecast_list))]
    retval = retval + lucky_numbers_are
    retval = retval + random.randint(1,99) + ", " random.randint(1,99) + ", " random.randint(1,99) + ", " random.randint(1,99) + ", and " random.randint(1,99) + ". "
    retval = retval + "Thank you, and goodbye."


#    return random.randint(1,10)
    print(retval)
    return retval

generate_horoscope()
