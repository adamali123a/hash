import base64
import hashlib
print("\nscript by Moscow\n")
#help(hashlib)
while True:
    try:
        a = r"""
        joar Encryptakan
        |----------------|
        |                |
        |   1-base64     |
        |                |
        |   2-hash       |
        |                |
        |   99-darchon   |
        |----------------|
        """
        print("\033[0;36m",a)

        b = input("zhmarya danyk halbzhera ==>   ")

        if b == '1':
             print("""
             |-----------|
             | 1-base85  |
             | 2-base64  |
             | 3-base32  |
             | 4-base16  |
             |-----------|
             """)
             e = int (input("zhmarya danyk halbzhera law chora ==>  "))
             if e == 1:
                d = str (input("\n \033[0;32m har shtek banwsa bo Encrypt ==>  "))
                c = base64.b85encode(d.encode("ascii"))
                print("\n \033[0;31m Awsh ba Encrypte ==>  {} \n".format(c))
             elif e == 2:
                 d = str (input("\n \033[0;32m har shtek banwsa bo Encrypt ==>  "))
                 c = base64.b64encode(d.encode("ascii"))
                 print("\n \033[0;31m Awsh ba Encrypte ==>  {} ".format(c))
             elif e == 3:
                 d = str (input("\n \033[0;32m har shtek banwsa bo Encrypt ==>  "))
                 c = base64.b32encode(d.encode("ascii"))
                 print("\n \033[0;31m Awsh ba Encrypte ==>  {} ".format(c))
             elif e == 4:
                 d = str (input("\n \033[0;32m har shtek banwsa bo Encrypt ==>  "))
                 c = base64.b16encode(d.encode("ascii"))
                 print("\n \033[0;31m Awsh ba Encrypte ==>  {} ".format(c))
             else:
            
                 print("\naw zhamarya bony nya {}".format(e))
                 
        elif b == '2':
        
            print(r"""
            
        
           |----------------------|
           |     1-sha1           |
           |     2-sha224         |
           |     3-sha256         |
           |     4-sha384         |
           |     5-md5            |
           |----------------------| 
            """)
            
            f = int (input("zhmarya danyk halbzhera law peanja ==>  "))
            if f == 1:
                n = str (input("\n \033[0;33m har shtek banwsa bo Encrypt ==>  "))
                s = hashlib.sha1(n.encode()).hexdigest()
                print("\n \033[1;31m Awsh ba Encrypte ==>  {} ".format(s))
            elif f == 2:
                n = str (input("\n \033[0;33m har shtek banwsa bo Encrypt ==>  "))
                s = hashlib.sha224(n.encode()).hexdigest()
                print("\n \033[1;31m Awsh ba Encrypte ==>  {} ".format(s))
                
            elif f == 3:
                n = str (input("\n \033[0;33m har shtek banwsa bo Encrypt ==>  "))
                s = hashlib.sha256(n.encode()).hexdigest()
                print("\n \033[1;31m Awsh ba Encrypte ==>  {} ".format(s))
                
            elif f == 4:
                n = str (input("\n \033[0;33m har shtek banwsa bo Encrypt ==>  "))
                s = hashlib.sha384(n.encode()).hexdigest()
                print("\n \033[1;31m Awsh ba Encrypte ==>  {} ".format(s))
                
            elif f == 5:
                n = str (input("\n \033[0;33m har shtek banwsa bo Encrypt ==>  "))
                s = hashlib.md5(n.encode()).hexdigest()
                print("\n \033[1;31m Awsh ba Encrypte ==>  {} ".format(s))
            else:
            
                print("\naw zhamarya bony nya {}".format(f))
                
                
        elif b == "99":
            break
            
        else:
            
            print("\naw zhamarya bony nya {}".format(b))
    except:
        print("\naw shta bony nya\n")