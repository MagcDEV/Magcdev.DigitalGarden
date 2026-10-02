# Frontmatter Reference

## Source Files

### LeetCode
```yaml
---
title: "LC-XXXX: Problem Name"
source_type: leetcode
source_url: https://leetcode.com/problems/problem-slug/
difficulty: easy | medium | hard
tags:
  - source
  - leetcode
  - pattern-name
date: YYYY-MM-DD
processed: false
compiled_to: []
---
```

### Book
```yaml
---
title: "Book Title - Chapter X Notes"
source_type: book
author: "Author Name"
tags:
  - source
  - books
  - topic-area
date: YYYY-MM-DD
processed: false
compiled_to: []
---
```

### Article
```yaml
---
title: "Article Title"
source_type: article
source_url: https://...
author: "Author Name"
tags:
  - source
  - articles
  - topic-area
date: YYYY-MM-DD
processed: false
compiled_to: []
---
```

### Video
```yaml
---
title: "Video Title"
source_type: video
source_url: https://youtube.com/watch?v=...
channel: "Channel Name"
tags:
  - source
  - videos
  - topic-area
date: YYYY-MM-DD
processed: false
compiled_to: []
---
```

### Course
```yaml
---
title: "Course Name - Module X"
source_type: course
source_url: https://...
platform: "Neetcode | Udemy | MIT OCW | etc."
tags:
  - source
  - courses
  - topic-area
date: YYYY-MM-DD
processed: false
compiled_to: []
---
```

## Wiki Files

```yaml
---
title: "Page Title"
tags:
  - wiki
  - area (the folder name: dsa | patterns | system-design | go | concepts | a new area)
  - specific-topic-tags
date_created: YYYY-MM-DD
date_modified: YYYY-MM-DD
sources:            # optional; omit when the note has no source file behind it
  - "[[sources/type/YYYY-MM-DD-slug]]"
---
```

## Wiki Pages That Embed Standalone HTML Guides

```yaml
---
title: "Subject Study Notes"
tags:
  - wiki
  - area
  - subject
date_created: YYYY-MM-DD
date_modified: YYYY-MM-DD
cssclasses:
  - subject        # matches the folder content/assets/<subject>/ and the selector in quartz/styles/custom.scss
---
```

Each guide section in the page has an "Open full page" form and an embed:

```html
<form class="guide-open" action="../../assets/<subject>/<guide>.html" method="get" target="_blank">
<button type="submit">Open full page</button>
</form>

<embed class="guide-frame" src="../../assets/<subject>/<guide>.html" type="text/html" title="Guide title">
```

## Conventions

- **Date format:** YYYY-MM-DD (ISO 8601)
- **File naming:** `YYYY-MM-DD-descriptive-slug.md` for sources, `descriptive-slug.md` for wiki
- **Tags:** Always include `source` or `wiki` as the first tag to identify the layer
- **compiled_to:** List of wikilinks to wiki pages that were created/updated from this source
- **sources:** List of wikilinks to source files that contributed to this wiki page; a note written directly has none
