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

class CustomerLanguage(object):
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
        """CustomerLanguage - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._ref_name = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if ref_name is not None:
            self.ref_name = ref_name

    @property
    def id(self):
        """Gets the id of this CustomerLanguage.  # noqa: E501


        :return: The id of this CustomerLanguage.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CustomerLanguage.


        :param id: The id of this CustomerLanguage.  # noqa: E501
        :type: str
        """
        allowed_values = ["ro_RO", "af_ZA", "tl_PH", "pt_BR", "th_TH", "bn_BD", "cs_CZ", "ca_ES", "hu_HU", "kn_IN", "sk_SK", "es_ES", "nl_NL", "is_IS", "te_IN", "sv_SE", "sq_AL", "es_AR", "da_DK", "ta_IN", "sr_RS", "en", "ar", "hr_HR", "ko_KR", "en_US", "lt_LT", "no_NO", "el_GR", "it_IT", "ru_RU", "pl_PL", "en_AU", "tr_TR", "id_ID", "hi_IN", "mr_IN", "fr_FR", "he_IL", "ja_JP", "de_DE", "ms_MY", "zh_TW", "fr_CA", "pa_IN", "fa_IR", "bg_BG", "vi_VN", "hy_AM", "lb_LU", "xx_US", "sh_RS", "ht_HT", "fi_FI", "en_GB", "gu_IN", "et_EE", "en_CA", "lv_LV", "uk_UA", "bs_BA", "zh_CN", "sl_SI", "pt_PT"]  # noqa: E501
        if id not in allowed_values:
            raise ValueError(
                "Invalid value for `id` ({0}), must be one of {1}"  # noqa: E501
                .format(id, allowed_values)
            )

        self._id = id

    @property
    def ref_name(self):
        """Gets the ref_name of this CustomerLanguage.  # noqa: E501


        :return: The ref_name of this CustomerLanguage.  # noqa: E501
        :rtype: str
        """
        return self._ref_name

    @ref_name.setter
    def ref_name(self, ref_name):
        """Sets the ref_name of this CustomerLanguage.


        :param ref_name: The ref_name of this CustomerLanguage.  # noqa: E501
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
        if issubclass(CustomerLanguage, dict):
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
        if not isinstance(other, CustomerLanguage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
