"""Contains the list of tasks available to fractal."""

from fractal_task_tools.task_models import (
    ParallelTask,
)

AUTHORS = "Maurice Kahnwald"


DOCS_LINK = "https://github.com/MauriceKahnwald/fractal-atmc-measurements"


TASK_LIST = [
    ParallelTask(
        name="ATMC Analysis Feature Extraction",
        executable="atmc_analysis_feature_extraction_task.py",
        # Modify the meta according to your task requirements
        # If the task requires a GPU, add "needs_gpu": True
        meta={"cpus_per_task": 1, "mem": 4000},
        category="Measurement",
        tags=["Region Properties", "Intensity", "Morphology"],
        docs_info="file:docs_info/atmc_analysis_feature_extraction_task.md",
    ),
]
