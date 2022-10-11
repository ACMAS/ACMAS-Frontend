import os  # from native modules
import fitz  # from PyMuPDF
import pytesseract  # from pytesseract
import cv2  # from Opencv
import io  # from native modules
from PIL import Image, ImageFile  # from Pillow
from colorama import Fore  # from native modules
import platform  # from native modules

ImageFile.LOAD_TRUNCATED_IMAGES = True

# Global variables
strPDF, textScanned, textScanned, inputTeEx, dirName = "", "", "", "", [
    "images", "output_txt"]

def gInUs():
    # Global var
    global strPDF
    global inputTeEx
    if(platform.system() == "Windows"):
        # Print input
        print(Fore.YELLOW +
              "[.] Add the tesseract.exe local path" + Fore.RESET)
        inputTeEx = input()
        # Print input
        print(Fore.GREEN + "[!] Add the PDF file local path:" + Fore.RESET)
        inputUser = input()
    # Print an alert if input is not valid, if not, call to fun reDoc
    if(inputUser == "" or len(inputUser.split("\\")) == 1):
        print(Fore.RED + "[X] Please enter a valid PATH to a file" + Fore.RESET)
    else:
        extIm(inputUser)