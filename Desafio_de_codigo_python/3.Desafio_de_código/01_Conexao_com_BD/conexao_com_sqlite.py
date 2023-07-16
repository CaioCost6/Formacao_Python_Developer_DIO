from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy import select
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Cliente(Base):
    __tablename__ = "cliente_banco"
    # atributos
    id = Column(Integer, primary_key=True)
    name = Column(String)
    cpf = Column(String(9))
    endereco = Column(String(9))

    conta = relationship(
        "Conta", back_populates="cliente", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"Cliente(id={self.id}, name={self.name}, endereco={self.endereco})"


class Conta(Base):
    __tablename__ = "conta"
    id = Column(Integer, primary_key=True)
    tipo = Column(String)
    agencia = Column(String)
    cliente_id = Column(Integer, ForeignKey("cliente_banco.id"), nullable=False)

    cliente = relationship("Cliente", back_populates="conta")

    def __repr__(self):
        return f"Conta(id={self.id}, agencia={self.agencia})"


print(Cliente.__tablename__)
print(Conta.__tablename__)


engine = create_engine("sqlite://")

Base.metadata.create_all(engine)


inspetor_engine = inspect(engine)
print(inspetor_engine.has_table("cliente_banco"))
print(inspetor_engine.get_table_names())
print(inspetor_engine.default_schema_name)

with Session(engine) as session:
    juliana = Cliente(
        name='juliana',
        cpf='850.703.602.65',
        conta={Conta(agencia='0007')}
    )

    sandy = Cliente(
        name='sandy',
        cpf='003.545.845.85',
        conta=[Conta(agencia='0004')]
    )

    patrick = Cliente(
        name='patrick',
        cpf='666.703.554.60',
        conta = [Conta(agencia='0004')]
    )

    # enviando para o BD (persitência de dados)
    session.add_all([juliana, sandy, patrick])

    session.commit()

stmt = select(Cliente).where(Cliente.name.in_(["juliana", 'sandy']))
print('Recuperando usuários a partir de condição de filtragem')
for cliente in session.scalars(stmt):
    print(cliente)

stmt_contas = select(Conta).where(Conta.user_id.in_([2]))
print('\nRecuperando os endereços de email de Sandy')
for conta in session.scalars(stmt_contas):
    print(conta)


stmt_order = select(Cliente).order_by(Cliente.fullname.desc())
print("\nRecuperando info de maneira ordenada")
for result in session.scalars(stmt_order):
    print(result)

stmt_join = select(Cliente.fullname, Conta.agencia).join_from(Conta, Cliente)
print("\n")
for result in session.scalars(stmt_join):
    print(result)


connection = engine.connect()
results = connection.execute(stmt_join).fetchall()
print("\nExecutando statement a partir da connection")
for result in results:
    print(result)
