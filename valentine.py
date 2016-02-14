# coding=utf-8
"""
    Happy Valentine's Day
    author: ozcaan11
"""

import os
import platform
import sys
import time

valentine = '''
##============================================================================##
||                ||  ||   /\\\  ||""|| ||""|| \\\ //                           ||
||                ||==||  //=\\\ ||__// ||__//  \\\/                            ||
||                ||  || //   \\\||     ||      //                             ||
||                                                                            ||
||    \\\   //  /\\\   ||    ||""" |\\\ || """""" || |\\\ || ||""" ll  ||"""      ||
||     \\\ //  //=\\\  ||    ||=== ||\\\||   ||   || ||\\\|| ||===     ll>>       ||
||      \\\/  //   \\\ ||### ||### || \\\|   ||   || || \\\| ||###     ___||      ||
||                                                                            ||
||                     ||""\\\   /\\\   \\\ //                                   ||
||                     ||  ||  //=\\\   \\\/                                    ||
||                     ||##// //   \\\  //                                     ||
##============================================================================##
'''


def valentines():
    while True:
        sys.stdout.write(valentine)
        time.sleep(0.2)
        if platform.system() == 'Linux':
            os.system("clear")
        else:
            os.system("cls")
        time.sleep(0.2)


print "Open it in full screen !!(Exit: CTRL+C)"
time.sleep(3)
if platform.system() == 'Linux':
            os.system("clear")
else:
    os.system("cls")
valentines()
