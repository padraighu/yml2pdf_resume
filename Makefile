WKHTMLTOPDF_PATH = '/mnt/c/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'
PDF_FILE = HPotter_cv.pdf

all: cv.html $(PDF_FILE)

cv.html: cv.yml cv_template.html script.py
	python script.py

$(PDF_FILE): cv.html
	$(WKHTMLTOPDF_PATH) -s Letter cv.html $(PDF_FILE)

clean: 
	rm -f cv.html $(PDF_FILE)