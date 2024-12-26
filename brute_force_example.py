import hashlib
import ecdsa
import base58

def generate_address_from_private_key(private_key_bytes):
    private_key = ecdsa.SigningKey.from_string(private_key_bytes, curve=ecdsa.SECP256k1)
    public_key = private_key.get_verifying_key().to_string()
    public_key_bytes = b'\x04' + public_key

    sha256_1 = hashlib.sha256(public_key_bytes).digest()
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(sha256_1)
    hashed_public_key = ripemd160.digest()

    network_byte = b'\x00' + hashed_public_key
    checksum = hashlib.sha256(hashlib.sha256(network_byte).digest()).digest()[:4]
    binary_address = network_byte + checksum
    bitcoin_address = base58.b58encode(binary_address).decode('utf-8')

    return {
        'private_key': private_key_bytes.hex(),
        'public_key': public_key_bytes.hex(),
        'bitcoin_address': bitcoin_address
    }


def brute_force_attack(target_address, start_key=1, max_attempts=1000*2):
    attempts = 0
    private_key_int = start_key
    
    while attempts < max_attempts:
        # Convert integer to 32-byte private key
        private_key_bytes = private_key_int.to_bytes(32, 'big')
        wallet = generate_address_from_private_key(private_key_bytes)
        attempts += 1
        
        if wallet['bitcoin_address'] == target_address:
            print(f"Match found after {attempts} attempts!")
            return wallet
        
        private_key_int += 1
        
        if attempts % 1000 == 0:
            print(f"Attempt {attempts}: Checked private key {private_key_int}")
    
    print("No match found within attempt limit.")
    return None


# Example usage
if __name__ == "__main__":
    # Choose a specific Bitcoin address to "attack"
    target_address = "1LdRcdxfbSnmCYYNdeYpUnztiYzVfBEQeC"
    brute_force_attack(target_address)
