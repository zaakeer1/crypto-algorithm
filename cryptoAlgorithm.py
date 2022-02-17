ctable_list =  []
ctable_list.append(["63","7c","77","7b","f2","6b","6f","c5","30","01","67","2b","fe","d7","ab","76"])
ctable_list.append(["ca","82","c9","7d","fa","59","47","f0","ad","d4","a2","af","9c","a4","72","c0"])
ctable_list.append(["b7","fd","93","26","36","3f","f7","cc","34","a5","e5","f1","71","d8","31","15"])
ctable_list.append(["04","c7","23","c3","18","96","05","9a","07","12","80","e2","eb","27","b2","75"])
ctable_list.append(["09","83","2c","1a","1b","6e","5a","a0","52","3b","d6","b3","29","e3","2f","84"])
ctable_list.append(["53","d1","00","ed","20","fc","b1","5b","6a","cb","be","39","4a","4c","58","cf"])
ctable_list.append(["d0","ef","aa","fb","43","4d","33","85","45","f9","02","7f","50","3c","9f","a8"])
ctable_list.append(["51","a3","40","8f","92","9d","38","f5","bc","b6","da","21","10","ff","f3","d2"])
ctable_list.append(["cd","0c","13","ec","5f","97","44","17","c4","a7","7e","3d","64","5d","19","73"])
ctable_list.append(["60","81","4f","dc","22","2a","90","88","46","ee","b8","14","de","5e","0b","db"])
ctable_list.append(["e0","32","3a","0a","49","06","24","5c","c2","d3","ac","62","91","95","e4","79"])
ctable_list.append(["e7","c8","37","6d","8d","d5","4e","a9","6c","56","f4","ea","65","7a","ae","08"])
ctable_list.append(["ba","78","25","2e","1c","a6","b4","c6","e8","dd","74","1f","4b","bd","8b","8a"])
ctable_list.append(["70","3e","b5","66","48","03","f6","0e","61","35","57","b9","86","c1","1d","9e"])
ctable_list.append(["e1","f8","98","11","69","d9","8e","94","9b","1e","87","e9","ce","55","28","df"])
ctable_list.append(["8c","a1","89","0d","bf","e6","42","68","41","99","2d","0f","b0","54","bb","16"])


dtable_list =  []
dtable_list.append(["52","09","6a","d5","30","36","a5","38","bf","40","a3","9e","81","f3","d7","fb"])
dtable_list.append(["7c","e3","39","82","9b","2f","ff","87","34","8e","43","44","c4","de","e9","cb"])
dtable_list.append(["54","7b","94","32","a6","c2","23","3d","ee","4c","95","0b","42","fa","c3","4e"])
dtable_list.append(["08","2e","a1","66","28","d9","24","b2","76","5b","a2","49","6d","8b","d1","25"])
dtable_list.append(["72","f8","f6","64","86","68","98","16","d4","a4","5c","cc","5d","65","b6","92"])
dtable_list.append(["6c","70","48","50","fd","ed","b9","da","5e","15","46","57","a7","8d","9d","84"])
dtable_list.append(["90","d8","ab","00","8c","bc","d3","0a","f7","e4","58","05","b8","b3","45","06"])
dtable_list.append(["d0","2c","1e","8f","ca","3f","0f","02","c1","af","bd","03","01","13","8a","6b"])
dtable_list.append(["3a","91","11","41","4f","67","dc","ea","97","f2","cf","ce","f0","b4","e6","73"])
dtable_list.append(["96","ac","74","22","e7","ad","35","85","e2","f9","37","e8","1c","75","df","6e"])
dtable_list.append(["47","f1","1a","71","1d","29","c5","89","6f","b7","62","0e","aa","18","be","1b"])
dtable_list.append(["fc","56","3e","4b","c6","d2","79","20","9a","db","c0","fe","78","cd","5a","f4"])
dtable_list.append(["1f","dd","a8","33","88","07","c7","31","b1","12","10","59","27","80","ec","5f"])
dtable_list.append(["60","51","7f","a9","19","b5","4a","0d","2d","e5","7a","9f","93","c9","9c","ef"])
dtable_list.append(["a0","e0","3b","4d","ae","2a","f5","b0","c8","eb","bb","3c","83","53","99","61"])
dtable_list.append(["17","2b","04","7e","ba","77","d6","26","e1","69","14","63","55","21","0c","7d"])


def string2bin(string):
    return ''.join(bin(ord(c)) for c in string).replace('b','')



def binaryToDecimal(n):   
    return int(n,2)



def encoder(rawData):
    
    encodedValues = [[0 for i in range(cols)]for j in range(rows)]
    i = 0
    j = 0
    count = 0
    
    while i<4:
        
        letter = rawData[count]
        
        s=string2bin(letter)
        so=s.zfill(8)
        s = so
        
        #print(letter," : ",s)
        
        p1 = s[0:4]
        p2 = s[4:8]
            
        n1 = binaryToDecimal(p1)
        n2 = binaryToDecimal(p2)
        
        
        encodedValues[i][j] = ctable_list[n1][n2]
        
        j += 1
        if j == 4:
            j=0
            i+=1
        count += 1
        
    return encodedValues



def shiftRows(encodedList):
    
    shiftedValues = [[0 for i in range(cols)] for j in range(rows)]    
    
    #shifting line 0
    shiftedValues[0]= encodedList[0]        
    
    
    #shifting line 1
    i=3
    while i > 0:
        shiftedValues[1][i-1] = encodedList[1][i]
        i -= 1
    shiftedValues[1][3] = encodedList[1][0]
    
    
    #shifting line 2
    i=3
    while i > 1:
        shiftedValues[2][i-2] = encodedList[2][i]
        i -= 1
    shiftedValues[2][3] = encodedList[2][1]
    shiftedValues[2][2] = encodedList[2][0]
    
    
    #shifting line 3
    i=0
    while i < 3:
        shiftedValues[3][i+1] = encodedList[3][i]
        i += 1
    shiftedValues[3][0] = encodedList[3][3]
    
    return shiftedValues



def hexToInt(shiftedList):
    
    intList = [[0 for i in range(len(shiftedList))]for j in range(len(shiftedList[0]))]
    
    for i in range(len(shiftedList)):
        for j in range(len(shiftedList[0])):
            intList[i][j] = int(shiftedList[i][j],16)
    
    return intList



def keyEncryption(multipliedList):
    
    encryptedList = [[0 for i in range(len(multipliedList))]for j in range(len(multipliedList[0]))]
    
    s = ""
    key = "12345678abcdefgh"
    count=0
    i=0
    j=0
    
    while count < 16:
        
        kv=ord(key[count])
        encryptedList[i][j] = multipliedList[i][j]^kv
        s += chr(encryptedList[i][j])
        
        j +=1
        if j == 4:
            j=0
            i+=1
        count +=1
        
    
    #print("Encrypted String: ",s)
    
    return encryptedList, s



def keyDecryption(s):
    
    new_list3 = [[0 for i in range(cols)] for j in range(rows)]
    key = "12345678abcdefgh"
    
    count=0
    i=0
    j=0
    
    while count < len(s):
        
        kv = ord(key[count])
        #print(count," : ",ord(s[count]))
        v = ord(s[count])
        new_list3[i][j] = v ^ kv
        
        j +=1
        if j == 4:
            j=0
            i+=1
        count +=1
    
    return new_list3



def intToHex(new_list3):
    
    new_list2 = [[0 for i in range(cols)] for j in range(rows)]
    
    for i in range(len(new_list3)):
        for j in range(len(new_list3[0])):
            temp = hex(new_list3[i][j])
            new_list2[i][j] = temp[2:]
            
    return new_list2



def InverseShiftRows(h):
    
    new_list1 = [[0 for i in range(cols)] for j in range(rows)]
    
    
    #shifting line 0
    new_list1[0] = h[0]
    
    
    #shifting line 1
    i=0
    while i < 3:
        new_list1[1][i+1] = h[1][i]
        i += 1
    new_list1[1][0] = h[1][3]
    
    
    #shifting line 2
    i=3
    while i > 1:
        new_list1[2][i-2] = h[2][i]
        i -= 1
    new_list1[2][3] = h[2][1]
    new_list1[2][2] = h[2][0]
    
    
    #shifting line 3
    i=3
    while i > 0:
        new_list1[3][i-1] = h[3][i]
        i -= 1
    new_list1[3][3] = h[3][0]
    
    
    return new_list1



def decoder(new_list1):
    ascii_string = ""
    new_list2 = new_list1
    
    for i in range(cols):
        # iterate through columns of Y
        for j in range(rows):
            # iterate through rows of Y
            
            
            
            
            # Code to convert hex to binary 
            s = "{0:08b}".format(int(new_list2[i][j], 16)) 
            # Print the resultant string 
            
            p1 = s[0:4]
            p2 = s[4:8]
            
            n1 = binaryToDecimal(p1)
            
            n2 = binaryToDecimal(p2)
            
            new_list1[i][j] = dtable_list[n1][n2]
            #print(new_list1[i][j])
            
            
            # Printing initial string 
            
            # Code to convert hex to binary 
            sf = "{0:08b}".format(int(new_list1[i][j], 16)) 
            # Print the resultant string  
            
            an_integer = int(sf, 2)
            
            ascii_character = chr(an_integer)
            
            ascii_string += ascii_character
    return ascii_string
    

    
rows, cols = 4, 4    

def encrypt(rawData):
    
    encodedList = encoder(rawData)
    
        
    shiftedList = shiftRows(encodedList)
    
    
    intList = hexToInt(shiftedList)
    
    
    encryptedList, cypherText = keyEncryption(intList)
        
    
    return cypherText



def decrypt(cypherText):
    
    decryptedList = keyDecryption(cypherText)
    
        
    hexMatrix = intToHex(decryptedList)
    
    
    inverseShiftedMatrix = InverseShiftRows(hexMatrix)
    
    
    decodedString = decoder(inverseShiftedMatrix)
    
   
    return decodedString


#inputText = ""           #If we want to give the text directly as string

with open('IWannaGoHome.txt') as f:
    lines = f.read()
    
inputText = lines
cypherText = ""
decodedText = ""

i = 0
l = len(inputText)
while i < l:
    
    j = i+16
    if j < l:
        temp = inputText[i:j]
    else:
        temp = inputText[i:l]
        temp = "{:<16}".format(temp)
    i += 16
    
    inputString = temp
    

    
    cypherString = encrypt(inputString)
    cypherText += cypherString
    
print("inputText:")
print(inputText)
print("input length",len(inputText),end='\n\n')
print("cypherText:")
print(cypherText)
print("cypher length",len(cypherText),end='\n\n')

i = 0
l = len(cypherText)
while i < l:
    j = i+16
    if j <= l:
        temp = cypherText[i:j]
    
    i += 16
    cypherString = temp
    decodedString = decrypt(cypherString)
    decodedText += decodedString
    
print("decodedText:")
print(decodedText)
print("decoded length",len(decodedText))