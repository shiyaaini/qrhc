import ddddocr
ocr = ddddocr.DdddOcr()
with open("11.png", 'rb') as f:
    image = f.read()
res = ocr.classification(image)
print(res)