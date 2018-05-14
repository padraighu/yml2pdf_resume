import yaml
import pprint
from jinja2 import Template

if __name__ == '__main__':
	# Deserialize from yaml.
	pp = pprint.PrettyPrinter(indent = 2)
	with open('cv.yml') as f:
		cv = yaml.load(f)
		f.close()
	#pp.pprint(cv)

	# Serialize into html using jinja templating.
	with open('cv_template.html') as f:
		template = Template(f.read())
		f.close()
	
	cv_html = template.render(
		info = cv['info'],
		education = cv['education'],
		experience = cv['experience'],
		projects = cv['projects'],
		skills = cv['skills']
		)
	#print(cv_html)
	with open('cv.html', 'w+') as f:
		f.write(cv_html)
		f.close()


	