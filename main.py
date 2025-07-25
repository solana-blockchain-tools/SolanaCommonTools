from solders.keypair import Keypair

private_key = "2Gajbe1FGgSsb42iD41tjFeLE9pBzN9UYLmqXb4tYqFDSeL5k73dLoJ25B4joQdrKaHJGv4Y4YW4DBRQdSuNHkJD"

keypair = Keypair.from_base58_string(private_key)

print(f"Address: {keypair.pubkey()}")
print(f"BS58: {keypair}")
print(f"UINT8: {keypair.to_bytes_array()}")
