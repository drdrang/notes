#!/usr/bin/python

import os

# Get the titles of all the notes files in the directory. The
# title is assumed to be the first line of the file. Truncate
# the title at a word boundary if it's longer than maxlength.
# Print out a JavaScript function that will write an HTML list
# of the notes files.

fileLI = []
maxlength = 35
allFiles = os.listdir('.')
baseNames = [ f[:-3] for f in allFiles if f[-3:] == '.md' ]
for fn in baseNames:
  f = file(fn + '.md')
  top = f.readline()
  title = top.strip('# \n')
  if len(title) > maxlength:
    words = title.split()
    twords = []
    count = 0
    for w in words:
      if count + len(w) > maxlength:
        break
      else:
        twords.append(w)
        count += len(w) + 1 
    title = ' '.join(twords) + "&#8230;"
  fileLI.append('<li><a href="%s.html">%s</a></li>' % (fn,title))
  f.close()

print '''function showNotesList(){
  document.write('%s')
}''' % ' '.join(fileLI)
