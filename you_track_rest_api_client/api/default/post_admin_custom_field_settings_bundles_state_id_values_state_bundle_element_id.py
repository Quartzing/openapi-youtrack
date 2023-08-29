from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.state_bundle_element import StateBundleElement
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    state_bundle_element_id: str,
    *,
    json_body: StateBundleElement,
    fields: Union[
        Unset, None, str
    ] = "$type,color($type,background,foreground,id),id,isResolved,localizedName,name,ordinal",
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["fields"] = fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/admin/customFieldSettings/bundles/state/{id}/values/{stateBundleElementId}".format(
            id=id,
            stateBundleElementId=state_bundle_element_id,
        ),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[StateBundleElement]:
    if response.status_code == HTTPStatus.OK:
        response_200 = StateBundleElement.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[StateBundleElement]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    state_bundle_element_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: StateBundleElement,
    fields: Union[
        Unset, None, str
    ] = "$type,color($type,background,foreground,id),id,isResolved,localizedName,name,ordinal",
) -> Response[StateBundleElement]:
    """
    Args:
        id (str):
        state_bundle_element_id (str):
        fields (Union[Unset, None, str]):  Default:
            '$type,color($type,background,foreground,id),id,isResolved,localizedName,name,ordinal'.
            Example:
            $type,color($type,background,foreground,id),id,isResolved,localizedName,name,ordinal.
        json_body (StateBundleElement):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StateBundleElement]
    """

    kwargs = _get_kwargs(
        id=id,
        state_bundle_element_id=state_bundle_element_id,
        json_body=json_body,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    state_bundle_element_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: StateBundleElement,
    fields: Union[
        Unset, None, str
    ] = "$type,color($type,background,foreground,id),id,isResolved,localizedName,name,ordinal",
) -> Optional[StateBundleElement]:
    """
    Args:
        id (str):
        state_bundle_element_id (str):
        fields (Union[Unset, None, str]):  Default:
            '$type,color($type,background,foreground,id),id,isResolved,localizedName,name,ordinal'.
            Example:
            $type,color($type,background,foreground,id),id,isResolved,localizedName,name,ordinal.
        json_body (StateBundleElement):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StateBundleElement
    """

    return sync_detailed(
        id=id,
        state_bundle_element_id=state_bundle_element_id,
        client=client,
        json_body=json_body,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    id: str,
    state_bundle_element_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: StateBundleElement,
    fields: Union[
        Unset, None, str
    ] = "$type,color($type,background,foreground,id),id,isResolved,localizedName,name,ordinal",
) -> Response[StateBundleElement]:
    """
    Args:
        id (str):
        state_bundle_element_id (str):
        fields (Union[Unset, None, str]):  Default:
            '$type,color($type,background,foreground,id),id,isResolved,localizedName,name,ordinal'.
            Example:
            $type,color($type,background,foreground,id),id,isResolved,localizedName,name,ordinal.
        json_body (StateBundleElement):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StateBundleElement]
    """

    kwargs = _get_kwargs(
        id=id,
        state_bundle_element_id=state_bundle_element_id,
        json_body=json_body,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    state_bundle_element_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: StateBundleElement,
    fields: Union[
        Unset, None, str
    ] = "$type,color($type,background,foreground,id),id,isResolved,localizedName,name,ordinal",
) -> Optional[StateBundleElement]:
    """
    Args:
        id (str):
        state_bundle_element_id (str):
        fields (Union[Unset, None, str]):  Default:
            '$type,color($type,background,foreground,id),id,isResolved,localizedName,name,ordinal'.
            Example:
            $type,color($type,background,foreground,id),id,isResolved,localizedName,name,ordinal.
        json_body (StateBundleElement):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StateBundleElement
    """

    return (
        await asyncio_detailed(
            id=id,
            state_bundle_element_id=state_bundle_element_id,
            client=client,
            json_body=json_body,
            fields=fields,
        )
    ).parsed
