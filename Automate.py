from Scrape import scrape
from file_utils import csvwrite
from templating import generate
from image import pass_gen
from mail import sendmail
#scraping
data = scrape('http://scrape.kjscecodecell.com')


#file save
csvwrite(data)

#templating

for bacche in data:
    message= generate(bacche)
    passs=pass_gen(bacche)
    ##emails
    sendmail(bacche[2],message,passs,bacche[-1])

    




