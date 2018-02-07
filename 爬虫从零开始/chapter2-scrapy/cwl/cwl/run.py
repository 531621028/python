from scrapy import cmdline
name = 'zhcw'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())