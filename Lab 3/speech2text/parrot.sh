# !/bin/bash
# from https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)
espeak -ven+f2 -k5 -s150 --stdout  "your phone number is $1 $2 $3 $4 $5 $6 $7" | aplay
