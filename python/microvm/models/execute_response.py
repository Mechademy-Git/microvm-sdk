from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.execution_error import ExecutionError


T = TypeVar("T", bound="ExecuteResponse")


@_attrs_define
class ExecuteResponse:
    """
    Attributes:
        success (bool): Whether the code executed successfully Example: True.
        execution_time_ms (float): Execution time in milliseconds Example: 12.5.
        memory_used_mb (float): Peak memory usage in megabytes Example: 45.2.
        output (Union[Unset, Any]): The return value from the executed function
        error (Union[Unset, ExecutionError]):
        stdout (Union[Unset, str]): Standard output captured during execution Default: ''.
        stderr (Union[Unset, str]): Standard error captured during execution Default: ''.
    """

    success: bool
    execution_time_ms: float
    memory_used_mb: float
    output: Union[Unset, Any] = UNSET
    error: Union[Unset, "ExecutionError"] = UNSET
    stdout: Union[Unset, str] = ""
    stderr: Union[Unset, str] = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        execution_time_ms = self.execution_time_ms

        memory_used_mb = self.memory_used_mb

        output = self.output

        error: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        stdout = self.stdout

        stderr = self.stderr

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "execution_time_ms": execution_time_ms,
                "memory_used_mb": memory_used_mb,
            }
        )
        if output is not UNSET:
            field_dict["output"] = output
        if error is not UNSET:
            field_dict["error"] = error
        if stdout is not UNSET:
            field_dict["stdout"] = stdout
        if stderr is not UNSET:
            field_dict["stderr"] = stderr

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execution_error import ExecutionError

        d = dict(src_dict)
        success = d.pop("success")

        execution_time_ms = d.pop("execution_time_ms")

        memory_used_mb = d.pop("memory_used_mb")

        output = d.pop("output", UNSET)

        _error = d.pop("error", UNSET)
        error: Union[Unset, ExecutionError]
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = ExecutionError.from_dict(_error)

        stdout = d.pop("stdout", UNSET)

        stderr = d.pop("stderr", UNSET)

        execute_response = cls(
            success=success,
            execution_time_ms=execution_time_ms,
            memory_used_mb=memory_used_mb,
            output=output,
            error=error,
            stdout=stdout,
            stderr=stderr,
        )

        execute_response.additional_properties = d
        return execute_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
