# Graph Report - D:\NoteBookLLM_Br  (2026-04-09)

## Corpus Check
- Corpus is ~27,058 words - fits in a single context window. You may not need a graph.

## Summary
- 189 nodes · 160 edges · 64 communities detected
- Extraction: 80% EXTRACTED · 20% INFERRED · 0% AMBIGUOUS · INFERRED: 32 edges (avg confidence: 0.5)
- Token cost: 0 input · 0 output

## God Nodes (most connected - your core abstractions)
1. `ExponentialBackoff` - 11 edges
2. `BrainConsolidator` - 7 edges
3. `AllProvidersDownError` - 6 edges
4. `SyncManager` - 6 edges
5. `ContextDistiller` - 6 edges
6. `ChatToMarkdownConverter` - 6 edges
7. `RateLimiter` - 5 edges
8. `Meta` - 5 edges
9. `SimpleFilteredStdout` - 5 edges
10. `BatchContextDistiller` - 5 edges

## Surprising Connections (you probably didn't know these)
- `LLM Client — Wrapper gọi AI qua litellm với:   - Retry tự động (tenacity + expo` --uses--> `ExponentialBackoff`  [INFERRED]
  libs\core\llm_client.py → libs\core\rate_limiter.py
- `Lỗi định tuyến khi toàn bộ hệ thống LLM (Proxy & Direct Fallbacks) đều sập hoặc` --uses--> `ExponentialBackoff`  [INFERRED]
  libs\core\llm_client.py → libs\core\rate_limiter.py
- `Cấu hình litellm để dùng OpenRouter.` --uses--> `ExponentialBackoff`  [INFERRED]
  libs\core\llm_client.py → libs\core\rate_limiter.py
- `Gọi worker model (Proxy Power/Main) để dịch một chunk.` --uses--> `ExponentialBackoff`  [INFERRED]
  libs\core\llm_client.py → libs\core\rate_limiter.py
- `Gọi validator qua Proxy.` --uses--> `ExponentialBackoff`  [INFERRED]
  libs\core\llm_client.py → libs\core\rate_limiter.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.18
Nodes (15): Exception, AllProvidersDownError, call_validator(), _call_with_retry(), call_worker(), LLM Client — Wrapper gọi AI qua litellm với:   - Retry tự động (tenacity + expo, Gọi validator qua Proxy., Gọi Proxy Router (localhost:4000) với Cascade Fallback tự động. (+7 more)

### Community 1 - "Community 1"
Cohesion: 0.17
Nodes (16): BaseModel, fail(), Meta, ok(), PipelineOutput, PipelineSummary, Schemas Pydantic chuẩn cho toàn bộ pipeline. Mọi bước xử lý đều trả về Pipeline, Báo cáo tổng kết sau khi xử lý xong một file PDF. (+8 more)

### Community 2 - "Community 2"
Cohesion: 0.13
Nodes (8): ContextDistiller, Sử dụng AI để chưng cất (summarize) dữ liệu thô từ Gemini thành ngữ cảnh tinh gọ, get_latest_context(), Thực hiện đồng bộ dữ liệu từ Gemini (input/gemini_sync/) và tóm tắt chúng bằng A, Trả về nội dung ngữ cảnh đã được tinh lọc mới nhất., sync_gemini(), Quản lý việc đồng bộ và chuẩn bị dữ liệu ngữ cảnh thô từ Gemini., SyncManager

### Community 3 - "Community 3"
Cohesion: 0.18
Nodes (7): get_limiter(), RateLimiter, Rate Limiter — Quản lý delay giữa các request để tránh bị OpenRouter chặn.  Gi, Trả về RateLimiter singleton., Token bucket rate limiter đơn giản.      Đảm bảo không gửi quá N request trong, Gọi trước mỗi request AI.         Tự động sleep nếu cần để tránh vượt rate limi, Reset bộ đếm (dùng khi chuyển sang model mới).

### Community 4 - "Community 4"
Cohesion: 0.25
Nodes (4): BrainConsolidator, Trích xuất Chủ đề chính từ file KI., Gom nhóm KIs dựa trên từ khóa trong chủ đề., Gọi Proxy Hub để tổng kết một nhóm KIs.

### Community 5 - "Community 5"
Cohesion: 0.29
Nodes (3): BatchContextDistiller, Sử dụng AI để chưng cất dự liệu thô từ file chunk thành các Knowledge Items rải, Xử lý duy nhất một file chunk. Đây là worker function.

### Community 6 - "Community 6"
Cohesion: 0.43
Nodes (1): ChatToMarkdownConverter

### Community 7 - "Community 7"
Cohesion: 0.47
Nodes (5): main_loop(), Đọc giá trị trung bình từ cảm biến để chống nhiễu., Logic tưới nước an toàn., read_moisture(), start_irrigation()

### Community 8 - "Community 8"
Cohesion: 0.33
Nodes (1): SimpleFilteredStdout

### Community 9 - "Community 9"
Cohesion: 0.6
Nodes (3): call_ai_with_cycler(), process_single_conv(), slugify()

### Community 10 - "Community 10"
Cohesion: 0.4
Nodes (1): GeminiActivityDecoder

### Community 11 - "Community 11"
Cohesion: 0.5
Nodes (3): get_logger(), Logger toàn cục cho pipeline — dùng Rich để hiển thị màu sắc đẹp. Đồng thời ghi, Tạo và trả về logger chuẩn cho pipeline.      Args:         name: Tên logger

### Community 12 - "Community 12"
Cohesion: 0.5
Nodes (3): get_dynamic_free_workers(), LLM Discovery Engine — Tự động tìm kiếm và lọc các model miễn phí chất lượng cao, Lấy danh sách các model miễn phí chất lượng cao (>10B) từ OpenRouter.     Có cơ

### Community 13 - "Community 13"
Cohesion: 0.67
Nodes (2): ask_category(), organize_file()

### Community 14 - "Community 14"
Cohesion: 0.5
Nodes (3): download_font(), Script tải font DejaVu Sans hỗ trợ tiếng Việt về thư mục fonts/. Chạy một lần t, Tải font DejaVuSans.ttf về thư mục fonts/.

### Community 15 - "Community 15"
Cohesion: 0.67
Nodes (2): check_openrouter_health(), Kiểm tra xem IP có bị khóa (403) hoặc hết Quota (429) không.          Returns:

### Community 16 - "Community 16"
Cohesion: 0.67
Nodes (0): 

### Community 17 - "Community 17"
Cohesion: 1.0
Nodes (2): get_client(), main()

### Community 18 - "Community 18"
Cohesion: 1.0
Nodes (2): main(), run_step()

### Community 19 - "Community 19"
Cohesion: 1.0
Nodes (2): generate_summary(), split_markdown_into_parts()

### Community 20 - "Community 20"
Cohesion: 1.0
Nodes (0): 

### Community 21 - "Community 21"
Cohesion: 1.0
Nodes (0): 

### Community 22 - "Community 22"
Cohesion: 1.0
Nodes (0): 

### Community 23 - "Community 23"
Cohesion: 1.0
Nodes (0): 

### Community 24 - "Community 24"
Cohesion: 1.0
Nodes (0): 

### Community 25 - "Community 25"
Cohesion: 1.0
Nodes (0): 

### Community 26 - "Community 26"
Cohesion: 1.0
Nodes (1): Factory method tạo kết quả thành công.

### Community 27 - "Community 27"
Cohesion: 1.0
Nodes (1): Factory method tạo kết quả lỗi.

### Community 28 - "Community 28"
Cohesion: 1.0
Nodes (0): 

### Community 29 - "Community 29"
Cohesion: 1.0
Nodes (0): 

### Community 30 - "Community 30"
Cohesion: 1.0
Nodes (0): 

### Community 31 - "Community 31"
Cohesion: 1.0
Nodes (0): 

### Community 32 - "Community 32"
Cohesion: 1.0
Nodes (0): 

### Community 33 - "Community 33"
Cohesion: 1.0
Nodes (0): 

### Community 34 - "Community 34"
Cohesion: 1.0
Nodes (0): 

### Community 35 - "Community 35"
Cohesion: 1.0
Nodes (0): 

### Community 36 - "Community 36"
Cohesion: 1.0
Nodes (0): 

### Community 37 - "Community 37"
Cohesion: 1.0
Nodes (0): 

### Community 38 - "Community 38"
Cohesion: 1.0
Nodes (0): 

### Community 39 - "Community 39"
Cohesion: 1.0
Nodes (0): 

### Community 40 - "Community 40"
Cohesion: 1.0
Nodes (0): 

### Community 41 - "Community 41"
Cohesion: 1.0
Nodes (0): 

### Community 42 - "Community 42"
Cohesion: 1.0
Nodes (0): 

### Community 43 - "Community 43"
Cohesion: 1.0
Nodes (0): 

### Community 44 - "Community 44"
Cohesion: 1.0
Nodes (0): 

### Community 45 - "Community 45"
Cohesion: 1.0
Nodes (0): 

### Community 46 - "Community 46"
Cohesion: 1.0
Nodes (0): 

### Community 47 - "Community 47"
Cohesion: 1.0
Nodes (0): 

### Community 48 - "Community 48"
Cohesion: 1.0
Nodes (0): 

### Community 49 - "Community 49"
Cohesion: 1.0
Nodes (0): 

### Community 50 - "Community 50"
Cohesion: 1.0
Nodes (0): 

### Community 51 - "Community 51"
Cohesion: 1.0
Nodes (0): 

### Community 52 - "Community 52"
Cohesion: 1.0
Nodes (0): 

### Community 53 - "Community 53"
Cohesion: 1.0
Nodes (0): 

### Community 54 - "Community 54"
Cohesion: 1.0
Nodes (0): 

### Community 55 - "Community 55"
Cohesion: 1.0
Nodes (0): 

### Community 56 - "Community 56"
Cohesion: 1.0
Nodes (0): 

### Community 57 - "Community 57"
Cohesion: 1.0
Nodes (0): 

### Community 58 - "Community 58"
Cohesion: 1.0
Nodes (0): 

### Community 59 - "Community 59"
Cohesion: 1.0
Nodes (0): 

### Community 60 - "Community 60"
Cohesion: 1.0
Nodes (0): 

### Community 61 - "Community 61"
Cohesion: 1.0
Nodes (0): 

### Community 62 - "Community 62"
Cohesion: 1.0
Nodes (0): 

### Community 63 - "Community 63"
Cohesion: 1.0
Nodes (0): 

## Knowledge Gaps
- **32 isolated node(s):** `Kiểm tra xem IP có bị khóa (403) hoặc hết Quota (429) không.          Returns:`, `Logger toàn cục cho pipeline — dùng Rich để hiển thị màu sắc đẹp. Đồng thời ghi`, `Tạo và trả về logger chuẩn cho pipeline.      Args:         name: Tên logger`, `Rate Limiter — Quản lý delay giữa các request để tránh bị OpenRouter chặn.  Gi`, `Token bucket rate limiter đơn giản.      Đảm bảo không gửi quá N request trong` (+27 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 20`** (2 nodes): `graphify_bootstrap.py`, `bootstrap()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 21`** (2 nodes): `analyze_markdown.py`, `main()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 22`** (2 nodes): `debug_proxy.py`, `test_9router()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 23`** (2 nodes): `test_9router_distillation.py`, `test_distillation()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 24`** (1 nodes): `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 25`** (1 nodes): `diagnostic_env.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 26`** (1 nodes): `Factory method tạo kết quả thành công.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 27`** (1 nodes): `Factory method tạo kết quả lỗi.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 28`** (1 nodes): `debug_router_config.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 29`** (1 nodes): `AGENTS.md`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 30`** (1 nodes): `CLAUDE.md`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 31`** (1 nodes): `CONTINUITY.md`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 32`** (1 nodes): `progress.md`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 33`** (1 nodes): `README.md`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 34`** (1 nodes): `optimized_context.md`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 35`** (1 nodes): `AI_Agent_Performance_Optimization.md`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 36`** (1 nodes): `Claude_Code_Full_Course_2026.md`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 37`** (1 nodes): `DevOps_IT_Automation_Wiki.md`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 38`** (1 nodes): `Difficulty_Assessment_SOP.md`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 39`** (1 nodes): `ECC_CodyMaster_Hybrid_Philosophy.md`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 40`** (1 nodes): `Education_AI_Handbook.md`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 41`** (1 nodes): `Engineering_Robotics_Master.md`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 42`** (1 nodes): `Lesson_Plan_Templates.md`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 43`** (1 nodes): `Pedagogical_Master_DNA.md`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 44`** (1 nodes): `Prompt_Engineering_Master.md`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 45`** (1 nodes): `_index.md`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 46`** (1 nodes): `Biology_Epidemiology_G11.md`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 47`** (1 nodes): `Building_AI_Brain_G10.md`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 48`** (1 nodes): `Math_Advanced_Geometry_G10.md`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 49`** (1 nodes): `Physics_Electromagnetism_G10.md`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 50`** (1 nodes): `mcp_maintenance.md`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 51`** (1 nodes): `Antigravity_Obsidian_Memory_LOM.md`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 52`** (1 nodes): `ToT_Irrigation_Rubric.md`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 53`** (1 nodes): `ToT_IoT_Smart_Irrigation.md`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 54`** (1 nodes): `ToT_Prompt_Engineering_G10.md`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 55`** (1 nodes): `Gemini_English_Coach_G10.md`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 56`** (1 nodes): `Gemini_History_Specialist_G10.md`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 57`** (1 nodes): `Gemini_Literature_Tutor_G10.md`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 58`** (1 nodes): `Gemini_Math_Tutor_G10.md`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 59`** (1 nodes): `Gemini_Physics_Tutor_G10.md`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 60`** (1 nodes): `Daily_Recap_Template.md`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 61`** (1 nodes): `Note_Template.md`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 62`** (1 nodes): `Wiki_Article_Template.md`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 63`** (1 nodes): `README.md`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `ExponentialBackoff` connect `Community 0` to `Community 3`?**
  _High betweenness centrality (0.015) - this node is a cross-community bridge._
- **Are the 7 inferred relationships involving `ExponentialBackoff` (e.g. with `AllProvidersDownError` and `LLM Client — Wrapper gọi AI qua litellm với:   - Retry tự động (tenacity + expo`) actually correct?**
  _`ExponentialBackoff` has 7 INFERRED edges - model-reasoned connections that need verification._
- **Are the 3 inferred relationships involving `AllProvidersDownError` (e.g. with `call_worker()` and `call_validator()`) actually correct?**
  _`AllProvidersDownError` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `SyncManager` (e.g. with `Thực hiện đồng bộ dữ liệu từ Gemini (input/gemini_sync/) và tóm tắt chúng bằng A` and `Trả về nội dung ngữ cảnh đã được tinh lọc mới nhất.`) actually correct?**
  _`SyncManager` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Kiểm tra xem IP có bị khóa (403) hoặc hết Quota (429) không.          Returns:`, `Logger toàn cục cho pipeline — dùng Rich để hiển thị màu sắc đẹp. Đồng thời ghi`, `Tạo và trả về logger chuẩn cho pipeline.      Args:         name: Tên logger` to the rest of the system?**
  _32 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Community 2` be split into smaller, more focused modules?**
  _Cohesion score 0.13 - nodes in this community are weakly interconnected._