"""
PromptOptimizer: Automated prompt testing and optimization system.

This module extends LLMOps-Eval with systematic prompt engineering capabilities,
including A/B testing, statistical analysis, and automated prompt optimization.
"""

__version__ = "0.1.0"

# Config
from src.llmops_eval.prompt_optimizer.config import (
    OptimizerSettings,
    get_optimizer_settings,
    optimizer_settings,
)

# Templates
from src.llmops_eval.prompt_optimizer.templates import (
    PromptTemplate,
    TemplateManager,
    create_template_manager,
)

# Variations
from src.llmops_eval.prompt_optimizer.variations import (
    VariationGenerator,
    PromptVariation,
    VariationSet,
    create_variation_generator,
)

# Experiments
from src.llmops_eval.prompt_optimizer.experiments import (
    ExperimentFramework,
    ExperimentConfig,
    ExperimentResult,
    ABTester,
    create_experiment_framework,
)

# Statistics
from src.llmops_eval.prompt_optimizer.statistics import (
    StatisticalTests,
    MultipleComparisonCorrection,
)

# Selection
from src.llmops_eval.prompt_optimizer.selection import (
    PromptSelector,
    PromptRanker,
    SelectionResult,
    RankingResult,
)

__all__ = [
    # Version
    "__version__",
    # Config
    "OptimizerSettings",
    "get_optimizer_settings",
    "optimizer_settings",
    # Templates
    "PromptTemplate",
    "TemplateManager",
    "create_template_manager",
    # Variations
    "VariationGenerator",
    "PromptVariation",
    "VariationSet",
    "create_variation_generator",
    # Experiments
    "ExperimentFramework",
    "ExperimentConfig",
    "ExperimentResult",
    "ABTester",
    "create_experiment_framework",
    # Statistics
    "StatisticalTests",
    "MultipleComparisonCorrection",
    # Selection
    "PromptSelector",
    "PromptRanker",
    "SelectionResult",
    "RankingResult",
]

