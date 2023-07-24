#ecall and ebreak need space
def encode(string):
    global binarr
    ty=0
    to_array=[]
    for letter in string:
        to_array.append(letter)
    
    l=len(to_array)
    i=0
    ins=str()

    while(to_array[i]!=' '):
        ins = ins + (to_array[i])
        i=i+1
    
    ty=decide(ins)

    if ty==0:
        binarr=['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','0','0','1','1']

    elif ty==0.1:
        binarr=['0','0','0','0','0','0','0','0','0','0','0','1','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','0','0','1','1']

    elif (ty==1 or ty==2 or ty==3):
        while(to_array[i]!='x'):
            i=i+1

        rd=str()
        i=i+1

        while(to_array[i]!=','):
            rd=rd+(to_array[i])
            i=i+1

        rd = int(rd)

        while(to_array[i]!='x'):
            i=i+1

        rs1=str()
        i=i+1

        while(to_array[i]!=','):
            rs1=rs1+(to_array[i])
            i=i+1

        rs1 = int(rs1)

        if ty==1:
            while(to_array[i]!='x'):
                i=i+1
        
        rs2=str()
        i=i+1

        while(i<l):
            rs2=rs2+(to_array[i])
            i=i+1

        rs2 = int(rs2)

        if (ty==1 or ty==2):
            rest(rd,rs1)
            resta(rs2)
        elif ty==3:
            rest(rd,rs1)
            restb(rs2)


    elif (ty==4):
        while(to_array[i]!='x'):
            i=i+1

        rd=str()
        i=i+1

        while(to_array[i]!=','):
            rd=rd+(to_array[i])
            i=i+1

        rd = int(rd)

        rs2=str()
        i=i+1

        while(to_array[i]!='('):
            rs2=rs2+(to_array[i])
            i=i+1

        rs2 = int(rs2)

        while(to_array[i]!='x'):
            i=i+1

        rs1=str()
        i=i+1

        while(to_array[i]!=')'):
            rs1=rs1+(to_array[i])
            i=i+1

        rs1 = int(rs1)

        
        rest(rd,rs1)
        restb(rs2) 
    

    elif (ty==5 or ty==6):
        while(to_array[i]!='x'):
            i=i+1

        rd=str()
        i=i+1

        while(to_array[i]!=','):
            rd=rd+(to_array[i])
            i=i+1

        rd = int(rd)

        rs2=str()
        i=i+1

        while(to_array[i]!=','):
            rs2=rs2+(to_array[i])
            i=i+1

        rs2 = int(rs2)

        if ty==5:
            while(to_array[i]!='x'):
                i=i+1
        

        rs1=str()
        i=i+1

        while(i<l):
            rs1=rs1+(to_array[i])
            i=i+1

        rs1 = int(rs1)

        
        rest(rd,rs1)
        restb(rs2) 






def decide(ins):

    if (ins=="add"):
        v="000"
        las="0110011"
        fir="0000000"
        fill(v,las)
        fillf(fir)
        ty=1

    elif(ins=="sub"):
        v="000"
        las="0110011"
        fir="0100000"
        fill(v,las)
        fillf(fir)
        ty=1

    elif(ins=="sll"):
        v="001"
        las="0110011"
        fir="0000000"
        fill(v,las)
        fillf(fir)
        ty=1

    elif(ins=="slt"):
        v="010"
        las="0110011"
        fir="0000000"
        fill(v,las)
        fillf(fir)
        ty=1

    elif(ins=="sltu"):
        v="011"
        las="0110011"
        fir="0000000"
        fill(v,las)
        fillf(fir)
        ty=1

    elif(ins=="xor"):
        v="100"
        las="0110011"
        fir="0000000"
        fill(v,las)
        fillf(fir)
        ty=1

    elif(ins=="srl"):
        v="101"
        las="0110011"
        fir="0000000"
        fill(v,las)
        fillf(fir)
        ty=1

    elif(ins=="sra"):
        v="101"
        las="0110011"
        fir="0100000"
        fill(v,las)
        fillf(fir)
        ty=1

    elif(ins=="or"):
        v="110"
        las="0110011"
        fir="0000000"
        fill(v,las)
        fillf(fir)
        ty=1

    elif(ins=="and"):
        v="111"
        las="0110011"
        fir="0000000"
        fill(v,las)
        fillf(fir)
        ty=1

    elif(ins=="slli"):
        v="001"
        las="0010011"
        fir="0000000"
        fill(v,las)
        fillf(fir)
        ty=2    

    elif(ins=="srli"):
        v="101"
        las="0010011"
        fir="0000000"
        fill(v,las)
        fillf(fir)
        ty=2

    elif(ins=="srai"):
        v="101"
        las="0010011"
        fir="0100000"
        fill(v,las)
        fillf(fir)
        ty=2

    elif(ins=="addi"):
        v="000"
        las="0010011"
        fill(v,las)
        ty=3

    elif(ins=="slti"):
        v="010"
        las="0010011"
        fill(v,las)
        ty=3

    elif(ins=="sltiu"):
        v="011"
        las="0010011"
        fill(v,las)
        ty=3
    
    elif(ins=="xori"):
        v="100"
        las="0010011"
        fill(v,las)
        ty=3

    elif(ins=="ori"):
        v="110"
        las="0010011"
        fill(v,las)
        ty=3

    elif(ins=="andi"):
        v="111"
        las="0010011"
        fill(v,las)
        ty=3

    elif(ins=="lb"):
        v="000"
        las="0000011"
        fill(v,las)
        ty=4
    
    elif(ins=="lh"):
        v="001"
        las="0000011"
        fill(v,las)
        ty=4

    elif(ins=="lw"):
        v="010"
        las="0000011"
        fill(v,las)
        ty=4

    elif(ins=="lbu"):
        v="100"
        las="0000011"
        fill(v,las)
        ty=4

    elif(ins=="lhu"):
        v="101"
        las="0000011"
        fill(v,las)
        ty=4

    elif(ins=="jalr"):
        v="000"
        las="1100111"
        fill(v,las)
        ty=4

    elif(ins=="csrrw"):
        v="001"
        las="1110011"
        fill(v,las)
        ty=5

    elif(ins=="csrrs"):
        v="010"
        las="1110011"
        fill(v,las)
        ty=5

    elif(ins=="csrrc"):
        v="011"
        las="1110011"
        fill(v,las)
        ty=5
    
    elif(ins=="csrrwi"):
        v="101"
        las="1110011"
        fill(v,las)
        ty=6

    elif(ins=="csrrsi"):
        v="110"
        las="1110011"
        fill(v,las)
        ty=6

    elif(ins=="csrrci"):
        v="111"
        las="1110011"
        fill(v,las)
        ty=6

    elif(ins=="ecall"):
        ty=0
    elif(ins=="ebreak"):
        ty=0.1


    return ty

def decimalToBinary5(n):
    f=bin(n).replace("0b","")
    le=len(f)
    j=0
    ex=0
    if(le<5):
        ex=5-le
    while(j<ex):
        f="0"+f
        j=j+1
    
    return f

def decimalToBinary12(n):
    f=bin(n).replace("0b","")
    le=len(f)
    j=0
    ex=0
    if(le<12):
        ex=12-le
    while(j<ex):
        f="0"+f
        j=j+1
    
    return f

def fill(v,las):
    global binarr
    j=0
    for i in range(17,20):
        binarr[i]=v[j]
        j=j+1
    
    j=0
    for i in range(25,32):
        binarr[i]=las[j]
        j=j+1
    
def fillf(fir):
    j=0
    for i in range(0,7):
        binarr[i]=fir[j]
        j=j+1

def rest(rd,rs1):
    a=decimalToBinary5(rd)
    b=decimalToBinary5(rs1)
    global binarr

    j=0
    for i in range(12,17):
        binarr[i]=b[j]
        j=j+1

    j=0
    for i in range(20,25):
        binarr[i]=a[j]
        j=j+1

def resta(rs2):
    global binarr
    c=decimalToBinary5(rs2)
        
    j=0
    for i in range(7,12):
        binarr[i]=c[j]
        j=j+1

def restb(rs2):
    global binarr
    c=decimalToBinary12(rs2)
        
    j=0
    for i in range(0,12):
        binarr[i]=c[j]
        j=j+1
    
binarr=[]
binarr = [None]*32
string = "ecall "
encode(string)
print(binarr)
a=""
for k in binarr:
    a=a+k
print(a)