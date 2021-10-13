# !/bin/bash
# from https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)
read texttoSpeech
espeak -ven+f2 -k5 -s150 --stdout  "your phone number is $texttoSpeech" | aplay
