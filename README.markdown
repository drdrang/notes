This is a no-server personal wiki system that I created to keep track of project notes for work. I've put it here because it may be useful to others.

<img class="ss" src="http://www.leancrew.com/all-this/images/notes-wiki-overview.png" />

# Goals #

This is what I want:

1. A self-contained file or folder of files that includes everything needed to write and view the notes. I want it to be easy to copy from one computer to another and to archive to DVD. This eliminates most of the available wiki systems, which store everything in a central database.
2. The notes themselves to be written in Markdown rather than some specialized wiki markup. I write everything in Markdown and don’t want to shift context when switching from notes to a report. In fact, I'd like to be able to copy directly from my notes—markup included—when writing a report.
3. To write the notes in my text editor of choice rather than in an HTML text input box or a word processor. Currently, that editor is TextMate, but TextMate itself isn’t the point. The point is to take advantage of the comfort I feel working in my normal editor. There's a reason old Unix hackers like to do everything in Emacs or vi; it's just more efficient to do all your text work in one environment.
4. To be able to change the visual style of the notes as my needs or tastes change.
5. To create new notes quickly and easily.

# Requirements #

Apart from what's in the repository, you'll need

* [Python][1]. The two build scripts, `buildPage.py` and `buildNotesList.py`, are written in Python.
* [GNU make][2]. The build scripts are controlled by a makefile.
* A [Markdown][3] processor. I use a self-customized version of Fletcher Penney's [MultiMarkdown][4]. Whatever you use, you'll have to provide the name of that command on Line 16 of `buildPage.py`.
* A [SmartyPants][5] processor. I use Gruber's SmartyPants. Again, you'll have to provide the name of that command on Line 16 of `buildPage.py`.

If you need to include mathematical formulas in your notes, you should consider installing Davide Cervone's [jsMath][6]. Once you've installed it, you can activate jsMath in the notes by uncommenting Line 10 of the `header.tmpl` file and adjusting the `jsmathpath` variable in the `project.info` file to point to jsMath's `easy.js` file.

# File structure #

The top level of the notes directory contains all the support files, that is, all the files that are distinct from the notes themselves. These files are:

* `header.tmpl`, the HTML template file with all the common code above the content.
* `footer.tmpl`, the HTML template file with all the common code below the content.
* `project.info`, a file of project-specific data, including the project name and number, the list of contacts (including links to Address Book entries if you're on a Mac), and the name of the PNotes directory.
* `notes.css`, the style file for browsing.
* `notes-print.css`, the style file for printing.
* `styleLineNumbers.js`, a [pair of JavaScript functions][7] that improve the formatting of source code.
* `buildPage.py`, a Python script that combines a Markdown input file with the template files and produces a single HTML file.
* `buildNotesList.py`, a Python script that searches the directory (and subdirectories) for notes files and generates a list of links to all the notes for display in the sidebar.
* `Makefile`, the makefile that controls the build scripts.

Notes files contain the actual content. These files should all have the extension `.md` and can be in both the top-level directory and in subdirectories. Two sample notes files are included: `aa-overview.md` in the top-level directory, and `testing1.md` in the `Lab` subdirectory.

# Creating notes #

As mentioned above, notes are just plain text files written in Markdown and saved with an `.md` extension. The first line will be the note's title and will appear in the sidebar.

<img class="ss" src="http://www.leancrew.com/all-this/images2010/notes-sidebar.png" />

I use ATX-style headers, with hash marks indicating the header level, and I start each file with a first-level header, like this:

		# Overview #

The build system is smart enough to get rid of the hash marks when making up the sidebar.

Notes files in subdirectories appear with greater indentation under the name of the directory—like an outline. Within each directory, the notes are ordered alphabetically according to their file names, so you can rearrange the order in which the notes appear in the sidebar by changing the file names without changing their content. At present, there's no way to change the order of the subdirectories.

Executing `make` from the top-level directory will generate all the HTML pages, which can be opened with any browser. Subsequent executions of `make` will generate only those pages whose `.md` files are new or have been modified. Executing `make clean` will erase all the HTML files, but will not touch the `.md` files.

# Editing notes #

You can, of course, open any `.md` file in any text editor to make changes. If you're using TextMate on a Mac, there's a faster way: click the Edit in TextMate link in the side bar to instantly open the `.md` file in TextMate—no need to switch to the Finder, open the folder, and double-click the file icon. If you're a BBEdit user, you can do the same thing, but you'll probably want to change the name of the link. It's on Line 33 of `header.tmpl`.

# More details #

I wrote a three-part series of blog posts describing this system and its scripts, [here][8], [here][9], and [here][10]. Updates to the system are described [here][12] and [here][13].

# License #

This work is licensed under a [Creative Commons Attribution-Share Alike 3.0 Unported License][11]. Do what you want with it, but provide a link back to either my blog posts or to my repository.


[1]: http://www.python.org/
[2]: http://www.gnu.org/software/make/
[3]: http://daringfireball.net/projects/markdown/
[4]: http://fletcherpenney.net/multimarkdown/
[5]: http://daringfireball.net/projects/smartypants/
[6]: http://www.math.union.edu/~dpvc/jsMath/
[7]: http://www.leancrew.com/all-this/2007/12/source-code-line-numbers-and-javascript/
[8]: http://www.leancrew.com/all-this/2008/06/my-no-server-personal-wiki-part-1/
[9]: http://www.leancrew.com/all-this/2008/06/my-no-server-personal-wiki-part-2/
[10]: http://www.leancrew.com/all-this/2008/06/my-no-server-personal-wiki-part-3/
[11]: http://creativecommons.org/licenses/by-sa/3.0/
[12]: http://www.leancrew.com/all-this/2010/02/the-no-server-notes-wiki/
[13]: http://www.leancrew.com/all-this/2010/05/relative-links-in-pnotes/
