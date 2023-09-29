import easyocr

reader = easyocr.Reader(['en'])  # Replace 'en' with the language you need
result = reader.readtext('downloaded_files/18/IMG-20230926-WA0005.jpg')

for detection in result:
    print(detection[1])
