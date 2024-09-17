r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Content
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from typing import Any, Dict, Optional
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class ApprovalFetchInstance(InstanceResource):
    """
    :ivar sid: The unique string that that we created to identify the Content resource.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/usage/api/account) that created Content resource.
    :ivar whatsapp: Contains the whatsapp approval information for the Content resource, with fields such as approval status, rejection reason, and category, amongst others.
    :ivar url: The URL of the resource, relative to `https://content.twilio.com`.
    """

    def __init__(self, version: Version, payload: Dict[str, Any], content_sid: str):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.whatsapp: Optional[Dict[str, object]] = payload.get("whatsapp")
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "content_sid": content_sid,
        }
        self._context: Optional[ApprovalFetchContext] = None

    @property
    def _proxy(self) -> "ApprovalFetchContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: ApprovalFetchContext for this ApprovalFetchInstance
        """
        if self._context is None:
            self._context = ApprovalFetchContext(
                self._version,
                content_sid=self._solution["content_sid"],
            )
        return self._context

    def fetch(self) -> "ApprovalFetchInstance":
        """
        Fetch the ApprovalFetchInstance


        :returns: The fetched ApprovalFetchInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "ApprovalFetchInstance":
        """
        Asynchronous coroutine to fetch the ApprovalFetchInstance


        :returns: The fetched ApprovalFetchInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Content.V1.ApprovalFetchInstance {}>".format(context)


class ApprovalFetchContext(InstanceContext):

    def __init__(self, version: Version, content_sid: str):
        """
        Initialize the ApprovalFetchContext

        :param version: Version that contains the resource
        :param content_sid: The Twilio-provided string that uniquely identifies the Content resource whose approval information to fetch.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "content_sid": content_sid,
        }
        self._uri = "/Content/{content_sid}/ApprovalRequests".format(**self._solution)

    def fetch(self) -> ApprovalFetchInstance:
        """
        Fetch the ApprovalFetchInstance


        :returns: The fetched ApprovalFetchInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return ApprovalFetchInstance(
            self._version,
            payload,
            content_sid=self._solution["content_sid"],
        )

    async def fetch_async(self) -> ApprovalFetchInstance:
        """
        Asynchronous coroutine to fetch the ApprovalFetchInstance


        :returns: The fetched ApprovalFetchInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return ApprovalFetchInstance(
            self._version,
            payload,
            content_sid=self._solution["content_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Content.V1.ApprovalFetchContext {}>".format(context)


class ApprovalFetchList(ListResource):

    def __init__(self, version: Version, content_sid: str):
        """
        Initialize the ApprovalFetchList

        :param version: Version that contains the resource
        :param content_sid: The Twilio-provided string that uniquely identifies the Content resource whose approval information to fetch.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "content_sid": content_sid,
        }

    def get(self) -> ApprovalFetchContext:
        """
        Constructs a ApprovalFetchContext

        """
        return ApprovalFetchContext(
            self._version, content_sid=self._solution["content_sid"]
        )

    def __call__(self) -> ApprovalFetchContext:
        """
        Constructs a ApprovalFetchContext

        """
        return ApprovalFetchContext(
            self._version, content_sid=self._solution["content_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Content.V1.ApprovalFetchList>"
