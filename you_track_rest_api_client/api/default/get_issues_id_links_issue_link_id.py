from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    issue_link_id: str,
    *,
    fields: Union[Unset, None, str] = "$type,direction,id,linkType($type,id,localizedName,name)",
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["fields"] = fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/issues/{id}/links/{issueLinkId}".format(
            id=id,
            issueLinkId=issue_link_id,
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
    issue_link_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, None, str] = "$type,direction,id,linkType($type,id,localizedName,name)",
) -> Response[Any]:
    """
    Args:
        id (str):
        issue_link_id (str):
        fields (Union[Unset, None, str]):  Default:
            '$type,direction,id,linkType($type,id,localizedName,name)'. Example:
            $type,direction,id,linkType($type,id,localizedName,name).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        issue_link_id=issue_link_id,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    id: str,
    issue_link_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, None, str] = "$type,direction,id,linkType($type,id,localizedName,name)",
) -> Response[Any]:
    """
    Args:
        id (str):
        issue_link_id (str):
        fields (Union[Unset, None, str]):  Default:
            '$type,direction,id,linkType($type,id,localizedName,name)'. Example:
            $type,direction,id,linkType($type,id,localizedName,name).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        issue_link_id=issue_link_id,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
