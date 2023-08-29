from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    query: Union[Unset, None, str] = UNSET,
    custom_fields: Union[Unset, None, str] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "$type,created,customFields($type,id,name,value($type,id,name)),description,id,idReadable,links($type,direction,id,linkType($type,id,localizedName,name)),numberInProject,project($type,id,name,shortName),reporter($type,id,login,ringId),resolved,summary,updated,updater($type,id,login,ringId),visibility($type,id,permittedGroups($type,id,name,ringId),permittedUsers($type,id,login,ringId))",
    skip: Union[Unset, None, int] = UNSET,
    top: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["query"] = query

    params["customFields"] = custom_fields

    params["fields"] = fields

    params["$skip"] = skip

    params["$top"] = top

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/issues",
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
    query: Union[Unset, None, str] = UNSET,
    custom_fields: Union[Unset, None, str] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "$type,created,customFields($type,id,name,value($type,id,name)),description,id,idReadable,links($type,direction,id,linkType($type,id,localizedName,name)),numberInProject,project($type,id,name,shortName),reporter($type,id,login,ringId),resolved,summary,updated,updater($type,id,login,ringId),visibility($type,id,permittedGroups($type,id,name,ringId),permittedUsers($type,id,login,ringId))",
    skip: Union[Unset, None, int] = UNSET,
    top: Union[Unset, None, int] = UNSET,
) -> Response[Any]:
    """
    Args:
        query (Union[Unset, None, str]):
        custom_fields (Union[Unset, None, str]):
        fields (Union[Unset, None, str]):  Default: '$type,created,customFields($type,id,name,valu
            e($type,id,name)),description,id,idReadable,links($type,direction,id,linkType($type,id,loc
            alizedName,name)),numberInProject,project($type,id,name,shortName),reporter($type,id,login
            ,ringId),resolved,summary,updated,updater($type,id,login,ringId),visibility($type,id,permi
            ttedGroups($type,id,name,ringId),permittedUsers($type,id,login,ringId))'. Example: $type,c
            reated,customFields($type,id,name,value($type,id,name)),description,id,idReadable,links($t
            ype,direction,id,linkType($type,id,localizedName,name)),numberInProject,project($type,id,n
            ame,shortName),reporter($type,id,login,ringId),resolved,summary,updated,updater($type,id,l
            ogin,ringId),visibility($type,id,permittedGroups($type,id,name,ringId),permittedUsers($typ
            e,id,login,ringId)).
        skip (Union[Unset, None, int]):
        top (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        query=query,
        custom_fields=custom_fields,
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
    query: Union[Unset, None, str] = UNSET,
    custom_fields: Union[Unset, None, str] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "$type,created,customFields($type,id,name,value($type,id,name)),description,id,idReadable,links($type,direction,id,linkType($type,id,localizedName,name)),numberInProject,project($type,id,name,shortName),reporter($type,id,login,ringId),resolved,summary,updated,updater($type,id,login,ringId),visibility($type,id,permittedGroups($type,id,name,ringId),permittedUsers($type,id,login,ringId))",
    skip: Union[Unset, None, int] = UNSET,
    top: Union[Unset, None, int] = UNSET,
) -> Response[Any]:
    """
    Args:
        query (Union[Unset, None, str]):
        custom_fields (Union[Unset, None, str]):
        fields (Union[Unset, None, str]):  Default: '$type,created,customFields($type,id,name,valu
            e($type,id,name)),description,id,idReadable,links($type,direction,id,linkType($type,id,loc
            alizedName,name)),numberInProject,project($type,id,name,shortName),reporter($type,id,login
            ,ringId),resolved,summary,updated,updater($type,id,login,ringId),visibility($type,id,permi
            ttedGroups($type,id,name,ringId),permittedUsers($type,id,login,ringId))'. Example: $type,c
            reated,customFields($type,id,name,value($type,id,name)),description,id,idReadable,links($t
            ype,direction,id,linkType($type,id,localizedName,name)),numberInProject,project($type,id,n
            ame,shortName),reporter($type,id,login,ringId),resolved,summary,updated,updater($type,id,l
            ogin,ringId),visibility($type,id,permittedGroups($type,id,name,ringId),permittedUsers($typ
            e,id,login,ringId)).
        skip (Union[Unset, None, int]):
        top (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        query=query,
        custom_fields=custom_fields,
        fields=fields,
        skip=skip,
        top=top,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
