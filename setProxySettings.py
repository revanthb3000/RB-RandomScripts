global proxyAddress
global proxyPort
global proxyUsername
global proxyPassword
global bashPath
global aptPath
global wgetPath
bashPath = '/etc/bash.bashrc'
aptPath  = '/etc/apt/apt.conf'
wgetPath = '/etc/wgetrc'

def bash():
    httpExport = "export http_proxy=http://"+proxyUsername+":"+proxyPassword+"@"+proxyAddress+":"+proxyPort+"/\n"
    ftpExport = "export ftp_proxy=http://"+proxyUsername+":"+proxyPassword+"@"+proxyAddress+":"+proxyPort+"/\n"
    matter = ""
    f=open(bashPath,"r")
    for line in f.readlines():
        if("export http_proxy" in line):
            line = httpExport
        if("export ftp_proxy" in line):
            line = ftpExport
        matter = matter + line
    f.close()
    f=open(bashPath,"w")
    f.write(matter)
    f.close()

def apt():
    httpAcquire = "Acquire::http::proxy \"http://"+proxyUsername+":"+proxyPassword+"@"+proxyAddress+":"+proxyPort+"/\";\n"
    ftpAcquire = "Acquire::ftp::proxy \"ftp://"+proxyUsername+":"+proxyPassword+"@"+proxyAddress+":"+proxyPort+"/\";\n"
    httpsAcquire = "Acquire::https::proxy \"https://"+proxyUsername+":"+proxyPassword+"@"+proxyAddress+":"+proxyPort+"/\";\n"
    matter = ""
    f=open(aptPath,"r")
    for line in f.readlines():
        if("Acquire::http::proxy" in line):
            line = httpAcquire
        if("Acquire::ftp::proxy" in line):
            line = ftpAcquire
        if("Acquire::https::proxy" in line):
            line = httpsAcquire          
        matter = matter + line
    f.close()
    f=open(aptPath,"w")
    f.write(matter)
    f.close()

def wget():
    proxy = "http://" + proxyAddress + ":" + proxyPort + "/\n"
    matter = ""
    f=open(wgetPath,"r")
    for line in f.readlines():
        if ("http_proxy=" in line):
            line = "htp_proxy=" + proxy
        if ("ftp_proxy=" in line):
            line = "ftp_proxy=" + proxy
        if("proxy_user=" in line):
            line = "proxy_user=" + proxyUsername + "\n"
        if("proxy_password" in line):
            line = "proxy_password=" + proxyPassword + "\n"
        matter = matter + line
    f.close()
    f=open(wgetPath,"w")
    f.write(matter)
    f.close()

if __name__ == "__main__":
    proxyAddress = str(raw_input("Proxy Address : "))
    proxyPort = str(raw_input("Proxy Port : "))
    proxyUsername = str(raw_input("Proxy Username : "))
    proxyPassword = str(raw_input("Proxy Password : "))
    bash()
    apt()
    wget()
