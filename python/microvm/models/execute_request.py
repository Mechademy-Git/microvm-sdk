from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.execute_request_args_item import ExecuteRequestArgsItem
    from ..models.execute_request_kwargs import ExecuteRequestKwargs


T = TypeVar("T", bound="ExecuteRequest")


@_attrs_define
class ExecuteRequest:
    """
    Attributes:
        code (str): Python code containing the function to execute Example: def add(a, b):
                return a + b.
        function_name (str): Name of the function to call from the provided code Example: add.
        args (Union[Unset, list['ExecuteRequestArgsItem']]): Positional arguments to pass to the function Example: [1,
            2].
        kwargs (Union[Unset, ExecuteRequestKwargs]): Keyword arguments to pass to the function Example: {'param1':
            'value'}.
        timeout (Union[Unset, int]): Maximum execution time in seconds Default: 30. Example: 30.
        memory_mb (Union[Unset, int]): Memory limit in megabytes (informational, actual limit set by Lambda) Default:
            512. Example: 512.
    """

    code: str
    function_name: str
    args: Union[Unset, list["ExecuteRequestArgsItem"]] = UNSET
    kwargs: Union[Unset, "ExecuteRequestKwargs"] = UNSET
    timeout: Union[Unset, int] = 30
    memory_mb: Union[Unset, int] = 512
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        function_name = self.function_name

        args: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.args, Unset):
            args = []
            for args_item_data in self.args:
                args_item = args_item_data.to_dict()
                args.append(args_item)

        kwargs: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.kwargs, Unset):
            kwargs = self.kwargs.to_dict()

        timeout = self.timeout

        memory_mb = self.memory_mb

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "function_name": function_name,
            }
        )
        if args is not UNSET:
            field_dict["args"] = args
        if kwargs is not UNSET:
            field_dict["kwargs"] = kwargs
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if memory_mb is not UNSET:
            field_dict["memory_mb"] = memory_mb

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execute_request_args_item import ExecuteRequestArgsItem
        from ..models.execute_request_kwargs import ExecuteRequestKwargs

        d = dict(src_dict)
        code = d.pop("code")

        function_name = d.pop("function_name")

        args = []
        _args = d.pop("args", UNSET)
        for args_item_data in _args or []:
            args_item = ExecuteRequestArgsItem.from_dict(args_item_data)

            args.append(args_item)

        _kwargs = d.pop("kwargs", UNSET)
        kwargs: Union[Unset, ExecuteRequestKwargs]
        if isinstance(_kwargs, Unset):
            kwargs = UNSET
        else:
            kwargs = ExecuteRequestKwargs.from_dict(_kwargs)

        timeout = d.pop("timeout", UNSET)

        memory_mb = d.pop("memory_mb", UNSET)

        execute_request = cls(
            code=code,
            function_name=function_name,
            args=args,
            kwargs=kwargs,
            timeout=timeout,
            memory_mb=memory_mb,
        )

        execute_request.additional_properties = d
        return execute_request

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
