#!/bin/bash
echo -e "         ██████     ██                    ██       ██ ███████     "
echo -e "       ██     ██   ██                    ██ ██ ██ ██ ██           "
echo -e "         ██     ██████   █████  █████   ██   ██  ██ ██████        "
echo -e "           ██    ██     ██  ██ ██   ██ ██       ██ ██             "
echo -e "      ██    ██  ██  ██ ██ ███   ████  ██       ██ ██              "
echo -e "       █████   ██████ ██████ ██  ██  ██       ██ ██████           "
echo -e "                              █████                                "
while [[ 1 ]]
do
echo "*****************************************************************"
echo "  1)Encode text in image (Set imagename - smi.jpg)"
echo "  2)Decode text from image"
echo "  3)Encode image in image "
echo "  4)Decode image from image"
echo "  0)EXIT"


read n
case $n in
  1) echo "encoding....Want to enter your secret text? (y=YES | n=NO)"
  read c
  case $c in
  y)
  nano steg.txt
  ;;
  n)
  esac
  SPATH="/root/Desktop/RCC/ITR/steg.txt"
	export SPATH
  SMI="/root/Desktop/RCC/ITR/smi.jpg"
	export SMI
  python3 textINimage.py enc $SMI $SPATH
  ;;
  2) echo "decoding...."
  python3 textINimage.py dec encoded.png
  ;;
  3) echo "image in image"
  python imageINimage.py merge --img1=res/img1.jpg --img2=res/img2.jpg --output=res/output.png
  ;;
  4) echo "image from image"
  python imageINimage.py unmerge --img=res/output.png --output=res/output2.png
  ;;
  0) echo "Have a good day!!"
  break;;
  *)
     echo "Invalid choice"
     ;;
esac
done
