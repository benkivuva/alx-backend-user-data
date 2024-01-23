#!/usr/bin/env python3
"""
Contains SQLAlchemy model named User.
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from typing import Optional

Base = declarative_base()


class User(Base):
    """
    Representation of a user.

    Attributes:
    - id: int, primary key
    - email: str, non-nullable
    - hashed_password: str, non-nullable
    - session_id: Optional[str], nullable
    - reset_token: Optional[str], nullable
    """
    __tablename__ = 'users'

    id: int = Column(Integer, primary_key=True)
    email: str = Column(String(250), nullable=False)
    hashed_password: str = Column(String(250), nullable=False)
    session_id: Optional[str] = Column(String(250), nullable=True)
    reset_token: Optional[str] = Column(String(250), nullable=True)
