from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.system_settings import SystemSettings
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    json_body: SystemSettings,
    fields: Union[Unset, None, str] = "$type,baseUrl,id,isApplicationReadOnly,maxExportItems,maxUploadFileSize",
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["fields"] = fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/admin/globalSettings/systemSettings",
        "json": json_json_body,
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SystemSettings]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SystemSettings.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SystemSettings]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: SystemSettings,
    fields: Union[Unset, None, str] = "$type,baseUrl,id,isApplicationReadOnly,maxExportItems,maxUploadFileSize",
) -> Response[SystemSettings]:
    """
    Args:
        fields (Union[Unset, None, str]):  Default:
            '$type,baseUrl,id,isApplicationReadOnly,maxExportItems,maxUploadFileSize'. Example:
            $type,baseUrl,id,isApplicationReadOnly,maxExportItems,maxUploadFileSize.
        json_body (SystemSettings):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SystemSettings]
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
    json_body: SystemSettings,
    fields: Union[Unset, None, str] = "$type,baseUrl,id,isApplicationReadOnly,maxExportItems,maxUploadFileSize",
) -> Optional[SystemSettings]:
    """
    Args:
        fields (Union[Unset, None, str]):  Default:
            '$type,baseUrl,id,isApplicationReadOnly,maxExportItems,maxUploadFileSize'. Example:
            $type,baseUrl,id,isApplicationReadOnly,maxExportItems,maxUploadFileSize.
        json_body (SystemSettings):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SystemSettings
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: SystemSettings,
    fields: Union[Unset, None, str] = "$type,baseUrl,id,isApplicationReadOnly,maxExportItems,maxUploadFileSize",
) -> Response[SystemSettings]:
    """
    Args:
        fields (Union[Unset, None, str]):  Default:
            '$type,baseUrl,id,isApplicationReadOnly,maxExportItems,maxUploadFileSize'. Example:
            $type,baseUrl,id,isApplicationReadOnly,maxExportItems,maxUploadFileSize.
        json_body (SystemSettings):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SystemSettings]
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
    json_body: SystemSettings,
    fields: Union[Unset, None, str] = "$type,baseUrl,id,isApplicationReadOnly,maxExportItems,maxUploadFileSize",
) -> Optional[SystemSettings]:
    """
    Args:
        fields (Union[Unset, None, str]):  Default:
            '$type,baseUrl,id,isApplicationReadOnly,maxExportItems,maxUploadFileSize'. Example:
            $type,baseUrl,id,isApplicationReadOnly,maxExportItems,maxUploadFileSize.
        json_body (SystemSettings):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SystemSettings
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            fields=fields,
        )
    ).parsed
