tfile = open("/sys/bus/w1/devices/28-00000485fa13/w&_slave")
text = tfile.read()
tfile.close()
print (text)



       
