array=list(range(0,10))
print ('1>>生成0-9的数组:\n',array)
array.reverse()
print ('2>>翻转:\n',array)
string=''.join(str(i) for i in array)
print('3>>拼接为字符串：\n',string)
a=string[2:8]
print('4>>取出第三到第八个字符：\n',a)
a_reverse=a[::-1]
print('5>>翻转：\n',a_reverse)
b=int(a_reverse)
print(b)
print('转为二进制：\n',bin(b))
print('转为八进制：\n',oct(b))
print('转为十六进制：\n',hex(b))