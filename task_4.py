class Comment:
    """
    A class representing a comment in a hierarchical comment system.
    Comments can have replies, which can also have replies, forming a tree structure.
    """
    
    def __init__(self, text, author):
        """
        Initialize a new comment.
        
        Args:
            text (str): The text content of the comment
            author (str): The author of the comment
        """
        self.text = text
        self.author = author
        self.replies = []
        self.is_deleted = False
    
    def add_reply(self, reply):
        """
        Add a reply to this comment.
        
        Args:
            reply (Comment): The reply comment to add
        """
        self.replies.append(reply)
    
    def remove_reply(self):
        """
        Remove this comment by marking it as deleted.
        Changes the text to a standard deletion message and sets is_deleted flag.
        """
        self.text = "This comment has been deleted."
        self.is_deleted = True
    
    def display(self, indent=0):
        """
        Display the comment and all its replies recursively with proper indentation.
        
        Args:
            indent (int): The current indentation level (number of spaces)
        """
        # Create indentation string
        indent_str = "    " * indent
        
        # Display current comment
        print(f"{indent_str}{self.author}: {self.text}")
        
        # Recursively display all replies with increased indentation
        for reply in self.replies:
            reply.display(indent + 1)


# Example usage as specified in the requirements
if __name__ == "__main__":
    root_comment = Comment("This is a great book!", "Bodya")
    reply1 = Comment("The book is a complete disappointment :(", "Andriy")
    reply2 = Comment("What is wonderful about it?", "Marina")

    root_comment.add_reply(reply1)
    root_comment.add_reply(reply2)

    reply1_1 = Comment("It's not a book, it's a pile of paper translated for nothing...", "Sergiy")
    reply1.add_reply(reply1_1)

    reply1.remove_reply()

    root_comment.display()
