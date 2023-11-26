import random
import optparse
import os
## mission cipher##
## upper only##
## lower only##
## special only##
## all in one##
print(""" 
    
    ####         ####           #####                            ###############
    #   #        #  #           #   #                           # #           # #
    #      #     #  #           #   #                           # #           # #
    #  #     #   #  #  *****    #   #               ******      # #           # #
    #  #  #    # #  #  *   *    #   #               *     *     # #           # #
    #  #    #    #  #  *****    #   #               ******      # #           # #
    #  #      #     #           #   #                           # #           # #
    #  #        #   #           #   ############                # #           # #  **********
    ####         ####           ################                 ###############   * owner  *
                                                                                   **********

""")


def help():
    print('***you can run : python Chipher_Tool.py -h***')

    parser = optparse.OptionParser()
    parser.add_option("-e", "--encode",  "-d", "--decode",
                      help="What would you like encode or decode, look at options ")
    options, arguments = parser.parse_args()
    return options


def Special():

    lower = [chr(ord('a')+i) for i in range(26)]
    special = [chr(ord(' ')+i) for i in range(26)]
    random.shuffle(special)
    upper = []
    for i in range(26):
        upper.append(chr(ord('A') + i))

    cipher_lower = input('Enter lower only character: ')
    encode = ""
    for cipher in cipher_lower:
        index = lower.index(cipher)
        encode += (special[index])
    print(encode)

    decode = ""
    for decoded in encode:
        index = special.index(decoded)
        decode += lower[index]
    print(decode)


def option():
    while True:

        print('0: Exiting ....')
        print('1: Help menu ....')
        print('2: Encoding for lower character to special ...')
        choice = int(input('what would you like to do: '))

        os.system("clear")
        if choice == 0:
            exit()
        elif choice == 1:
            help()
        elif choice == 2:
            Special()
        else:
            print('Invalid choice, Please chose 0 to 2 ...')


option()
