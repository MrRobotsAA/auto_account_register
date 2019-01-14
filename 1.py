#! -*- encoding:utf-8 -*-

from urllib import request

# 要访问的目标页面
targetUrl = "http://vip.luol3.club/bbs-5057004.htm"
#targetUrl = "http://proxy.abuyun.com/switch-ip"
#targetUrl = "http://proxy.abuyun.com/current-ip"

# 代理服务器
proxyHost = "http-pro.abuyun.com"
proxyPort = "9010"

# 代理隧道验证信息
proxyUser = "H1DM325559080OVP"
proxyPass = "E07D915F205D3481"

proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
    "host" : proxyHost,
    "port" : proxyPort,
    "user" : proxyUser,
    "pass" : proxyPass,
}

proxy_handler = request.ProxyHandler({
    "http"  : proxyMeta,
    "https" : proxyMeta,
})

#auth = request.HTTPBasicAuthHandler()
#opener = request.build_opener(proxy_handler, auth, request.HTTPHandler)

opener = request.build_opener(proxy_handler)

# opener.addheaders = [("Proxy-Switch-Ip", "yes")]
request.install_opener(opener)
resp = request.urlopen(targetUrl)


print (resp.getcode())

print ("ok")

response = request.Request(url='http://vip.luol3.club/user-create.htm', 	data={"username":"9962a324245","password":"bf6a0768465d59c8fca4d2e7d8a470c","email":"9423av24965@qq.com"})

print (response)