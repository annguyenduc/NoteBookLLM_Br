"""
Pedagogical pipeline orchestrator for the Swarm training workflow.
"""
from __future__ import annotations

from typing import Any, Dict, Optional

from libs.core.llm_client import (
    call_creative,
    call_designer,
    call_evaluator,
    call_pedagogical_engineer,
    call_profiler,
)
from libs.core.logger import get_logger
from libs.core.schemas import PipelineOutput


logger = get_logger("pedagogical_pipeline")


def _normalize_text_block(value: str) -> str:
    return value.strip() if value else ""


def build_profile_prompt(
    trainer_id: str,
    trainer_level: str,
    trainer_context: str,
    module_name: str,
) -> str:
    return (
        f"Trainer ID: {trainer_id}\n"
        f"Requested Level: {trainer_level}\n"
        f"Module: {module_name}\n"
        f"Trainer Context:\n{trainer_context}\n\n"
        "Hãy tạo Trainer Profile ngắn gọn gồm: level xác nhận, tóm tắt bối cảnh, "
        "điểm mạnh, khoảng trống năng lực, nhu cầu hỗ trợ, và khuyến nghị hành động tiếp theo."
    )


def build_design_prompt(
    module_name: str,
    trainer_level: str,
    profile_text: str,
    constraints: str = "",
) -> str:
    return (
        f"Module: {module_name}\n"
        f"Trainer Level: {trainer_level}\n"
        f"Trainer Profile:\n{profile_text}\n\n"
        f"Constraints:\n{constraints or 'Không có ràng buộc bổ sung.'}\n\n"
        "Hãy thiết kế Learning Design ngắn gọn gồm: mục tiêu học tập, learning sequence, "
        "scaffolding, hoạt động chính, đánh giá minh chứng, và lưu ý triển khai."
    )


def build_content_prompt(
    module_name: str,
    content_type: str,
    profile_text: str,
    design_text: str,
    extra_requirements: str = "",
) -> str:
    return (
        f"Module: {module_name}\n"
        f"Requested Content Type: {content_type}\n"
        f"Trainer Profile:\n{profile_text}\n\n"
        f"Learning Design:\n{design_text}\n\n"
        f"Extra Requirements:\n{extra_requirements or 'Không có yêu cầu bổ sung.'}\n\n"
        "Hãy tạo nội dung bám chặt vào Learning Design. "
        "Nếu là lesson outline thì xuất theo các phần rõ ràng; "
        "nếu là quiz hay worksheet thì trình bày theo định dạng dễ dùng lại."
    )


def build_evaluation_prompt(
    module_name: str,
    profile_text: str,
    design_text: str,
    learner_feedback: str,
) -> str:
    return (
        f"Module: {module_name}\n"
        f"Trainer Profile:\n{profile_text}\n\n"
        f"Learning Design:\n{design_text}\n\n"
        f"Feedback / Observations:\n{learner_feedback}\n\n"
        "Hãy đánh giá kết quả theo tư duy Kirkpatrick, chỉ ra knowledge gap, "
        "điểm nghẽn chính, và remediation path ưu tiên."
    )


def run_profiler_step(
    trainer_id: str,
    trainer_level: str,
    trainer_context: str,
    module_name: str,
    preset: Optional[str] = None,
) -> PipelineOutput:
    prompt = build_profile_prompt(trainer_id, trainer_level, trainer_context, module_name)
    try:
        content, actual_model = call_profiler([{"role": "user", "content": prompt}], preset=preset)
        return PipelineOutput.ok(
            data={
                "trainer_id": trainer_id,
                "module_name": module_name,
                "profile_text": content,
            },
            model=actual_model,
            notes="Profiler step completed.",
        )
    except Exception as exc:
        logger.error(f"Profiler step failed: {exc}")
        return PipelineOutput.fail(str(exc), notes="Profiler step failed.")


def run_designer_step(
    module_name: str,
    trainer_level: str,
    profile_text: str,
    constraints: str = "",
    preset: Optional[str] = None,
) -> PipelineOutput:
    prompt = build_design_prompt(module_name, trainer_level, profile_text, constraints=constraints)
    try:
        content, actual_model = call_designer([{"role": "user", "content": prompt}], preset=preset)
        return PipelineOutput.ok(
            data={
                "module_name": module_name,
                "learning_design_text": content,
            },
            model=actual_model,
            notes="Designer step completed.",
        )
    except Exception as exc:
        logger.error(f"Designer step failed: {exc}")
        return PipelineOutput.fail(str(exc), notes="Designer step failed.")


def run_engineer_step(
    module_name: str,
    content_type: str,
    profile_text: str,
    design_text: str,
    extra_requirements: str = "",
    preset: Optional[str] = None,
) -> PipelineOutput:
    prompt = build_content_prompt(
        module_name,
        content_type,
        profile_text,
        design_text,
        extra_requirements=extra_requirements,
    )
    try:
        content, actual_model = call_pedagogical_engineer([{"role": "user", "content": prompt}], preset=preset)
        return PipelineOutput.ok(
            data={
                "module_name": module_name,
                "content_type": content_type,
                "content_text": content,
            },
            model=actual_model,
            notes="Engineer step completed.",
        )
    except Exception as exc:
        logger.error(f"Engineer step failed: {exc}")
        return PipelineOutput.fail(str(exc), notes="Engineer step failed.")


def run_evaluator_step(
    module_name: str,
    profile_text: str,
    design_text: str,
    learner_feedback: str,
    preset: Optional[str] = None,
) -> PipelineOutput:
    prompt = build_evaluation_prompt(module_name, profile_text, design_text, learner_feedback)
    try:
        content, actual_model = call_evaluator([{"role": "user", "content": prompt}], preset=preset)
        return PipelineOutput.ok(
            data={
                "module_name": module_name,
                "evaluation_text": content,
            },
            model=actual_model,
            notes="Evaluator step completed.",
        )
    except Exception as exc:
        logger.error(f"Evaluator step failed: {exc}")
        return PipelineOutput.fail(str(exc), notes="Evaluator step failed.")


def run_creative_step(
    module_name: str,
    profile_text: str,
    design_text: str,
    scenario_goal: str,
    preset: Optional[str] = None,
) -> PipelineOutput:
    prompt = (
        f"Module: {module_name}\n"
        f"Trainer Profile:\n{profile_text}\n\n"
        f"Learning Design:\n{design_text}\n\n"
        f"Scenario Goal:\n{scenario_goal}\n\n"
        "Hãy tạo case study hoặc roleplay scenario hấp dẫn, thực tế, dễ dùng cho trainer."
    )
    try:
        content, actual_model = call_creative([{"role": "user", "content": prompt}], preset=preset)
        return PipelineOutput.ok(
            data={
                "module_name": module_name,
                "creative_text": content,
            },
            model=actual_model,
            notes="Creative step completed.",
        )
    except Exception as exc:
        logger.error(f"Creative step failed: {exc}")
        return PipelineOutput.fail(str(exc), notes="Creative step failed.")


def run_pedagogical_pipeline(
    trainer_id: str,
    trainer_level: str,
    trainer_context: str,
    module_name: str,
    content_type: str = "lesson_outline",
    constraints: str = "",
    extra_requirements: str = "",
    learner_feedback: str = "",
    include_evaluation: bool = False,
    preset: Optional[str] = None,
) -> Dict[str, PipelineOutput]:
    results: Dict[str, PipelineOutput] = {}

    profile_result = run_profiler_step(
        trainer_id=trainer_id,
        trainer_level=trainer_level,
        trainer_context=trainer_context,
        module_name=module_name,
        preset=preset,
    )
    results["profiler"] = profile_result
    if profile_result.status != "success":
        return results

    profile_text = _normalize_text_block(profile_result.data["profile_text"])
    designer_result = run_designer_step(
        module_name=module_name,
        trainer_level=trainer_level,
        profile_text=profile_text,
        constraints=constraints,
        preset=preset,
    )
    results["designer"] = designer_result
    if designer_result.status != "success":
        return results

    design_text = _normalize_text_block(designer_result.data["learning_design_text"])
    engineer_result = run_engineer_step(
        module_name=module_name,
        content_type=content_type,
        profile_text=profile_text,
        design_text=design_text,
        extra_requirements=extra_requirements,
        preset=preset,
    )
    results["engineer"] = engineer_result

    if include_evaluation and learner_feedback.strip():
        evaluator_result = run_evaluator_step(
            module_name=module_name,
            profile_text=profile_text,
            design_text=design_text,
            learner_feedback=learner_feedback,
            preset=preset,
        )
        results["evaluator"] = evaluator_result

    return results
