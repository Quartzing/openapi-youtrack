from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.build_bundle_element import BuildBundleElement
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    build_bundle_element_id: str,
    *,
    fields: Union[Unset, None, str] = "$type,assembleDate,color($type,background,foreground,id),id,name,ordinal",
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["fields"] = fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/admin/customFieldSettings/bundles/build/{id}/values/{buildBundleElementId}".format(
            id=id,
            buildBundleElementId=build_bundle_element_id,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[BuildBundleElement]:
    if response.status_code == HTTPStatus.OK:
        response_200 = BuildBundleElement.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[BuildBundleElement]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    build_bundle_element_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, None, str] = "$type,assembleDate,color($type,background,foreground,id),id,name,ordinal",
) -> Response[BuildBundleElement]:
    """
    Args:
        id (str):
        build_bundle_element_id (str):
        fields (Union[Unset, None, str]):  Default:
            '$type,assembleDate,color($type,background,foreground,id),id,name,ordinal'. Example:
            $type,assembleDate,color($type,background,foreground,id),id,name,ordinal.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BuildBundleElement]
    """

    kwargs = _get_kwargs(
        id=id,
        build_bundle_element_id=build_bundle_element_id,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    build_bundle_element_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, None, str] = "$type,assembleDate,color($type,background,foreground,id),id,name,ordinal",
) -> Optional[BuildBundleElement]:
    """
    Args:
        id (str):
        build_bundle_element_id (str):
        fields (Union[Unset, None, str]):  Default:
            '$type,assembleDate,color($type,background,foreground,id),id,name,ordinal'. Example:
            $type,assembleDate,color($type,background,foreground,id),id,name,ordinal.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BuildBundleElement
    """

    return sync_detailed(
        id=id,
        build_bundle_element_id=build_bundle_element_id,
        client=client,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    id: str,
    build_bundle_element_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, None, str] = "$type,assembleDate,color($type,background,foreground,id),id,name,ordinal",
) -> Response[BuildBundleElement]:
    """
    Args:
        id (str):
        build_bundle_element_id (str):
        fields (Union[Unset, None, str]):  Default:
            '$type,assembleDate,color($type,background,foreground,id),id,name,ordinal'. Example:
            $type,assembleDate,color($type,background,foreground,id),id,name,ordinal.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BuildBundleElement]
    """

    kwargs = _get_kwargs(
        id=id,
        build_bundle_element_id=build_bundle_element_id,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    build_bundle_element_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, None, str] = "$type,assembleDate,color($type,background,foreground,id),id,name,ordinal",
) -> Optional[BuildBundleElement]:
    """
    Args:
        id (str):
        build_bundle_element_id (str):
        fields (Union[Unset, None, str]):  Default:
            '$type,assembleDate,color($type,background,foreground,id),id,name,ordinal'. Example:
            $type,assembleDate,color($type,background,foreground,id),id,name,ordinal.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BuildBundleElement
    """

    return (
        await asyncio_detailed(
            id=id,
            build_bundle_element_id=build_bundle_element_id,
            client=client,
            fields=fields,
        )
    ).parsed
