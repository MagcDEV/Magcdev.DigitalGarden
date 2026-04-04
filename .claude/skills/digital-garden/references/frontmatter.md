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
  - area (dsa | patterns | system-design | go | concepts)
  - specific-topic-tags
date_created: YYYY-MM-DD
date_modified: YYYY-MM-DD
sources:
  - "[[sources/type/YYYY-MM-DD-slug]]"
---
```

## Conventions

- **Date format:** YYYY-MM-DD (ISO 8601)
- **File naming:** `YYYY-MM-DD-descriptive-slug.md` for sources, `descriptive-slug.md` for wiki
- **Tags:** Always include `source` or `wiki` as the first tag to identify the layer
- **compiled_to:** List of wikilinks to wiki pages that were created/updated from this source
- **sources:** List of wikilinks to source files that contributed to this wiki page
