import sys
import time

# python ugh-test.py ugh 34 .05

# init
# ----
# word - the word to be printed
# times - the number of times you want to print the word (both down and across)
# sleep - how long to sleep for in between lines

word = str(sys.argv[1])
times = int(sys.argv[2])
sleep = float(sys.argv[3]) # how long to sleep for between new lines

def main():
    # init
    x = 0
    y = 0
    word_iter = word

    # prime the pump, or something
    print word

    # sleep so it's funnier
    time.sleep(sleep)

    # now start looping - nested to going across and down
    while (x < times):
        while (y < times):

            # add the word an extra time for each new line
            word_iter += " " + word
            print word_iter

            # next iter
            y = y + 1
            time.sleep(sleep)

        # next iter    
        x = x + 1
    
    # now we're done going across 
    while(True):
        print word_iter
        time.sleep(sleep)

if __name__ == '__main__':
    main()