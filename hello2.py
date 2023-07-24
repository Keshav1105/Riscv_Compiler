string = "slt     0x3,0x23,0x10"

to_array=[]


for letter in string:
    to_array.append(letter)

print(to_array)
l=len(to_array)
print(l)
i=0
ins=str()

while(to_array[i]!=' '):
    ins = ins + (to_array[i])
    i=i+1

print(ins)

while(to_array[i]!='x'):
    i=i+1
print(i)

rd=str()
i=i+1

while(to_array[i]!=','):
    rd=rd+(to_array[i])
    i=i+1

rd = int(rd)
print(rd)

while(to_array[i]!='x'):
    i=i+1
print(i)

rs1=str()
i=i+1

while(to_array[i]!=','):
    rs1=rs1+(to_array[i])
    i=i+1

rs1 = int(rs1)
print(rs1)

while(to_array[i]!='x'):
    i=i+1
print(i)

rs2=str()
i=i+1

while(i<l):
    rs2=rs2+(to_array[i])
    i=i+1

rs2 = int(rs2)
print(rs2)

def decimalToBinary(n):
    f=bin(n).replace("0b","")
    le=len(f)
    j=0
    ex=0
    if(le<5):
        ex=5-le
        print(ex)
    while(j<ex):
        f="0"+f
        j=j+1
    
    return f
f=decimalToBinary(3)
print(f)
le=len(f)

print(f)

a=decimalToBinary(rd)
b=decimalToBinary(rs1)
c=decimalToBinary(rs2)

d="0000000"+c+b+"010"+a+"0110011"
print(d)
print(len(d))
