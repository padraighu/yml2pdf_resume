# yml2pdf_resume

This repo showcases how I make my resume. The idea is that you only need to edit a simple yaml file, and then you can get a pdf version of your resume. I used Harry Potter as an example in this showcase.

## How does it work?
script.py contains script that parses cv.yml, and transforms it into cv.html through Jinja2 templates. Then wkhtml2pdf is used to render the html into a pdf.
File dependencies are outlined in Makefile.

## Why?
Because editing my resume in Word was inconvient. Since I have knowledge of html and css, I figured that would give me more flexibility in designing my own resume directly through code instead of all the buttons and widgets in Word.
However, html is a little too much when you're directly editing it, so I wrote my resume content in yaml, a human-readable format, and transformed it into a html file using templating. The final touch is to render it as a pdf file.
Obviously latex is an alternative, however I prefer html/css because it's lighter since you need to install latex environment and editor.

## How to use it?
Edit content in cv.yml, and call make (assuming you're in a Unix-like environment).

## Dependencies
- python 3
  - pyyaml
  - jinja2
- wkhtmltopdf

## TODO
  - Make a Word version of resume
