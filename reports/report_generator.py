def generate(original, modified, detected):
    print("\n--- EVASION TEST REPORT ---")
    print(f"Original Payload: {original}")
    print(f"Modified Payload: {modified}")
    print(f"Detected: {'YES' if detected else 'NO'}")
