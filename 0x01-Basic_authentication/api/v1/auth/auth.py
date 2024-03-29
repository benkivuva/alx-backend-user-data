#!/usr/bin/env python3
"""
Class Auth
"""
from flask import request
from typing import List, TypeVar


class Auth():
    """flask authorization Auth Class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Public method that define which routes don't need authentication.
        This method must be slash tolerant.
            Returns:
            True if the path is not in the list of strings excluded_paths.
            True if path is None
            True if excluded_paths is None or empty
            False if path is in excluded_paths
            excluded_paths contains string path always ending by a /
        """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True

        if path[-1] != '/':
            path = path + '/'

        if path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """Public method for authorization header
            Returns: None - request
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Public method that requires authentication
            Returns: None - request
        """
        return None

    def authorization_header(self, request=None) -> str:
        """Public method for authorization header
        Returns:
            None if request is None or the header key Authorization isn't
            present Otherwise, returns the value of the Authorization header
        """
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']
