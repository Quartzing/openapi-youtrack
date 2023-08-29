from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.license_ import License
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    json_body: License,
    fields: Union[Unset, None, str] = "$type,error,id,license,username",
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["fields"] = fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/admin/globalSettings/license",
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[License]:
    if response.status_code == HTTPStatus.OK:
        response_200 = License.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[License]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: License,
    fields: Union[Unset, None, str] = "$type,error,id,license,username",
) -> Response[License]:
    """
    Args:
        fields (Union[Unset, None, str]):  Default: '$type,error,id,license,username'. Example:
            $type,error,id,license,username.
        json_body (License):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[License]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: License,
    fields: Union[Unset, None, str] = "$type,error,id,license,username",
) -> Optional[License]:
    """
    Args:
        fields (Union[Unset, None, str]):  Default: '$type,error,id,license,username'. Example:
            $type,error,id,license,username.
        json_body (License):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        License
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: License,
    fields: Union[Unset, None, str] = "$type,error,id,license,username",
) -> Response[License]:
    """
    Args:
        fields (Union[Unset, None, str]):  Default: '$type,error,id,license,username'. Example:
            $type,error,id,license,username.
        json_body (License):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[License]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: License,
    fields: Union[Unset, None, str] = "$type,error,id,license,username",
) -> Optional[License]:
    """
    Args:
        fields (Union[Unset, None, str]):  Default: '$type,error,id,license,username'. Example:
            $type,error,id,license,username.
        json_body (License):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        License
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            fields=fields,
        )
    ).parsed
