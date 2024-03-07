#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
os.system('pause')
import serial
import time
ser = serial.Serial('COM5', 9600)
f=open("C:/Users/PC/Desktop/smart_attendance/attendance.h","w")
N=int(input('사용자수를 입력해주세요 : '))
f.write("#define N")
f.write(" ")
f.write(str (N))
f.write("\n")
if ser.readable():
    for n in range(1,N+1):
        val = ser.readline()
        globals()['USER%d' % n] = val.decode()[:len(val)-1].rstrip()
        globals()['USER%d' % n]='"'+globals()['USER%d' % n].lstrip()+'"'
        f.write("#define USER")
        f.write(str(n))
        f.write(" ")
        f.write(globals()['USER%d' % n])
        f.write('\n')
        name=input("%d번 사용자 이름을 입력하세요 :" %n)
        f.write("#define USERNAME")
        f.write(str(n))
        f.write(' "')
        f.write(name)
        f.write('"\n')
        num=input("%d번 사용자 학번을 입력하세요 :" %n)
        f.write("#define USERNUM")
        f.write(str(n))
        f.write(' "')
        f.write(num)
        f.write('"\n')
f.write("String Name_arr[N+1]={")    
for n in range(1,N+1) :
    f.write("USERNAME")
    f.write(str(n))
    f.write(', ')
f.write('"Not User"};\n')
f.write("String Num_arr[N+1]={")
for n in range(1,N+1) :
    f.write("USERNUM")
    f.write(str(n))
    f.write(', ')
f.write('"0"};\n')
f.write("int Log_arr[N]={")
for n in range(1,N) :
    f.write("0,")
f.write("0};\n")
f.close()
f=open("C:/Users/PC/Desktop/smart_attendance/codemake.h","w")
f.write("#ifndef abcd\n#include <MFRC522.h>\n#endif\n")
for n in range(2,N+1):
    f.write("\telse if (content.substring(1) == U(USER,")
    f.write(str(n))
    f.write("))\n\t{\n\t")
    f.write("student_name = Name_arr[")
    f.write(str(n-1))
    f.write("];\n\t")
    f.write("num = Num_arr[")
    f.write(str(n-1))
    f.write("];\n\tif(Log_arr[")
    f.write(str(n-1))
    f.write(']){\n\t\tlog_data = "LOG OUT";\n\t\tLog_arr[')
    f.write(str(n-1))
    f.write(']=0;\n\t}\n\telse{\n\t\tlog_data = "LOG IN";\n\t\tLog_arr[')
    f.write(str(n-1))
    f.write(']=1;\n\t}')
    f.write("\n\t")
    f.write('Serial.print("DATA,TIME, ");\n\tSerial.print(student_name);\n\tSerial.print(",");\n\tSerial.print(num);\n\t')
    f.write('Serial.print(",");\n\tSerial.print(log_data);\n\tSerial.print(",");\n\tbuffer = Serial.available();\n\tSerial.println(buffer);\n\tdelay(300);\n\t')
    f.write('if(buffer == 64) Serial.println(Serial.peek());\n\tlcd.setCursor(0,0);\n\tlcd.print(Name_arr[')
    f.write(str(n-1))
    f.write("]);\n\t")
    f.write('lcd.setCursor(0,1);\n\tlcd.print(log_data);\n\tdigitalWrite(LED_GREEN, HIGH);\n\ttone(BUZZER, 500);\n\tdelay(300);\n\t')
    f.write("noTone(BUZZER);\n\tdelay(3000);\n\tdigitalWrite(LED_GREEN, LOW);\n\tlcd.clear();\n\t}\n")
f.close()


# In[ ]:




