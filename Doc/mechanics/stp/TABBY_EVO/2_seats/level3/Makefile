SRC=$(wildcard *.stp)
HTML=$(SRC:.stp=.html)

html: $(HTML)

%.html: %.stp
	stp2html.py  $< 2> /dev/null >/dev/null
	cp $@ $(WEBOSV)/level3
clean:
	rm -f *.html
	rm -f *.x3d
