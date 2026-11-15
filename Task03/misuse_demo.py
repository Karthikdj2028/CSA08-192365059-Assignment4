"""Show why except Exception: pass can hide a programming error."""
print("Specific handling reports unexpected errors.")
try:
    total = 10
    print(totla)  # Deliberate spelling mistake
except NameError as error:
    print("Name error found:", error)

print("\nBare except hides the same error.")
try:
    total = 10
    print(totla)  # Same deliberate spelling mistake
except Exception:
    pass
print("Program continued, but the mistake was hidden.")
