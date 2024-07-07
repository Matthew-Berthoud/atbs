import random

BIG_STREAK = 6
TRIALS = 10000

trials_with_streaks = 0

for t in range(TRIALS):

    values = [random.choice(['H', 'T']) for i in range(100)]

#    for i in range(100):
#        if i % 10 == 0:
#            print()
#        print(values[i], end='')
#    print()


    big_streaks = 0
    h_streak = 0
    t_streak = 0

    for x in values:
        if x == 'H':
            h_streak += 1
            if t_streak >= BIG_STREAK:
                big_streaks += 1
                print(f"Trial" + str(t + 1).rjust(len(str(TRIALS)) + 1)
                    + " | Streak " + str(big_streaks).rjust(2) 
                    + " | " + str(t_streak).rjust(2) + " Tails"
                    + " | Results " + str(float(trials_with_streaks + 1) / (t + 1)) )
            t_streak = 0
        else:
            t_streak += 1
            if h_streak >= BIG_STREAK:
                big_streaks += 1
                print(f"Trial" + str(t + 1).rjust(len(str(TRIALS)) + 1)
                    + " | Streak " + str(big_streaks).rjust(2) 
                    + " | " + str(h_streak).rjust(2) + " Heads"
                    + " | Results " + str(float(trials_with_streaks + 1) / (t + 1)) )
            h_streak = 0
    
    if big_streaks > 0:
        trials_with_streaks += 1

print("\nFinal Results:", float(trials_with_streaks) / TRIALS)


    

