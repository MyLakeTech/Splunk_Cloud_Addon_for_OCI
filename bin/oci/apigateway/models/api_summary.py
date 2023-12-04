# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ApiSummary(object):
    """
    A summary of the API.
    """

    #: A constant which can be used with the lifecycle_state property of a ApiSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a ApiSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ApiSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a ApiSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a ApiSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a ApiSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new ApiSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ApiSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this ApiSummary.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ApiSummary.
        :type compartment_id: str

        :param time_created:
            The value to assign to the time_created property of this ApiSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ApiSummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ApiSummary.
            Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this ApiSummary.
        :type lifecycle_details: str

        :param specification_type:
            The value to assign to the specification_type property of this ApiSummary.
        :type specification_type: str

        :param validation_results:
            The value to assign to the validation_results property of this ApiSummary.
        :type validation_results: list[oci.apigateway.models.ApiValidationResult]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ApiSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ApiSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'specification_type': 'str',
            'validation_results': 'list[ApiValidationResult]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'specification_type': 'specificationType',
            'validation_results': 'validationResults',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._specification_type = None
        self._validation_results = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ApiSummary.
        The `OCID`__ of the resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this ApiSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ApiSummary.
        The `OCID`__ of the resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this ApiSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        Gets the display_name of this ApiSummary.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My new resource`


        :return: The display_name of this ApiSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ApiSummary.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My new resource`


        :param display_name: The display_name of this ApiSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ApiSummary.
        The `OCID`__ of the compartment in which the
        resource is created.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ApiSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ApiSummary.
        The `OCID`__ of the compartment in which the
        resource is created.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ApiSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def time_created(self):
        """
        Gets the time_created of this ApiSummary.
        The time this resource was created. An RFC3339 formatted datetime string.


        :return: The time_created of this ApiSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ApiSummary.
        The time this resource was created. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this ApiSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this ApiSummary.
        The time this resource was last updated. An RFC3339 formatted datetime string.


        :return: The time_updated of this ApiSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ApiSummary.
        The time this resource was last updated. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this ApiSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this ApiSummary.
        The current state of the API.

        Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ApiSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ApiSummary.
        The current state of the API.


        :param lifecycle_state: The lifecycle_state of this ApiSummary.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this ApiSummary.
        A message describing the current lifecycleState in more detail. For ACTIVE
        state it describes if the document has been validated and the possible values are:
        - 'New' for just updated API Specifications
        - 'Validating' for a document which is being validated.
        - 'Valid' the document has been validated without any errors or warnings
        - 'Warning' the document has been validated and contains warnings
        - 'Error' the document has been validated and contains errors
        - 'Failed' the document validation failed
        - 'Canceled' the document validation was canceled

        For other states it may provide more details like actionable information.


        :return: The lifecycle_details of this ApiSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this ApiSummary.
        A message describing the current lifecycleState in more detail. For ACTIVE
        state it describes if the document has been validated and the possible values are:
        - 'New' for just updated API Specifications
        - 'Validating' for a document which is being validated.
        - 'Valid' the document has been validated without any errors or warnings
        - 'Warning' the document has been validated and contains warnings
        - 'Error' the document has been validated and contains errors
        - 'Failed' the document validation failed
        - 'Canceled' the document validation was canceled

        For other states it may provide more details like actionable information.


        :param lifecycle_details: The lifecycle_details of this ApiSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def specification_type(self):
        """
        Gets the specification_type of this ApiSummary.
        Type of API Specification file.


        :return: The specification_type of this ApiSummary.
        :rtype: str
        """
        return self._specification_type

    @specification_type.setter
    def specification_type(self, specification_type):
        """
        Sets the specification_type of this ApiSummary.
        Type of API Specification file.


        :param specification_type: The specification_type of this ApiSummary.
        :type: str
        """
        self._specification_type = specification_type

    @property
    def validation_results(self):
        """
        Gets the validation_results of this ApiSummary.
        Status of each feature available from the API.


        :return: The validation_results of this ApiSummary.
        :rtype: list[oci.apigateway.models.ApiValidationResult]
        """
        return self._validation_results

    @validation_results.setter
    def validation_results(self, validation_results):
        """
        Sets the validation_results of this ApiSummary.
        Status of each feature available from the API.


        :param validation_results: The validation_results of this ApiSummary.
        :type: list[oci.apigateway.models.ApiValidationResult]
        """
        self._validation_results = validation_results

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ApiSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair
        with no predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this ApiSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ApiSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair
        with no predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this ApiSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ApiSummary.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this ApiSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ApiSummary.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this ApiSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other