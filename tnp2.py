def longest_palindrome(s: str) -> str:
    """
    Finds the longest palindromic substring in a given string s using the
    "Expand Around Center" technique, without using helper functions.

    Time Complexity: O(n^2), where n is the length of the string.
    Space Complexity: O(1) (excluding the space for the returned string).

    Args:
        s: The input string.

    Returns:
        The longest palindromic substring found in s.
    """
    n = len(s)
    if n < 2:
        return s  # A string of 0 or 1 character is a palindrome

    # Variables to track the start index and length of the overall longest palindrome
    longest_start = 0
    longest_length = 1

    # Iterate through all possible center points (i)
    for i in range(n):
        
        # --- 1. Odd-length palindromes (Center at index i) ---
        left, right = i, i
        
        # Expand outward as long as characters match and indices are valid
        while left >= 0 and right < n and s[left] == s[right]:
            current_length = right - left + 1
            
            # Check if this is the new longest palindrome
            if current_length > longest_length:
                longest_length = current_length
                longest_start = left
            
            # Move boundaries outward
            left -= 1
            right += 1

        # --- 2. Even-length palindromes (Center between index i and i+1) ---
        left, right = i, i + 1
        
        # Expand outward as long as characters match and indices are valid
        while left >= 0 and right < n and s[left] == s[right]:
            current_length = right - left + 1
            
            # Check if this is the new longest palindrome
            if current_length > longest_length:
                longest_length = current_length
                longest_start = left
            
            # Move boundaries outward
            left -= 1
            right += 1

    # Return the substring based on the stored start index and length
    return s[longest_start : longest_start + longest_length]

# --- Example Usage ---
if __name__ == "__main__":
    test_strings = [
        "babad",
        "cbbd",
        "racecarx",
        "forgeeksskeegfor",
        "a",
        "",
        "abacaba",
        "banana", # Another test case
    ]

    print("--- Longest Palindrome Finder (No Functions) ---")

    for s in test_strings:
        result = longest_palindrome(s)
        print(f"Input: '{s}'")
        print(f"Longest Palindrome: '{result}' (Length: {len(result)})")
        print("-" * 20)
