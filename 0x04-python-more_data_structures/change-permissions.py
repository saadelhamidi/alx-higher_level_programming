import os

def change_permissions(file_path, permissions):
    try:
        os.chmod(file_path, permissions)
        print(f"Permissions changed for file: {file_path}")
    except OSError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Specify the file path and permissions
    file_path = "C:\Users\saadoun\Desktop\0x04-python-more-data-structures"
    permissions = 0o755  # Numeric mode for rwxr-xr-x

    # Call the function to change permissions
    change_permissions(file_path, permissions)
