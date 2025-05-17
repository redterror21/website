import datetime

title = input("Post title: ").strip()
slug = title.lower().replace(' ', '-')
date = datetime.datetime.now().strftime('%Y-%m-%d')
filename = f"_posts/{date}-{slug}.md"

content = f"""---
layout: post
title: "{title}"
---

Start writing here...
"""

with open(filename, "w") as f:
    f.write(content)

print(f"Created new post: {filename}")
