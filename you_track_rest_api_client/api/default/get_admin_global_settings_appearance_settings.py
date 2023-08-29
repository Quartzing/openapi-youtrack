from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.appearance_settings import AppearanceSettings
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    fields: Union[
        Unset, None, str
    ] = "$type,dateFieldFormat($type,datePattern,id,pattern,presentation),id,timeZone($type,id,offset,presentation)",
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["fields"] = fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/admin/globalSettings/appearanceSettings",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AppearanceSettings]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AppearanceSettings.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AppearanceSettings]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[
        Unset, None, str
    ] = "$type,dateFieldFormat($type,datePattern,id,pattern,presentation),id,timeZone($type,id,offset,presentation)",
) -> Response[AppearanceSettings]:
    """
    Args:
        fields (Union[Unset, None, str]):  Default: '$type,dateFieldFormat($type,datePattern,id,pa
            ttern,presentation),id,timeZone($type,id,offset,presentation)'. Example: $type,dateFieldFo
            rmat($type,datePattern,id,pattern,presentation),id,timeZone($type,id,offset,presentation).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppearanceSettings]
    """

    kwargs = _get_kwargs(
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[
        Unset, None, str
    ] = "$type,dateFieldFormat($type,datePattern,id,pattern,presentation),id,timeZone($type,id,offset,presentation)",
) -> Optional[AppearanceSettings]:
    """
    Args:
        fields (Union[Unset, None, str]):  Default: '$type,dateFieldFormat($type,datePattern,id,pa
            ttern,presentation),id,timeZone($type,id,offset,presentation)'. Example: $type,dateFieldFo
            rmat($type,datePattern,id,pattern,presentation),id,timeZone($type,id,offset,presentation).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppearanceSettings
    """

    return sync_detailed(
        client=client,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[
        Unset, None, str
    ] = "$type,dateFieldFormat($type,datePattern,id,pattern,presentation),id,timeZone($type,id,offset,presentation)",
) -> Response[AppearanceSettings]:
    """
    Args:
        fields (Union[Unset, None, str]):  Default: '$type,dateFieldFormat($type,datePattern,id,pa
            ttern,presentation),id,timeZone($type,id,offset,presentation)'. Example: $type,dateFieldFo
            rmat($type,datePattern,id,pattern,presentation),id,timeZone($type,id,offset,presentation).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppearanceSettings]
    """

    kwargs = _get_kwargs(
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[
        Unset, None, str
    ] = "$type,dateFieldFormat($type,datePattern,id,pattern,presentation),id,timeZone($type,id,offset,presentation)",
) -> Optional[AppearanceSettings]:
    """
    Args:
        fields (Union[Unset, None, str]):  Default: '$type,dateFieldFormat($type,datePattern,id,pa
            ttern,presentation),id,timeZone($type,id,offset,presentation)'. Example: $type,dateFieldFo
            rmat($type,datePattern,id,pattern,presentation),id,timeZone($type,id,offset,presentation).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppearanceSettings
    """

    return (
        await asyncio_detailed(
            client=client,
            fields=fields,
        )
    ).parsed
