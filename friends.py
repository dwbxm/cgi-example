#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()

reshtml = '''Content-Type: text/html\r\n\r\n
<HTML><HEAD><TITLE>
Friends CGI Demo <dynamic screen)
</TITLE></HEAD>
<BODY><H3>Friends list for: <I>%s</I></H3>
Your name is: <B>%s</B><P>
You have <B>%s</B> friends.
</BODY></HTML>'''

form = cgi.FieldStorage()
who = form['person'].value
howmany = form['howmany'].value
print(reshtml % (who, who, howmany))




