# -*- coding: utf-8 -*-
"""
Created on Tue May  5 15:00:26 2020

@author: KutayGONEN
"""
"""
STUDENT NAME: KUTAY GÖNEN
STUDENT ID : 2016502047

----------- C++ TO ASSEMBLY CODE --------------
Please Read The Supporting .pdf File Before Start
Your Assembly File Will be Named As c2assembly_kutay_gonen in both .txt and .asm format

"""


file = open('c2assembly_kutay_gonen.txt','w') #open the file assembly representation of the c file will be written as .txt format

#addf function is the assembly provisions of sum(+) operator
def addf(a,b):
    file.write('MOV.W #{ilk} 4(R1)\nMOV.W #{iki},2(R1)\nMOV.W 4(R1),R12\nADD.W 2(R1),R12\nMOV.W R12,@R1\n' .format(ilk=a,iki=b))
    
#subf function is the assembly provisions of subtract(-) operator    
def subf(a,b):
        file.write('MOV.W #{ilk} 4(R1)\nMOV.W #{iki},2(R1)\nMOV.W 4(R1),R12\nSUB.W 2(R1),R12\nMOV.W R12,@R1\n' .format(ilk=a,iki=b))
        
#mulf function is the assembly provisions of multiplication(*) operator        
def mulf(a,b):
        file.write('MOV.W #{ilk} 4(R1)\nMOV.W #{iki},2(R1)\nMOV.W 2(R1),R13\nMOV.W 4(R1), R12\nCALL #__mspabi_mpyi\nMOV.W R12,@R1\n' .format(ilk=a,iki=b))
        
#andf function is the assembly provisions of and(&&) operator     
def andf(a,b):
        file.write('\n\tMOV.W   #{ilk}, 4(R1)\n\n\tMOV.W   #{iki}, 2(R1)\n\tCMP.W   #0, 4(R1)\nJEQ       .L2\n\tCMP.W   #0, 2(R1)\nJEQ       .L2\n\tMOV.B   #1, R12\n\tBR      #.L3\n.L2:\n\tMOV.B   #0, R12\n.L3:\n\tMOV.W   R12, @R1' .format(ilk=a,iki=b))

#orf function is the assembly provisions of or(||) operator           
def orf(a,b):
        file.write('\n\tMOV.W   #{ilk}, 4(R1)\n\tMOV.W   #{iki}, 2(R1)\n\tCMP.W   #0, 4(R1)\nJNE       .L2\n\tCMP.W   #0, 2(R1)\nJEQ       .L3\n.L2:\n\tMOV.B   #1, R12\n\tBR      #.L4\n.L3:\n\tMOV.B   #0, R12\n.L4:\n\tMOV.W   R12, @R1' .format(ilk=a,iki=b))
 
#xorf function is the assembly provisions of exor(^) operator          
def xorf(a,b):
        file.write('\nMOV.W   #{ilk}, 4(R1)\nMOV.W   #{iki}, 2(R1)\nMOV.W   4(R1), R12\nXOR.W   2(R1), R12\nMOV.W   R12, @R1\nMOV.B   #0, R12\n' .format(ilk=a,iki=b))
'''
#greater function is the assembly provisions of greater(>) operator         
def greater(a,b):
        file.write('\n\tMOV.W   #{ilk}}, 4(R1)\n\tMOV.W   #{iki}, 2(R1)\n\tMOV.B   #1, R12\n\tCMP.W   4(R1), 2(R1) { JL     .L2\n\tMOV.B   #0, R12\n.L2:\n\tAND     #0xff, R12\n\tMOV.W   R12, @R1' .format(ilk=a,iki=b))

#smaller function is the assembly provisions of smaller(<) operator 
def smaller(a,b):
        file.write('\n\tMOV.W   #{ilk}, 4(R1)\n\tMOV.W   #{iki}, 2(R1)\n\tMOV.B   #1, R12\n\tCMP.W   2(R1), 4(R1) { JL     .L2\n\tMOV.B   #0, R12\n.L2:\n\tAND     #0xff, R12\n\tMOV.W   R12, @R1\n' .format(ilk=a,iki=b))
   
#greatequal function is the assembly provisions of greater or equal(>=) operator      
def greatequal(a,b):
        file.write('\n\tMOV.W   #{ilk}, 4(R1)\n\tMOV.W   #{iki}, 2(R1)\n\tMOV.B   #1, R12\n\tCMP.W   2(R1), 4(R1) { JGE    .L2\n\tMOV.B   #0, R12\n.L2:\n\tAND     #0xff, R12\n\tMOV.W   R12, @R1\n' .format(ilk=a,iki=b))
        
#smallequal function is the assembly provisions of smaller or equal(<=) operator
def smallequal(a,b):
        file.write('\n\tMOV.W   #{ilk}}, 4(R1)\n\tMOV.W   #{iki}, 2(R1)\n\tMOV.B   #1, R12\n\tCMP.W   4(R1), 2(R1) { JGE    .L2\n\tMOV.B   #0, R12\n.L2:\n\tAND     #0xff, R12\n\tMOV.W   R12, @R1' .format(ilk=a,iki=b))

#equall function is the assembly provisions of the equality(==) operator        
def equall(a,b):
        file.write('\n\tMOV.W   #{ilk}, 4(R1)\n\tMOV.W   #{iki}, 2(R1)\n\tMOV.B   #1, R12\n\tCMP.W   2(R1), 4(R1) { JEQ    .L2\n\tMOV.B   #0, R12\n.L2:\n\tAND     #0xff, R12\n\tMOV.W   R12, @R1' .format(ilk=a,iki=b))
'''
#loop function is the assembly provisions of the for loop in c language
def loopfunction(a,b,c):
    if c == '+':
        file.write('\nMOV.W   #{ilk}, @R1\nBR      #.L2\n.L3:\n\tADD.W   #1, @R1\n.L2:'.format(ilk=a))
    else:
        file.write('\nMOV.W   #{ilk}, @R1\nBR      #.L2\n.L3:\n\tADD.W   #-1, @R1\n.L2:'.format(ilk=a))
        
#forse function is the smaller or equal(<=) for provision for loopfunction       
def forse(a,b,c):
    loopfunction(a,b,c)
    file.write('\n\tMOV.W   #{iki}, R12\n\tCMP.W   @R1, R12 \n\tJGE        .L3\n\tMOV.B   #0, R12'.format(iki=b))
    
#forge function is the greater(>=) or equal for provision for loopfunction   
def forge(a,b,c):
    loopfunction(a,b,c)
    file.write('\n\tMOV.W   #{iki}, R12\n\tCMP.W   @R1, R12 \n\tJL .L3\n\tMOV.B   #0, R12'.format(iki=(b-1)))
    
#forgr function is the greater(>) for provision for loopfunction   
def forgr(a,b,c):
    loopfunction(a,b,c)
    file.write('\n\tMOV.W   #{iki}, R12\n\tCMP.W   @R1, R12 \n\tJL .L3\n\tMOV.B   #0, R12'.format(iki=b))
    
#forsm function is the smaller(<) for provision for loopfunction   
def forsm(a,b,c):
    loopfunction(a,b,c)
    file.write('\n\tMOV.W   #{iki}, R12\n\tCMP.W   @R1, R12 \n\tJGE        .L3\n\tMOV.B   #0, R12'.format(iki=(b-1)))
    
        

lol = [] #list of list to keep the readed files string char. by char.

x = input('Please enter the file name with extension (like as myfile.cpp or myfile.c etc.)') #get c file name to be translated
rfile = open('{girilendosya}'.format(girilendosya=x),'r') #open the c file in read operation to translate

file.write('_main:\nSUB.W   #6, R1\n') #first line written in assembly representation R1 = SP (int main() -->)

for m in range(200): #c file's length must be smaller than 200 line
    if rfile.readline == '\n': #read untill see \n
        break
    else:
        lol.append(rfile.readline()) #write the readed lines in to the list
        
stringfile=str(lol) #convert list to a string
# print(rfile.tell()) #for debugger
rfile.seek(0) #return the begining
# print(rfile.tell()) #for debugger

while 1: # in a infinity loop
    
    #CONVERT ADD
    for a in range(len(lol)-1):
        for b in range(len(lol[a])):
            if lol[a][b] == '+' :
                addf(lol[a][b-1],lol[a][b+1])
                break

    #CONVERT SUBTRACT
    for a in range(len(lol)-1):
        for b in range(len(lol[a])):
            if lol[a][b] == '-' :
                subf(lol[a][b-1],lol[a][b+1])
                break    
        
    #CONVERT MULTIPLICATION
    for a in range(len(lol)-1):
        for b in range(len(lol[a])):
            if lol[a][b] == '*' :
                mulf(lol[a][b-1],lol[a][b+1])
                break
            
    #CONVERT AND
    for a in range(len(lol)-1):
        for b in range(len(lol[a])):
            if lol[a][b] == '&' and lol[a][b+1] == '&' :
                andf(lol[a][b-1],lol[a][b+2])
                break 
    #CONVERT OR
    for a in range(len(lol)-1):
        for b in range(len(lol[a])):
            if lol[a][b] == '|' and lol[a][b+1] == '|' :
                orf(lol[a][b-1],lol[a][b+2])
                break 
    #CONVERT XOR
    for a in range(len(lol)-1):
        for b in range(len(lol[a])):
            if lol[a][b] == '^' :
                xorf(lol[a][b-1],lol[a][b+1])
                break
            
            
    #CONVERT FOR LOOP 
    for a in range(len(lol)-1):
        for b in range(len(lol[a])):
            if lol[a][b] == 'f' and lol[a][b+1] == 'o' and lol[a][b+2] == 'r' :
                if lol[a][b+11] !=';': # if x = 10,11,12........
                    jf=[lol[a][b+10] , lol[a][b+11]] #for join function
                    intnumber = int(''.join(jf)) #create the integer number comes after operator
                    
                    
                    if lol[a][b+14] == '<' and lol[a][b+15] == '=':
                        if lol[a][b+17] != ';':
                            rangeofx=[lol[a][b+16] , lol[a][b+17]]
                            forse(intnumber, int(''.join(rangeofx)), lol[a][b+20])
                        else:
                            forse(intnumber,int(lol[a][b+17]),lol[a][b+20])
                    elif lol[a][b+14] == '>' and lol[a][b+15] == '=':
                        if lol[a][b+17] != ';':
                            rangeofx=[lol[a][b+16] , lol[a][b+17]]
                            forge(intnumber, int(''.join(rangeofx)), lol[a][b+20])
                        else:
                            forge(intnumber, int(lol[a][b+15]), lol[a][b+20])
                            
                            
                    elif lol[a][b+14] == '>' and lol[a][b+15] != '=':
                        if lol[a][b+16] != ';':
                            rangeofx=[lol[a][b+15] , lol[a][b+16]]
                            forgr(intnumber,int(''.join(rangeofx)), lol[a][b+20])
                        else:
                            forgr(intnumber,int(lol[a][b+15]), lol[a][b+20]) 
                    elif lol[a][b+14] == '<' and lol[a][b+15] != '=':
                        if lol[a][b+16] != ';':                            
                            rangeofx=[lol[a][b+15] , lol[a][b+16]]
                            forsm(intnumber,int(''.join(rangeofx)), lol[a][b+20])
                        else:
                            forsm(intnumber,int(lol[a][b+15]), lol[a][b+20])
                            
                            
                else:#if x =0,1,2,3,4...9
                    intnumber=lol[a][b+10]
                    if lol[a][b+13] == '<' and lol[a][b+14] == '=':
                        if lol[a][b+16] != ';':
                            rangeofx=[lol[a][b+15] , lol[a][b+16]]
                            forse(intnumber, int(''.join(rangeofx)), lol[a][b+19])
                        else:
                            forse(intnumber,int(lol[a][b+15]),lol[a][b+19])
                    elif lol[a][b+13] == '>' and lol[a][b+14] == '=':
                        if lol[a][b+16] != ';':
                            rangeofx=[lol[a][b+15] , lol[a][b+16]]
                            forge(intnumber,int( ''.join(rangeofx)), lol[a][b+19])
                        else:
                            forge(intnumber, int(lol[a][b+15]), lol[a][b+19])
                            
                    elif lol[a][b+13] == '>' and lol[a][b+14] != '=':
                        if lol[a][b+15] != ';':
                            rangeofx=[lol[a][b+14] , lol[a][b+15]]
                            forgr(intnumber,int(''.join(rangeofx)), lol[a][b+19])
                        else:
                            forgr(intnumber,int(lol[a][b+14]), lol[a][b+19]) 
                    elif lol[a][b+13] == '<' and lol[a][b+14] != '=':
                        if lol[a][b+15] != ';':                            
                            rangeofx=[lol[a][b+14] , lol[a][b+15]]
                            forsm(intnumber,int(''.join(rangeofx)), lol[a][b+19])
                        else:
                            forsm(intnumber,int(lol[a][b+14]), lol[a][b+19])                                              
    break

#Here it is tried to convert if-else and else if statements but its not succesfull
# #CONVERT IF STATEMENTS
#     for a in range(len(lol)-1):
#         for b in range(len(lol[a])):
#             if lol[a][b] == 'i' and lol[a][b+1] == 'f' :
#                 if lol[a][b+4] == '&' and lol[a][b+5] == '&':
#                     and_if(lol[a][b+3],lol[a][b+6])
#                 if lol[a][b+4] == '|' and lol[a][b+5] == '|':
#                     or_if(lol[a][b+3],lol[a][b+6])
#                 if lol[a][b+4] == '^':
#                     xor_if(lol[a][b+3],lol[a][b+6])
#               #if 'else if' in stringfile:
#                 break             
            
file.write('\nADD.W   #6, R1\nRET\n') #end of file for assembly code R1=SP
rfile.close()
file.close()

fileoffile=open('c2assembly_kutay_gonen.txt' ,'r') #open the .txt file to convert it to .asm file
fileoffile2=open('c2assembly_kutay_gonen.asm','w') #.asm file for assembly compilers

addtoasm=[] #list of list to keep readed values from .txt form

for m in range(200):
    if fileoffile.readline == '\n':
        break
    else:
        addtoasm.append(fileoffile.readline())

for m in range(200):
        addtoasm.append(fileoffile.readline())
        fileoffile2.write(addtoasm[m]) #write each ine to .asm format

fileoffile.close()
fileoffile2.close()
