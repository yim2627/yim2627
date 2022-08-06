import feedparser, datetime

tistory_blog_uri="https://limjs-dev.tistory.com/rss"

rss_feed = feedparser.parse(tistory_blog_uri)

MAX_POST_NUM = 10

latest_blog_post_list = ""

MAX_POST_NUM = 10

for idx, feed in enumerate(rss_feed['entries']):
    if idx > MAX_POST_NUM:
        break
    dt = datetime.datetime.strptime(feed['published'], "%a, %d %b %Y %H:%M:%S %z").strftime("%b %d, %Y")
    feed_date = feed['published_parsed']
    latest_blog_post_list += f"[{feed['title']}]({feed['link']}) - {dt}<br>\n"
    
markdown_text = """
<div align="center"> 
![](./profile-3d-contrib/profile-night-green.svg)

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fyim2627%2Fhit-counter&count_bg=%2379C83D&title_bg=%23555555&icon=github.svg&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

### Recent Post...

</div>
"""

readme_text = f"{markdown_text}{latest_blog_post_list}"

with open("README.md", 'w', encoding='utf-8') as f:
    f.write(readme_text)
