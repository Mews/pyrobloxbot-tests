import easyocr as ocr

reader = ocr.Reader(["en"])
result = reader.readtext("text_example.png", detail=0)
print(result)