from scrapy import cmdline
name = 'jdSpider'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())