"""Prints out a word of your choice to the console in fun patterns."""

import sys
import time

def printError():
    """Prints error to the console if the correct number of arguments is not specified."""
    print "Incorrect params given. Require $ python ugh-1.1.py [word] [times] [sleep]"
    print "[word]  - the word to be printed"
    print "[times] - the number of times you want to print the word (both down and across)"
    print "[sleep] - how long to sleep for in between the printed lines"

def main():
    """Main function. Does essentially everything."""

    # before we do anything make sure there are the correct number of params
    if(len(sys.argv[1]) > 1):
        if(len(sys.argv[2]) > 1):
            if(len(sys.argv[3]) > 1):
                printError()
                exit()
        else:
            printError()
            exit()
    else:
        printError()
        exit()
        
    word = str(sys.argv[1])
    times = int(sys.argv[2])
    sleep = float(sys.argv[3])

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
    
    # now we're done going across so go straight down
    while(True):
        print word_iter
        time.sleep(sleep)

if __name__ == '__main__':
    main()