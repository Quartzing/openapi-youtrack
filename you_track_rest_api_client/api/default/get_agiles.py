from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    fields: Union[
        Unset, None, str
    ] = "$type,columnSettings($type,columns($type,id),field($type,fieldType($type,id),id,localizedName,name),id),id,name,owner($type,id,login,ringId),projects($type,id,name,shortName),status($type,id,valid),swimlaneSettings($type,enabled,field($type,customField($type,fieldType($type,id),id,localizedName,name),id,name),id,values($type,id,name))",
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
        "url": "/agiles",
        "params": params,
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
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
    ] = "$type,columnSettings($type,columns($type,id),field($type,fieldType($type,id),id,localizedName,name),id),id,name,owner($type,id,login,ringId),projects($type,id,name,shortName),status($type,id,valid),swimlaneSettings($type,enabled,field($type,customField($type,fieldType($type,id),id,localizedName,name),id,name),id,values($type,id,name))",
    skip: Union[Unset, None, int] = UNSET,
    top: Union[Unset, None, int] = UNSET,
) -> Response[Any]:
    """
    Args:
        fields (Union[Unset, None, str]):  Default: '$type,columnSettings($type,columns($type,id),
            field($type,fieldType($type,id),id,localizedName,name),id),id,name,owner($type,id,login,ri
            ngId),projects($type,id,name,shortName),status($type,id,valid),swimlaneSettings($type,enab
            led,field($type,customField($type,fieldType($type,id),id,localizedName,name),id,name),id,v
            alues($type,id,name))'. Example: $type,columnSettings($type,columns($type,id),field($type,
            fieldType($type,id),id,localizedName,name),id),id,name,owner($type,id,login,ringId),projec
            ts($type,id,name,shortName),status($type,id,valid),swimlaneSettings($type,enabled,field($t
            ype,customField($type,fieldType($type,id),id,localizedName,name),id,name),id,values($type,
            id,name)).
        skip (Union[Unset, None, int]):
        top (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
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


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[
        Unset, None, str
    ] = "$type,columnSettings($type,columns($type,id),field($type,fieldType($type,id),id,localizedName,name),id),id,name,owner($type,id,login,ringId),projects($type,id,name,shortName),status($type,id,valid),swimlaneSettings($type,enabled,field($type,customField($type,fieldType($type,id),id,localizedName,name),id,name),id,values($type,id,name))",
    skip: Union[Unset, None, int] = UNSET,
    top: Union[Unset, None, int] = UNSET,
) -> Response[Any]:
    """
    Args:
        fields (Union[Unset, None, str]):  Default: '$type,columnSettings($type,columns($type,id),
            field($type,fieldType($type,id),id,localizedName,name),id),id,name,owner($type,id,login,ri
            ngId),projects($type,id,name,shortName),status($type,id,valid),swimlaneSettings($type,enab
            led,field($type,customField($type,fieldType($type,id),id,localizedName,name),id,name),id,v
            alues($type,id,name))'. Example: $type,columnSettings($type,columns($type,id),field($type,
            fieldType($type,id),id,localizedName,name),id),id,name,owner($type,id,login,ringId),projec
            ts($type,id,name,shortName),status($type,id,valid),swimlaneSettings($type,enabled,field($t
            ype,customField($type,fieldType($type,id),id,localizedName,name),id,name),id,values($type,
            id,name)).
        skip (Union[Unset, None, int]):
        top (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        fields=fields,
        skip=skip,
        top=top,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
