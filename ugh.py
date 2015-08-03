"""Prints out a word of your choice to the console in fun patterns."""

import sys
import time

def print_error():
    """Prints error to the console if the correct number of arguments is not specified."""
    print "Incorrect params given." 
    print "python ugh-1.1.py [word] [times] [sleep] [design]"
    print "[word]  - the word to be printed"
    print "[times] - the number of times you want to print the word (both down and across)"
    print "[sleep] - how long to sleep for in between the printed lines"
    # print "[design] - array of integers of all designs to execute in order"

def check_env():
    """Check environment for the correct number of args."""

    # add argv[4] for design
    if(len(sys.argv[1]) < 1 and len(sys.argv[2] < 1 and len(sys.argv[3] < 1))):
        printError()
        exit()

def down_and_right(word, times, sleep):
    """Down and to the right."""
    x = 0
    y = 0
    word_iter = word

    # prime the pump, or something
    print word

    # sleep so it's funnier
    time.sleep(sleep)

    # going across and down
    while (x < times):
        while (y < times):
            word_iter += " " + word
            print word_iter

            # next iter
            y = y + 1
            time.sleep(sleep)

        # next iter    
        x = x + 1

def main():
    """Main function."""

    # before we do anything make sure there are the correct number of params
    check_env()
        
    word = str(sys.argv[1])
    times = int(sys.argv[2])
    sleep = float(sys.argv[3])
    # design = str(sys.argv[4]) (array???)
    
    options = {1 : down_and_right,
               2 : down_and_left, 
               3 : stars,
    }


    # for each number in the array
    # case where you execute each design's corresponding method
    # 4,2,1,5,3,1,2
    
    # now we're done going across so go straight down
    while(True):
        print word_iter
        time.sleep(sleep)

if __name__ == '__main__':
    main()