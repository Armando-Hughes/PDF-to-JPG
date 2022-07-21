'''
By Armando Hughes
21/07/2022
The function pdf_to_jpg convert converts files in
'.pdf' format to files in '.jpg' format
'''
import fitz

def pdf_to_jpg(pdf_name, img_name):
    doc = fitz.open(pdf_name + '.pdf')
    for pg in range(doc.pageCount):
        page = doc[pg]
        rotate = int(0)
        zoom_x = 4.0
        zoom_y = 4.0
        trans = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
        pm = page.getPixmap(matrix=trans, alpha=False)
        pm.writePNG(img_name + '.jpg')