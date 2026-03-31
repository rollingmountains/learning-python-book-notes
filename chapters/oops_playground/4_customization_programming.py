"""One of the reason OOP is preferred over modules and functions to write program is because it provides an option to customize an existing program.
    1. An existing program (OOP class) that requires an additional behaviour or feature can be solved by subclassing the existing class and customizing the subclass with the requried additional behaviour sometimes overriding paretn class behaviour. This allows changes without chaging the original behaviour nor writing the new requirements from scratch as if writing a new program.
    2. The customization can in fact expand to cases where a new program needs certain behaviours and features which are already available in program written by others. Then i can subclass from those program and add my customized behaviour without having to write other behaviours that we get from the parent class.
    3. This customization is actually very obvision in the frameworks that are built on top of a programming language. Frameowrks provide plenty of parent classes that we can import and sublcass and start using in our program by adding additional behviour we want into the subclass

Let's see the third point in detail keeping SQLALCHEMY as the framework that helps us do the work of sql table construction without knowing anything about sql commands"""

# sqlalchemy's orm module exposes DeclarativeBase, Mapped and a function mapped_column
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

# DeclarativeBase abstracts the raw conversion of python code to sql table creating and syntaxes designed in the sqlalchemy metaclass and provides a developer friendly interface to work with


# Base class subclasses from DeclarativeBase superclass so that an identify can be set which then acts as the namespace for all the models created by subclassing base. By this all the instance of Base gets to access all the funcionalities of the metaclass so as to create tables and make entries into the tables in a customized way
class Base(DeclarativeBase):
    pass


# User class subclasses from the Base class and customizes the table structure and column permissions as per the need of the app
class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str]
