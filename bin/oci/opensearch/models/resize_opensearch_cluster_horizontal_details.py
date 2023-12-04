# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ResizeOpensearchClusterHorizontalDetails(object):
    """
    The node count configuration to update on an existing OpenSearch cluster for `horizontal resizing`__.

    __ https://docs.cloud.oracle.com/iaas/Content/search-opensearch/Tasks/resizingacluster.htm#horizontalresize
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ResizeOpensearchClusterHorizontalDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param master_node_count:
            The value to assign to the master_node_count property of this ResizeOpensearchClusterHorizontalDetails.
        :type master_node_count: int

        :param data_node_count:
            The value to assign to the data_node_count property of this ResizeOpensearchClusterHorizontalDetails.
        :type data_node_count: int

        :param opendashboard_node_count:
            The value to assign to the opendashboard_node_count property of this ResizeOpensearchClusterHorizontalDetails.
        :type opendashboard_node_count: int

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ResizeOpensearchClusterHorizontalDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ResizeOpensearchClusterHorizontalDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'master_node_count': 'int',
            'data_node_count': 'int',
            'opendashboard_node_count': 'int',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'master_node_count': 'masterNodeCount',
            'data_node_count': 'dataNodeCount',
            'opendashboard_node_count': 'opendashboardNodeCount',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._master_node_count = None
        self._data_node_count = None
        self._opendashboard_node_count = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def master_node_count(self):
        """
        Gets the master_node_count of this ResizeOpensearchClusterHorizontalDetails.
        The number of master nodes to configure for the cluster.


        :return: The master_node_count of this ResizeOpensearchClusterHorizontalDetails.
        :rtype: int
        """
        return self._master_node_count

    @master_node_count.setter
    def master_node_count(self, master_node_count):
        """
        Sets the master_node_count of this ResizeOpensearchClusterHorizontalDetails.
        The number of master nodes to configure for the cluster.


        :param master_node_count: The master_node_count of this ResizeOpensearchClusterHorizontalDetails.
        :type: int
        """
        self._master_node_count = master_node_count

    @property
    def data_node_count(self):
        """
        Gets the data_node_count of this ResizeOpensearchClusterHorizontalDetails.
        The number of data nodes to configure for the cluster.


        :return: The data_node_count of this ResizeOpensearchClusterHorizontalDetails.
        :rtype: int
        """
        return self._data_node_count

    @data_node_count.setter
    def data_node_count(self, data_node_count):
        """
        Sets the data_node_count of this ResizeOpensearchClusterHorizontalDetails.
        The number of data nodes to configure for the cluster.


        :param data_node_count: The data_node_count of this ResizeOpensearchClusterHorizontalDetails.
        :type: int
        """
        self._data_node_count = data_node_count

    @property
    def opendashboard_node_count(self):
        """
        Gets the opendashboard_node_count of this ResizeOpensearchClusterHorizontalDetails.
        The number of OpenSearch Dashboard nodes to configure for the cluster.


        :return: The opendashboard_node_count of this ResizeOpensearchClusterHorizontalDetails.
        :rtype: int
        """
        return self._opendashboard_node_count

    @opendashboard_node_count.setter
    def opendashboard_node_count(self, opendashboard_node_count):
        """
        Sets the opendashboard_node_count of this ResizeOpensearchClusterHorizontalDetails.
        The number of OpenSearch Dashboard nodes to configure for the cluster.


        :param opendashboard_node_count: The opendashboard_node_count of this ResizeOpensearchClusterHorizontalDetails.
        :type: int
        """
        self._opendashboard_node_count = opendashboard_node_count

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ResizeOpensearchClusterHorizontalDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this ResizeOpensearchClusterHorizontalDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ResizeOpensearchClusterHorizontalDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this ResizeOpensearchClusterHorizontalDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ResizeOpensearchClusterHorizontalDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this ResizeOpensearchClusterHorizontalDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ResizeOpensearchClusterHorizontalDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this ResizeOpensearchClusterHorizontalDetails.
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