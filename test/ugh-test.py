import sys
import time

# example:
# python ugh-test.py ugh 34 .05

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

    while (x < times): # go down
        while (y < times): # go across
            word_iter += " " + word
            print word_iter
            y = y + 1
        time.sleep(sleep)
        x = x + 1
    
    # now we're done going across,
    # so go down until terminated
    while(True):
        print word_iter
        time.sleep(sleep)

if __name__ == '__main__':
    main()
