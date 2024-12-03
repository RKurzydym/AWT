from prisma import Prisma, register
from prisma.models import Root,Link,Parent
import asyncio

async def main():
    await printDB("root")
    
    await checkIfInDB("a")
    #await generateDB()

async def generateDB():
    prisma = Prisma()
    await prisma.connect()
    Root = await prisma.root.create(
        data={
            'name': 'test',
            'parents': {
                'create': {
                    'name': 'parent',
                },
            },
            'links':{
                'create':{
                    'name': 'link',
                },
            },
        },
    )
    await prisma.disconnect()
    
async def printDB(name):
    prisma = Prisma()
    await prisma.connect()
    posts = await prisma.query_raw(
    '''
    SELECT *
    FROM %s
    ''' % name
    )
    print(posts)
    await prisma.disconnect()

async def checkIfInDB(name):
    prisma = Prisma()
    await prisma.connect()
    exist = await prisma.query_raw(
    '''
    SELECT *
    FROM root
    WHERE name LIKE '%s'
    ''' % name
    )
    if exist == []:
        await prisma.disconnect()
        print("nothing")
        return False
    
    
    await prisma.disconnect()
    return True


if __name__ == "__main__":
    asyncio.run(main())