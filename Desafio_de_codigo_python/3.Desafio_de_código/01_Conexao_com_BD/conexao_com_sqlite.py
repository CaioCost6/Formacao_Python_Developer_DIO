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
    id = Column(Integer, primary_key=True)
    name = Column(String)
    cpf = Column(String(14))
    endereco = Column(String)

    conta = relationship(
        "Conta", back_populates="cliente", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"Cliente(id={self.id}, name={self.name}, cpf={self.cpf}, endereco={self.endereco})"


class Conta(Base):
    __tablename__ = "conta"
    id = Column(Integer, primary_key=True)
    tipo = Column(String)
    agencia = Column(Integer)
    cliente_id = Column(Integer, ForeignKey("cliente_banco.id"), nullable=False)

    cliente = relationship("Cliente", back_populates="conta")

    def __repr__(self):
        return f"Conta(id={self.id}, Tipo de Conta={self.tipo}, agencia={self.agencia})"


print(Cliente.__tablename__)
print(Conta.__tablename__)

# Conexão com o banco de dados
engine = create_engine("sqlite://")

# Criando as classes como tabelas no banco de dados
Base.metadata.create_all(engine)

# Investiga o esquema de banco de dados

inspetor_engine = inspect(engine)
print(inspetor_engine.has_table("cliente_banco"))
print(inspetor_engine.get_table_names())
print(inspetor_engine.default_schema_name)


with Session(engine) as session:
    juliana = Cliente(
        name='juliana',
        cpf='850.703.602.65',
        endereco='Rua piaui N°355',
        conta=[Conta(tipo='Corrente', agencia=413)],
    )

    sandy = Cliente(
        name='sandy',
        cpf='003.545.845.85',
        endereco='Rua Idealista N°1390',
        conta=[Conta(tipo='Poupança', agencia=412)],
    )

    patrick = Cliente(
        name='patrick',
        cpf='666.703.554.60',
        endereco='Rua São Paulo N°2022',
        conta=[Conta(tipo='Corrente', agencia=415)]
    )

# Enviando para o BD (persitência de dados)
    session.add_all([juliana, sandy, patrick])

    session.commit()

stmt = select(Cliente)
print('\nRecuperando usuários:')
for cliente in session.scalars(stmt):
    print(cliente)

stmt = select(Cliente).where(Cliente.name.in_(["juliana", "sandy"]))
print('\nRecuperando usuários por filtro:')
for cliente in session.scalars(stmt):
    print(cliente)

stmt_contas = select(Conta).where(Conta.cliente_id.in_([2]))
print('\nRecuperando os dados da conta de Sandy:')
for conta in session.scalars(stmt_contas):
    print(conta)


stmt_order = select(Cliente).order_by(Cliente.name.desc())
print("\nRecuperando info de maneira ordenada:")
for result in session.scalars(stmt_order):
    print(result)

stmt_join = select(Cliente.cpf, Conta.agencia).join_from(Conta, Cliente)
print("\nCPF dos Clientes:")
for result in session.scalars(stmt_join):
    print(result)

connection = engine.connect()
results = connection.execute(stmt_join).fetchall()
print("\nExecutando statement a partir da connection:")
for result in results:
    print(result)

