import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk
import tkinter.font as tkFont
import os
import time

# Initialize an empty list for selected files
FILES = []

# Search algorithms implementations
def brute_force_search(text, pattern, case_sensitive=False, whole_word=False):
    # Find this line in your code (around line 148):
    title_label = ttk.Label(header_frame, text="Word Search Application", font=('Segoe UI', 16, 'bold'))
    
    results = []
    n, m = len(text), len(pattern)
    
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        
        if match:
            # Check if it's a whole word match if required
            if whole_word:
                prev_char = ' ' if i == 0 else text[i - 1]
                next_char = ' ' if i + m >= n else text[i + m]
                if prev_char.isalnum() or next_char.isalnum():
                    continue
            results.append(i)
            
    return results

def compute_lps(pattern):
    m = len(pattern)
    lps = [0] * m
    
    length = 0
    i = 1
    
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
                
    return lps

def kmp_search(text, pattern, case_sensitive=False, whole_word=False):
    if not case_sensitive:
        text = text.lower()
        pattern = pattern.lower()
    
    results = []
    n, m = len(text), len(pattern)
    
    if m == 0:
        return results
    
    lps = compute_lps(pattern)
    
    i = 0  # index for text
    j = 0  # index for pattern
    
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        
        if j == m:
            # Check if it's a whole word match if required
            if whole_word:
                prev_char = ' ' if i - j == 0 else text[i - j - 1]
                next_char = ' ' if i >= n else text[i]
                if not (prev_char.isalnum() or next_char.isalnum()):
                    results.append(i - j)
            else:
                results.append(i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
                
    return results

# GUI Setup with improved styling
root = tk.Tk()
root.title("Made by Saim Nadeem")
root.geometry("800x700")
root.configure(bg="#2b2b2b")

# Custom styles
style = ttk.Style()
style.theme_use('clam')  # Use 'clam' theme as base
style.configure("TFrame", background="#2b2b2b")
style.configure("TButton", 
                background="#3a7ebf", 
                foreground="white", 
                font=('Segoe UI', 10, 'bold'),
                padding=8,
                borderwidth=1,
                relief="flat")
style.map("TButton",
          background=[('active', '#5a9edf')],
          relief=[('pressed', 'sunken')])
style.configure("TCheckbutton", 
                background="#2b2b2b", 
                foreground="white",
                font=('Segoe UI', 10))
style.map("TCheckbutton",
          background=[('active', '#2b2b2b')])
style.configure("TLabel", 
                background="#2b2b2b", 
                foreground="white",
                font=('Segoe UI', 11))

# Main container frame
main_frame = ttk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# Header and search section
header_frame = ttk.Frame(main_frame)
header_frame.pack(fill=tk.X, pady=(0, 15))

title_label = ttk.Label(header_frame, text="Word Search Application", font=('Segoe UI', 16, 'bold'))
title_label.pack()

search_frame = ttk.Frame(main_frame)
search_frame.pack(fill=tk.X, pady=5)

# Search term entry with label
search_label = ttk.Label(search_frame, text="Enter Search Term:")
search_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

search_term_entry = tk.Entry(search_frame, width=40, bg="#333333", fg="white", 
                           insertbackground="white", font=('Segoe UI', 11))
search_term_entry.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

# Options frame
options_frame = ttk.Frame(main_frame)
options_frame.pack(fill=tk.X, pady=5)

# Checkboxes for options
whole_word_var = tk.BooleanVar()
whole_word_checkbox = ttk.Checkbutton(options_frame, text="Whole Word Match", variable=whole_word_var)
whole_word_checkbox.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

case_sensitive_var = tk.BooleanVar()
case_sensitive_checkbox = ttk.Checkbutton(options_frame, text="Case Sensitive", variable=case_sensitive_var)
case_sensitive_checkbox.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

# Algorithm selection
algorithm_var = tk.StringVar(value="kmp")
algorithm_label = ttk.Label(options_frame, text="Search Algorithm:")
algorithm_label.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)

kmp_radio = ttk.Radiobutton(options_frame, text="KMP", variable=algorithm_var, value="kmp")
kmp_radio.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

brute_radio = ttk.Radiobutton(options_frame, text="Brute Force", variable=algorithm_var, value="brute")
brute_radio.grid(row=1, column=2, sticky=tk.W, padx=5, pady=5)

# Buttons frame
buttons_frame = ttk.Frame(main_frame)
buttons_frame.pack(fill=tk.X, pady=10)

# Function to select files
def select_files():
    global FILES
    FILES = filedialog.askopenfilenames(title="Select Files to Search", filetypes=[("Text Files", "*.txt")])
    if FILES:
        file_label.config(text=f"{len(FILES)} files selected")
    else:
        file_label.config(text="No files selected")

select_files_button = ttk.Button(buttons_frame, text="Select Files", command=select_files)
select_files_button.grid(row=0, column=0, padx=5, pady=5)

file_label = ttk.Label(buttons_frame, text="No files selected")
file_label.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

search_button = ttk.Button(buttons_frame, text="Search", command=lambda: search())
search_button.grid(row=0, column=2, padx=5, pady=5)

# Results section
results_label = ttk.Label(main_frame, text="Search Results:")
results_label.pack(anchor=tk.W, pady=(10, 5))

# Result display area with custom styling
result_area = scrolledtext.ScrolledText(main_frame, width=80, height=20, bg="#1e1e1e", 
                                      fg="#e0e0e0", insertbackground="white", font=('Consolas', 11))
result_area.pack(fill=tk.BOTH, expand=True, pady=5)

# Status bar
status_frame = ttk.Frame(main_frame)
status_frame.pack(fill=tk.X, pady=(10, 0))

status_label = ttk.Label(status_frame, text="Ready")
status_label.pack(side=tk.LEFT)

# Search Function
def search():
    search_term = search_term_entry.get().strip()
    
    if not search_term:
        messagebox.showwarning("Empty Search", "Please enter a search term")
        return
    
    if not FILES:
        messagebox.showwarning("No Files", "Please select files to search")
        return
    
    result_area.delete(1.0, tk.END)
    status_label.config(text="Searching...")
    root.update()
    
    case_sensitive = case_sensitive_var.get()
    whole_word = whole_word_var.get()
    algorithm = algorithm_var.get()
    
    start_time = time.time()
    total_occurrences = 0
    
    result_area.insert(tk.END, f"Searching for '{search_term}' in {len(FILES)} files\n")
    result_area.insert(tk.END, f"Options: Case Sensitive: {case_sensitive}, Whole Word: {whole_word}, Algorithm: {algorithm.upper()}\n\n")
    
    for file_path in FILES:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                
            file_name = os.path.basename(file_path)
            
            # Choose search algorithm based on user selection
            if algorithm == "kmp":
                occurrences = kmp_search(content, search_term, case_sensitive, whole_word)
            else:  # brute force
                occurrences = brute_force_search(content, search_term, case_sensitive, whole_word)
            
            if occurrences:
                result_area.insert(tk.END, f"File: {file_name}\n")
                result_area.insert(tk.END, f"Found {len(occurrences)} occurrences\n")
                
                # Display context for each occurrence (show a few characters before and after)
                context_size = 20
                for pos in occurrences[:20]:  # Limit to first 20 occurrences to avoid very large output
                    start = max(0, pos - context_size)
                    end = min(len(content), pos + len(search_term) + context_size)
                    
                    # Format the context with the match highlighted
                    pre_match = content[start:pos]
                    match = content[pos:pos+len(search_term)]
                    post_match = content[pos+len(search_term):end]
                    
                    result_area.insert(tk.END, f"[Pos {pos}]: ...{pre_match}")
                    result_area.insert(tk.END, match, "highlight")
                    result_area.insert(tk.END, f"{post_match}...\n")
                
                if len(occurrences) > 20:
                    result_area.insert(tk.END, f"(Only showing first 20 occurrences)\n")
                
                result_area.insert(tk.END, "\n")
                total_occurrences += len(occurrences)
        
        except Exception as e:
            result_area.insert(tk.END, f"Error processing {file_path}: {str(e)}\n\n")
    
    end_time = time.time()
    search_time = end_time - start_time
    
    result_area.insert(tk.END, f"\nSearch completed in {search_time:.4f} seconds.\n")
    result_area.insert(tk.END, f"Total occurrences found: {total_occurrences}\n")
    
    # Configure tag for highlighting matched text
    result_area.tag_config("highlight", background="#5a9edf", foreground="black")
    
    status_label.config(text=f"Search completed. Found {total_occurrences} occurrences.")

root.mainloop()
