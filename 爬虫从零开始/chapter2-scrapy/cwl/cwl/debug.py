from scrapy import cmdline
name = 'cwl'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())