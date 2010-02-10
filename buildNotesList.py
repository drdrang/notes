#!/usr/bin/python

import os

# Get the titles of all the notes files in the directory. The
# title is assumed to be the first line of the file. Truncate
# the title at a word boundary if it's longer than maxlength,
# and turn it into a link in a list item.
def nameList(dir):
  fileLI = []
  maxlength = 35
  allFiles = os.listdir(dir)
  baseNames = [ f[:-3] for f in allFiles if f[-3:] == '.md' ]
  # print baseNames
  for fn in baseNames:
    f = file(os.path.join(d, fn + '.md'))
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
    f.close()
    fileLI.append('<li><a href="%s.html">%s</a></li>' % (os.path.join(d, fn),title))
  return fileLI

# Find all the directories that have md files.
mdDirs = []
for root, dirs, files in os.walk('.'):
  for f in files:
    if f[-3:] == '.md':
      mdDirs.append(root)
      break

# Go through the directories and generate the list of links.
linkList = []
for d in mdDirs:
  if d == '.':
    linkList += nameList(d)
    # print linkList
  else:
    linkList += ['<li>%s' % d[2:], '<ul>']
    # print linkList
    linkList += nameList(d)
    # print linkList
    linkList += ['</ul>', '</li>']

print '''function showNotesList(){
  document.write('%s')
}''' % ''.join(linkList)
