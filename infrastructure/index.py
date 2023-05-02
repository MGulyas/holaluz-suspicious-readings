from domain.client.client_repository import ClientRepository
from domain.reading.reading_repository import ReadingRepository

reading_repository = ReadingRepository()

client_repository = ClientRepository(reading_repository)


