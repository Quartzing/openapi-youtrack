from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    project_custom_field_id: str,
    *,
    fields: Union[
        Unset, None, str
    ] = "$type,bundle($type,id),canBeEmpty,defaultValues($type,id,name),emptyFieldText,field($type,fieldType($type,id),id,localizedName,name),id,isPublic,ordinal",
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["fields"] = fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/admin/projects/{id}/customFields/{projectCustomFieldId}".format(
            id=id,
            projectCustomFieldId=project_custom_field_id,
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
    project_custom_field_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[
        Unset, None, str
    ] = "$type,bundle($type,id),canBeEmpty,defaultValues($type,id,name),emptyFieldText,field($type,fieldType($type,id),id,localizedName,name),id,isPublic,ordinal",
) -> Response[Any]:
    """
    Args:
        id (str):
        project_custom_field_id (str):
        fields (Union[Unset, None, str]):  Default: '$type,bundle($type,id),canBeEmpty,defaultValu
            es($type,id,name),emptyFieldText,field($type,fieldType($type,id),id,localizedName,name),id
            ,isPublic,ordinal'. Example: $type,bundle($type,id),canBeEmpty,defaultValues($type,id,name
            ),emptyFieldText,field($type,fieldType($type,id),id,localizedName,name),id,isPublic,ordina
            l.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        project_custom_field_id=project_custom_field_id,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    id: str,
    project_custom_field_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[
        Unset, None, str
    ] = "$type,bundle($type,id),canBeEmpty,defaultValues($type,id,name),emptyFieldText,field($type,fieldType($type,id),id,localizedName,name),id,isPublic,ordinal",
) -> Response[Any]:
    """
    Args:
        id (str):
        project_custom_field_id (str):
        fields (Union[Unset, None, str]):  Default: '$type,bundle($type,id),canBeEmpty,defaultValu
            es($type,id,name),emptyFieldText,field($type,fieldType($type,id),id,localizedName,name),id
            ,isPublic,ordinal'. Example: $type,bundle($type,id),canBeEmpty,defaultValues($type,id,name
            ),emptyFieldText,field($type,fieldType($type,id),id,localizedName,name),id,isPublic,ordina
            l.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        project_custom_field_id=project_custom_field_id,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
