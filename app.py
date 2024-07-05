import tkinter as tk
from tkinter import ttk, messagebox
from .analyze import analyze_campaigns

class CampaignAnalyzerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Campaign Analyzer")
        self.master.geometry("400x300")
        self.master.configure(bg='#E6F3FF')
        self.campaign_data = {}

        self.style = ttk.Style()
        self.style.configure('TLabel', background='#E6F3FF', font=('Arial', 10))
        self.style.configure('TButton', background='#0056b3', font=('Arial', 10, 'bold'))
        self.style.map('TButton', background=[('active', '#003d82')])

        self.create_input_widgets()

    def create_input_widgets(self):
        main_frame = ttk.Frame(self.master, padding="10 10 10 10", style='TFrame')
        main_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(0, weight=1)
        main_frame.configure(style='TFrame')

        ttk.Label(main_frame, text="Campaign Name:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.campaign_entry = ttk.Entry(main_frame, width=30)
        self.campaign_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(main_frame, text="Cost:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.cost_entry = ttk.Entry(main_frame, width=30)
        self.cost_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(main_frame, text="Clicks:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.clicks_entry = ttk.Entry(main_frame, width=30)
        self.clicks_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(main_frame, text="Impressions:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.impressions_entry = ttk.Entry(main_frame, width=30)
        self.impressions_entry.grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(main_frame, text="Conversions:").grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.conversions_entry = ttk.Entry(main_frame, width=30)
        self.conversions_entry.grid(row=4, column=1, padx=5, pady=5)

        button_frame = ttk.Frame(main_frame, style='TFrame')
        button_frame.grid(row=5, column=0, columnspan=2, pady=10)

        ttk.Button(button_frame, text="Add Campaign", command=self.add_campaign, style='TButton').grid(row=0, column=0, padx=5)
        ttk.Button(button_frame, text="Analyze Campaigns", command=self.show_analysis, style='TButton').grid(row=0, column=1, padx=5)

    def add_campaign(self):
        try:
            campaign = self.campaign_entry.get()
            cost = float(self.cost_entry.get())
            clicks = int(self.clicks_entry.get())
            impressions = int(self.impressions_entry.get())
            conversions = int(self.conversions_entry.get())

            self.campaign_data[campaign] = {
                'Cost': cost,
                'Clicks': clicks,
                'Impressions': impressions,
                'Conversions': conversions
            }

            messagebox.showinfo("Success", f"Campaign '{campaign}' added successfully!")
            self.clear_entries()
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for cost, clicks, impressions, and conversions.")

    def clear_entries(self):
        self.campaign_entry.delete(0, tk.END)
        self.cost_entry.delete(0, tk.END)
        self.clicks_entry.delete(0, tk.END)
        self.impressions_entry.delete(0, tk.END)
        self.conversions_entry.delete(0, tk.END)

    def show_analysis(self):
        if not self.campaign_data:
            messagebox.showwarning("Warning", "No campaigns to analyze. Please add campaigns first.")
            return

        analysis = analyze_campaigns(self.campaign_data)
        
        analysis_window = tk.Toplevel(self.master)
        analysis_window.title("Campaign Analysis Results")
        analysis_window.geometry("500x400")
        analysis_window.configure(bg='#E6F3FF')

        results_frame = ttk.Frame(analysis_window, padding="10 10 10 10", style='TFrame')
        results_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        results_frame.columnconfigure(0, weight=1)
        results_frame.rowconfigure(0, weight=1)

        results_text = tk.Text(results_frame, wrap=tk.WORD, width=60, height=20, bg='white', font=('Arial', 10))
        results_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        scrollbar = ttk.Scrollbar(results_frame, orient=tk.VERTICAL, command=results_text.yview)
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        results_text['yscrollcommand'] = scrollbar.set

        for campaign, metrics in analysis.items():
            results_text.insert(tk.END, f"Campaign: {campaign}\n", 'bold')
            results_text.insert(tk.END, f"CPC: {metrics['CPC']:.2f}\n")
            results_text.insert(tk.END, f"CTR: {metrics['CTR']:.2%}\n")
            results_text.insert(tk.END, f"CPA: {metrics['CPA']:.2f}\n\n")

        results_text.tag_configure('bold', font=('Arial', 10, 'bold'))
        results_text.config(state=tk.DISABLED)

def main():
    root = tk.Tk()
    root.configure(bg='#E6F3FF')
    app = CampaignAnalyzerApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()

