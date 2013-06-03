from alembic import context
from spire.schema import Schema

interface = Schema.interface('narrative')

def run_migrations_offline():
    context.configure(url=interface['url'])
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    engine = interface.get_engine()
    connection = engine.connect()

    context.configure(connection=connection,
        compare_type=True,
        target_metadata=interface.schema.metadata,
        sqlalchemy_module_prefix=None)

    try:
        with context.begin_transaction():
            context.run_migrations()
    finally:
        connection.close()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
