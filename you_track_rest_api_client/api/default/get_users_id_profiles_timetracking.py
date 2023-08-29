from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.time_tracking_user_profile import TimeTrackingUserProfile
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    fields: Union[Unset, None, str] = "$type,id,periodFormat($type,id)",
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["fields"] = fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/users/{id}/profiles/timetracking".format(
            id=id,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[TimeTrackingUserProfile]:
    if response.status_code == HTTPStatus.OK:
        response_200 = TimeTrackingUserProfile.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[TimeTrackingUserProfile]:
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
    fields: Union[Unset, None, str] = "$type,id,periodFormat($type,id)",
) -> Response[TimeTrackingUserProfile]:
    """
    Args:
        id (str):
        fields (Union[Unset, None, str]):  Default: '$type,id,periodFormat($type,id)'. Example:
            $type,id,periodFormat($type,id).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TimeTrackingUserProfile]
    """

    kwargs = _get_kwargs(
        id=id,
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
    fields: Union[Unset, None, str] = "$type,id,periodFormat($type,id)",
) -> Optional[TimeTrackingUserProfile]:
    """
    Args:
        id (str):
        fields (Union[Unset, None, str]):  Default: '$type,id,periodFormat($type,id)'. Example:
            $type,id,periodFormat($type,id).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TimeTrackingUserProfile
    """

    return sync_detailed(
        id=id,
        client=client,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, None, str] = "$type,id,periodFormat($type,id)",
) -> Response[TimeTrackingUserProfile]:
    """
    Args:
        id (str):
        fields (Union[Unset, None, str]):  Default: '$type,id,periodFormat($type,id)'. Example:
            $type,id,periodFormat($type,id).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TimeTrackingUserProfile]
    """

    kwargs = _get_kwargs(
        id=id,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, None, str] = "$type,id,periodFormat($type,id)",
) -> Optional[TimeTrackingUserProfile]:
    """
    Args:
        id (str):
        fields (Union[Unset, None, str]):  Default: '$type,id,periodFormat($type,id)'. Example:
            $type,id,periodFormat($type,id).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TimeTrackingUserProfile
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            fields=fields,
        )
    ).parsed
