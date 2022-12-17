from app.api.models import TicketSchema
from app.db import ticket, database
from sqlalchemy import func

# ticket table 





# SELECT * from ticket where ID = ?
async def get(id: int):
    query = ticket.select().where(id == ticket.c.id)
    return await database.fetch_one(query=query)

# SELECT count(id) from ticket
async def t_count():
    query = "SELECT count(id) FROM ticket"
    return await database.fetch_one(query=query)

# SELCT * from ticket # expenssive 
async def get_all():
    query = ticket.select()
    return await database.fetch_all(query=query)

# insert new entry into ticket table
async def post(payload: TicketSchema):
    query = ticket.insert().values(title=payload.title, description=payload.description,\
            status=payload.status, agent=payload.agent, customer=payload.customer, agent_notes=payload.agent_notes)
    return await database.execute(query=query)

# update existing ticket using id column 
async def put(id: int, payload: TicketSchema):
    query = (
        ticket
        .update()
        .where(id == ticket.c.id)
        .values(title=payload.title, description=payload.description, \
        customer=payload.customer, status=payload.status, agent=payload.agent)
        #.values(status=payload.status, agent=payload.agent)
        .returning(ticket.c.id)
    )
    return await database.execute(query=query)

# delete entry from ticket table using ID 
# this will be removed in future 
async def delete(id: int):
    query = ticket.delete().where(id == ticket.c.id)
    return await database.execute(query=query)
