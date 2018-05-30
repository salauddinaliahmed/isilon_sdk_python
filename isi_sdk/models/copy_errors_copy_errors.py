# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 6
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CopyErrorsCopyErrors(object):
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
        'error_src': 'str',
        'message': 'str',
        'source': 'str',
        'target': 'str'
    }

    attribute_map = {
        'error_src': 'error_src',
        'message': 'message',
        'source': 'source',
        'target': 'target'
    }

    def __init__(self, error_src=None, message=None, source=None, target=None):  # noqa: E501
        """CopyErrorsCopyErrors - a model defined in Swagger"""  # noqa: E501

        self._error_src = None
        self._message = None
        self._source = None
        self._target = None
        self.discriminator = None

        if error_src is not None:
            self.error_src = error_src
        if message is not None:
            self.message = message
        if source is not None:
            self.source = source
        if target is not None:
            self.target = target

    @property
    def error_src(self):
        """Gets the error_src of this CopyErrorsCopyErrors.  # noqa: E501


        :return: The error_src of this CopyErrorsCopyErrors.  # noqa: E501
        :rtype: str
        """
        return self._error_src

    @error_src.setter
    def error_src(self, error_src):
        """Sets the error_src of this CopyErrorsCopyErrors.


        :param error_src: The error_src of this CopyErrorsCopyErrors.  # noqa: E501
        :type: str
        """

        self._error_src = error_src

    @property
    def message(self):
        """Gets the message of this CopyErrorsCopyErrors.  # noqa: E501


        :return: The message of this CopyErrorsCopyErrors.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this CopyErrorsCopyErrors.


        :param message: The message of this CopyErrorsCopyErrors.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def source(self):
        """Gets the source of this CopyErrorsCopyErrors.  # noqa: E501


        :return: The source of this CopyErrorsCopyErrors.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this CopyErrorsCopyErrors.


        :param source: The source of this CopyErrorsCopyErrors.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def target(self):
        """Gets the target of this CopyErrorsCopyErrors.  # noqa: E501


        :return: The target of this CopyErrorsCopyErrors.  # noqa: E501
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this CopyErrorsCopyErrors.


        :param target: The target of this CopyErrorsCopyErrors.  # noqa: E501
        :type: str
        """

        self._target = target

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CopyErrorsCopyErrors):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
