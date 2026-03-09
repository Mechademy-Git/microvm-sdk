from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.execute_request import ExecuteRequest
from ...models.execute_response import ExecuteResponse
from ...types import Response


def _get_kwargs(
    *,
    body: ExecuteRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/execute",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, ExecuteResponse]]:
    if response.status_code == 200:
        response_200 = ExecuteResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 408:
        response_408 = ErrorResponse.from_dict(response.json())

        return response_408

    if response.status_code == 429:
        response_429 = ErrorResponse.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, ExecuteResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ExecuteRequest,
) -> Response[Union[ErrorResponse, ExecuteResponse]]:
    """Execute Python code

     Executes a Python function in a secure, isolated environment.

    ## Usage
    1. Provide Python code as a string
    2. Specify the function name to execute
    3. Pass arguments as positional args or kwargs
    4. Optionally set timeout and memory limits

    ## Limitations
    - Pure Python only, no external imports allowed by default
    - Maximum execution time: 60 seconds
    - No file system access
    - No network access
    - Restricted builtins

    Args:
        body (ExecuteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, ExecuteResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: ExecuteRequest,
) -> Optional[Union[ErrorResponse, ExecuteResponse]]:
    """Execute Python code

     Executes a Python function in a secure, isolated environment.

    ## Usage
    1. Provide Python code as a string
    2. Specify the function name to execute
    3. Pass arguments as positional args or kwargs
    4. Optionally set timeout and memory limits

    ## Limitations
    - Pure Python only, no external imports allowed by default
    - Maximum execution time: 60 seconds
    - No file system access
    - No network access
    - Restricted builtins

    Args:
        body (ExecuteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, ExecuteResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ExecuteRequest,
) -> Response[Union[ErrorResponse, ExecuteResponse]]:
    """Execute Python code

     Executes a Python function in a secure, isolated environment.

    ## Usage
    1. Provide Python code as a string
    2. Specify the function name to execute
    3. Pass arguments as positional args or kwargs
    4. Optionally set timeout and memory limits

    ## Limitations
    - Pure Python only, no external imports allowed by default
    - Maximum execution time: 60 seconds
    - No file system access
    - No network access
    - Restricted builtins

    Args:
        body (ExecuteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, ExecuteResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ExecuteRequest,
) -> Optional[Union[ErrorResponse, ExecuteResponse]]:
    """Execute Python code

     Executes a Python function in a secure, isolated environment.

    ## Usage
    1. Provide Python code as a string
    2. Specify the function name to execute
    3. Pass arguments as positional args or kwargs
    4. Optionally set timeout and memory limits

    ## Limitations
    - Pure Python only, no external imports allowed by default
    - Maximum execution time: 60 seconds
    - No file system access
    - No network access
    - Restricted builtins

    Args:
        body (ExecuteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, ExecuteResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
