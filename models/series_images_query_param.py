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


class SeriesImagesQueryParam(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        SeriesImagesQueryParam - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'key_type': 'str',
            'language_id': 'str',
            'resolution': 'list[str]',
            'sub_key': 'list[str]'
        }

        self.attribute_map = {
            'key_type': 'keyType',
            'language_id': 'languageId',
            'resolution': 'resolution',
            'sub_key': 'subKey'
        }

        self._key_type = None
        self._language_id = None
        self._resolution = None
        self._sub_key = None

    @property
    def key_type(self):
        """
        Gets the key_type of this SeriesImagesQueryParam.


        :return: The key_type of this SeriesImagesQueryParam.
        :rtype: str
        """
        return self._key_type

    @key_type.setter
    def key_type(self, key_type):
        """
        Sets the key_type of this SeriesImagesQueryParam.


        :param key_type: The key_type of this SeriesImagesQueryParam.
        :type: str
        """
        self._key_type = key_type

    @property
    def language_id(self):
        """
        Gets the language_id of this SeriesImagesQueryParam.


        :return: The language_id of this SeriesImagesQueryParam.
        :rtype: str
        """
        return self._language_id

    @language_id.setter
    def language_id(self, language_id):
        """
        Sets the language_id of this SeriesImagesQueryParam.


        :param language_id: The language_id of this SeriesImagesQueryParam.
        :type: str
        """
        self._language_id = language_id

    @property
    def resolution(self):
        """
        Gets the resolution of this SeriesImagesQueryParam.


        :return: The resolution of this SeriesImagesQueryParam.
        :rtype: list[str]
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution):
        """
        Sets the resolution of this SeriesImagesQueryParam.


        :param resolution: The resolution of this SeriesImagesQueryParam.
        :type: list[str]
        """
        self._resolution = resolution

    @property
    def sub_key(self):
        """
        Gets the sub_key of this SeriesImagesQueryParam.


        :return: The sub_key of this SeriesImagesQueryParam.
        :rtype: list[str]
        """
        return self._sub_key

    @sub_key.setter
    def sub_key(self, sub_key):
        """
        Sets the sub_key of this SeriesImagesQueryParam.


        :param sub_key: The sub_key of this SeriesImagesQueryParam.
        :type: list[str]
        """
        self._sub_key = sub_key

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

