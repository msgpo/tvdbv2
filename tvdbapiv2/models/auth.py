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


class Auth(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Auth - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'apikey': 'str',
            'username': 'str',
            'userpass': 'str'
        }

        self.attribute_map = {
            'apikey': 'apikey',
            'username': 'username',
            'userpass': 'userpass'
        }

        self._apikey = None
        self._username = None
        self._userpass = None

    @property
    def apikey(self):
        """
        Gets the apikey of this Auth.


        :return: The apikey of this Auth.
        :rtype: str
        """
        return self._apikey

    @apikey.setter
    def apikey(self, apikey):
        """
        Sets the apikey of this Auth.


        :param apikey: The apikey of this Auth.
        :type: str
        """
        self._apikey = apikey

    @property
    def username(self):
        """
        Gets the username of this Auth.


        :return: The username of this Auth.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this Auth.


        :param username: The username of this Auth.
        :type: str
        """
        self._username = username

    @property
    def userpass(self):
        """
        Gets the userpass of this Auth.


        :return: The userpass of this Auth.
        :rtype: str
        """
        return self._userpass

    @userpass.setter
    def userpass(self, userpass):
        """
        Sets the userpass of this Auth.


        :param userpass: The userpass of this Auth.
        :type: str
        """
        self._userpass = userpass

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
