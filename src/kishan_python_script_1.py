from PIL import Image

im = Image.open("/home/kishankumar/my_work/YTs/pan_ocr/pan_kishan_1.png")
rgb_im = im.convert('RGB')

rgb_im.save('/home/kishankumar/my_work/YTs/pan_ocr/test1.png')
