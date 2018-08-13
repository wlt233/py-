### project ɨ��
import random
import math
import sys

#���ɵ�ͼ
x,y=10,10
maps=[]
total=15
fl=['!']*(x+2)
maps.append(fl)
for ytimes in range(0,y):
    xlist=['!']
    for xtimes in range(0,x):
        xlist.append(' ')
    xlist.append('!')
    maps.append(xlist)
maps.append(fl)

#����
for createbomb in range(0,total):
    radx=random.randint(0,x-1)+1
    rady=random.randint(0,y-1)+1
    maps[rady][radx]='@'

#��ʼ�����ǲ�
layer=[]
layer.append(fl)
for yly in range(0,y):
    ytp=['#']*(x+2)
    layer.append(ytp)  
layer.append(fl)

#���������Χ��������
def cb(cbx,cby):
    bomb=[]
    bomb.append(maps[cby-1][cbx-1])
    bomb.append(maps[cby-1][cbx])
    bomb.append(maps[cby-1][cbx+1])
    bomb.append(maps[cby][cbx-1])
    bomb.append(maps[cby][cbx+1])
    bomb.append(maps[cby+1][cbx-1])
    bomb.append(maps[cby+1][cbx])
    bomb.append(maps[cby+1][cbx+1])
    num=bomb.count('@')
    if num==0:
        maps[cby][cbx]=' '
    elif num!=0:
        maps[cby][cbx]=num

#�����ж���Χ�ո���
def css(csxx,csyy):
    if maps[csyy][csxx]==' 'and layer[csyy][csxx]=='#':
        cslx.append(csxx)
        csly.append(csyy)
    elif maps[csyy][csxx]!=(' ' and '@'):
        layer[csyy][csxx]=maps[csyy][csxx]
    
def cs(csx,csy):
    if maps[csy][csx]==' ' and layer[csy][csx]=='#' :
        css(csx-1,csy)
        css(csx+1,csy)
        css(csx,csy-1)
        css(csx,csy+1) 
        layer[csy][csx]=' '
    elif maps[csy][csx]!=' ':
        layer[csy][csx]=maps[csy][csx]
         
#�����������
def pr(lists):
    print('  ',end='')
    for prxtp in range(0,x):
        print('',str(prxtp).zfill(2),end='')
    print('')
    for prtmy in range(0,y): 
        print(str(prtmy).zfill(2),end=' ')
        for prtmx in range(0,x):
            print(lists[prtmy+1][prtmx+1],end='  ')
        print('')

#�������δ��ɸ���
def cu():
    cus,cul=0,[]
    for cuy in range(1,y+1):
        for cux in range(1,x+1):
            cul.append(layer[cuy][cux])
    cus=cul.count('#')
    print ('��ʣ%d������δ���'%cus)
    return cus
        
#�����ͼ
for chy in range(1,y+1):
    for chx in range(1,x+1):
        if maps[chy][chx]!='@':
            cb(chx,chy) 
        
#������         
pr(maps)        
        
#������    
print('��ӭ����ɨ�����磡\n���ֹ���',total,'����')
    #��ʼ���
pr(layer)

    
    #ѭ��ɨ��
while True:  
    selx=int(input('x?  '))+1
    sely=int(input('y?  '))+1

    #�����ж�
    if maps[sely][selx]=='@':
        print('You lose!')
        layer[sely][selx]='@'
        #������ʾ
        pr(layer)
        sys.exit()    
    
    #������Χ�ո�
    cslx,csly=[],[]
    cs(selx,sely)    
    while len(cslx)!=0:
        cslxi,cslyi=cslx[0],csly[0]
        del cslx[0]
        del csly[0]
        cs(cslxi,cslyi)
    
    #ʤ���ж�
    cus=cu()
    if cus==total:
        print('You win !')
        pr(maps)
        sys.exit() 
    
    #���
    pr(layer)

