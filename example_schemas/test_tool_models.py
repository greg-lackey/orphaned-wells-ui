from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String, Integer, DateTime, Float, Boolean
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import MetaData
import datetime

class Base(DeclarativeBase):
    pass

class Wells(Base):
    """Sqlalchemy wells model"""
    __tablename__ = "wells"
    id: Mapped[int] = mapped_column(primary_key = True)
    api_uwi: Mapped[str] = mapped_column(String)
    name: Mapped[str] = mapped_column(String)
    well_type: Mapped[str] = mapped_column(String)
    spud_date: Mapped[datetime.datetime] = mapped_column(DateTime)
    completion_date: Mapped[datetime.datetime] = mapped_column(DateTime)
    first_production_date: Mapped[datetime.datetime] = mapped_column(DateTime)
    configuration: Mapped[str] = mapped_column(String)
    max_tvd: Mapped[float] = mapped_column(Float)
    max_md: Mapped[float] = mapped_column(Float)
    status: Mapped[str] = mapped_column(String)
    status_date: Mapped[datetime.datetime] = mapped_column(DateTime)
    current_operator: Mapped[str] = mapped_column(String)
    original_operator: Mapped[str] = mapped_column(String)
    surface_latitude: Mapped[float] = mapped_column(Float)
    surface_longitude: Mapped[float] = mapped_column(Float)
    elevation: Mapped[float] = mapped_column(Float)
    plug_date: Mapped[datetime.datetime] = mapped_column(DateTime)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())


class CompletionReports(Base):
    """Sqlalchemy completion reports model"""
    __tablename__ = "completion_reports"
    id: Mapped[int] = mapped_column(primary_key = True)
    well_id: Mapped[int] = mapped_column(ForeignKey("wells.id"))
    api_uwi: Mapped[str] = mapped_column(String)
    document_number: Mapped[int] = mapped_column(Integer)
    date_received: Mapped[datetime.datetime] = mapped_column(DateTime)
    operator_name: Mapped[str] = mapped_column(String)
    Address: Mapped[str] = mapped_column(String)
    city: Mapped[str] = mapped_column(String)
    state: Mapped[str] = mapped_column(String)
    zip_code: Mapped[str] = mapped_column(String)
    county: Mapped[str] = mapped_column(String)
    well_name: Mapped[str] = mapped_column(String)
    well_no: Mapped[str] = mapped_column(String)
    latitude: Mapped[float] = mapped_column(Float)
    longitude: Mapped[float] = mapped_column(Float)
    field_name: Mapped[str] = mapped_column(String)
    spud_date: Mapped[datetime.datetime] = mapped_column(DateTime)
    td_date: Mapped[datetime.datetime] = mapped_column(DateTime)
    casing_set_date: Mapped[datetime.datetime] = mapped_column(DateTime)
    rig_release_date: Mapped[datetime.datetime] = mapped_column(DateTime)
    well_type: Mapped[str] = mapped_column(String)
    true_vertical_td: Mapped[float] = mapped_column(Float)
    true_vertical_pb: Mapped[float] = mapped_column(Float)
    measured_td: Mapped[float] = mapped_column(Float)
    measured_pb: Mapped[float] = mapped_column(Float)
    ground_elevation: Mapped[float] = mapped_column(Float)
    kb_elevation: Mapped[float] = mapped_column(Float)

class User(Base):
    """sqlalchemy user model"""
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key = True)
    username: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)
    password: Mapped[str] = mapped_column(String)
    

def initialize_engine(filename):
    return create_engine(f"sqlite+pysqlite:///{filename}", echo=True)


def initialize_tables(engine):
    Base.metadata.create_all(engine)


def add_row(engine, name):
    this_row = MyTable(name=name)
    print(this_row)
    with Session(engine) as session:
        session.add(this_row)
        session.commit()


my_file = "test_tool.db"

my_engine = initialize_engine(my_file)
initialize_tables(my_engine)


# # Now create the schema graph
# graph = create_schema_graph(
#     metadata=Base.metadata,
#     show_datatypes=False,
#     show_indexes=False,
#     rankdir='LR',
#     concentrate=False)
# graph.write_png('dbschema.png')
