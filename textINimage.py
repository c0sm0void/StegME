import sys
from PIL import Image
import re

def decode(img):
    width, height = img.size
    msg = ""
    size_of_msg = ""
    return_msg = ""
    index_pixel = 0

    for row in range(height-1,0,-1):
        for col in range(width-1,0,-1):

            if index_pixel < 11:
                r,g,b = img.getpixel((col,row))
                #taking binary value and converting into string for later use
                red_bin = str(bin(r))
                green_bin = str(bin(g))
                blue_bin = str(bin(b))

                if index_pixel == 10:
                    newString = red_bin[len(red_bin) - 1] + green_bin[len(green_bin) - 1]
                    size_of_msg = size_of_msg + newString
                    num_pixels_req = ((int(size_of_msg[:len(size_of_msg)], 2)))/3 + 11
                    index_pixel += 1
                else:
                    newString = red_bin[len(red_bin) - 1] + green_bin[len(green_bin) - 1] + blue_bin[len(blue_bin) - 1]
                    size_of_msg = size_of_msg + newString
                    index_pixel += 1

            elif index_pixel > 10 and index_pixel <= num_pixels_req:
                r, g, b = img.getpixel((col, row))
                # taking binary value and converting into string for later use
                red_bin = str(bin(r))
                green_bin = str(bin(g))
                blue_bin = str(bin(b))
                index_pixel += 1
                newString = red_bin[len(red_bin) - 1] + green_bin[len(green_bin) - 1] + blue_bin[len(blue_bin) - 1]
                msg = msg + newString

    #used regex to slice the long string of
    #binary numbers in order to convert
    #binary to Int then to ascii

    bin_text = re.findall('........', msg)
    for i in range(len(bin_text)):
        return_msg += chr(int(bin_text[i],2))

    return return_msg



def encode(img,msg):

    length = len(msg) * 8 # 8 for the bits
    length_string = '{0:032b}'.format(length)
    rev_string = ''.join(reversed(length_string))
    length_list = list(rev_string)
    list_len = len(length_list)
    index_pixel = 0
    msg_index = 0
    bin_msg = ''.join(format(ord(x), '08b') for x in msg)
    bin_msg_list = list(bin_msg)
    msg_len = len(bin_msg_list)
    msg_len_marker = len(bin_msg_list)
    msg_rev_bin = ''.join(reversed(bin_msg_list))

    # use a copy of image to hide the text in
    encoded = img.copy()
    width, height = img.size


    for row in range(height - 1, 0, -1):
        for col in range(width - 1, 0, -1):
            if index_pixel < 11:


                r,g,b = img.getpixel((col,row))
                # taking binary value and converting into string for later use
                red_bin = str(bin(r))
                green_bin = str(bin(g))
                blue_bin = str(bin(b))

                # need to put bit that needs to encoded from length num
                red_list = list(red_bin)
                red_list[len(red_list) - 1] = length_list[list_len-1]

                list_len -= 1

                green_list = list(green_bin)
                green_list[len(green_list) - 1] = length_list[list_len-1]

                list_len -= 1

                if index_pixel == 10:
                    blue_list = list(blue_bin)
                    blue_list[len(blue_list) - 1] = blue_bin[len(blue_list)-1]
                    list_len -= 1

                else:
                    blue_list = list(blue_bin)
                    blue_list[len(blue_list) - 1] = length_list[list_len - 1]

                    list_len -= 1

                #converting back to string then int for rgb values
                red_conv_from_list_2_str = ''.join(red_list)
                red_str_in_bin = red_conv_from_list_2_str[2:]
                red_bin_to_integer = int(red_str_in_bin,2)

                green_conv_from_list_2_str = ''.join(green_list)
                green_str_in_bin = green_conv_from_list_2_str[2:]
                green_bin_to_integer = int(green_str_in_bin, 2)

                blue_conv_from_list_2_str = ''.join(blue_list)
                blue_str_in_bin = blue_conv_from_list_2_str[2:]
                blue_bin_to_integer = int(blue_str_in_bin, 2)


                blue_conv_from_list_2_str = ''.join(blue_list)
                blue_str_in_bin = blue_conv_from_list_2_str[2:]
                blue_bin_to_integer = int(blue_str_in_bin, 2)
                encoded.putpixel((col, row), (red_bin_to_integer, green_bin_to_integer, blue_bin_to_integer))

                if index_pixel == 10:
                    index_pixel += 2
                    continue
                else:
                    index_pixel += 1

            if index_pixel > 11 and msg_index < msg_len_marker -1 and msg_index > -1:
                rr, gg, bb = img.getpixel((col, row))
                # taking binary value and converting into string for later use
                red_binn = str(bin(rr))
                green_binn = str(bin(gg))
                blue_binn = str(bin(bb))

                if msg_len < 0:
                    continue
                else:
                    # need to put bit that needs to encoded from length num
                    red_listt = list(red_binn)
                    red_listt[len(red_listt) - 1] = msg_rev_bin[msg_len - 1]

                    msg_len -= 1

                if msg_len < 0:
                    continue
                else:
                    green_listt = list(green_binn)
                    green_listt[len(green_listt) - 1] = msg_rev_bin[msg_len - 1]

                    msg_len -= 1

                if msg_len < 0:
                    continue
                else:
                    blue_listt = list(blue_binn)
                    blue_listt[len(blue_listt) - 1] = msg_rev_bin[msg_len - 1]

                    msg_len -= 1

                red_conv_from_list_2_strr = ''.join(red_listt)
                red_str_in_binn = red_conv_from_list_2_strr[2:]
                red_bin_to_integerr = int(red_str_in_binn, 2)

                green_conv_from_list_2_strr = ''.join(green_listt)
                green_str_in_binn = green_conv_from_list_2_strr[2:]
                green_bin_to_integerr = int(green_str_in_binn, 2)

                blue_conv_from_list_2_strr = ''.join(blue_listt)
                blue_str_in_binn = blue_conv_from_list_2_strr[2:]
                blue_bin_to_integerr = int(blue_str_in_binn, 2)

                encoded.putpixel((col, row), (red_bin_to_integerr, green_bin_to_integerr, blue_bin_to_integerr))
                msg_index += 1
                index_pixel += 1

    return encoded


Encode_OR_Decode = sys.argv[1]
Image_To_Enc_OR_Dec = sys.argv[2]

Image_File_For_Encoding = '.jpg'
Image_File_For_Decoding = '.png'
txt_ext = '.txt'

if Encode_OR_Decode == 'enc' or Encode_OR_Decode == 'ENC':
    print('Encoding text in image...')
    if Image_File_For_Encoding in sys.argv[2]:
        img = Image.open(Image_To_Enc_OR_Dec)

        try:
            txt_to_encode = sys.argv[3]
        except IndexError:
            print('\n!!!Please Provide txt file to encode.(python steg.py enc <jpg> <txt file>)\n\n')
            exit()

        if txt_ext in txt_to_encode:
            with open(txt_to_encode, 'r') as myfile:
                data = myfile.read()
            image_encoded = encode(img,data)
            image_encoded.save("encoded.png")
        else:
            print('\nPlease use a .txt file to encode in image!\n')
    else:
        print('\n!!!Make sure image type is .jpg for encoding!!!\n')
elif Encode_OR_Decode == 'dec' or Encode_OR_Decode == 'DEC':
    print('Decoding text in image...')
    if Image_File_For_Decoding in sys.argv[2]:
        img = Image.open(Image_To_Enc_OR_Dec)
        decoded_msg = decode(img)
        print('Printing Message Now....\n')
        print(decoded_msg + '\n')
    else:
        print('\n!!!Make sure image type is .png for decoding!(python steg.py dec <png>)\n')
else:
    print('First or argument needs to be either enc/dec lower case or uppercase\n'
          '(python steg.py enc/dec <Image> <txt file>)')
