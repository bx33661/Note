print(r'''
 _________     
|        |                      (_) (_)  
  | |_ \_|_   _   __   .--.     __  __   
  |  _| _[ \ [ \ [  ]/ .'`\ \  [  |[  |  
 _| |__/ |\ \/\ \/ / | \__. |_  | | | |  
|________| \__/\__/   '.__.'[ \_| |[___] 
                             \____/      
      
''')
site = input("[+]Input the site you want to find something\n")
if(site==""):
   exit("site不能为空！")
   
def infiletype(types):
    for i,v in enumerate(types):
         types[i] = "filetype:"+v
    return types
   
   
def inurl(urls):
    for i,v in enumerate(urls):
        urls[i] = "inurl:\""+v+"\""
    return urls

def intitle(titles):
    for i,v in enumerate(titles):
        titles[i] = "intitle:\""+v+"\""
    return titles

def intext(texts):
    for i,v in enumerate(texts):
        texts[i] = "intext:\""+v+"\""
    return texts
        
def max(urls,titles,texts,filetypes):
    OR = " OR "
    f = OR.join(filetypes)
    u = OR.join(urls)
    ti = OR.join(titles)
    te = OR.join(texts)
    if(f!="filetype:"):
       f+=" "
    else:
       f=""
    if(u!="inurl:\"\""):
       u+=" OR "
    else:
       u=""
    if(ti!="intitle:\"\""):
       ti+=" OR "
    else:
       ti=""
    return "site:"+site+" "+f+u+ti+te
    

file = input("[+]Input what filetype you need\n").strip().split(" ")
a = input("[+]Input what you want in url\n").strip().split(" ")
b = input("[+]Input what you want in title\n").strip().split(" ")
c = input("[+]Input what you want in text\n").strip().split(" ")

print(max(inurl(a),intitle(b),intext(c),infiletype(file)))