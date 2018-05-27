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


class User(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        User - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'user_name': 'str',
            'language': 'str',
            'favorites_displaymode': 'str'
        }

        self.attribute_map = {
            'user_name': 'userName',
            'language': 'language',
            'favorites_displaymode': 'favoritesDisplaymode'
        }

        self._user_name = None
        self._language = None
        self._favorites_displaymode = None

    @property
    def user_name(self):
        """
        Gets the user_name of this User.


        :return: The user_name of this User.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this User.


        :param user_name: The user_name of this User.
        :type: str
        """
        self._user_name = user_name

    @property
    def language(self):
        """
        Gets the language of this User.


        :return: The language of this User.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """
        Sets the language of this User.


        :param language: The language of this User.
        :type: str
        """
        self._language = language

    @property
    def favorites_displaymode(self):
        """
        Gets the favorites_displaymode of this User.


        :return: The favorites_displaymode of this User.
        :rtype: str
        """
        return self._favorites_displaymode

    @favorites_displaymode.setter
    def favorites_displaymode(self, favorites_displaymode):
        """
        Sets the favorites_displaymode of this User.


        :param favorites_displaymode: The favorites_displaymode of this User.
        :type: str
        """
        self._favorites_displaymode = favorites_displaymode

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
