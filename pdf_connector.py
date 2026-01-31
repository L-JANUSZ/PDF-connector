from PyPDF2 import PdfMerger
import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from typing import List


def merge_pdfs(pdfs_path:list, output_path: str) -> None:
    """
    Scala listę plików PDF w jeden plik.
    
    Args:
        pdfs_path (list): Lista ścieżek do plików PDF
        output_path (str): Ścieżka do wyjściowego pliku PDF
    """
    try:
        # Utworzenie obiektu PdfMerger
        merger = PdfMerger()
        
        # Dodanie plików PDF z listy
        for pdf_path in pdfs_path:
            if not os.path.exists(pdf_path):
                raise FileNotFoundError(f"Plik nie istnieje: {pdf_path}")
            merger.append(pdf_path)
        
        # Zapisanie połączonego pliku
        merger.write(output_path)
        merger.close()
        
        print(f"Sukces! Pliki zostały scalone do: {output_path}")
        
    except Exception as e:
        print(f"Błąd: {e}")


class PDFConnectorGUI:
    """
    Graficzny interfejs użytkownika do łączenia plików PDF.
    """
    
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Connector - Łączenie plików PDF")
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        
        # Lista przechowująca ścieżki do wybranych plików PDF
        self.pdf_files: List[str] = []
        
        # Konfiguracja stylu
        style = ttk.Style()
        style.theme_use('clam')
        
        self.create_widgets()
    
    def create_widgets(self):
        """Tworzy wszystkie widgety w oknie."""
        
        # Główny frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Konfiguracja siatki
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(2, weight=1)
        
        # Tytuł
        title_label = ttk.Label(
            main_frame,
            text="PDF Connector",
            font=('Arial', 16, 'bold')
        )
        title_label.grid(row=0, column=0, pady=10)
        
        # Sekcja wyboru plików
        files_frame = ttk.LabelFrame(main_frame, text="Wybierz pliki PDF", padding="10")
        files_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=5)
        files_frame.columnconfigure(0, weight=1)
        
        # Przycisk dodawania plików
        add_button = ttk.Button(
            files_frame,
            text="➕ Dodaj pliki PDF",
            command=self.add_pdf_files
        )
        add_button.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=5, pady=5)
        
        # Przycisk czyszczenia listy
        clear_button = ttk.Button(
            files_frame,
            text="🗑️ Wyczyść listę",
            command=self.clear_files
        )
        clear_button.grid(row=0, column=1, padx=5, pady=5)
        
        # Lista plików z przewijaniem
        list_frame = ttk.Frame(main_frame)
        list_frame.grid(row=2, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        list_frame.columnconfigure(0, weight=1)
        list_frame.rowconfigure(0, weight=1)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(list_frame)
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        # Listbox
        self.files_listbox = tk.Listbox(
            list_frame,
            yscrollcommand=scrollbar.set,
            height=10,
            font=('Arial', 9)
        )
        self.files_listbox.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.config(command=self.files_listbox.yview)
        
        # Przyciski do zarządzania kolejnością
        order_frame = ttk.Frame(main_frame)
        order_frame.grid(row=3, column=0, pady=5)
        
        move_up_button = ttk.Button(
            order_frame,
            text="⬆️ Przesuń w górę",
            command=self.move_up
        )
        move_up_button.grid(row=0, column=0, padx=5)
        
        move_down_button = ttk.Button(
            order_frame,
            text="⬇️ Przesuń w dół",
            command=self.move_down
        )
        move_down_button.grid(row=0, column=1, padx=5)
        
        remove_button = ttk.Button(
            order_frame,
            text="❌ Usuń zaznaczony",
            command=self.remove_selected
        )
        remove_button.grid(row=0, column=2, padx=5)
        
        # Sekcja nazwy pliku wyjściowego
        output_frame = ttk.LabelFrame(main_frame, text="Nazwa pliku wynikowego", padding="10")
        output_frame.grid(row=4, column=0, sticky=(tk.W, tk.E), pady=10)
        output_frame.columnconfigure(1, weight=1)
        
        ttk.Label(output_frame, text="Nazwa:").grid(row=0, column=0, padx=5)
        
        self.output_name_var = tk.StringVar(value="output.pdf")
        output_entry = ttk.Entry(
            output_frame,
            textvariable=self.output_name_var,
            font=('Arial', 10)
        )
        output_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=5)
        
        browse_button = ttk.Button(
            output_frame,
            text="📁 Wybierz lokalizację",
            command=self.choose_output_location
        )
        browse_button.grid(row=0, column=2, padx=5)
        
        # Przycisk łączenia
        merge_button = ttk.Button(
            main_frame,
            text="🔗 Połącz pliki PDF",
            command=self.merge_pdfs_gui,
            style='Accent.TButton'
        )
        merge_button.grid(row=5, column=0, pady=10, ipady=10)
        
        # Status bar
        self.status_var = tk.StringVar(value="Gotowy")
        status_label = ttk.Label(
            main_frame,
            textvariable=self.status_var,
            relief=tk.SUNKEN,
            anchor=tk.W
        )
        status_label.grid(row=6, column=0, sticky=(tk.W, tk.E))
    
    def add_pdf_files(self):
        """Otwiera okno dialogowe do wyboru plików PDF."""
        files = filedialog.askopenfilenames(
            title="Wybierz pliki PDF",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
        )
        
        if files:
            for file in files:
                if file not in self.pdf_files:
                    self.pdf_files.append(file)
                    self.files_listbox.insert(tk.END, os.path.basename(file))
            
            self.update_status(f"Dodano {len(files)} plików. Łącznie: {len(self.pdf_files)}")
    
    def clear_files(self):
        """Czyści listę wybranych plików."""
        self.pdf_files.clear()
        self.files_listbox.delete(0, tk.END)
        self.update_status("Lista plików została wyczyszczona")
    
    def remove_selected(self):
        """Usuwa zaznaczony plik z listy."""
        selection = self.files_listbox.curselection()
        if selection:
            index = selection[0]
            self.files_listbox.delete(index)
            self.pdf_files.pop(index)
            self.update_status("Usunięto zaznaczony plik")
    
    def move_up(self):
        """Przesuwa zaznaczony plik w górę listy."""
        selection = self.files_listbox.curselection()
        if selection and selection[0] > 0:
            index = selection[0]
            # Zamiana w liście plików
            self.pdf_files[index], self.pdf_files[index-1] = \
                self.pdf_files[index-1], self.pdf_files[index]
            # Zamiana w listbox
            item = self.files_listbox.get(index)
            self.files_listbox.delete(index)
            self.files_listbox.insert(index-1, item)
            self.files_listbox.selection_set(index-1)
    
    def move_down(self):
        """Przesuwa zaznaczony plik w dół listy."""
        selection = self.files_listbox.curselection()
        if selection and selection[0] < len(self.pdf_files) - 1:
            index = selection[0]
            # Zamiana w liście plików
            self.pdf_files[index], self.pdf_files[index+1] = \
                self.pdf_files[index+1], self.pdf_files[index]
            # Zamiana w listbox
            item = self.files_listbox.get(index)
            self.files_listbox.delete(index)
            self.files_listbox.insert(index+1, item)
            self.files_listbox.selection_set(index+1)
    
    def choose_output_location(self):
        """Otwiera okno dialogowe do wyboru lokalizacji i nazwy pliku wynikowego."""
        file_path = filedialog.asksaveasfilename(
            title="Wybierz lokalizację i nazwę pliku wynikowego",
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")],
            initialfile=self.output_name_var.get()
        )
        
        if file_path:
            self.output_name_var.set(file_path)
    
    def merge_pdfs_gui(self):
        """Łączy wybrane pliki PDF."""
        if not self.pdf_files:
            messagebox.showwarning(
                "Brak plików",
                "Proszę dodać przynajmniej jeden plik PDF!"
            )
            return
        
        output_path = self.output_name_var.get()
        if not output_path:
            messagebox.showwarning(
                "Brak nazwy",
                "Proszę podać nazwę pliku wynikowego!"
            )
            return
        
        # Dodanie rozszerzenia .pdf jeśli nie istnieje
        if not output_path.lower().endswith('.pdf'):
            output_path += '.pdf'
            self.output_name_var.set(output_path)
        
        try:
            self.update_status("Łączenie plików...")
            merge_pdfs(self.pdf_files, output_path)
            
            messagebox.showinfo(
                "Sukces",
                f"Pliki zostały połączone!\nZapisano jako: {output_path}"
            )
            self.update_status(f"Sukces! Utworzono: {os.path.basename(output_path)}")
            
        except Exception as e:
            messagebox.showerror(
                "Błąd",
                f"Wystąpił błąd podczas łączenia plików:\n{str(e)}"
            )
            self.update_status(f"Błąd: {str(e)}")
    
    def update_status(self, message: str):
        """Aktualizuje pasek statusu."""
        self.status_var.set(message)
        self.root.update_idletasks()


def run_gui():
    """Uruchamia aplikację z interfejsem graficznym."""
    root = tk.Tk()
    app = PDFConnectorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    run_gui()

