import tkinter as tk
from tkinter import ttk,messagebox
import pandas as pd

# List of anime data
animes = [['Jobless Reincarnation', 'Adventure', 'medium', 'series' ],
          ['Eminence in Shadow', 'Comedy', 'medium', 'series'],
          ['Heavenly Delusion', 'Mystery', 'short', 'series']]

# Convert the list to a Pandas DataFrame
anime_df = pd.DataFrame(animes, columns=['Anime Name', 'Genre', 'Length', 'Type'])

# List to store the history of selected genres
genre_history = []

# Function to display anime based on selected genre
def display_anime():
    selected_genre = genre_combobox.get()
    
    valid_genres = ['Adventure', 'Comedy', 'Mystery']
    
    if selected_genre in valid_genres:
        # Append the selected genre to the history list
        genre_history.append(selected_genre)
        
        # Filter the DataFrame based on the selected genre
        filtered_anime = anime_df[anime_df['Genre'] == selected_genre]

        # Display the filtered anime DataFrame in a messagebox
        messagebox.showinfo(f"Anime in the {selected_genre} genre", filtered_anime.to_string(index=False))
    else:
        messagebox.showerror("Error", "Please select a valid genre.")

# Function to update genre history display
def update_history():
    history_text.delete(1.0, tk.END)
    history_text.insert(tk.END, "\n".join(genre_history)) 


# Create the main application window
app = tk.Tk()
app.title("Anime Selector")

# Label and Combobox for genre selection
genre_label = tk.Label(app, text="Select Genre:")
genre_label.pack(pady=10)

genres = ['Adventure', 'Comedy', 'Mystery']
genre_combobox = ttk.Combobox(app, values=genres)
genre_combobox.pack(pady=10)

# Button to trigger anime display
display_button = tk.Button(app, text="Display Anime", command=display_anime)
display_button.pack(pady=20)

# Label to display genre history
history_label = tk.Label(app, text="Genre History:")
history_label.pack(pady=10)

# Text widget to display genre history
history_text = tk.Text(app, height=5, width=30)
history_text.pack(pady=10)

# Button to update genre history display
update_history_button = tk.Button(app, text="Update History", command=update_history)
update_history_button.pack(pady=10)

# Start the GUI event loop
app.mainloop()
