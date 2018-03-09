#
# Created by maliang on 2017/12/17.
#

from scrapy.cmdline import execute

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(['scrapy','crawl','jobbole'])