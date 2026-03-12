import tkinter as tk
from tkinter import messagebox

# ---------------------------------------------------------
# Node class for the circular linked list
# ---------------------------------------------------------
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# ---------------------------------------------------------
# Circular Linked List for Josephus game logic
# ---------------------------------------------------------
class CircularLinkedList:
    def __init__(self, n):
        self.head = None
        self.size = 0
        self.create_list(n)

    # Create circular linked list 0..n-1
    def create_list(self, n):
        if n <= 0:
            return

        first = Node(0)
        self.head = first
        current = first

        # Build list
        for i in range(1, n):
            new_node = Node(i)
            current.next = new_node
            current = new_node

        # Close loop
        current.next = first
        self.size = n

    # Eliminate every k-th node
    def eliminate(self, k):
        if self.size == 0:
            return None

        # If only 1 left, return it
        if self.size == 1:
            winner = self.head.value
            self.size -= 1
            self.head = None
            return winner

        # Move (k-1) steps
        prev = self.head
        for _ in range(k - 2):
            prev = prev.next

        eliminated = prev.next
        prev.next = eliminated.next

        # Move head forward
        self.head = eliminated.next

        self.size -= 1
        return eliminated.value


# ---------------------------------------------------------
# Main GUI Class
# ---------------------------------------------------------
class CountingGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Counting-Out Game")

        # Game variables
        self.N = None
        self.K = None
        self.players = {}  # stores label widgets keyed by player number
        self.clist = None  # circular linked list

        # ----------------------------
        # Input fields for N and K
        # ----------------------------
        tk.Label(root, text="Enter N (2-11):").grid(row=0, column=0)
        self.entry_N = tk.Entry(root, width=5)
        self.entry_N.grid(row=0, column=1)

        tk.Label(root, text="Enter K (>=1):").grid(row=1, column=0)
        self.entry_K = tk.Entry(root, width=5)
        self.entry_K.grid(row=1, column=1)

        # Start button
        self.start_button = tk.Button(root, text="Start", command=self.start_game)
        self.start_button.grid(row=2, column=0, columnspan=2, pady=5)

        # Text widget for messages
        self.text_widget = tk.Text(root, width=40, height=10)
        self.text_widget.grid(row=3, column=0, columnspan=2, pady=10)

        # Frame to hold player icons
        self.players_frame = tk.Frame(root)
        self.players_frame.grid(row=4, column=0, columnspan=2)

        self.eliminate_button = None

    # -----------------------------------------------------
    # Validate input, create players, show Eliminate button
    # -----------------------------------------------------
    def start_game(self):
        try:
            self.N = int(4)
            self.K = int(6)

        except ValueError:
            messagebox.showinfo("Invalid", "Please enter valid integer values.")
            return

        # Validate N & K
        if not (1 < self.N < 12):
            messagebox.showinfo("Invalid", "N must be between 2 and 11.")
            return
        if self.K < 1:
            messagebox.showinfo("Invalid", "K must be >= 1.")
            return

        # Clear previous messages/UI
        self.text_widget.delete("1.0", tk.END)
        for widget in self.players_frame.winfo_children():
            widget.destroy()

        # Create circular linked list
        self.clist = CircularLinkedList(self.N)

        # Create player icons
        self.players = {}
        for i in range(self.N):
            lbl = tk.Label(self.players_frame, text=f"Player {i}", borderwidth=2, relief="groove", width=10)
            lbl.grid(row=0, column=i, padx=5)
            self.players[i] = lbl

        # Create eliminate button
        if self.eliminate_button:
            self.eliminate_button.destroy()

        self.eliminate_button = tk.Button(self.root, text="Eliminate", command=self.eliminate_round)
        self.eliminate_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.text_widget.insert(tk.END, f"Game started. N={self.N} K={self.K}\n")

    # -----------------------------------------------------
    # Handle one elimination round
    # -----------------------------------------------------
    def eliminate_round(self):
        if not self.clist or self.clist.size == 0:
            return

        # If 2 players left → final elimination
        if self.clist.size == 2:
            loser = self.clist.eliminate(self.K)

            # Determine winner
            remaining = self.clist.head.value
            messagebox.showinfo("Winner!", f"Winner is Player {remaining}")

            # Clear screen
            self.text_widget.delete("1.0", tk.END)
            for widget in self.players_frame.winfo_children():
                widget.destroy()
            self.eliminate_button.destroy()
            return

        # Regular elimination
        eliminated = self.clist.eliminate(self.K)

        # Remove icon
        if eliminated in self.players:
            self.players[eliminated].destroy()
            del self.players[eliminated]

        # Write update
        self.text_widget.insert(tk.END, f"Player {eliminated} eliminated.\n")
        self.text_widget.see(tk.END)


# ---------------------------------------------------------
# Run GUI
# ---------------------------------------------------------
root = tk.Tk()
app = CountingGameGUI(root)
root.mainloop()
