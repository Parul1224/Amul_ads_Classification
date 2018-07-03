The two files(extract_text.py) and (text_extract.py) mentioned extracts the texts from the images.





For the correct implementation of the two codes the installation of certain modules is necessary.

1.PIL
2.openCV
3.python 2.7
4.Pytesseract
5.numpy



After your system meets the above-mentioned requirements the execution of above two codes are simple




1.For text_extract.py provide the path of your input file in 'src.path'. It's better to keep the images in the same directory so that it's easy to recall.



Command to run the file:
python text_extract.py>"specify the filename where you want to store the extracted text"
Example: python text_extract.py>output.txt
The text is stored in output.txt in the same directory and the denoised image is saved in 'sr_path' + "removed_noise.jpg" in the same directory








2.For extract_text.py




Command to run the file
python extract_text.py
The extracted text is displayed in the teminal(Linux) or command prompt(Windows)


