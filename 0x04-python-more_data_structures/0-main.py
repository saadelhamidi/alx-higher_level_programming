import os

def chmod(file_path, mode):
    """
    Change the permissions of a file or directory.

    Args:
        file_path (str): Path to the file or directory.
        mode (str or int): Permissions to set. Can be specified in numeric or symbolic mode.
            Numeric mode: An octal number representing the permissions.
            Symbolic mode: A string representing the permissions in symbolic mode.
                Example: "u+rwx,g+rx,o+rx" for rwxr-xr-x.

    Returns:
        None
    """
    try:
        # Convert symbolic mode to numeric mode if necessary
        if isinstance(mode, str):
            mode = sum([getattr(os, f"S_I{perm.upper()}") for perm in mode.split('+')])

        # Change file permissions
        os.chmod(file_path, mode)
        print(f"Permissions changed for {file_path}")
    except OSError as e:
        print(f"Error: {e}")

# Example usage:
# Change permissions of example.txt to rwxr-xr-x (755)
chmod("example.txt", 0o755)
# Or using symbolic mode
chmod("example.txt", "u+rwx,g+rx,o+rx")
