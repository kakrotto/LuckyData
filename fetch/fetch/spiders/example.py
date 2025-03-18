import re

import scrapy


class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["*"]
    start_urls = ["https://www.cwl.gov.cn/ygkj/ssq/ydjzjmx/"]

    def parse(self, response, **kwargs):
        html = response.text
        pattern = r"slsj\.push\(\{[\s\S]*?\}\);"

        matches = re.findall(pattern, html)

        for v in matches:
            v = v.strip()
            v = v.replace('slsj.push(', '').replace(');', '').replace('\r\n', '')
            date = v[v.find('qh:'):v.find('",            rq:')].replace('qh:"', '').strip()

            time = v[v.find('rq:'):v.find('",            hj:')].replace('rq:"', '').strip()
            num = v[v.find('hj:'):v.find('",            xq:gsh(')].replace('hj:"', '').strip()
            l = v[v.find('xq:gsh("'):v.find('"),')].replace('xq:gsh("', '').strip()
            l = l.split('**')
            self.logger.info(date, time, num)
            for j in l:
                j = [o.replace('\t', '').replace('&#32;', '') for o in j.split('*')]
                self.logger.info(j)

