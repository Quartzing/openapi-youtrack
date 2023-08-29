from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.work_item_type import WorkItemType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    work_item_type_id: str,
    *,
    fields: Union[Unset, None, str] = "$type,autoAttached,id,name",
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["fields"] = fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/admin/timeTrackingSettings/workItemTypes/{workItemTypeId}".format(
            workItemTypeId=work_item_type_id,
        ),
        "params": params,
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[WorkItemType]:
    if response.status_code == HTTPStatus.OK:
        response_200 = WorkItemType.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[WorkItemType]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    work_item_type_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, None, str] = "$type,autoAttached,id,name",
) -> Response[WorkItemType]:
    """
    Args:
        work_item_type_id (str):
        fields (Union[Unset, None, str]):  Default: '$type,autoAttached,id,name'. Example:
            $type,autoAttached,id,name.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WorkItemType]
    """

    kwargs = _get_kwargs(
        work_item_type_id=work_item_type_id,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    work_item_type_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, None, str] = "$type,autoAttached,id,name",
) -> Optional[WorkItemType]:
    """
    Args:
        work_item_type_id (str):
        fields (Union[Unset, None, str]):  Default: '$type,autoAttached,id,name'. Example:
            $type,autoAttached,id,name.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WorkItemType
    """

    return sync_detailed(
        work_item_type_id=work_item_type_id,
        client=client,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    work_item_type_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, None, str] = "$type,autoAttached,id,name",
) -> Response[WorkItemType]:
    """
    Args:
        work_item_type_id (str):
        fields (Union[Unset, None, str]):  Default: '$type,autoAttached,id,name'. Example:
            $type,autoAttached,id,name.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WorkItemType]
    """

    kwargs = _get_kwargs(
        work_item_type_id=work_item_type_id,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    work_item_type_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, None, str] = "$type,autoAttached,id,name",
) -> Optional[WorkItemType]:
    """
    Args:
        work_item_type_id (str):
        fields (Union[Unset, None, str]):  Default: '$type,autoAttached,id,name'. Example:
            $type,autoAttached,id,name.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WorkItemType
    """

    return (
        await asyncio_detailed(
            work_item_type_id=work_item_type_id,
            client=client,
            fields=fields,
        )
    ).parsed
