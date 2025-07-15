stages = [  # From 0 lives (full hangman) to 6 lives (empty gallows)
    # 0 lives left
    """
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |     / \\
       -
    """,
    # 1 life left
    """
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |     / 
       -
    """,
    # 2 lives left
    """
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |      
       -
    """,
    # 3 lives left
    """
       --------
       |      |
       |      O
       |     \\|
       |      |
       |     
       -
    """,
    # 4 lives left
    """
       --------
       |      |
       |      O
       |      |
       |      |
       |     
       -
    """,
    # 5 lives left
    """
       --------
       |      |
       |      O
       |    
       |      
       |     
       -
    """,
    # 6 lives left (start of game)
    """
       --------
       |      |
       |      
       |    
       |      
       |     
       -
    """
]
