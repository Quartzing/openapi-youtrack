from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.version_bundle_element import VersionBundleElement
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    fields: Union[
        Unset, None, str
    ] = "$type,archived,color($type,background,foreground,id),id,name,ordinal,releaseDate,released",
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
        "url": "/admin/customFieldSettings/bundles/version/{id}/values".format(
            id=id,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["VersionBundleElement"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = VersionBundleElement.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["VersionBundleElement"]]:
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
    ] = "$type,archived,color($type,background,foreground,id),id,name,ordinal,releaseDate,released",
    skip: Union[Unset, None, int] = UNSET,
    top: Union[Unset, None, int] = UNSET,
) -> Response[List["VersionBundleElement"]]:
    """
    Args:
        id (str):
        fields (Union[Unset, None, str]):  Default: '$type,archived,color($type,background,foregro
            und,id),id,name,ordinal,releaseDate,released'. Example:
            $type,archived,color($type,background,foreground,id),id,name,ordinal,releaseDate,released.
        skip (Union[Unset, None, int]):
        top (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['VersionBundleElement']]
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
    ] = "$type,archived,color($type,background,foreground,id),id,name,ordinal,releaseDate,released",
    skip: Union[Unset, None, int] = UNSET,
    top: Union[Unset, None, int] = UNSET,
) -> Optional[List["VersionBundleElement"]]:
    """
    Args:
        id (str):
        fields (Union[Unset, None, str]):  Default: '$type,archived,color($type,background,foregro
            und,id),id,name,ordinal,releaseDate,released'. Example:
            $type,archived,color($type,background,foreground,id),id,name,ordinal,releaseDate,released.
        skip (Union[Unset, None, int]):
        top (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['VersionBundleElement']
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
    ] = "$type,archived,color($type,background,foreground,id),id,name,ordinal,releaseDate,released",
    skip: Union[Unset, None, int] = UNSET,
    top: Union[Unset, None, int] = UNSET,
) -> Response[List["VersionBundleElement"]]:
    """
    Args:
        id (str):
        fields (Union[Unset, None, str]):  Default: '$type,archived,color($type,background,foregro
            und,id),id,name,ordinal,releaseDate,released'. Example:
            $type,archived,color($type,background,foreground,id),id,name,ordinal,releaseDate,released.
        skip (Union[Unset, None, int]):
        top (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['VersionBundleElement']]
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
    ] = "$type,archived,color($type,background,foreground,id),id,name,ordinal,releaseDate,released",
    skip: Union[Unset, None, int] = UNSET,
    top: Union[Unset, None, int] = UNSET,
) -> Optional[List["VersionBundleElement"]]:
    """
    Args:
        id (str):
        fields (Union[Unset, None, str]):  Default: '$type,archived,color($type,background,foregro
            und,id),id,name,ordinal,releaseDate,released'. Example:
            $type,archived,color($type,background,foreground,id),id,name,ordinal,releaseDate,released.
        skip (Union[Unset, None, int]):
        top (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['VersionBundleElement']
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
