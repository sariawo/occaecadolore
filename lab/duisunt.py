try:
    locale_str = locale_bytes.decode("utf-8").strip("\x00")
except UnicodeDecodeError as e:
    print(f"Decoding error: {e}")
    locale_str = None  # or handle the error appropriately
