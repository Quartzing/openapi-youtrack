from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.enum_bundle_element import EnumBundleElement
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    enum_bundle_element_id: str,
    *,
    fields: Union[Unset, None, str] = "$type,color($type,background,foreground,id),id,localizedName,name,ordinal",
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["fields"] = fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/admin/customFieldSettings/bundles/enum/{id}/values/{enumBundleElementId}".format(
            id=id,
            enumBundleElementId=enum_bundle_element_id,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[EnumBundleElement]:
    if response.status_code == HTTPStatus.OK:
        response_200 = EnumBundleElement.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[EnumBundleElement]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    enum_bundle_element_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, None, str] = "$type,color($type,background,foreground,id),id,localizedName,name,ordinal",
) -> Response[EnumBundleElement]:
    """
    Args:
        id (str):
        enum_bundle_element_id (str):
        fields (Union[Unset, None, str]):  Default:
            '$type,color($type,background,foreground,id),id,localizedName,name,ordinal'. Example:
            $type,color($type,background,foreground,id),id,localizedName,name,ordinal.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EnumBundleElement]
    """

    kwargs = _get_kwargs(
        id=id,
        enum_bundle_element_id=enum_bundle_element_id,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    enum_bundle_element_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, None, str] = "$type,color($type,background,foreground,id),id,localizedName,name,ordinal",
) -> Optional[EnumBundleElement]:
    """
    Args:
        id (str):
        enum_bundle_element_id (str):
        fields (Union[Unset, None, str]):  Default:
            '$type,color($type,background,foreground,id),id,localizedName,name,ordinal'. Example:
            $type,color($type,background,foreground,id),id,localizedName,name,ordinal.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EnumBundleElement
    """

    return sync_detailed(
        id=id,
        enum_bundle_element_id=enum_bundle_element_id,
        client=client,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    id: str,
    enum_bundle_element_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, None, str] = "$type,color($type,background,foreground,id),id,localizedName,name,ordinal",
) -> Response[EnumBundleElement]:
    """
    Args:
        id (str):
        enum_bundle_element_id (str):
        fields (Union[Unset, None, str]):  Default:
            '$type,color($type,background,foreground,id),id,localizedName,name,ordinal'. Example:
            $type,color($type,background,foreground,id),id,localizedName,name,ordinal.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EnumBundleElement]
    """

    kwargs = _get_kwargs(
        id=id,
        enum_bundle_element_id=enum_bundle_element_id,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    enum_bundle_element_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, None, str] = "$type,color($type,background,foreground,id),id,localizedName,name,ordinal",
) -> Optional[EnumBundleElement]:
    """
    Args:
        id (str):
        enum_bundle_element_id (str):
        fields (Union[Unset, None, str]):  Default:
            '$type,color($type,background,foreground,id),id,localizedName,name,ordinal'. Example:
            $type,color($type,background,foreground,id),id,localizedName,name,ordinal.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EnumBundleElement
    """

    return (
        await asyncio_detailed(
            id=id,
            enum_bundle_element_id=enum_bundle_element_id,
            client=client,
            fields=fields,
        )
    ).parsed
