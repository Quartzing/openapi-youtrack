from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    categories: Union[Unset, None, str] = UNSET,
    reverse: Union[Unset, None, bool] = UNSET,
    start: Union[Unset, None, str] = UNSET,
    end: Union[Unset, None, str] = UNSET,
    author: Union[Unset, None, str] = UNSET,
    issue_query: Union[Unset, None, str] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "$type,added,author($type,id,login,ringId),category($type,id),field($type,customField($type,fieldType($type,id),id,localizedName,name),id,name),id,removed,target,targetMember,timestamp",
    skip: Union[Unset, None, int] = UNSET,
    top: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["categories"] = categories

    params["reverse"] = reverse

    params["start"] = start

    params["end"] = end

    params["author"] = author

    params["issueQuery"] = issue_query

    params["fields"] = fields

    params["$skip"] = skip

    params["$top"] = top

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/activities",
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
    categories: Union[Unset, None, str] = UNSET,
    reverse: Union[Unset, None, bool] = UNSET,
    start: Union[Unset, None, str] = UNSET,
    end: Union[Unset, None, str] = UNSET,
    author: Union[Unset, None, str] = UNSET,
    issue_query: Union[Unset, None, str] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "$type,added,author($type,id,login,ringId),category($type,id),field($type,customField($type,fieldType($type,id),id,localizedName,name),id,name),id,removed,target,targetMember,timestamp",
    skip: Union[Unset, None, int] = UNSET,
    top: Union[Unset, None, int] = UNSET,
) -> Response[Any]:
    """
    Args:
        categories (Union[Unset, None, str]):
        reverse (Union[Unset, None, bool]):
        start (Union[Unset, None, str]):
        end (Union[Unset, None, str]):
        author (Union[Unset, None, str]):
        issue_query (Union[Unset, None, str]):
        fields (Union[Unset, None, str]):  Default: '$type,added,author($type,id,login,ringId),cat
            egory($type,id),field($type,customField($type,fieldType($type,id),id,localizedName,name),i
            d,name),id,removed,target,targetMember,timestamp'. Example: $type,added,author($type,id,lo
            gin,ringId),category($type,id),field($type,customField($type,fieldType($type,id),id,locali
            zedName,name),id,name),id,removed,target,targetMember,timestamp.
        skip (Union[Unset, None, int]):
        top (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        categories=categories,
        reverse=reverse,
        start=start,
        end=end,
        author=author,
        issue_query=issue_query,
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
    categories: Union[Unset, None, str] = UNSET,
    reverse: Union[Unset, None, bool] = UNSET,
    start: Union[Unset, None, str] = UNSET,
    end: Union[Unset, None, str] = UNSET,
    author: Union[Unset, None, str] = UNSET,
    issue_query: Union[Unset, None, str] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "$type,added,author($type,id,login,ringId),category($type,id),field($type,customField($type,fieldType($type,id),id,localizedName,name),id,name),id,removed,target,targetMember,timestamp",
    skip: Union[Unset, None, int] = UNSET,
    top: Union[Unset, None, int] = UNSET,
) -> Response[Any]:
    """
    Args:
        categories (Union[Unset, None, str]):
        reverse (Union[Unset, None, bool]):
        start (Union[Unset, None, str]):
        end (Union[Unset, None, str]):
        author (Union[Unset, None, str]):
        issue_query (Union[Unset, None, str]):
        fields (Union[Unset, None, str]):  Default: '$type,added,author($type,id,login,ringId),cat
            egory($type,id),field($type,customField($type,fieldType($type,id),id,localizedName,name),i
            d,name),id,removed,target,targetMember,timestamp'. Example: $type,added,author($type,id,lo
            gin,ringId),category($type,id),field($type,customField($type,fieldType($type,id),id,locali
            zedName,name),id,name),id,removed,target,targetMember,timestamp.
        skip (Union[Unset, None, int]):
        top (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        categories=categories,
        reverse=reverse,
        start=start,
        end=end,
        author=author,
        issue_query=issue_query,
        fields=fields,
        skip=skip,
        top=top,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
