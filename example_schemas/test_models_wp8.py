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


class WellSidetracks(Base):
    """Sqlalchemy well sidetracks model"""
    __tablename__ = "sidetracks"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    well_id: Mapped[int] = mapped_column(ForeignKey("wells.id"))
    api_uwi_12: Mapped[str] = mapped_column(String)
    number: Mapped[int] = mapped_column(Integer)
    spud_date: Mapped[datetime.datetime] = mapped_column(DateTime)
    completion_date: Mapped[datetime.datetime] = mapped_column(DateTime)
    first_production_date: Mapped[datetime.datetime] = mapped_column(DateTime)
    status: Mapped[str] = mapped_column(String)
    status_date: Mapped[datetime.datetime] = mapped_column(DateTime)
    measured_td: Mapped[float] = mapped_column(Float)
    measured_pb_depth: Mapped[float] = mapped_column(Float)
    true_vertical_td: Mapped[float] = mapped_column(Float)
    true_vertical_pb_depth: Mapped[float] = mapped_column(Float)
    bottom_hole_latitude: Mapped[float] = mapped_column(Float)
    bottom_hole_longitude: Mapped[float] = mapped_column(Float)
    last_sidetrack: Mapped[bool] = mapped_column(Boolean, nullable = False, default = False)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

class WellCasings(Base):
    """Sqlalchemy well casings model"""
    __tablename__ = "casings"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    sidetrack_id: Mapped[int] = mapped_column(ForeignKey("sidetracks.id"))
    number: Mapped[int] = mapped_column(Integer)
    casing_type: Mapped[str] = mapped_column(String)
    hole_size: Mapped[float] = mapped_column(Float)
    outer_diameter: Mapped[float] = mapped_column(Float)
    inner_diameter: Mapped[float] = mapped_column(Float)
    weight: Mapped[float] = mapped_column(Float)
    grade: Mapped[float] = mapped_column(Float)
    is_liner: Mapped[bool] = mapped_column(Boolean)
    is_cut: Mapped[bool] = mapped_column(Boolean)
    top_depth: Mapped[float] = mapped_column(Float)
    true_vertical_td: Mapped[float] = mapped_column(Float)
    measured_td: Mapped[float] = mapped_column(Float)
    perf_top: Mapped[float] = mapped_column(Float)
    perf_bottom: Mapped[float] = mapped_column(Float)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())


class WellTubings(Base):
    """Sqlalchemy well tubings model"""
    __tablename__ = "tubings"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    sidetrack_id: Mapped[int] = mapped_column(ForeignKey("sidetracks.id"))
    outer_diameter: Mapped[float] = mapped_column(Float)
    inner_diameter: Mapped[float] = mapped_column(Float)
    weight: Mapped[float] = mapped_column(Float)
    grade: Mapped[float] = mapped_column(Float)
    is_cut: Mapped[bool] = mapped_column(Boolean)
    top_depth: Mapped[float] = mapped_column(Float)
    true_vertical_td: Mapped[float] = mapped_column(Float)
    measured_td: Mapped[float] = mapped_column(Float)
    packer_depth: Mapped[float] = mapped_column(Float)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())


class WellCement(Base):
    """Sqlalchemy well cement model"""
    __tablename__ = "cement"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    casing_id: Mapped[int] = mapped_column(ForeignKey("casings.id"))
    install_method: Mapped[str] = mapped_column(String)
    cement_type: Mapped[str] = mapped_column(String)
    density: Mapped[Float] = mapped_column(Float)
    quantity: Mapped[Float] = mapped_column(Float)
    reported_top: Mapped[Float] = mapped_column(Float)
    bottom: Mapped[Float] = mapped_column(Float)
    estimated_top: Mapped[Float] = mapped_column(Float)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

class WellCasingPlugs(Base):
    """Sqlalchemy well casing plugs model"""
    __tablename__ = "casing_plugs"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    casing_id: Mapped[int] = mapped_column(ForeignKey("casings.id"))
    plug_type: Mapped[str] = mapped_column(String)
    cement_type: Mapped[str] = mapped_column(String)
    density: Mapped[Float] = mapped_column(Float)
    volume: Mapped[Float] = mapped_column(Float)
    top: Mapped[Float] = mapped_column(Float)
    bottom: Mapped[Float] = mapped_column(Float)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    
class WellAnnularPlugs(Base):
    """Sqlalchemy well casing plugs model"""
    __tablename__ = "annular_plugs"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    casing_id: Mapped[int] = mapped_column(ForeignKey("casings.id"))
    plug_type: Mapped[str] = mapped_column(String)
    cement_type: Mapped[str] = mapped_column(String)
    density: Mapped[Float] = mapped_column(Float)
    volume: Mapped[Float] = mapped_column(Float)
    top: Mapped[Float] = mapped_column(Float)
    bottom: Mapped[Float] = mapped_column(Float)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    
class FieldMeasurements(Base):
    """Sqlalchemy field measurements model"""
    __tablename__ = "field_measurements"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    well_id: Mapped[int] = mapped_column(ForeignKey("wells.id"))
    site_condition: Mapped[str] = mapped_column(String)
    emissions_measurement: Mapped[float] = mapped_column(Float)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())


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


my_file = "test.db"

my_engine = initialize_engine(my_file)
initialize_tables(my_engine)


# Now create the schema graph
graph = create_schema_graph(
    metadata=Base.metadata,
    show_datatypes=False,
    show_indexes=False,
    rankdir='LR',
    concentrate=False)
graph.write_png('dbschema.png')