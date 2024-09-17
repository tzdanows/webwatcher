r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Preview
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from datetime import datetime
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.preview.sync.service.document import DocumentList
from twilio.rest.preview.sync.service.sync_list import SyncListList
from twilio.rest.preview.sync.service.sync_map import SyncMapList


class ServiceInstance(InstanceResource):
    """
    :ivar sid:
    :ivar account_sid:
    :ivar friendly_name:
    :ivar date_created:
    :ivar date_updated:
    :ivar url:
    :ivar webhook_url:
    :ivar reachability_webhooks_enabled:
    :ivar acl_enabled:
    :ivar links:
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], sid: Optional[str] = None
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.url: Optional[str] = payload.get("url")
        self.webhook_url: Optional[str] = payload.get("webhook_url")
        self.reachability_webhooks_enabled: Optional[bool] = payload.get(
            "reachability_webhooks_enabled"
        )
        self.acl_enabled: Optional[bool] = payload.get("acl_enabled")
        self.links: Optional[Dict[str, object]] = payload.get("links")

        self._solution = {
            "sid": sid or self.sid,
        }
        self._context: Optional[ServiceContext] = None

    @property
    def _proxy(self) -> "ServiceContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: ServiceContext for this ServiceInstance
        """
        if self._context is None:
            self._context = ServiceContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the ServiceInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the ServiceInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "ServiceInstance":
        """
        Fetch the ServiceInstance


        :returns: The fetched ServiceInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "ServiceInstance":
        """
        Asynchronous coroutine to fetch the ServiceInstance


        :returns: The fetched ServiceInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        webhook_url: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        reachability_webhooks_enabled: Union[bool, object] = values.unset,
        acl_enabled: Union[bool, object] = values.unset,
    ) -> "ServiceInstance":
        """
        Update the ServiceInstance

        :param webhook_url:
        :param friendly_name:
        :param reachability_webhooks_enabled:
        :param acl_enabled:

        :returns: The updated ServiceInstance
        """
        return self._proxy.update(
            webhook_url=webhook_url,
            friendly_name=friendly_name,
            reachability_webhooks_enabled=reachability_webhooks_enabled,
            acl_enabled=acl_enabled,
        )

    async def update_async(
        self,
        webhook_url: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        reachability_webhooks_enabled: Union[bool, object] = values.unset,
        acl_enabled: Union[bool, object] = values.unset,
    ) -> "ServiceInstance":
        """
        Asynchronous coroutine to update the ServiceInstance

        :param webhook_url:
        :param friendly_name:
        :param reachability_webhooks_enabled:
        :param acl_enabled:

        :returns: The updated ServiceInstance
        """
        return await self._proxy.update_async(
            webhook_url=webhook_url,
            friendly_name=friendly_name,
            reachability_webhooks_enabled=reachability_webhooks_enabled,
            acl_enabled=acl_enabled,
        )

    @property
    def documents(self) -> DocumentList:
        """
        Access the documents
        """
        return self._proxy.documents

    @property
    def sync_lists(self) -> SyncListList:
        """
        Access the sync_lists
        """
        return self._proxy.sync_lists

    @property
    def sync_maps(self) -> SyncMapList:
        """
        Access the sync_maps
        """
        return self._proxy.sync_maps

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Preview.Sync.ServiceInstance {}>".format(context)


class ServiceContext(InstanceContext):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the ServiceContext

        :param version: Version that contains the resource
        :param sid:
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/Services/{sid}".format(**self._solution)

        self._documents: Optional[DocumentList] = None
        self._sync_lists: Optional[SyncListList] = None
        self._sync_maps: Optional[SyncMapList] = None

    def delete(self) -> bool:
        """
        Deletes the ServiceInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the ServiceInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> ServiceInstance:
        """
        Fetch the ServiceInstance


        :returns: The fetched ServiceInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return ServiceInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> ServiceInstance:
        """
        Asynchronous coroutine to fetch the ServiceInstance


        :returns: The fetched ServiceInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return ServiceInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    def update(
        self,
        webhook_url: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        reachability_webhooks_enabled: Union[bool, object] = values.unset,
        acl_enabled: Union[bool, object] = values.unset,
    ) -> ServiceInstance:
        """
        Update the ServiceInstance

        :param webhook_url:
        :param friendly_name:
        :param reachability_webhooks_enabled:
        :param acl_enabled:

        :returns: The updated ServiceInstance
        """
        data = values.of(
            {
                "WebhookUrl": webhook_url,
                "FriendlyName": friendly_name,
                "ReachabilityWebhooksEnabled": serialize.boolean_to_string(
                    reachability_webhooks_enabled
                ),
                "AclEnabled": serialize.boolean_to_string(acl_enabled),
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ServiceInstance(self._version, payload, sid=self._solution["sid"])

    async def update_async(
        self,
        webhook_url: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        reachability_webhooks_enabled: Union[bool, object] = values.unset,
        acl_enabled: Union[bool, object] = values.unset,
    ) -> ServiceInstance:
        """
        Asynchronous coroutine to update the ServiceInstance

        :param webhook_url:
        :param friendly_name:
        :param reachability_webhooks_enabled:
        :param acl_enabled:

        :returns: The updated ServiceInstance
        """
        data = values.of(
            {
                "WebhookUrl": webhook_url,
                "FriendlyName": friendly_name,
                "ReachabilityWebhooksEnabled": serialize.boolean_to_string(
                    reachability_webhooks_enabled
                ),
                "AclEnabled": serialize.boolean_to_string(acl_enabled),
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ServiceInstance(self._version, payload, sid=self._solution["sid"])

    @property
    def documents(self) -> DocumentList:
        """
        Access the documents
        """
        if self._documents is None:
            self._documents = DocumentList(
                self._version,
                self._solution["sid"],
            )
        return self._documents

    @property
    def sync_lists(self) -> SyncListList:
        """
        Access the sync_lists
        """
        if self._sync_lists is None:
            self._sync_lists = SyncListList(
                self._version,
                self._solution["sid"],
            )
        return self._sync_lists

    @property
    def sync_maps(self) -> SyncMapList:
        """
        Access the sync_maps
        """
        if self._sync_maps is None:
            self._sync_maps = SyncMapList(
                self._version,
                self._solution["sid"],
            )
        return self._sync_maps

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Preview.Sync.ServiceContext {}>".format(context)


class ServicePage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> ServiceInstance:
        """
        Build an instance of ServiceInstance

        :param payload: Payload response from the API
        """
        return ServiceInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Preview.Sync.ServicePage>"


class ServiceList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the ServiceList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/Services"

    def create(
        self,
        friendly_name: Union[str, object] = values.unset,
        webhook_url: Union[str, object] = values.unset,
        reachability_webhooks_enabled: Union[bool, object] = values.unset,
        acl_enabled: Union[bool, object] = values.unset,
    ) -> ServiceInstance:
        """
        Create the ServiceInstance

        :param friendly_name:
        :param webhook_url:
        :param reachability_webhooks_enabled:
        :param acl_enabled:

        :returns: The created ServiceInstance
        """

        data = values.of(
            {
                "FriendlyName": friendly_name,
                "WebhookUrl": webhook_url,
                "ReachabilityWebhooksEnabled": serialize.boolean_to_string(
                    reachability_webhooks_enabled
                ),
                "AclEnabled": serialize.boolean_to_string(acl_enabled),
            }
        )
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        payload = self._version.create(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return ServiceInstance(self._version, payload)

    async def create_async(
        self,
        friendly_name: Union[str, object] = values.unset,
        webhook_url: Union[str, object] = values.unset,
        reachability_webhooks_enabled: Union[bool, object] = values.unset,
        acl_enabled: Union[bool, object] = values.unset,
    ) -> ServiceInstance:
        """
        Asynchronously create the ServiceInstance

        :param friendly_name:
        :param webhook_url:
        :param reachability_webhooks_enabled:
        :param acl_enabled:

        :returns: The created ServiceInstance
        """

        data = values.of(
            {
                "FriendlyName": friendly_name,
                "WebhookUrl": webhook_url,
                "ReachabilityWebhooksEnabled": serialize.boolean_to_string(
                    reachability_webhooks_enabled
                ),
                "AclEnabled": serialize.boolean_to_string(acl_enabled),
            }
        )
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        payload = await self._version.create_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return ServiceInstance(self._version, payload)

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[ServiceInstance]:
        """
        Streams ServiceInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[ServiceInstance]:
        """
        Asynchronously streams ServiceInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(page_size=limits["page_size"])

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[ServiceInstance]:
        """
        Lists ServiceInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return list(
            self.stream(
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[ServiceInstance]:
        """
        Asynchronously lists ServiceInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return [
            record
            async for record in await self.stream_async(
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> ServicePage:
        """
        Retrieve a single page of ServiceInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of ServiceInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return ServicePage(self._version, response)

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> ServicePage:
        """
        Asynchronously retrieve a single page of ServiceInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of ServiceInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return ServicePage(self._version, response)

    def get_page(self, target_url: str) -> ServicePage:
        """
        Retrieve a specific page of ServiceInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of ServiceInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return ServicePage(self._version, response)

    async def get_page_async(self, target_url: str) -> ServicePage:
        """
        Asynchronously retrieve a specific page of ServiceInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of ServiceInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return ServicePage(self._version, response)

    def get(self, sid: str) -> ServiceContext:
        """
        Constructs a ServiceContext

        :param sid:
        """
        return ServiceContext(self._version, sid=sid)

    def __call__(self, sid: str) -> ServiceContext:
        """
        Constructs a ServiceContext

        :param sid:
        """
        return ServiceContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Preview.Sync.ServiceList>"
