# Source Lab

`source-lab` là nơi xử lý thử tài liệu dài trước khi quyết định ingest.

Luồng mặc định:

```text
source
-> NotebookLM / preview
-> learning map
-> SKIP | KEEP_SUMMARY | PROMOTE
```

Không ghi trực tiếp vào `3-resources/`.

