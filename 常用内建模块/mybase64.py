#Base64是一种用64个字符来表示任意二进制数据的方法
import base64
base64.b64encode(b'binary\x00string')

