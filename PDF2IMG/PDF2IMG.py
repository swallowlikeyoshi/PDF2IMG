import fitz
import os
import sys

######################################

# 화질 설정(저화질: 75, 중간: 150, 고화질: 300)
PPI = 150

# 확장자 설정("jpg", "png")
FORMAT = "jpg"

######################################

def PDF2IMG(path, file_name):
    if not os.path.exists(os.path.join(file_name)):
        os.mkdir(os.path.join(file_name))
    document = fitz.open(path)
    for i, page in enumerate(document):
        page_image = page.get_pixmap(matrix=fitz.Matrix(PPI/72, PPI/72))
        page_image.save(os.path.join(file_name, f"{file_name} ({i}).{FORMAT}"), FORMAT)
    print("변환 끝!")

if __name__ == "__main__":
    PDF2IMG(sys.argv[1], sys.argv[2])