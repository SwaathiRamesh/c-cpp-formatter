lines = tuple(open('get.c', 'r'))
#print len(lines)
i=0
for item in lines:
            pa=str(item).strip()
            if(i==0):
                    if(len(pa)>=1 and pa[0]=='#'):
                            i=1
            else:
                    #print('Trying for -'+pa+'-'+str(len(pa)))
                    if len(pa)>=1:
                            if pa[0]=='#':
                                    print pa
                    if pa =='{' or pa =='}':
                            print pa
                    elif (len(pa)>=1 and pa[0] !='#') :
                            print('    '+pa)
