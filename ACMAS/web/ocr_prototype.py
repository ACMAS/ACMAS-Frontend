from multiprocessing import reduction
import os,sys
from pdf2image import convert_from_path

#Gets the ending types of files
def endingtype(string):
    index = string.rfind('.')
    return string[index+1:]

def png_conversion(pdf_name):
    #makes sure we are only converting pdfs if
    #the file type isnt pdf returns ending type
    if(endingtype(pdf_name) == 'pdf'):
        pass
    else:
        return []

    print("CONVERTING PNG")
    os.system("mkdir ocr_images")
    image_names =[]
    images_from_path = convert_from_path(pdf_name)
    for i in range(len(images_from_path)):
        # Save pages as images in the pdf
        images_from_path[i].save('ocr_images/'+'page'+ str(i) +'.jpg', 'JPEG')
        image_names.append('ocr_images/'+'page'+str(i)+'.jpg')
    return image_names

def run_ocr(image_names):
    ocr_output_files = []
    acceptable_formats = set({'png','jpg','gif','tiff'})
    os.system("mkdir ocr_results")
    for i in range(0,len(image_names)):
        if endingtype(image_names[i]) not in acceptable_formats:
            return
        print("RUNNING OCR FOR IMAGE {} OF {} NAMED {}".format(i,len(image_names), image_names[i]))
        #ocr_cmd = "tesseract {}  --l eng".format(image_names[i])
       
        ocr_cmd = "tesseract {} {}".format(image_names[i],'ocr_results/page'+str(i))
        os.system(ocr_cmd)
        ocr_output_files.append('ocr_results/page'+str(i))

    return ocr_output_files

def parse_ocr(file_name):
    ocr_results_data = open(file_name,'r')
    parsed_data = ocr_results_data.read().strip().replace('\n', ' ').split('.')

    return parsed_data


def parse_ocr_results(ocr_output_files):
    parsed_questions = []
    for i in range(0,len(ocr_output_files)):
        question = parse_ocr(ocr_output_files[i]+'.txt')
        for parsed_question in question:
            parsed_questions.append(parsed_question.strip())
    
    return parsed_questions






pdf = 'Foam_Hw4.pdf'
images = png_conversion(pdf)
ocr_output = run_ocr(images)

# ###NEED TO STAND UP A PROPER MAIN FILE. THIS WILL ALLOW US TO PASS IN
# ##1. If the file is converted
# if __name__ == '__main__':
#     #Input file as an argument
#     #this makes this code runnable with only having to specify
#     #an input file. Example workflow. react ->(pdf) python ->(keys for db)
#     pdf = sys.argv[1] #'Foam_Hw4.pdf'
#     #creates a folder with the jpeg images from the pdf
#     # images = png_conversion(pdf)
#     # ocr_output = run_ocr(images)
#     ocr_output = ['ocr_results/page0']
#     #questions  = parse_ocr_results(ocr_output)
#     #could then send json from questions over flask server or otherwise send it to the front end.
#     #ex: send(req,res = questions.json)
