import os
import time
from PIL import Image
from pdf2image import convert_from_path
import pytesseract

pdf_folder = '時代華語2'
md_folder = '時代華語2md檔'

start_time = time.time()

os.makedirs(md_folder, exist_ok=True)

for filename in os.listdir(pdf_folder):
    if filename.endswith('.pdf'):
        pdf_path = os.path.join(pdf_folder, filename)
        md_path = os.path.join(md_folder, os.path.splitext(filename)[0] + '.md')

        images = convert_from_path(pdf_path)
        text = ''

        for i, image in enumerate(images, start=1):
            text += pytesseract.image_to_string(image, lang='chi_tra')

        with open(md_path, 'w') as md_file:
            md_file.write(text)

        print(f'Text from {pdf_path} has been successfully written to {md_path}')

end_time = time.time()

elapsed_time = end_time - start_time
minutes, seconds = divmod(elapsed_time, 60)
hours, minutes = divmod(minutes, 60)

print(f"The script took {int(hours)} hours, {int(minutes)} minutes and {int(seconds)} seconds to finish.")