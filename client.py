#ChitChat client code

def main():
    print "Welcome to ChitChat v1.0"
    print "ChitChat is a very simple, lightweight application to make chatting simple and powerful."
    print "Using ChitChat you can start a personal chat, share files or engage in a group conversation."
    print "Type H for the list of commands.\n"
    
    while 1:
        inp = raw_input()
        if inp=='H':
            print "C:<username> - To connect to the server. Your username will be the name displayed to other users."
            print "Q - Quit ChitChat."
            print
        elif inp=='Q':
            print
            quit()
        else:
            print "Input not recognized. Please try again!\n"



    
if __name__=='__main__':
    main()