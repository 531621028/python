from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
im = Image.open('test.jpg')
w,h = im.size
print('Original image size: %sx%s' % (w, h))
im.thumbnail((w//2, h//2))
print('Resize image to: %sx%s' % (w//2, h//2))
im.save('thumbnail.jpg', 'jpeg')
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg', 'jpeg')