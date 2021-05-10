import os,sys
c=""
n=[]
v=[]
m=os.system("xsel -cb")
if m:
    print("未安装xsel,退出")
print("输入quit退出,依赖xsel、zhcon\n使用xsel -ob 粘贴")
sys.argv.pop(0)
if sys.argv[0]=="o":
    sys.argv.pop(0)
    for nb1 in sys.argv:
        try:
            v.append(chr(int(nb1)))
        except:
            v.append(nb1)
    h=''.join(v)
    print("粘贴至粘贴版")
    os.system("echo " + h + "| xsel -ib")
    print("最后的结果:" + c)
while True:
    a=input("输入字符的Unicode编码:")
    try:
        if a!="quit":
            b=chr(int(a))
        else:
            c=''.join(n)
            print("粘贴至粘贴版")
            print("最后的结果:"+c)
            os.system("echo "+c+"| xsel -ib")
            break
    except:
        print("输入不大于65535的正数字")
    else:
        print("您要输入的是:"+b+"按Y确认")
        if input()=="y"or"Y":
            n.append(b)
