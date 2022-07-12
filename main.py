import os
from PIL import Image

justAlpha = False
funny = False


def main():
    if not justAlpha:
        for i in os.listdir(
                os.path.relpath('Input files here/Input1')):  # For loop will grab the last image file in Input1
            img1 = Image.open(os.path.join(os.path.relpath('Input files here/Input1/' + i))).convert('RGBA')

    for i in os.listdir(os.path.relpath('Input files here/Input2')):  # For loop will grab the last image file in Input2
        img2 = Image.open(os.path.join(os.path.relpath('Input files here/Input2/' + i)))

    # --- Make greyscale image ---
    img2Data = img2.getdata()

    if justAlpha:
        img2New = []
        img1 = img2.copy().convert('RGBA')
        img1NewList = []
        for i in img1.getdata():
            img1NewList.append((0, 0, 0, 255))
            #img1NewList.append((114, 137, 218, 255))
        img1.putdata(img1NewList)
        img1.save(os.path.relpath("Input files here/Input1/img.png"), 'PNG')

    for x in img2Data:
        Y = int(x[0] * 0.299) + int(x[1] * 0.587) + int(x[
                                                            2] * 0.114)  # Helpful website: https://www.dynamsoft.com/blog/insights/image-processing/image-processing-101-color-space-conversion/
        Y = 255 - Y  # create inverse
        img2New.append((Y, Y, Y))
    img2.putdata(img2New)
    img2.save(os.path.relpath("output/grayscale/image.png"))

    img1Data = img1.convert('RGBA').getdata()

    img1New = []
    for x in range(len(img1Data)):
        if not funny:
            img1New.append((img1Data[x][0], img1Data[x][1], img1Data[x][2], img2Data[x][0]))
        if funny:
            img1New.append((54,57,62, img2Data[x][0]))
    img1.putdata(img1New)
    img1.save(os.path.relpath("output/final output/image.png"), "PNG")


if __name__ == '__main__':
    main()
