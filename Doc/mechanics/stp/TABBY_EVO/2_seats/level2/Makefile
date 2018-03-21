SRC=$(wildcard *.stp)
HTML=$(SRC:.stp=.html)

html: $(HTML)

%.html: %.stp
	python ./stp2html.py  $< 2 2> /dev/null >/dev/null
	cp $@ $(WEBOSV)/level2
clean:
	rm -f *.html
	rm -f *.x3d
trans: $(SRC)
	
