import os
import hashlib
from cryptography.fernet import Fernet

KEY_FILE = "secret.key"

def load_or_generate_key():
    """Loads an existing key from a local file, or generates a new one if missing."""
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as f:
            return f.read()
    else:
        # Generate a new key and save it locally
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)
        print(f"[!] New key generated and saved locally to '{KEY_FILE}'. Do not upload this file to GitHub!")
        return key

def encrypt_file(input_filepath, output_filepath, key):
    """Encrypts a file using Fernet symmetric encryption."""
    fernet = Fernet(key)
    
    with open(input_filepath, "rb") as f:
        original_data = f.read()
        
    encrypted_data = fernet.encrypt(original_data)
    
    with open(output_filepath, "wb") as f:
        f.write(encrypted_data)
    print(f"[+] File '{input_filepath}' successfully encrypted to '{output_filepath}'.")


def decrypt_file(input_filepath, output_filepath, key):
    """Decrypts a Fernet encrypted file."""
    fernet = Fernet(key)
    
    with open(input_filepath, "rb") as f:
        encrypted_data = f.read()
        
    decrypted_data = fernet.decrypt(encrypted_data)
    
    with open(output_filepath, "wb") as f:
        f.write(decrypted_data)
    print(f"[+] File '{input_filepath}' successfully decrypted to '{output_filepath}'.")


def calculate_sha256(filepath):
    """Calculates the SHA-256 hash of a file to check its integrity."""
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        # Read in blocks to handle large files efficiently
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


def main():
    print("--- Polytechnic Security Toolkit ---")
    key = load_or_generate_key()
    
    # Example usage mimicking operations requested by the lecturer
    sample_file = "student_records.csv"
    encrypted_file = "student_records.enc"
    decrypted_file = "student_records_decrypted.csv"
    
    # Create a dummy sample file locally if it doesn't exist yet for testing
    if not os.path.exists(sample_file):
        with open(sample_file, "w") as f:
            f.write("id,name,gpa\n1001,Alice Smith,3.8\n1002,Bob Jones,3.2\n")
        print(f"[!] Created dummy test file '{sample_file}'")

    try:
        # Calculate original hash
        orig_hash = calculate_sha256(sample_file)
        print(f"[*] Original SHA-256: {orig_hash}")
        
        # a. Encrypt
        encrypt_file(sample_file, encrypted_file, key)
        
        # b. Decrypt
        decrypt_file(encrypted_file, decrypted_file, key)
        
        # Verify contents match by comparing hashes
        new_hash = calculate_sha256(decrypted_file)
        print(f"[*] Decrypted SHA-256: {new_hash}")
        
        if orig_hash == new_hash:
            print("[+] Integrity Verification: Success! Files match perfectly.")
        else:
            print("[-] Integrity Verification: Failed! File contents do not match.")
            
    except FileNotFoundError:
        print("[-] Error: The targeted file could not be found. Please check your path.")
    except Exception as e:
        print(f"[-] A security system error occurred: {e}")

if __name__ == "__main__":
    main()

