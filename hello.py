def rdv():
    j=0
    rdreg=0
    for i in range (24,19,-1):
        if arr[i]==0:
            j=j+1
        elif arr[i]==1:
            rdreg=rdreg+2**j
            j=j+1
    return rdreg

def rs1v():
    j=0
    rs1reg=0
    for i in range (16,11,-1):
        if arr[i]==0:
            j=j+1
        elif arr[i]==1:
            rs1reg=rs1reg+2**j
            j=j+1
    return rs1reg

def rs2v():
    j=0
    rs2reg=0
    for i in range (11,6,-1):
        if arr[i]==0:
            j=j+1
        elif arr[i]==1:
            rs2reg=rs2reg+2**j
            j=j+1
    return rs2reg

def immv():
    j=0
    imm=0
    for i in range (11,-1,-1):
        if arr[i]==0:
            j=j+1
        elif arr[i]==1:
            imm=imm+2**j
            j=j+1
    return imm


opcode =str()
rrd=str()
sta=str()
ec=str()
string = "00000000000000000000000001110011"

arr=[]
for letter in string:
    arr.append(int(letter))

# arr=[0,1,0,0,0,0,0,0,1,0,1,1,0,1,0,1,0,0,0,0,0,1,0,1,1,0,1,1,0,0,1,1]
#arr1=[0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,1,1,0,1,0,0,0,0,1,1,0,1,1,0,0,1,1]
#print(arr1)
for i in range (25,32):
    opcode=opcode+str(arr[i])

for i in range (17,20):
    rrd=rrd+str(arr[i])

for i in range (0,7):
    sta=sta+str(arr[i])


match opcode:
    case "1100111":
        if rrd=="000":
            imm=immv()
            rs1=rs1v()
            rd=rdv()
            print("jalr\t"+"0x"+str(rd)+","+str(imm)+"(0x"+str(rs1)+")\n")
            

    case "0000011":
        imm=immv()
        rs1=rs1v()
        rd=rdv()
        match rrd:
            case "000":
                print("lbr\t"+"0x"+str(rd)+","+str(imm)+"(0x"+str(rs1)+")\n")
            case "001":
                print("lh\t"+"0x"+str(rd)+","+str(imm)+"(0x"+str(rs1)+")\n")
            case "010":
                print("lw\t"+"0x"+str(rd)+","+str(imm)+"(0x"+str(rs1)+")\n")
            case "100":
                print("lbu\t"+"0x"+str(rd)+","+str(imm)+"(0x"+str(rs1)+")\n")
            case "101":
                print("lhu\t"+"0x"+str(rd)+","+str(imm)+"(0x"+str(rs1)+")\n")
            case _:
                print("wrong")
    
    case "0010011":
        imm=immv()
        rs1=rs1v()
        rd=rdv()
        match rrd:
            case "000":
                print("addi\t"+"0x"+str(rd)+","+"0x"+str(rs1)+","+str(imm)+"\n")
            case "010":
                print("slti\t"+"0x"+str(rd)+","+"0x"+str(rs1)+","+str(imm)+"\n")
            case "011":
                print("sltiu\t"+"0x"+str(rd)+","+"0x"+str(rs1)+","+str(imm)+"\n")
            case "100":
                print("xori\t"+"0x"+str(rd)+","+"0x"+str(rs1)+","+str(imm)+"\n")
            case "110":
                print("ori\t"+"0x"+str(rd)+","+"0x"+str(rs1)+","+str(imm)+"\n")
            case "111":
                print("andi\t"+"0x"+str(rd)+","+"0x"+str(rs1)+","+str(imm)+"\n")
            case "001":
                if sta=="0000000":
                    shamt=rs2v()
                    print("slli\t"+"0x"+str(rd)+","+"0x"+str(rs1)+","+str(shamt)+"\n")
                else:
                    print("wrong")
            case "101":
                if sta=="0000000":
                    shamt=rs2v()
                    print("srli\t"+"0x"+str(rd)+","+"0x"+str(rs1)+","+str(shamt)+"\n")
                elif sta=="0100000":
                    shamt=rs2v()
                    print("srai\t"+"0x"+str(rd)+","+"0x"+str(rs1)+","+str(shamt)+"\n")
                else:
                    print("wrong")
            case _:
                print("wrong")
    
    case "1110011":
        imm=immv()
        rs1=rs1v()
        rd=rdv()
        for i in range (0,12):
            ec=ec+str(arr[i])
        match rrd:
            case "000":
                if ec=="000000000000":
                    print("ecall")
                elif ec=="000000000001":
                    print("ebreak")
                else:
                    print("wrong")
            case "001":
                print("csrrw\t0x"+str(rd)+","+str(imm)+",0x"+str(rs1)+"\n")
            case "010":
                print("csrrs\t0x"+str(rd)+","+str(imm)+",0x"+str(rs1)+"\n")
            case "011":
                print("csrrc\t0x"+str(rd)+","+str(imm)+",0x"+str(rs1)+"\n")
            case "101":
                print("csrrwi\t0x"+str(rd)+","+str(imm)+","+str(rs1)+"\n")
            case "110":
                print("csrrsi\t0x"+str(rd)+","+str(imm)+","+str(rs1)+"\n")
            case "111":
                print("csrrci\t0x"+str(rd)+","+str(imm)+","+str(rs1)+"\n")
            case _:
                print("wrong again")            
    case "0110011":
        rs2=rs2v()
        rs1=rs1v()
        rd=rdv()
        match rrd,sta:
            case "000","0000000":
                print("add\t0x"+str(rd)+",0x"+str(rs1)+",0x"+str(rs2)+"\n")
            case "000","0100000":
                print("sub\t0x"+str(rd)+",0x"+str(rs1)+",0x"+str(rs2)+"\n")
            case "001","0000000":
                print("sll\t0x"+str(rd)+",0x"+str(rs1)+",0x"+str(rs2)+"\n")
            case "010","0000000":
                print("slt\t0x"+str(rd)+",0x"+str(rs1)+",0x"+str(rs2)+"\n")
            case "011","0000000":
                print("sltu\t0x"+str(rd)+",0x"+str(rs1)+",0x"+str(rs2)+"\n")
            case "100","0000000":
                print("xor\t0x"+str(rd)+",0x"+str(rs1)+",0x"+str(rs2)+"\n")
            case "101","0000000":
                print("srl\t0x"+str(rd)+",0x"+str(rs1)+",0x"+str(rs2)+"\n")
            case "101","0100000":
                print("sra\t0x"+str(rd)+",0x"+str(rs1)+",0x"+str(rs2)+"\n")
            case "110","0000000":
                print("or\t0x"+str(rd)+",0x"+str(rs1)+",0x"+str(rs2)+"\n")
            case "111","0000000":
                print("and\t0x"+str(rd)+",0x"+str(rs1)+",0x"+str(rs2)+"\n")
            case _:
                print("wroong")
    case _:
        print("enter correct")


    