def Uni(code1,code2):
    print(ord(code1))
    print(ord(code2))
    if int(ord(code1)) >= int(ord(code2)):
        a = int(ord(code1))-int(ord(code2))
    else:
        a = int(ord(code2))-int(ord(code1))
    print(a)

def De():
    cc1 = 0
    cc2 = 0
    for i in list('鎬т环姣斿緢楂橈紙绠€鍗曠綉绔欙紝澶х墖鍐呭锛�'):
        cc1 += int(ord(i))
    for j in list('性价比很高（简单网站，大片内容）'):
        cc2 += int(ord(j))
    Uni(cc1,cc2)

De()

