import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():
    server_params = StdioServerParameters(
        command="python",
        args=["prompt_server.py"],
        env=None,
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            print("\nConnected to Study Prompt Server.\n")

            while True:
                print("Choose an option:")
                print("1. Get explanation prompt")
                print("2. Get quiz prompt")
                print("3. Exit")

                choice = input("Enter 1, 2, or 3: ").strip()

                if choice == "1":
                    topic = input("Enter topic: ").strip()
                    level = input("Enter level (example: beginner, 10th class): ").strip()

                    result = await session.get_prompt(
                        "explain_topic",
                        arguments={"topic": topic, "level": level}
                    )

                    print("\nReturned prompt:\n")
                    for msg in result.messages:
                        print(msg.content)

                elif choice == "2":
                    topic = input("Enter topic: ").strip()
                    num_questions = int(input("How many questions? ").strip())

                    result = await session.get_prompt(
                        "make_quiz",
                        arguments={"topic": topic, "num_questions": num_questions}
                    )

                    print("\nReturned prompt:\n")
                    for msg in result.messages:
                        print(msg.content)

                elif choice == "3":
                    print("Goodbye!")
                    break

                else:
                    print("Invalid choice. Try again.")


if __name__ == "__main__":
    asyncio.run(main())