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

  a = fp.read() 
  m = re1.search(a) 
  print(m.group(1))	
  a = re2.sub(' ',a)
  a = re3.sub(' ',a) 
  for m in re4.finditer(a): 
    print('{}    {}'.format(m.group(1),m.group(2)))
  a = re5p1.sub(' ',a) 
  a = re5p2.sub(' ',a) 
  a = re6.sub(function,a) 
  a = re7.sub(' ',a) 
  print(a)
