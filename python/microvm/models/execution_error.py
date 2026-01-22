from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExecutionError")


@_attrs_define
class ExecutionError:
    """
    Attributes:
        type_ (str): Python exception type Example: RuntimeError.
        message (str): Error message Example: division by zero.
        line_number (Union[None, Unset, int]): Line number where error occurred (if available) Example: 2.
        traceback (Union[None, Unset, str]): Full Python traceback Example: Traceback (most recent call last):
              File "<string>", line 2, in divide
            ZeroDivisionError: division by zero.
    """

    type_: str
    message: str
    line_number: Union[None, Unset, int] = UNSET
    traceback: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        message = self.message

        line_number: Union[None, Unset, int]
        if isinstance(self.line_number, Unset):
            line_number = UNSET
        else:
            line_number = self.line_number

        traceback: Union[None, Unset, str]
        if isinstance(self.traceback, Unset):
            traceback = UNSET
        else:
            traceback = self.traceback

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "message": message,
            }
        )
        if line_number is not UNSET:
            field_dict["line_number"] = line_number
        if traceback is not UNSET:
            field_dict["traceback"] = traceback

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        message = d.pop("message")

        def _parse_line_number(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        line_number = _parse_line_number(d.pop("line_number", UNSET))

        def _parse_traceback(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        traceback = _parse_traceback(d.pop("traceback", UNSET))

        execution_error = cls(
            type_=type_,
            message=message,
            line_number=line_number,
            traceback=traceback,
        )

        execution_error.additional_properties = d
        return execution_error

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
