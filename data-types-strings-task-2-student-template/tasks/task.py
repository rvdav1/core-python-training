def get_longest_word( s: str) -> str:
    """
     Add your code here 
    """
    words = s.split()
    longest_word = max(words, key=len)
    return longest_word