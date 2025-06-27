from sqlalchemy import Column, String, DateTime, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# SQLAlchemy models base
Base = declarative_base()

class BikeReservation(Base):

    __tablename__ = "bike_reservations" # nome da tabela no banco

    # colunas da tabela(usando postgresql
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()"),
        index=True
    )
    user_id = Column(String(50), nullable=False) # string com tamanho máximo
    bike_id = Column(String(50), nullable=False)
    station_id = Column(String(50), nullable=False)
    reserved_at = Column(
        DateTime(timezone=True),
        server_default=text("NOW()") # usa a função "NOW" do postegrsql

    )
    status = Column(
        String(20),
        nullable=False,
        server_default="pending" #valor padrão
    )

    # metodo para representação em string (debug)
    def __repr__(self):
        return (f"<BikeReservation(id={self.id}"
                f"user_id={self.user_id}"
                f"station={self.station_id}"
                f"status={self.status}")
