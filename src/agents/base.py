"""Shared lightweight protocol types for the unified agent repo."""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class AgentExecutionResult:
    status: str
    payload: dict[str, Any] = field(default_factory=dict)

