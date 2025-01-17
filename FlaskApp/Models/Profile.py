from typing import List
from sqlalchemy import String
from sqlalchemy.dialects.sqlite import TEXT
from sqlalchemy.orm import Mapped, mapped_column, relationship
from FlaskApp import db


class Profile(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(80), nullable=True)
    tagline: Mapped[str] = mapped_column(String(120), nullable=True)
    email: Mapped[str] = mapped_column(String(120), nullable=True)
    github: Mapped[str] = mapped_column(String(120), nullable=True)
    linkedin: Mapped[str] = mapped_column(String(120), nullable=True)
    about: Mapped[str] = mapped_column(TEXT, nullable=True)
    projects: Mapped[List['Project']] = relationship(back_populates='profile')
    employers: Mapped[List['Employer']] = relationship(back_populates='profile')
    consulting: Mapped[List['Consulting']] = relationship(back_populates='profile')
    education: Mapped[List['Education']] = relationship(back_populates='profile')
