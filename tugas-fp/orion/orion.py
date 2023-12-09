n = int(input())
items = [
    dict(zip(("i_id", "name", "price", "quality"), input().split())) for _ in range(n)
]
prices = sorted(items, key=lambda x: (int(x["price"]), int(x["i_id"])))
qualities = sorted(
    items, key=lambda x: (int(x["quality"]), -int(x["i_id"])), reverse=True
)

print(
    f'Best item for price is: {prices[0]["i_id"]} {prices[0]["name"]} {prices[0]["price"]} {prices[0]["quality"]}'
)
print(
    f'Best item for quality is : {qualities[0]["i_id"]} {qualities[0]["name"]} {qualities[0]["price"]} {qualities[0]["quality"]}'
)  # See that space? This one ^
# Before the colon, yeah, I know, very crucial, amirite.
