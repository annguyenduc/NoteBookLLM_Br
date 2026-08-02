"""
Schemas Pydantic chuẩn cho toàn bộ pipeline.
Mọi bước xử lý đều trả về PipelineOutput để đảm bảo tính nhất quán.
"""
from __future__ import annotations

from datetime import datetime
from typing import Any, List, Literal, Optional

from pydantic import BaseModel, Field


# -----------------------------------------------------------
# Schema nền tảng — dùng ở mọi bước
# -----------------------------------------------------------

class Meta(BaseModel):
    """Metadata đính kèm theo mỗi kết quả xử lý."""
    confidence: float = Field(default=1.0, ge=0.0, le=1.0)
    notes: str = ""
    model_used: str = ""
    timestamp: str = Field(
        default_factory=lambda: datetime.now().isoformat()
    )


class PipelineOutput(BaseModel):
    """
    Schema chuẩn bắt buộc cho mọi bước trong pipeline.

    Ví dụ kết quả thành công:
        {
            "status": "success",
            "data": { ... },
            "error": null,
            "meta": { "confidence": 0.95, "notes": "", "model_used": "qwen-..." }
        }

    Ví dụ khi lỗi:
        {
            "status": "error",
            "data": null,
            "error": "Không parse được JSON từ model",
            "meta": { "confidence": 0, "notes": "Lần retry thứ 2/3" }
        }
    """
    status: Literal["success", "error"]
    data: Any = None
    error: Optional[str] = None
    meta: Meta = Field(default_factory=Meta)

    @classmethod
    def ok(cls, data: Any, confidence: float = 1.0, notes: str = "", model: str = "") -> "PipelineOutput":
        """Factory method tạo kết quả thành công."""
        return cls(
            status="success",
            data=data,
            meta=Meta(confidence=confidence, notes=notes, model_used=model),
        )

    @classmethod
    def fail(cls, error: str, notes: str = "") -> "PipelineOutput":
        """Factory method tạo kết quả lỗi."""
        return cls(
            status="error",
            error=error,
            meta=Meta(confidence=0.0, notes=notes),
        )


# -----------------------------------------------------------
# Schema cho từng bước pipeline
# -----------------------------------------------------------

class TranslationChunk(BaseModel):
    """Một đoạn text đã được chia nhỏ — chờ dịch ở Step 3."""
    chunk_id: str          # Định danh duy nhất: f"{stem}_p{page}_{idx}"
    page: int              # Số trang trong PDF gốc (bắt đầu từ 1)
    index: int             # Vị trí chunk trong trang (bắt đầu từ 0)
    original: str          # Text gốc (tiếng Anh)
    token_count: int       # Số token ước tính (dùng tiktoken)


class TranslatedChunk(BaseModel):
    """Kết quả dịch đã hoàn chỉnh của một chunk."""
    chunk_id: str
    page: int
    index: int
    original: str
    translated: str
    validated: bool = False    # True nếu đã qua Step 5 kiểm chứng
    skipped: bool = False      # True nếu bị skip sau max_retries


class ValidationResult(BaseModel):
    """Kết quả kiểm chứng chất lượng dịch từ Step 5."""
    valid: bool
    score: float = Field(ge=0.0, le=1.0)
    reason: str = ""


class PipelineSummary(BaseModel):
    """Báo cáo tổng kết sau khi xử lý xong một file PDF."""
    input_file: str
    output_file: str
    total_pages: int
    total_chunks: int
    success_chunks: int
    failed_chunks: int
    skipped_chunks: int
    validated_chunks: int
    duration_seconds: float
    success_rate: float        # success_chunks / total_chunks
