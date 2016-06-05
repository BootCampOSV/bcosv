SRC=$(wildcard *.stp)
HTML=$(SRC:.stp=.html)
STEP=$(SRC:.stp=.step)

html: $(HTML)

step: $(STEP)

%.step: %.stp
	filterstp.py $< > $@

%.html: %.stp
	stp2html.py  $< 4 2> /dev/null >/dev/null
	cp $@ $(WEBOSV)/level4
clean:
	rm -f *.html
	rm -f *.x3d
trans: $(SRC)
	
