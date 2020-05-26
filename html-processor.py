def function(m):

  if (m.group(0)=='&amp;'):
    return '&'
  
  elif (m.group(0)=='&gt;'):
    return '>'

  elif (m.group(0)=='&lt;'):
    return '<'

  else:
    return ' '	

re1 = re.compile('<title>(.+?)</title>')

re2 = re.compile('<!--.*?-->',re.DOTALL)

re3 = re.compile(r'<(s(?:cript|tyle)).*?>.*?</\1>',re.DOTALL)

re4 = re.compile(r'<a.+?href="(.*?)".*?>(.*?)</a>',re.DOTALL)

re5p1 = re.compile(r'<.+?>|</.+?>',re.DOTALL)

re5p2 = re.compile(r'<.+?/>',re.DOTALL)

re6 = re.compile(r'&(amp|gt|lt|nbsp);')

re7 = re.compile(r'\s+')


with open('testpage.txt','r') as fp:

  t = fp.read() 
  m = re1.search(t) 
  print(m.group(1))	
  t = re2.sub(' ',t)
  t = re3.sub(' ',t) 
  for m in re4.finditer(t): 
    print('{}    {}'.format(m.group(1),m.group(2)))
  t = re5p1.sub(' ',t) 
  t = re5p2.sub(' ',t) 
  t = re6.sub(function,t) 
  t = re7.sub(' ',t) 
  print(t)
