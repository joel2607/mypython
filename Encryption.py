exitvar = False
while not exitvar:
    print('Enter 1 to encrypt a text file. \nEnter 2 to decrypt a text file.\n\n\t')
    choice = str(input(''))

    if choice == '1':
        ifilename = input('\n\nEnter file to be encrypted: ')
        encryptkey = input('Enter the Encryption Key: ')
        ofilename = input('Enter file where encrypted data is written: ')
        
        with open(ifilename, 'r') as ifile:
            rawdata = ifile.read()
            encrypteddata = ''
            for char in rawdata:
                char = chr(ord(char) + encryptkey)
                encrypteddata += char
            
        with open(ofilename, 'a') as ofile:
            ofile.write(encrypteddata)

    elif choice == '2':

        ifilename = input('\n\nEnter file to be decrypted: ')
        encryptkey = input('Enter the Encryption Key: ')
        ofilename = input('Enter file where decrypted data is written: ')
        
        with open(ifilename, 'r') as ifile:
            rawdata = ifile.read()
            encrypteddata = ''
            for char in rawdata:
                char = chr(ord(char) - encryptkey)
                encrypteddata += char
            
        with open(ofilename, 'a') as ofile:
            ofile.write(encrypteddata)
    
    elif choice == 'exit':
        exitvar = True
        break
    
    else: print('Please enter valid input.')

        



