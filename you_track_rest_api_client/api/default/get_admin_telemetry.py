from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.telemetry import Telemetry
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    fields: Union[
        Unset, None, str
    ] = "$type,allocatedMemory,availableMemory,availableProcessors,blobStringsCacheHitRate,cachedResultsCountInDBQueriesCache,databaseBackgroundThreads,databaseLocation,databaseQueriesCacheHitRate,databaseSize,fullDatabaseSize,id,installationFolder,logsLocation,notificationAnalyzerThreads,onlineUsers($type,id,users),pendingAsyncJobs,reportCalculatorThreads,requestsPerSecond,startedTime,textIndexSize,totalTransactions,transactionsPerSecond,uptime,usedMemory",
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["fields"] = fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/admin/telemetry",
        "params": params,
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Telemetry]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Telemetry.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Telemetry]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[
        Unset, None, str
    ] = "$type,allocatedMemory,availableMemory,availableProcessors,blobStringsCacheHitRate,cachedResultsCountInDBQueriesCache,databaseBackgroundThreads,databaseLocation,databaseQueriesCacheHitRate,databaseSize,fullDatabaseSize,id,installationFolder,logsLocation,notificationAnalyzerThreads,onlineUsers($type,id,users),pendingAsyncJobs,reportCalculatorThreads,requestsPerSecond,startedTime,textIndexSize,totalTransactions,transactionsPerSecond,uptime,usedMemory",
) -> Response[Telemetry]:
    """
    Args:
        fields (Union[Unset, None, str]):  Default: '$type,allocatedMemory,availableMemory,availab
            leProcessors,blobStringsCacheHitRate,cachedResultsCountInDBQueriesCache,databaseBackground
            Threads,databaseLocation,databaseQueriesCacheHitRate,databaseSize,fullDatabaseSize,id,inst
            allationFolder,logsLocation,notificationAnalyzerThreads,onlineUsers($type,id,users),pendin
            gAsyncJobs,reportCalculatorThreads,requestsPerSecond,startedTime,textIndexSize,totalTransa
            ctions,transactionsPerSecond,uptime,usedMemory'. Example: $type,allocatedMemory,availableM
            emory,availableProcessors,blobStringsCacheHitRate,cachedResultsCountInDBQueriesCache,datab
            aseBackgroundThreads,databaseLocation,databaseQueriesCacheHitRate,databaseSize,fullDatabas
            eSize,id,installationFolder,logsLocation,notificationAnalyzerThreads,onlineUsers($type,id,
            users),pendingAsyncJobs,reportCalculatorThreads,requestsPerSecond,startedTime,textIndexSiz
            e,totalTransactions,transactionsPerSecond,uptime,usedMemory.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Telemetry]
    """

    kwargs = _get_kwargs(
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[
        Unset, None, str
    ] = "$type,allocatedMemory,availableMemory,availableProcessors,blobStringsCacheHitRate,cachedResultsCountInDBQueriesCache,databaseBackgroundThreads,databaseLocation,databaseQueriesCacheHitRate,databaseSize,fullDatabaseSize,id,installationFolder,logsLocation,notificationAnalyzerThreads,onlineUsers($type,id,users),pendingAsyncJobs,reportCalculatorThreads,requestsPerSecond,startedTime,textIndexSize,totalTransactions,transactionsPerSecond,uptime,usedMemory",
) -> Optional[Telemetry]:
    """
    Args:
        fields (Union[Unset, None, str]):  Default: '$type,allocatedMemory,availableMemory,availab
            leProcessors,blobStringsCacheHitRate,cachedResultsCountInDBQueriesCache,databaseBackground
            Threads,databaseLocation,databaseQueriesCacheHitRate,databaseSize,fullDatabaseSize,id,inst
            allationFolder,logsLocation,notificationAnalyzerThreads,onlineUsers($type,id,users),pendin
            gAsyncJobs,reportCalculatorThreads,requestsPerSecond,startedTime,textIndexSize,totalTransa
            ctions,transactionsPerSecond,uptime,usedMemory'. Example: $type,allocatedMemory,availableM
            emory,availableProcessors,blobStringsCacheHitRate,cachedResultsCountInDBQueriesCache,datab
            aseBackgroundThreads,databaseLocation,databaseQueriesCacheHitRate,databaseSize,fullDatabas
            eSize,id,installationFolder,logsLocation,notificationAnalyzerThreads,onlineUsers($type,id,
            users),pendingAsyncJobs,reportCalculatorThreads,requestsPerSecond,startedTime,textIndexSiz
            e,totalTransactions,transactionsPerSecond,uptime,usedMemory.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Telemetry
    """

    return sync_detailed(
        client=client,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[
        Unset, None, str
    ] = "$type,allocatedMemory,availableMemory,availableProcessors,blobStringsCacheHitRate,cachedResultsCountInDBQueriesCache,databaseBackgroundThreads,databaseLocation,databaseQueriesCacheHitRate,databaseSize,fullDatabaseSize,id,installationFolder,logsLocation,notificationAnalyzerThreads,onlineUsers($type,id,users),pendingAsyncJobs,reportCalculatorThreads,requestsPerSecond,startedTime,textIndexSize,totalTransactions,transactionsPerSecond,uptime,usedMemory",
) -> Response[Telemetry]:
    """
    Args:
        fields (Union[Unset, None, str]):  Default: '$type,allocatedMemory,availableMemory,availab
            leProcessors,blobStringsCacheHitRate,cachedResultsCountInDBQueriesCache,databaseBackground
            Threads,databaseLocation,databaseQueriesCacheHitRate,databaseSize,fullDatabaseSize,id,inst
            allationFolder,logsLocation,notificationAnalyzerThreads,onlineUsers($type,id,users),pendin
            gAsyncJobs,reportCalculatorThreads,requestsPerSecond,startedTime,textIndexSize,totalTransa
            ctions,transactionsPerSecond,uptime,usedMemory'. Example: $type,allocatedMemory,availableM
            emory,availableProcessors,blobStringsCacheHitRate,cachedResultsCountInDBQueriesCache,datab
            aseBackgroundThreads,databaseLocation,databaseQueriesCacheHitRate,databaseSize,fullDatabas
            eSize,id,installationFolder,logsLocation,notificationAnalyzerThreads,onlineUsers($type,id,
            users),pendingAsyncJobs,reportCalculatorThreads,requestsPerSecond,startedTime,textIndexSiz
            e,totalTransactions,transactionsPerSecond,uptime,usedMemory.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Telemetry]
    """

    kwargs = _get_kwargs(
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[
        Unset, None, str
    ] = "$type,allocatedMemory,availableMemory,availableProcessors,blobStringsCacheHitRate,cachedResultsCountInDBQueriesCache,databaseBackgroundThreads,databaseLocation,databaseQueriesCacheHitRate,databaseSize,fullDatabaseSize,id,installationFolder,logsLocation,notificationAnalyzerThreads,onlineUsers($type,id,users),pendingAsyncJobs,reportCalculatorThreads,requestsPerSecond,startedTime,textIndexSize,totalTransactions,transactionsPerSecond,uptime,usedMemory",
) -> Optional[Telemetry]:
    """
    Args:
        fields (Union[Unset, None, str]):  Default: '$type,allocatedMemory,availableMemory,availab
            leProcessors,blobStringsCacheHitRate,cachedResultsCountInDBQueriesCache,databaseBackground
            Threads,databaseLocation,databaseQueriesCacheHitRate,databaseSize,fullDatabaseSize,id,inst
            allationFolder,logsLocation,notificationAnalyzerThreads,onlineUsers($type,id,users),pendin
            gAsyncJobs,reportCalculatorThreads,requestsPerSecond,startedTime,textIndexSize,totalTransa
            ctions,transactionsPerSecond,uptime,usedMemory'. Example: $type,allocatedMemory,availableM
            emory,availableProcessors,blobStringsCacheHitRate,cachedResultsCountInDBQueriesCache,datab
            aseBackgroundThreads,databaseLocation,databaseQueriesCacheHitRate,databaseSize,fullDatabas
            eSize,id,installationFolder,logsLocation,notificationAnalyzerThreads,onlineUsers($type,id,
            users),pendingAsyncJobs,reportCalculatorThreads,requestsPerSecond,startedTime,textIndexSiz
            e,totalTransactions,transactionsPerSecond,uptime,usedMemory.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Telemetry
    """

    return (
        await asyncio_detailed(
            client=client,
            fields=fields,
        )
    ).parsed
