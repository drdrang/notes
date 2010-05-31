#!/usr/bin/env python

import sys
import os
import os.path
import time
import string
import urllib

# The argument is the basename of the Markdown source file.
mdFile = sys.argv[1] + '.md'

# Open the page files and process the content.
header = open('header.tmpl', 'r')
footer = open('footer.tmpl', 'r')
cmd = 'MultiMarkdown %s | SmartyPants' % mdFile
content = os.popen(cmd, 'r')

#  Make the template.
templateParts = [header.read(), content.read(), footer.read()]
template = string.Template(''.join(templateParts))

# Close the page files.
header.close()
footer.close()
content.close()

# Initialize the dictionary of dynamic information.
info = {}

# Dictionary entry with relative path to notes root. We allow only one
# level of subdirectory, so the root can be at most one level up from
# the file we're working on.
if os.path.split(mdFile)[0] == '':
  info['root'] = ''
else:
  info['root'] = '../'

# Dictionary entry with long modification date of the Markdown file.
mdModTime = time.localtime(os.path.getmtime(mdFile))
info['modldate'] = time.strftime('%B %e, %Y', mdModTime)
info['modldate'] = info['modldate'].replace('  ', ' ')

# Dictionary entry with short modification date of the Markdown file.
info['modsdate'] = time.strftime('%m/%e/%y', mdModTime)
info['modsdate'] = info['modsdate'].replace(' ', '')

# Dictionary entry with modification time of the Markdown file.
info['modtime'] = time.strftime('%l:%M %p', mdModTime)
if info['modtime'][0] == ' ':
  info['modtime'] = info['modtime'][1:]

# Dictionary entry with absolute path to the Markdown file (for editing).
# info['mdpath'] = os.path.abspath(mdFile)

# Add project info to the dictionary.
projInfo = open('project.info', 'r')
for line in projInfo:
  if line[0] == '#' or line.strip() == '':
    continue
  name, value = [s.strip() for s in line.split('=', 1)]
  if name in info:
    info[name] += '\n' + value
  else:
    info[name] = value

projInfo.close()

# Dictionary entry with path to project info file (for editing).
# info['infopath'] = os.path.abspath('project.info')

# Convert the contacts into a series of HTML list items.
if 'contact' in info:
  contactLI = []
  cl = [s.split(':',1) for s in info['contact'].split('\n')]
  for c in cl:
    if len(c) == 1:
      contactLI.append('<li>%s</li>' % c[0])
    else:
      contactLI.append('<li><a href="addressbook://%s">%s</a></li>'\
      % tuple(reversed(c)))
  info['contactlist'] = '\n'.join(contactLI)
else:
  info['contactlist'] = ''

# Output the template with the dynamic information substituted in.
print template.safe_substitute(info)
