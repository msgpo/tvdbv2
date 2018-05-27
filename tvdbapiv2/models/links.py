# coding: utf-8

"""
Copyright 2015 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat

from six import iteritems


class Links(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Links - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'first': 'int',
            'last': 'int',
            'next': 'int',
            'previous': 'int'
        }

        self.attribute_map = {
            'first': 'first',
            'last': 'last',
            'next': 'next',
            'previous': 'previous'
        }

        self._first = None
        self._last = None
        self._next = None
        self._previous = None

    @property
    def first(self):
        """
        Gets the first of this Links.


        :return: The first of this Links.
        :rtype: int
        """
        return self._first

    @first.setter
    def first(self, first):
        """
        Sets the first of this Links.


        :param first: The first of this Links.
        :type: int
        """
        self._first = first

    @property
    def last(self):
        """
        Gets the last of this Links.


        :return: The last of this Links.
        :rtype: int
        """
        return self._last

    @last.setter
    def last(self, last):
        """
        Sets the last of this Links.


        :param last: The last of this Links.
        :type: int
        """
        self._last = last

    @property
    def next(self):
        """
        Gets the next of this Links.


        :return: The next of this Links.
        :rtype: int
        """
        return self._next

    @next.setter
    def next(self, next):
        """
        Sets the next of this Links.


        :param next: The next of this Links.
        :type: int
        """
        self._next = next

    @property
    def previous(self):
        """
        Gets the previous of this Links.


        :return: The previous of this Links.
        :rtype: int
        """
        return self._previous

    @previous.setter
    def previous(self, previous):
        """
        Sets the previous of this Links.


        :param previous: The previous of this Links.
        :type: int
        """
        self._previous = previous

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
