"""
来源：Python-100-Days（骆昊）
示例：二进制文件拷贝（分块读写），需准备 guido.jpg 源文件。
"""
# ---- 代码块10 ----
try:
    with open('guido.jpg', 'rb') as file1, open('吉多.jpg', 'wb') as file2:
        data = file1.read(512)
        while data:
            file2.write(data)
            data = file1.read()
except FileNotFoundError:
    print('指定的文件无法打开.')
except IOError:
    print('读写文件时出现错误.')
print('程序执行结束.')
