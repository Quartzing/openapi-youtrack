from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.backup_file import BackupFile
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    fields: Union[Unset, None, str] = "$type,creationDate,id,link,name,size",
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
        "url": "/admin/databaseBackup/backups",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["BackupFile"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = BackupFile.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["BackupFile"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, None, str] = "$type,creationDate,id,link,name,size",
    skip: Union[Unset, None, int] = UNSET,
    top: Union[Unset, None, int] = UNSET,
) -> Response[List["BackupFile"]]:
    """
    Args:
        fields (Union[Unset, None, str]):  Default: '$type,creationDate,id,link,name,size'.
            Example: $type,creationDate,id,link,name,size.
        skip (Union[Unset, None, int]):
        top (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['BackupFile']]
    """

    kwargs = _get_kwargs(
        fields=fields,
        skip=skip,
        top=top,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, None, str] = "$type,creationDate,id,link,name,size",
    skip: Union[Unset, None, int] = UNSET,
    top: Union[Unset, None, int] = UNSET,
) -> Optional[List["BackupFile"]]:
    """
    Args:
        fields (Union[Unset, None, str]):  Default: '$type,creationDate,id,link,name,size'.
            Example: $type,creationDate,id,link,name,size.
        skip (Union[Unset, None, int]):
        top (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['BackupFile']
    """

    return sync_detailed(
        client=client,
        fields=fields,
        skip=skip,
        top=top,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, None, str] = "$type,creationDate,id,link,name,size",
    skip: Union[Unset, None, int] = UNSET,
    top: Union[Unset, None, int] = UNSET,
) -> Response[List["BackupFile"]]:
    """
    Args:
        fields (Union[Unset, None, str]):  Default: '$type,creationDate,id,link,name,size'.
            Example: $type,creationDate,id,link,name,size.
        skip (Union[Unset, None, int]):
        top (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['BackupFile']]
    """

    kwargs = _get_kwargs(
        fields=fields,
        skip=skip,
        top=top,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, None, str] = "$type,creationDate,id,link,name,size",
    skip: Union[Unset, None, int] = UNSET,
    top: Union[Unset, None, int] = UNSET,
) -> Optional[List["BackupFile"]]:
    """
    Args:
        fields (Union[Unset, None, str]):  Default: '$type,creationDate,id,link,name,size'.
            Example: $type,creationDate,id,link,name,size.
        skip (Union[Unset, None, int]):
        top (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['BackupFile']
    """

    return (
        await asyncio_detailed(
            client=client,
            fields=fields,
            skip=skip,
            top=top,
        )
    ).parsed
