#!/usr/bin/env python3

import cgi
from urllib.parse import quote_plus
import cgitb
cgitb.enable()

header = 'Content-Type: text/html\r\n\r\n'
url = '/cgi-bin/friendsA.py'

errorhtml = '''<HTML><HEAD><TITLE>
Friends CGI Demo</TITLE></HEAD>
<BODY><H3>ERROR</H3>
<B>%s</B><P>
<FORM><INPUT TYPE=button  VALUE=back ONCLICK="window.history.back()"></FORM>
</BODY></HTML>'''

def showError(error_str):
	print(header + errorhtml %(error_str))
	
formhtml = '''<HTML><HEAD><TITLE>
Friends CGI Demo</TITLE></HEAD>
<BODY><H3>Friends list for: <I>%s</I></H3>
<FORM ACTION="%s">
<INPUT TYPE=text NAME=lbk VALUE="lkjb" SIZE=15>
<B>Enter your name:</B>
<INPUT  TYPE=text NAME=action VALUE=edit>  
<INPUT TYPE=text NAME=person VALUE="%s" SIZE=15>
<P><B>How many friends do you have?</B>
%s
<P><INPUT TYPE=submit></FORM></BODY></HTML>'''   #实际情况是， HTML页面只能显示出提交，其他输入字段name没有显示，未知原因

fradio = '<INPUT TYPE=radio NAME=howmany VALUE="%s" %s> %s\r\n'

def showForm(who, howmany):
	friends = []
	for i in (0,10,25,50,100):
		checked = ''
		if str(i) == howmany:
			checked = 'CHECKED' 
		friends.append(fradio % (str(i), checked, str(i)))
	
	print('%s%s' % (header, formhtml % (who, url, who, ''.join(friends))))
	
reshtml = '''<HTML><HEAD><TITLE>
Friends CGI Demo</TITLE></HEAD>
<BODY><H3>Friends list for: <I>%s</I></H3>
Your name is: <B>%s</B><P>
You have <B>%s</B> friends.
<P>Click <A HREF="%s">here</A> to edit your data again.
</BODY></HTML>'''

def doResults(who, howmany):
	newurl = url + '?action=reedit&person=%s&howmany=%s' % (quote_plus(who), howmany)
	print(header + reshtml % (who, who, howmany, newurl))

def process():
	error = ''
	form = cgi.FieldStorage()
	if 'person' in form:
		who = form['person'].value.title()
	else:
		who = 'New User'
		
	if 'howmany' in form:
		howmany = form['howmany'].value
	else:
		if 'action' in form and form['action'].value == 'edit':
			error = 'Please select number of friends.'
		else:
			howmany = 0
		
	if not error:
		if 'action' in form and form['action'].value != 'reedit':
			doResults(who, howmany)
		else:
			showForm(who, howmany)
	else:
		showError(error)
		
if __name__ == '__main__':
	process()

