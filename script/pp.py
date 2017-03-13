import mechanize
from lxml import html


def processParagraph(text1,text2):
	major_abbr= 'CMPS'
	class_number
	br = mechanize.Browser()
	br.open("https://pisa.ucsc.edu/class_search/")
	br.select_form('searchForm')
	br.form['binds[:term]'] = ['2172',]
	br.form['binds[:reg_status]'] = ['all',]
	br.form['binds[:subject]'] = [text1,]
	br.form['binds[:catalog_nbr]'] = text2
	response = br.submit()                          #get the search result page

	page = html.document_fromstring(response.read())

	class_index= page.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/h2/a[2]/@href')[0]
	return class_index








