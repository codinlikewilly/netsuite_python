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

class CustomerAlcoholRecipientType(object):
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
        'id': 'str',
        'ref_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'ref_name': 'refName'
    }

    def __init__(self, id=None, ref_name=None):  # noqa: E501
        """CustomerAlcoholRecipientType - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._ref_name = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if ref_name is not None:
            self.ref_name = ref_name

    @property
    def id(self):
        """Gets the id of this CustomerAlcoholRecipientType.  # noqa: E501


        :return: The id of this CustomerAlcoholRecipientType.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CustomerAlcoholRecipientType.


        :param id: The id of this CustomerAlcoholRecipientType.  # noqa: E501
        :type: str
        """
        allowed_values = ["CONSUMER", "LICENSEE"]  # noqa: E501
        if id not in allowed_values:
            raise ValueError(
                "Invalid value for `id` ({0}), must be one of {1}"  # noqa: E501
                .format(id, allowed_values)
            )

        self._id = id

    @property
    def ref_name(self):
        """Gets the ref_name of this CustomerAlcoholRecipientType.  # noqa: E501


        :return: The ref_name of this CustomerAlcoholRecipientType.  # noqa: E501
        :rtype: str
        """
        return self._ref_name

    @ref_name.setter
    def ref_name(self, ref_name):
        """Sets the ref_name of this CustomerAlcoholRecipientType.


        :param ref_name: The ref_name of this CustomerAlcoholRecipientType.  # noqa: E501
        :type: str
        """

        self._ref_name = ref_name

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
        if issubclass(CustomerAlcoholRecipientType, dict):
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
        if not isinstance(other, CustomerAlcoholRecipientType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
