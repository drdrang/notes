# Makefile for project notes.

mdfiles := $(wildcard *.md)
htmlfiles := $(patsubst %.md, %.html, $(mdfiles))

all: notesList.js $(htmlfiles)

notesList.js::
	python buildNotesList.py > notesList.js

%.html: %.md project.info header.tmpl footer.tmpl
	python buildPage.py $* > $@
	
clean:
	rm $(htmlfiles) notesList.js
