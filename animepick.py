import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import requests

# List of anime data
animes = [['Jobless Reincarnation', 'Adventure', 'Medium', 'Series'],
          ['Eminence in Shadow', 'Comedy', 'Medium', 'Series'],
          ['Heavenly Delusion', 'Mystery', 'Short', 'Series'],
          ['Jujutsu Kaisen', 'Action', 'Medium', 'Series'],
          ['Akame ga Kill!', 'Action', 'Short', 'Series'],
          ['Havent You Heard? Im Sakamoto', 'Comedy', 'Short', 'Series']]

# Convert the list to a Pandas DataFrame
anime_df = pd.DataFrame(animes, columns=['Anime Name', 'Genre', 'Length', 'Type'])

# List to store the history of selected genres
genre_history = []

# Function to display anime based on selected criteria
def display_anime():
    selected_genre = genre_combobox.get()
    selected_length = length_combobox.get()
    selected_type = type_combobox.get()
    
    valid_genres = ['Action', 'Adventure', 'Comedy', 'Mystery']
    valid_lengths = ['Short', 'Medium', 'Long']
    valid_types = ['Series', 'Movie']
    
    if selected_genre in valid_genres and selected_length in valid_lengths and selected_type in valid_types:
        # Append the selected criteria to the history list
        genre_history.append(f"Genre: {selected_genre}, Length: {selected_length}, Type: {selected_type}")
        
        # Filter the DataFrame based on the selected criteria
        filtered_anime = anime_df[(anime_df['Genre'] == selected_genre) &
                                  (anime_df['Length'] == selected_length) &
                                  (anime_df['Type'] == selected_type)]
        
        if not filtered_anime.empty:
            display_search_results(filtered_anime)
        else:
            messagebox.showinfo("No Results", "No anime found with the selected criteria.")
    else:
        messagebox.showerror("Error", "Please select valid criteria.")

# Function to update genre history display
def update_history():
    history_text.delete(1.0, tk.END)
    history_text.insert(tk.END, "\n".join(genre_history))

# Function to search for anime details using Jikan API
def search_anime(anime_name):
    url = f"https://api.jikan.moe/v4/anime?q={anime_name}&limit=1"
    response = requests.get(url)
    if response.status_code == 200:
        anime_list = response.json().get('data', [])
        if anime_list:
            return anime_list[0]
    return None

# Function to display search results
def display_search_results(filtered_anime):
    results_text.delete(1.0, tk.END)
    for _, row in filtered_anime.iterrows():
        anime_name = row['Anime Name']
        anime_details = search_anime(anime_name)
        if anime_details:
            title = anime_details.get('title', 'N/A')
            synopsis = anime_details.get('synopsis', 'No synopsis available')
            results_text.insert(tk.END, f"Title: {title}\nSynopsis: {synopsis}\n\n")

# Create the main application window
app = tk.Tk()
app.title("Anime Selector")

# Label and Combobox for genre selection
genre_label = tk.Label(app, text="Select Genre:")
genre_label.pack(pady=10)

genres = ['Action', 'Adventure', 'Comedy', 'Mystery']
genre_combobox = ttk.Combobox(app, values=genres)
genre_combobox.pack(pady=10)

# Label and Combobox for length selection
length_label = tk.Label(app, text="Select Length:")
length_label.pack(pady=10)

lengths = ['Short', 'Medium', 'Long']
length_combobox = ttk.Combobox(app, values=lengths)
length_combobox.pack(pady=10)

# Label and Combobox for type selection
type_label = tk.Label(app, text="Select Type:")
type_label.pack(pady=10)

types = ['Series', 'Movie']
type_combobox = ttk.Combobox(app, values=types)
type_combobox.pack(pady=10)

# Button to trigger anime display
display_button = tk.Button(app, text="Display Anime", command=display_anime)
display_button.pack(pady=20)

# Label to display genre history
history_label = tk.Label(app, text="Selection History:")
history_label.pack(pady=10)

# Text widget to display genre history
history_text = tk.Text(app, height=5, width=50)
history_text.pack(pady=10)

# Button to update genre history display
update_history_button = tk.Button(app, text="Update History", command=update_history)
update_history_button.pack(pady=10)

# Label for search results
results_label = tk.Label(app, text="Search Results:")
results_label.pack(pady=10)

# Text widget to display search results
results_text = tk.Text(app, height=20, width=70)
results_text.pack(pady=10)

# Start the GUI event loop
app.mainloop()

