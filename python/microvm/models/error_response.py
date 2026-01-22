from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_response_details import ErrorResponseDetails


T = TypeVar("T", bound="ErrorResponse")


@_attrs_define
class ErrorResponse:
    """
    Attributes:
        error (str): Error type/code Example: ValidationError.
        message (str): Human-readable error message Example: Invalid request parameters.
        details (Union[Unset, ErrorResponseDetails]): Additional error details
        request_id (Union[Unset, str]): Unique request identifier for debugging Example: req_abc123xyz.
    """

    error: str
    message: str
    details: Union[Unset, "ErrorResponseDetails"] = UNSET
    request_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error = self.error

        message = self.message

        details: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        request_id = self.request_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "error": error,
                "message": message,
            }
        )
        if details is not UNSET:
            field_dict["details"] = details
        if request_id is not UNSET:
            field_dict["request_id"] = request_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_response_details import ErrorResponseDetails

        d = dict(src_dict)
        error = d.pop("error")

        message = d.pop("message")

        _details = d.pop("details", UNSET)
        details: Union[Unset, ErrorResponseDetails]
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = ErrorResponseDetails.from_dict(_details)

        request_id = d.pop("request_id", UNSET)

        error_response = cls(
            error=error,
            message=message,
            details=details,
            request_id=request_id,
        )

        error_response.additional_properties = d
        return error_response

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
