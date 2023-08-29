from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.state_bundle_element import StateBundleElement
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    fields: Union[
        Unset, None, str
    ] = "$type,color($type,background,foreground,id),id,isResolved,localizedName,name,ordinal",
    skip: Union[Unset, None, int] = UNSET,
    top: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["fields"] = fields

    params["$skip"] = skip

    params["$top"] = top

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/admin/customFieldSettings/bundles/state/{id}/values".format(
            id=id,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["StateBundleElement"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = StateBundleElement.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["StateBundleElement"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[
        Unset, None, str
    ] = "$type,color($type,background,foreground,id),id,isResolved,localizedName,name,ordinal",
    skip: Union[Unset, None, int] = UNSET,
    top: Union[Unset, None, int] = UNSET,
) -> Response[List["StateBundleElement"]]:
    """
    Args:
        id (str):
        fields (Union[Unset, None, str]):  Default:
            '$type,color($type,background,foreground,id),id,isResolved,localizedName,name,ordinal'.
            Example:
            $type,color($type,background,foreground,id),id,isResolved,localizedName,name,ordinal.
        skip (Union[Unset, None, int]):
        top (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['StateBundleElement']]
    """

    kwargs = _get_kwargs(
        id=id,
        fields=fields,
        skip=skip,
        top=top,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[
        Unset, None, str
    ] = "$type,color($type,background,foreground,id),id,isResolved,localizedName,name,ordinal",
    skip: Union[Unset, None, int] = UNSET,
    top: Union[Unset, None, int] = UNSET,
) -> Optional[List["StateBundleElement"]]:
    """
    Args:
        id (str):
        fields (Union[Unset, None, str]):  Default:
            '$type,color($type,background,foreground,id),id,isResolved,localizedName,name,ordinal'.
            Example:
            $type,color($type,background,foreground,id),id,isResolved,localizedName,name,ordinal.
        skip (Union[Unset, None, int]):
        top (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['StateBundleElement']
    """

    return sync_detailed(
        id=id,
        client=client,
        fields=fields,
        skip=skip,
        top=top,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[
        Unset, None, str
    ] = "$type,color($type,background,foreground,id),id,isResolved,localizedName,name,ordinal",
    skip: Union[Unset, None, int] = UNSET,
    top: Union[Unset, None, int] = UNSET,
) -> Response[List["StateBundleElement"]]:
    """
    Args:
        id (str):
        fields (Union[Unset, None, str]):  Default:
            '$type,color($type,background,foreground,id),id,isResolved,localizedName,name,ordinal'.
            Example:
            $type,color($type,background,foreground,id),id,isResolved,localizedName,name,ordinal.
        skip (Union[Unset, None, int]):
        top (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['StateBundleElement']]
    """

    kwargs = _get_kwargs(
        id=id,
        fields=fields,
        skip=skip,
        top=top,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[
        Unset, None, str
    ] = "$type,color($type,background,foreground,id),id,isResolved,localizedName,name,ordinal",
    skip: Union[Unset, None, int] = UNSET,
    top: Union[Unset, None, int] = UNSET,
) -> Optional[List["StateBundleElement"]]:
    """
    Args:
        id (str):
        fields (Union[Unset, None, str]):  Default:
            '$type,color($type,background,foreground,id),id,isResolved,localizedName,name,ordinal'.
            Example:
            $type,color($type,background,foreground,id),id,isResolved,localizedName,name,ordinal.
        skip (Union[Unset, None, int]):
        top (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['StateBundleElement']
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            fields=fields,
            skip=skip,
            top=top,
        )
    ).parsed
