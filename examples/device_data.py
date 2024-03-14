from asyncarve import Arve
import asyncio


async def main() -> None:
    async with Arve("249e597c-e0cc-436e-abbd-867d61d6c5a9", "73bdb639-a454-4f9e-879c-793ee39bb268",
                    "A0120-0000-0000-1798") as arv_cl:
        data = await arv_cl.device_sensor_data()

        print(data)


if __name__ == "__main__":
    asyncio.run(main())
