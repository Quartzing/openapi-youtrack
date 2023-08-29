from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.locale_settings import LocaleSettings
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    json_body: LocaleSettings,
    fields: Union[Unset, None, str] = "$type,id,isRTL,locale($type,community,id,language,locale,name)",
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["fields"] = fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/admin/globalSettings/localeSettings",
        "json": json_json_body,
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[LocaleSettings]:
    if response.status_code == HTTPStatus.OK:
        response_200 = LocaleSettings.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[LocaleSettings]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: LocaleSettings,
    fields: Union[Unset, None, str] = "$type,id,isRTL,locale($type,community,id,language,locale,name)",
) -> Response[LocaleSettings]:
    """
    Args:
        fields (Union[Unset, None, str]):  Default:
            '$type,id,isRTL,locale($type,community,id,language,locale,name)'. Example:
            $type,id,isRTL,locale($type,community,id,language,locale,name).
        json_body (LocaleSettings):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LocaleSettings]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: LocaleSettings,
    fields: Union[Unset, None, str] = "$type,id,isRTL,locale($type,community,id,language,locale,name)",
) -> Optional[LocaleSettings]:
    """
    Args:
        fields (Union[Unset, None, str]):  Default:
            '$type,id,isRTL,locale($type,community,id,language,locale,name)'. Example:
            $type,id,isRTL,locale($type,community,id,language,locale,name).
        json_body (LocaleSettings):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LocaleSettings
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: LocaleSettings,
    fields: Union[Unset, None, str] = "$type,id,isRTL,locale($type,community,id,language,locale,name)",
) -> Response[LocaleSettings]:
    """
    Args:
        fields (Union[Unset, None, str]):  Default:
            '$type,id,isRTL,locale($type,community,id,language,locale,name)'. Example:
            $type,id,isRTL,locale($type,community,id,language,locale,name).
        json_body (LocaleSettings):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LocaleSettings]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: LocaleSettings,
    fields: Union[Unset, None, str] = "$type,id,isRTL,locale($type,community,id,language,locale,name)",
) -> Optional[LocaleSettings]:
    """
    Args:
        fields (Union[Unset, None, str]):  Default:
            '$type,id,isRTL,locale($type,community,id,language,locale,name)'. Example:
            $type,id,isRTL,locale($type,community,id,language,locale,name).
        json_body (LocaleSettings):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LocaleSettings
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            fields=fields,
        )
    ).parsed