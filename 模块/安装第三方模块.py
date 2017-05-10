from PIL import Image
im = Image.open('test.png')
print(im.format,im.size,im.mode)
im.convert('RGB')
print(im.format,im.size,im.mode)
#Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中
import sys
print(sys.path)