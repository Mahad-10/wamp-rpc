import txaio

txaio.use_asyncio()  # noqa

from autobahn.asyncio import ApplicationSession
from autobahn.asyncio.wamp import ApplicationRunner


class WampRegister(ApplicationSession):

    async def onJoin(self, details):
        async def add(a, b):
            return a + b

        await self.register(add, 'pk.codebase.add')
        print('Registered methods; ready for frontend.')


if __name__ == '__main__':
    runner = ApplicationRunner('ws://0.0.0.0:8081/ws', 'realm1')
    runner.run(WampRegister)
