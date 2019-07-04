
#Get System Realted Information
import SystemInfo
s1=SystemInfo.SystemInfo()
result=s1.GetSystemInfo()
print('\n{0:-^80s}\n'.format('Operating System Information'))
for key,value in result.items():
    print('{}\t:\t{}'.format(key,value))


#Network Information
import NetworkInfo
print('\n\n{0:-^80s}'.format('Network Related Information'))
n1=NetworkInfo.NetworkInfo()
for i in n1.networkinfo():
    name="\n\n{0:*^80s}".format(i['name'])
    print(name)
    for values in i['details']:
        val=list(values.items())[0]
        print('{}\t:\t{}'.format(val[0],val[1]))


