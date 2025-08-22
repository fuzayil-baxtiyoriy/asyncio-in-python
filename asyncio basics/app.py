import asyncio
# coroutine
async def coroutine_add_one(number: int) -> int:
    return number + 1

# normal function
def add_one(number: int) -> int:
    return number + 1

# function_result = add_one(1)
# coroutine_result = coroutine_add_one(1)

# print(f"Function result: {function_result} and the type is {type(function_result)}")
# print(f"Coroutine result: {coroutine_result} and the type is {type(coroutine_result)}")

result = asyncio.run(coroutine_add_one(1))
print(f"Result from asyncio.run: {result} and the type is {type(result)}")