from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker


DATABASE_URL = 'sqlite+aiosqlite:///./mydatabase.db'

engine = create_async_engine(DATABASE_URL, echo=True)

async_session_maker = async_sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession,
)
