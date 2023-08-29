from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.general_user_profile import GeneralUserProfile
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    fields: Union[
        Unset, None, str
    ] = "$type,dateFieldFormat($type,datePattern,id,pattern,presentation),id,locale($type,community,id,language,locale,name),timezone($type,id,offset,presentation)",
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["fields"] = fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/users/{id}/profiles/general".format(
            id=id,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GeneralUserProfile]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GeneralUserProfile.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GeneralUserProfile]:
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
    fields: Union[
        Unset, None, str
    ] = "$type,dateFieldFormat($type,datePattern,id,pattern,presentation),id,locale($type,community,id,language,locale,name),timezone($type,id,offset,presentation)",
) -> Response[GeneralUserProfile]:
    """
    Args:
        id (str):
        fields (Union[Unset, None, str]):  Default: '$type,dateFieldFormat($type,datePattern,id,pa
            ttern,presentation),id,locale($type,community,id,language,locale,name),timezone($type,id,o
            ffset,presentation)'. Example: $type,dateFieldFormat($type,datePattern,id,pattern,presenta
            tion),id,locale($type,community,id,language,locale,name),timezone($type,id,offset,presenta
            tion).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GeneralUserProfile]
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
    fields: Union[
        Unset, None, str
    ] = "$type,dateFieldFormat($type,datePattern,id,pattern,presentation),id,locale($type,community,id,language,locale,name),timezone($type,id,offset,presentation)",
) -> Optional[GeneralUserProfile]:
    """
    Args:
        id (str):
        fields (Union[Unset, None, str]):  Default: '$type,dateFieldFormat($type,datePattern,id,pa
            ttern,presentation),id,locale($type,community,id,language,locale,name),timezone($type,id,o
            ffset,presentation)'. Example: $type,dateFieldFormat($type,datePattern,id,pattern,presenta
            tion),id,locale($type,community,id,language,locale,name),timezone($type,id,offset,presenta
            tion).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GeneralUserProfile
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
    fields: Union[
        Unset, None, str
    ] = "$type,dateFieldFormat($type,datePattern,id,pattern,presentation),id,locale($type,community,id,language,locale,name),timezone($type,id,offset,presentation)",
) -> Response[GeneralUserProfile]:
    """
    Args:
        id (str):
        fields (Union[Unset, None, str]):  Default: '$type,dateFieldFormat($type,datePattern,id,pa
            ttern,presentation),id,locale($type,community,id,language,locale,name),timezone($type,id,o
            ffset,presentation)'. Example: $type,dateFieldFormat($type,datePattern,id,pattern,presenta
            tion),id,locale($type,community,id,language,locale,name),timezone($type,id,offset,presenta
            tion).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GeneralUserProfile]
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
    fields: Union[
        Unset, None, str
    ] = "$type,dateFieldFormat($type,datePattern,id,pattern,presentation),id,locale($type,community,id,language,locale,name),timezone($type,id,offset,presentation)",
) -> Optional[GeneralUserProfile]:
    """
    Args:
        id (str):
        fields (Union[Unset, None, str]):  Default: '$type,dateFieldFormat($type,datePattern,id,pa
            ttern,presentation),id,locale($type,community,id,language,locale,name),timezone($type,id,o
            ffset,presentation)'. Example: $type,dateFieldFormat($type,datePattern,id,pattern,presenta
            tion),id,locale($type,community,id,language,locale,name),timezone($type,id,offset,presenta
            tion).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GeneralUserProfile
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            fields=fields,
        )
    ).parsed
