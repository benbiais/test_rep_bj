tfile = open("/sys/bus/w1/devices/28-00000485fa13/w&_slave")
text = tfile.read()
tfile.close()
print (text)
secondline = text.split("\n")[1]
print (secondline)
tdata = secondline.split(" ")[9]
print (tdata)
temperature = float(tdata[2:])
print (temperature)
temp = temperature / 1000
print temp




       
