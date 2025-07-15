import hashlib
import os
def get_file_hash(filepath):
    """Generate SHA-256 hash of a file"""
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return None
def check_file_integrity(original_hash, filepath):
    """Check if file integrity is maintained"""
    current_hash = get_file_hash(filepath)
    if current_hash is None:
        return "File not found!"
    elif current_hash == original_hash:
        return "✅ File integrity verified. No changes detected."
    else:
        return "⚠️ File has been modified!"
if __name__ == "__main__":
    file_path = input("Enter the file path: ")
    original_hash = get_file_hash(file_path)
    print("Original SHA-256 Hash:", original_hash)
    input("Make changes to the file if you want, then press Enter to check integrity...")
    result = check_file_integrity(original_hash, file_path)
    print(result)