import asyncio
from bot_config import bot, dp, db
from handlers import (myinfo, random, start, review_dialog,dish_fsm)


async def main():
    db.create_tables()
    dp.include_router(myinfo.myinfo_router)
    dp.include_router(random.random_router)
    dp.include_router(start.start_router)
    dp.include_router(review_dialog.review_router)
    dp.include_router(dish_fsm.dish_router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
