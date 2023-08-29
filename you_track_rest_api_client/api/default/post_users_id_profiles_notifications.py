from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.notifications_user_profile import NotificationsUserProfile
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    json_body: NotificationsUserProfile,
    fields: Union[Unset, None, str] = "$type,id",
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["fields"] = fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/users/{id}/profiles/notifications".format(
            id=id,
        ),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[NotificationsUserProfile]:
    if response.status_code == HTTPStatus.OK:
        response_200 = NotificationsUserProfile.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[NotificationsUserProfile]:
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
    json_body: NotificationsUserProfile,
    fields: Union[Unset, None, str] = "$type,id",
) -> Response[NotificationsUserProfile]:
    """
    Args:
        id (str):
        fields (Union[Unset, None, str]):  Default: '$type,id'. Example: $type,id.
        json_body (NotificationsUserProfile):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NotificationsUserProfile]
    """

    kwargs = _get_kwargs(
        id=id,
        json_body=json_body,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: NotificationsUserProfile,
    fields: Union[Unset, None, str] = "$type,id",
) -> Optional[NotificationsUserProfile]:
    """
    Args:
        id (str):
        fields (Union[Unset, None, str]):  Default: '$type,id'. Example: $type,id.
        json_body (NotificationsUserProfile):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NotificationsUserProfile
    """

    return sync_detailed(
        id=id,
        client=client,
        json_body=json_body,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: NotificationsUserProfile,
    fields: Union[Unset, None, str] = "$type,id",
) -> Response[NotificationsUserProfile]:
    """
    Args:
        id (str):
        fields (Union[Unset, None, str]):  Default: '$type,id'. Example: $type,id.
        json_body (NotificationsUserProfile):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NotificationsUserProfile]
    """

    kwargs = _get_kwargs(
        id=id,
        json_body=json_body,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: NotificationsUserProfile,
    fields: Union[Unset, None, str] = "$type,id",
) -> Optional[NotificationsUserProfile]:
    """
    Args:
        id (str):
        fields (Union[Unset, None, str]):  Default: '$type,id'. Example: $type,id.
        json_body (NotificationsUserProfile):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NotificationsUserProfile
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            json_body=json_body,
            fields=fields,
        )
    ).parsed
