# coding: utf-8

"""
    NetSuite REST API

    NetSuite REST Record API generated 2023-01-18 at 19:40:11 UTC for account 472052, user will@theapiguys.com with role Keap Integration.  # noqa: E501

    OpenAPI spec version: v1
    Contact: info@netsuite.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class NsResourceCollection(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'links': 'list[NsLink]',
        'total_results': 'int',
        'items': 'list[NsResource]',
        'count': 'int',
        'has_more': 'bool',
        'offset': 'int'
    }

    attribute_map = {
        'links': 'links',
        'total_results': 'totalResults',
        'items': 'items',
        'count': 'count',
        'has_more': 'hasMore',
        'offset': 'offset'
    }

    def __init__(self, links=None, total_results=None, items=None, count=None, has_more=None, offset=None):  # noqa: E501
        """NsResourceCollection - a model defined in Swagger"""  # noqa: E501
        self._links = None
        self._total_results = None
        self._items = None
        self._count = None
        self._has_more = None
        self._offset = None
        self.discriminator = None
        if links is not None:
            self.links = links
        if total_results is not None:
            self.total_results = total_results
        if items is not None:
            self.items = items
        if count is not None:
            self.count = count
        if has_more is not None:
            self.has_more = has_more
        if offset is not None:
            self.offset = offset

    @property
    def links(self):
        """Gets the links of this NsResourceCollection.  # noqa: E501


        :return: The links of this NsResourceCollection.  # noqa: E501
        :rtype: list[NsLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this NsResourceCollection.


        :param links: The links of this NsResourceCollection.  # noqa: E501
        :type: list[NsLink]
        """

        self._links = links

    @property
    def total_results(self):
        """Gets the total_results of this NsResourceCollection.  # noqa: E501


        :return: The total_results of this NsResourceCollection.  # noqa: E501
        :rtype: int
        """
        return self._total_results

    @total_results.setter
    def total_results(self, total_results):
        """Sets the total_results of this NsResourceCollection.


        :param total_results: The total_results of this NsResourceCollection.  # noqa: E501
        :type: int
        """

        self._total_results = total_results

    @property
    def items(self):
        """Gets the items of this NsResourceCollection.  # noqa: E501


        :return: The items of this NsResourceCollection.  # noqa: E501
        :rtype: list[NsResource]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this NsResourceCollection.


        :param items: The items of this NsResourceCollection.  # noqa: E501
        :type: list[NsResource]
        """

        self._items = items

    @property
    def count(self):
        """Gets the count of this NsResourceCollection.  # noqa: E501


        :return: The count of this NsResourceCollection.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this NsResourceCollection.


        :param count: The count of this NsResourceCollection.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def has_more(self):
        """Gets the has_more of this NsResourceCollection.  # noqa: E501


        :return: The has_more of this NsResourceCollection.  # noqa: E501
        :rtype: bool
        """
        return self._has_more

    @has_more.setter
    def has_more(self, has_more):
        """Sets the has_more of this NsResourceCollection.


        :param has_more: The has_more of this NsResourceCollection.  # noqa: E501
        :type: bool
        """

        self._has_more = has_more

    @property
    def offset(self):
        """Gets the offset of this NsResourceCollection.  # noqa: E501


        :return: The offset of this NsResourceCollection.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this NsResourceCollection.


        :param offset: The offset of this NsResourceCollection.  # noqa: E501
        :type: int
        """

        self._offset = offset

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(NsResourceCollection, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NsResourceCollection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
