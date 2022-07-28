import feedparser, datetime

tistory_blog_uri="https://limjs-dev.tistory.com/rss"

rss_feed = feedparser.parse(tistory_blog_uri)

MAX_POST_NUM = 10

latest_blog_post_list = ""

MAX_POST_NUM = 10

dt = datetime.datetime.strptime(i['published'], "%a, %d %b %Y %H:%M:%S %z").strftime("%b %d, %Y")

for idx, feed in enumerate(rss_feed['entries']):
    if idx > MAX_POST_NUM:
        break
    feed_date = feed['published_parsed']
    latest_blog_post_list += f"[{feed['title']}]({feed['link']}) - {dt}<br>\n"
    
markdown_text = """
![Anurag's GitHub stats](https://github-readme-stats.vercel.app/api?username=yim2627&&count_private=true)

[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=yim2627&layout=compact)](https://github.com/anuraghazra/github-readme-stats)

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fyim2627%2Fhit-counter&count_bg=%2379C83D&title_bg=%23555555&icon=github.svg&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

### Recent Post..

"""

readme_text = f"{markdown_text}{latest_blog_post_list}"

with open("README.md", 'w', encoding='utf-8') as f:
    f.write(readme_text)
