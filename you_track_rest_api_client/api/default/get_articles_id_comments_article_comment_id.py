from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    article_comment_id: str,
    *,
    fields: Union[
        Unset, None, str
    ] = "$type,attachments($type,id),author($type,id,login,ringId),created,id,text,updated,visibility($type,id,permittedGroups($type,id,name,ringId),permittedUsers($type,id,login,ringId))",
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["fields"] = fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/articles/{id}/comments/{articleCommentId}".format(
            id=id,
            articleCommentId=article_comment_id,
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
    article_comment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[
        Unset, None, str
    ] = "$type,attachments($type,id),author($type,id,login,ringId),created,id,text,updated,visibility($type,id,permittedGroups($type,id,name,ringId),permittedUsers($type,id,login,ringId))",
) -> Response[Any]:
    """
    Args:
        id (str):
        article_comment_id (str):
        fields (Union[Unset, None, str]):  Default: '$type,attachments($type,id),author($type,id,l
            ogin,ringId),created,id,text,updated,visibility($type,id,permittedGroups($type,id,name,rin
            gId),permittedUsers($type,id,login,ringId))'. Example: $type,attachments($type,id),author(
            $type,id,login,ringId),created,id,text,updated,visibility($type,id,permittedGroups($type,i
            d,name,ringId),permittedUsers($type,id,login,ringId)).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        article_comment_id=article_comment_id,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    id: str,
    article_comment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[
        Unset, None, str
    ] = "$type,attachments($type,id),author($type,id,login,ringId),created,id,text,updated,visibility($type,id,permittedGroups($type,id,name,ringId),permittedUsers($type,id,login,ringId))",
) -> Response[Any]:
    """
    Args:
        id (str):
        article_comment_id (str):
        fields (Union[Unset, None, str]):  Default: '$type,attachments($type,id),author($type,id,l
            ogin,ringId),created,id,text,updated,visibility($type,id,permittedGroups($type,id,name,rin
            gId),permittedUsers($type,id,login,ringId))'. Example: $type,attachments($type,id),author(
            $type,id,login,ringId),created,id,text,updated,visibility($type,id,permittedGroups($type,i
            d,name,ringId),permittedUsers($type,id,login,ringId)).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        article_comment_id=article_comment_id,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
