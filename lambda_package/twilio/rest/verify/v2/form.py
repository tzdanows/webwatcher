r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Verify
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


class FormInstance(InstanceResource):

    class FormTypes(object):
        FORM_PUSH = "form-push"

    """
    :ivar form_type: 
    :ivar forms: Object that contains the available forms for this type. This available forms are given in the standard [JSON Schema](https://json-schema.org/) format
    :ivar form_meta: Additional information for the available forms for this type. E.g. The separator string used for `binding` in a Factor push.
    :ivar url: The URL to access the forms for this type.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        form_type: Optional[FormTypes] = None,
    ):
        super().__init__(version)

        self.form_type: Optional["FormInstance.FormTypes"] = payload.get("form_type")
        self.forms: Optional[Dict[str, object]] = payload.get("forms")
        self.form_meta: Optional[Dict[str, object]] = payload.get("form_meta")
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "form_type": form_type or self.form_type,
        }
        self._context: Optional[FormContext] = None

    @property
    def _proxy(self) -> "FormContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: FormContext for this FormInstance
        """
        if self._context is None:
            self._context = FormContext(
                self._version,
                form_type=self._solution["form_type"],
            )
        return self._context

    def fetch(self) -> "FormInstance":
        """
        Fetch the FormInstance


        :returns: The fetched FormInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "FormInstance":
        """
        Asynchronous coroutine to fetch the FormInstance


        :returns: The fetched FormInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Verify.V2.FormInstance {}>".format(context)


class FormContext(InstanceContext):

    def __init__(self, version: Version, form_type: "FormInstance.FormTypes"):
        """
        Initialize the FormContext

        :param version: Version that contains the resource
        :param form_type: The Type of this Form. Currently only `form-push` is supported.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "form_type": form_type,
        }
        self._uri = "/Forms/{form_type}".format(**self._solution)

    def fetch(self) -> FormInstance:
        """
        Fetch the FormInstance


        :returns: The fetched FormInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return FormInstance(
            self._version,
            payload,
            form_type=self._solution["form_type"],
        )

    async def fetch_async(self) -> FormInstance:
        """
        Asynchronous coroutine to fetch the FormInstance


        :returns: The fetched FormInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return FormInstance(
            self._version,
            payload,
            form_type=self._solution["form_type"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Verify.V2.FormContext {}>".format(context)


class FormList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the FormList

        :param version: Version that contains the resource

        """
        super().__init__(version)

    def get(self, form_type: "FormInstance.FormTypes") -> FormContext:
        """
        Constructs a FormContext

        :param form_type: The Type of this Form. Currently only `form-push` is supported.
        """
        return FormContext(self._version, form_type=form_type)

    def __call__(self, form_type: "FormInstance.FormTypes") -> FormContext:
        """
        Constructs a FormContext

        :param form_type: The Type of this Form. Currently only `form-push` is supported.
        """
        return FormContext(self._version, form_type=form_type)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Verify.V2.FormList>"
