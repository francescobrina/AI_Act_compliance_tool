import tkinter as tk
from tkinter import messagebox, filedialog
from data import DataManager
from utils import generate_pdf_report

class RiskAssessmentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Valutazione del Rischio - AI ACT Compliance")
        self.root.geometry("600x600")

        self.data_manager = DataManager()

        self.current_question = 0
        self.answers = []
        self.user_info = {}

        self.create_main_menu()

    def create_main_menu(self):
        self.clear_screen()

        menubar = tk.Menu(self.root)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Nuova Valutazione", command=self.new_assessment)
        file_menu.add_command(label="Apri Valutazione", command=self.load_assessment)
        file_menu.add_command(label="Salva Valutazione", command=self.save_assessment)
        file_menu.add_separator()
        file_menu.add_command(label="Esporta Report PDF", command=self.export_pdf)
        file_menu.add_separator()
        file_menu.add_command(label="Esci", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="Risorse Aggiuntive", command=self.show_resources)
        menubar.add_cascade(label="Aiuto", menu=help_menu)

        self.root.config(menu=menubar)

        self.info_frame = tk.Frame(self.root)
        tk.Label(self.info_frame, text="Nome del Progetto:").grid(row=0, column=0, sticky='e')
        self.project_name_entry = tk.Entry(self.info_frame, width=40)
        self.project_name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.info_frame, text="Descrizione del Progetto:").grid(row=1, column=0, sticky='ne')
        self.project_desc_text = tk.Text(self.info_frame, width=40, height=4)
        self.project_desc_text.grid(row=1, column=1, padx=5, pady=5)

        self.info_frame.pack(pady=10)

        # Area delle domande
        self.question_frame = tk.Frame(self.root)
        self.question_label = tk.Label(self.question_frame, text="", wraplength=500, justify='left', font=("Arial", 12))
        self.question_label.pack(pady=10)

        self.button_frame = tk.Frame(self.question_frame)
        self.button_frame.pack()

        self.yes_button = tk.Button(self.button_frame, text="Sì", width=15, command=lambda: self.next_question(True))
        self.yes_button.pack(side="left", padx=10)

        self.no_button = tk.Button(self.button_frame, text="No", width=15, command=lambda: self.next_question(False))
        self.no_button.pack(side="left", padx=10)

        self.back_button = tk.Button(self.question_frame, text="Indietro", width=10, command=self.previous_question)
        self.back_button.pack(pady=10)

        self.question_frame.pack()

        self.update_question()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def update_question(self):
        if self.current_question < len(self.data_manager.questions):
            q_text = self.data_manager.questions[self.current_question]['question']
            self.question_label.config(text=f"Domanda {self.current_question + 1}/{len(self.data_manager.questions)}: {q_text}")
        else:
            self.show_result()

    def next_question(self, answer):
        if self.current_question == 0:
            # Salva le informazioni sul progetto
            self.user_info['project_name'] = self.project_name_entry.get()
            self.user_info['project_description'] = self.project_desc_text.get("1.0", tk.END).strip()
            self.info_frame.pack_forget()

        self.answers.append({
            'id': self.data_manager.questions[self.current_question]['id'],
            'response': answer
        })
        self.current_question += 1
        if self.current_question < len(self.data_manager.questions):
            self.update_question()
        else:
            self.show_result()

    def previous_question(self):
        if self.current_question > 0:
            self.current_question -= 1
            self.answers.pop()
            self.update_question()

    def evaluate_risk(self):
        level, criteria, suggestions = self.data_manager.evaluate_risk(self.answers)
        return level, criteria, suggestions

    def show_result(self):
        level, criteria, suggestions = self.evaluate_risk()
        self.user_info['risk_level'] = level
        self.user_info['criteria'] = criteria
        self.user_info['suggestions'] = suggestions

        message = f"Livello di Rischio: {level}\n\nCriterio: {criteria}\n\n"

        # Aggiungere informazioni sui requisiti in base al livello di rischio
        requirements = self.data_manager.get_requirements(level)
        self.user_info['requirements'] = requirements

        message += requirements

        if suggestions:
            message += "\n\nSuggerimenti Personalizzati:\n" + suggestions

        messagebox.showinfo("Risultato della Valutazione", message)

        # Chiedi all'utente se desidera esportare un report
        save_report = messagebox.askyesno("Esporta Report", "Desideri esportare un report in PDF?")
        if save_report:
            self.export_pdf()

    def export_pdf(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf",
                                                 filetypes=[("PDF files", "*.pdf")],
                                                 title="Salva Report")
        if file_path:
            generate_pdf_report(file_path, self.user_info)
            messagebox.showinfo("Esportazione completata", "Il report è stato esportato con successo.")

    def save_assessment(self):
        data = {
            'user_info': self.user_info,
            'answers': self.answers,
            'current_question': self.current_question
        }
        file_path = filedialog.asksaveasfilename(defaultextension=".json",
                                                 filetypes=[("JSON files", "*.json")],
                                                 title="Salva Valutazione")
        if file_path:
            self.data_manager.save_assessment(file_path, data)
            messagebox.showinfo("Salvataggio completato", "La valutazione è stata salvata con successo.")

    def load_assessment(self):
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")],
                                               title="Apri Valutazione")
        if file_path:
            data = self.data_manager.load_assessment(file_path)
            if data:
                self.user_info = data.get('user_info', {})
                self.answers = data.get('answers', [])
                self.current_question = data.get('current_question', 0)
                self.update_question_loaded()
                messagebox.showinfo("Caricamento completato", "La valutazione è stata caricata con successo.")
            else:
                messagebox.showerror("Errore", "Impossibile caricare la valutazione.")

    def update_question_loaded(self):
        # Aggiorna le informazioni sull'utente
        self.project_name_entry.delete(0, tk.END)
        self.project_name_entry.insert(0, self.user_info.get('project_name', ''))

        self.project_desc_text.delete("1.0", tk.END)
        self.project_desc_text.insert(tk.END, self.user_info.get('project_description', ''))

        if self.current_question == 0:
            self.info_frame.pack(pady=10)
        else:
            self.info_frame.pack_forget()

        if self.current_question < len(self.data_manager.questions):
            self.update_question()
        else:
            self.show_result()

    def new_assessment(self):
        self.current_question = 0
        self.answers = []
        self.user_info = {}

        self.info_frame.pack(pady=10)
        self.project_name_entry.delete(0, tk.END)
        self.project_desc_text.delete("1.0", tk.END)

        self.update_question()

    def show_resources(self):
        resources = self.data_manager.get_resources()
        messagebox.showinfo("Risorse Aggiuntive", resources)
