from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.global_settings import GlobalSettings
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    json_body: GlobalSettings,
    fields: Union[
        Unset, None, str
    ] = "$type,appearanceSettings($type,dateFieldFormat($type,datePattern,id,pattern,presentation),id,timeZone($type,id,offset,presentation)),id,license($type,error,id,license,username),localeSettings($type,id,isRTL,locale($type,community,id,language,locale,name)),notificationSettings($type,emailSettings($type,id,isEnabled),id,jabberSettings($type,id,isEnabled)),restSettings($type,allowAllOrigins,allowedOrigins,id),systemSettings($type,baseUrl,id,isApplicationReadOnly,maxExportItems,maxUploadFileSize)",
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["fields"] = fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/admin/globalSettings",
        "json": json_json_body,
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GlobalSettings]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GlobalSettings.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GlobalSettings]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: GlobalSettings,
    fields: Union[
        Unset, None, str
    ] = "$type,appearanceSettings($type,dateFieldFormat($type,datePattern,id,pattern,presentation),id,timeZone($type,id,offset,presentation)),id,license($type,error,id,license,username),localeSettings($type,id,isRTL,locale($type,community,id,language,locale,name)),notificationSettings($type,emailSettings($type,id,isEnabled),id,jabberSettings($type,id,isEnabled)),restSettings($type,allowAllOrigins,allowedOrigins,id),systemSettings($type,baseUrl,id,isApplicationReadOnly,maxExportItems,maxUploadFileSize)",
) -> Response[GlobalSettings]:
    """
    Args:
        fields (Union[Unset, None, str]):  Default: '$type,appearanceSettings($type,dateFieldForma
            t($type,datePattern,id,pattern,presentation),id,timeZone($type,id,offset,presentation)),id
            ,license($type,error,id,license,username),localeSettings($type,id,isRTL,locale($type,commu
            nity,id,language,locale,name)),notificationSettings($type,emailSettings($type,id,isEnabled
            ),id,jabberSettings($type,id,isEnabled)),restSettings($type,allowAllOrigins,allowedOrigins
            ,id),systemSettings($type,baseUrl,id,isApplicationReadOnly,maxExportItems,maxUploadFileSiz
            e)'. Example: $type,appearanceSettings($type,dateFieldFormat($type,datePattern,id,pattern,
            presentation),id,timeZone($type,id,offset,presentation)),id,license($type,error,id,license
            ,username),localeSettings($type,id,isRTL,locale($type,community,id,language,locale,name)),
            notificationSettings($type,emailSettings($type,id,isEnabled),id,jabberSettings($type,id,is
            Enabled)),restSettings($type,allowAllOrigins,allowedOrigins,id),systemSettings($type,baseU
            rl,id,isApplicationReadOnly,maxExportItems,maxUploadFileSize).
        json_body (GlobalSettings):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GlobalSettings]
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
    json_body: GlobalSettings,
    fields: Union[
        Unset, None, str
    ] = "$type,appearanceSettings($type,dateFieldFormat($type,datePattern,id,pattern,presentation),id,timeZone($type,id,offset,presentation)),id,license($type,error,id,license,username),localeSettings($type,id,isRTL,locale($type,community,id,language,locale,name)),notificationSettings($type,emailSettings($type,id,isEnabled),id,jabberSettings($type,id,isEnabled)),restSettings($type,allowAllOrigins,allowedOrigins,id),systemSettings($type,baseUrl,id,isApplicationReadOnly,maxExportItems,maxUploadFileSize)",
) -> Optional[GlobalSettings]:
    """
    Args:
        fields (Union[Unset, None, str]):  Default: '$type,appearanceSettings($type,dateFieldForma
            t($type,datePattern,id,pattern,presentation),id,timeZone($type,id,offset,presentation)),id
            ,license($type,error,id,license,username),localeSettings($type,id,isRTL,locale($type,commu
            nity,id,language,locale,name)),notificationSettings($type,emailSettings($type,id,isEnabled
            ),id,jabberSettings($type,id,isEnabled)),restSettings($type,allowAllOrigins,allowedOrigins
            ,id),systemSettings($type,baseUrl,id,isApplicationReadOnly,maxExportItems,maxUploadFileSiz
            e)'. Example: $type,appearanceSettings($type,dateFieldFormat($type,datePattern,id,pattern,
            presentation),id,timeZone($type,id,offset,presentation)),id,license($type,error,id,license
            ,username),localeSettings($type,id,isRTL,locale($type,community,id,language,locale,name)),
            notificationSettings($type,emailSettings($type,id,isEnabled),id,jabberSettings($type,id,is
            Enabled)),restSettings($type,allowAllOrigins,allowedOrigins,id),systemSettings($type,baseU
            rl,id,isApplicationReadOnly,maxExportItems,maxUploadFileSize).
        json_body (GlobalSettings):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GlobalSettings
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: GlobalSettings,
    fields: Union[
        Unset, None, str
    ] = "$type,appearanceSettings($type,dateFieldFormat($type,datePattern,id,pattern,presentation),id,timeZone($type,id,offset,presentation)),id,license($type,error,id,license,username),localeSettings($type,id,isRTL,locale($type,community,id,language,locale,name)),notificationSettings($type,emailSettings($type,id,isEnabled),id,jabberSettings($type,id,isEnabled)),restSettings($type,allowAllOrigins,allowedOrigins,id),systemSettings($type,baseUrl,id,isApplicationReadOnly,maxExportItems,maxUploadFileSize)",
) -> Response[GlobalSettings]:
    """
    Args:
        fields (Union[Unset, None, str]):  Default: '$type,appearanceSettings($type,dateFieldForma
            t($type,datePattern,id,pattern,presentation),id,timeZone($type,id,offset,presentation)),id
            ,license($type,error,id,license,username),localeSettings($type,id,isRTL,locale($type,commu
            nity,id,language,locale,name)),notificationSettings($type,emailSettings($type,id,isEnabled
            ),id,jabberSettings($type,id,isEnabled)),restSettings($type,allowAllOrigins,allowedOrigins
            ,id),systemSettings($type,baseUrl,id,isApplicationReadOnly,maxExportItems,maxUploadFileSiz
            e)'. Example: $type,appearanceSettings($type,dateFieldFormat($type,datePattern,id,pattern,
            presentation),id,timeZone($type,id,offset,presentation)),id,license($type,error,id,license
            ,username),localeSettings($type,id,isRTL,locale($type,community,id,language,locale,name)),
            notificationSettings($type,emailSettings($type,id,isEnabled),id,jabberSettings($type,id,is
            Enabled)),restSettings($type,allowAllOrigins,allowedOrigins,id),systemSettings($type,baseU
            rl,id,isApplicationReadOnly,maxExportItems,maxUploadFileSize).
        json_body (GlobalSettings):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GlobalSettings]
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
    json_body: GlobalSettings,
    fields: Union[
        Unset, None, str
    ] = "$type,appearanceSettings($type,dateFieldFormat($type,datePattern,id,pattern,presentation),id,timeZone($type,id,offset,presentation)),id,license($type,error,id,license,username),localeSettings($type,id,isRTL,locale($type,community,id,language,locale,name)),notificationSettings($type,emailSettings($type,id,isEnabled),id,jabberSettings($type,id,isEnabled)),restSettings($type,allowAllOrigins,allowedOrigins,id),systemSettings($type,baseUrl,id,isApplicationReadOnly,maxExportItems,maxUploadFileSize)",
) -> Optional[GlobalSettings]:
    """
    Args:
        fields (Union[Unset, None, str]):  Default: '$type,appearanceSettings($type,dateFieldForma
            t($type,datePattern,id,pattern,presentation),id,timeZone($type,id,offset,presentation)),id
            ,license($type,error,id,license,username),localeSettings($type,id,isRTL,locale($type,commu
            nity,id,language,locale,name)),notificationSettings($type,emailSettings($type,id,isEnabled
            ),id,jabberSettings($type,id,isEnabled)),restSettings($type,allowAllOrigins,allowedOrigins
            ,id),systemSettings($type,baseUrl,id,isApplicationReadOnly,maxExportItems,maxUploadFileSiz
            e)'. Example: $type,appearanceSettings($type,dateFieldFormat($type,datePattern,id,pattern,
            presentation),id,timeZone($type,id,offset,presentation)),id,license($type,error,id,license
            ,username),localeSettings($type,id,isRTL,locale($type,community,id,language,locale,name)),
            notificationSettings($type,emailSettings($type,id,isEnabled),id,jabberSettings($type,id,is
            Enabled)),restSettings($type,allowAllOrigins,allowedOrigins,id),systemSettings($type,baseU
            rl,id,isApplicationReadOnly,maxExportItems,maxUploadFileSize).
        json_body (GlobalSettings):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GlobalSettings
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            fields=fields,
        )
    ).parsed
