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

## Folders

```text
inbox/      # nguồn đặt tạm để xử lý thử
converted/  # markdown/assets convert thử, non-canonical
reports/    # quality report, preview report, recommendation
runs/       # run packages tạm cho tài liệu dài hoặc OCR/convert thử
```

Chỉ khi AN GO official ingest mới handoff sang workflow canonical.
