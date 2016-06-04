SRC=$(wildcard *.stp)
HTML=$(SRC:.stp=.html)

html: $(HTML)

%.html: %.stp
	stp2html.py  $<
clean:
	rm -f *.html
	rm -f *.x3d
