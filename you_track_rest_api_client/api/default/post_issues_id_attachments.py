from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_issues_id_attachments_multipart_data import PostIssuesIdAttachmentsMultipartData
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    multipart_data: PostIssuesIdAttachmentsMultipartData,
    mute_update_notifications: Union[Unset, None, bool] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "$type,author($type,id,login,ringId),charset,created,extension,id,metaData,mimeType,name,size,updated,url",
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["muteUpdateNotifications"] = mute_update_notifications

    params["fields"] = fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "method": "post",
        "url": "/issues/{id}/attachments".format(
            id=id,
        ),
        "files": multipart_multipart_data,
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
    multipart_data: PostIssuesIdAttachmentsMultipartData,
    mute_update_notifications: Union[Unset, None, bool] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "$type,author($type,id,login,ringId),charset,created,extension,id,metaData,mimeType,name,size,updated,url",
) -> Response[Any]:
    """
    Args:
        id (str):
        mute_update_notifications (Union[Unset, None, bool]):
        fields (Union[Unset, None, str]):  Default: '$type,author($type,id,login,ringId),charset,c
            reated,extension,id,metaData,mimeType,name,size,updated,url'. Example: $type,author($type,
            id,login,ringId),charset,created,extension,id,metaData,mimeType,name,size,updated,url.
        multipart_data (PostIssuesIdAttachmentsMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        multipart_data=multipart_data,
        mute_update_notifications=mute_update_notifications,
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
    multipart_data: PostIssuesIdAttachmentsMultipartData,
    mute_update_notifications: Union[Unset, None, bool] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "$type,author($type,id,login,ringId),charset,created,extension,id,metaData,mimeType,name,size,updated,url",
) -> Response[Any]:
    """
    Args:
        id (str):
        mute_update_notifications (Union[Unset, None, bool]):
        fields (Union[Unset, None, str]):  Default: '$type,author($type,id,login,ringId),charset,c
            reated,extension,id,metaData,mimeType,name,size,updated,url'. Example: $type,author($type,
            id,login,ringId),charset,created,extension,id,metaData,mimeType,name,size,updated,url.
        multipart_data (PostIssuesIdAttachmentsMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        multipart_data=multipart_data,
        mute_update_notifications=mute_update_notifications,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
