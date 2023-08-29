from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    categories: Union[Unset, None, str] = UNSET,
    reverse: Union[Unset, None, bool] = UNSET,
    start: Union[Unset, None, str] = UNSET,
    end: Union[Unset, None, str] = UNSET,
    author: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, str] = UNSET,
    activity_id: Union[Unset, None, str] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "$type,activities($type,added,author($type,id,login,ringId),category($type,id),field($type,customField($type,fieldType($type,id),id,localizedName,name),id,name),id,removed,target,targetMember,timestamp),afterCursor,beforeCursor,hasAfter,hasBefore,id",
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["categories"] = categories

    params["reverse"] = reverse

    params["start"] = start

    params["end"] = end

    params["author"] = author

    params["cursor"] = cursor

    params["activityId"] = activity_id

    params["fields"] = fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/issues/{id}/activitiesPage".format(
            id=id,
        ),
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
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    categories: Union[Unset, None, str] = UNSET,
    reverse: Union[Unset, None, bool] = UNSET,
    start: Union[Unset, None, str] = UNSET,
    end: Union[Unset, None, str] = UNSET,
    author: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, str] = UNSET,
    activity_id: Union[Unset, None, str] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "$type,activities($type,added,author($type,id,login,ringId),category($type,id),field($type,customField($type,fieldType($type,id),id,localizedName,name),id,name),id,removed,target,targetMember,timestamp),afterCursor,beforeCursor,hasAfter,hasBefore,id",
) -> Response[Any]:
    """
    Args:
        id (str):
        categories (Union[Unset, None, str]):
        reverse (Union[Unset, None, bool]):
        start (Union[Unset, None, str]):
        end (Union[Unset, None, str]):
        author (Union[Unset, None, str]):
        cursor (Union[Unset, None, str]):
        activity_id (Union[Unset, None, str]):
        fields (Union[Unset, None, str]):  Default: '$type,activities($type,added,author($type,id,
            login,ringId),category($type,id),field($type,customField($type,fieldType($type,id),id,loca
            lizedName,name),id,name),id,removed,target,targetMember,timestamp),afterCursor,beforeCurso
            r,hasAfter,hasBefore,id'. Example: $type,activities($type,added,author($type,id,login,ring
            Id),category($type,id),field($type,customField($type,fieldType($type,id),id,localizedName,
            name),id,name),id,removed,target,targetMember,timestamp),afterCursor,beforeCursor,hasAfter
            ,hasBefore,id.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        categories=categories,
        reverse=reverse,
        start=start,
        end=end,
        author=author,
        cursor=cursor,
        activity_id=activity_id,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    categories: Union[Unset, None, str] = UNSET,
    reverse: Union[Unset, None, bool] = UNSET,
    start: Union[Unset, None, str] = UNSET,
    end: Union[Unset, None, str] = UNSET,
    author: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, str] = UNSET,
    activity_id: Union[Unset, None, str] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "$type,activities($type,added,author($type,id,login,ringId),category($type,id),field($type,customField($type,fieldType($type,id),id,localizedName,name),id,name),id,removed,target,targetMember,timestamp),afterCursor,beforeCursor,hasAfter,hasBefore,id",
) -> Response[Any]:
    """
    Args:
        id (str):
        categories (Union[Unset, None, str]):
        reverse (Union[Unset, None, bool]):
        start (Union[Unset, None, str]):
        end (Union[Unset, None, str]):
        author (Union[Unset, None, str]):
        cursor (Union[Unset, None, str]):
        activity_id (Union[Unset, None, str]):
        fields (Union[Unset, None, str]):  Default: '$type,activities($type,added,author($type,id,
            login,ringId),category($type,id),field($type,customField($type,fieldType($type,id),id,loca
            lizedName,name),id,name),id,removed,target,targetMember,timestamp),afterCursor,beforeCurso
            r,hasAfter,hasBefore,id'. Example: $type,activities($type,added,author($type,id,login,ring
            Id),category($type,id),field($type,customField($type,fieldType($type,id),id,localizedName,
            name),id,name),id,removed,target,targetMember,timestamp),afterCursor,beforeCursor,hasAfter
            ,hasBefore,id.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        categories=categories,
        reverse=reverse,
        start=start,
        end=end,
        author=author,
        cursor=cursor,
        activity_id=activity_id,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
