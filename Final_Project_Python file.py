# Names/Coders: Cole Tyson, Sohail Mohammed
# Course: Core Concepts in Computer Science (Comp 123)
# Professor: Dr. Lauren Milne

import tkinter as tk
from tkinter import ttk
from yfinance import *
import matplotlib.pyplot as plt

def wholeProject():
    '''This function runs the entire code!!!'''
    sector_stocks = { # This is a dictionary containing 8 different sectors and 5 stocks for each sector.
        'Technology': ['AAPL', 'MSFT', 'GOOGL', 'META', 'NVDA'],
        'Finance': ['PGR', 'GS', 'V', 'MA', 'AXP'],
        'Healthcare': ['TMO', 'LLY', 'UNH', 'PFE', 'AMGN'],
        'Energy': ['XOM', 'VLO', 'COP', 'EOG', 'MPC'],
        'Industrial': ['CAT', 'GE', 'UBER', 'UNP','RTX'],
        'Consumer Discretionary': ['AMZN', 'TSLA', 'HD', 'MCD', 'LOW'],
        'Consumer Staples': ['PG','COST','WMT','KO','PEP'],
        'Real Estate': ['PLD', 'AMT', 'EQIX', 'SPG', 'O']
    }

    class Interface:
        def __init__(self):  # Constructor
            self.window = tk.Tk()
            self.window.title("Comparative Stock Data")

            # Dropdown menu for stock sectors
            sectorDrop = ttk.Label(self.window, text="Select Sector")
            sectorDrop.grid(row=0, column=0)
            self.sector_combobox = ttk.Combobox(self.window, values=list(sector_stocks.keys()), state="readonly")
            self.sector_combobox.set('Choose your sector here!')
            self.sector_combobox.grid(row=0, column=1)
            self.sector_combobox.bind("<<ComboboxSelected>>", self.on_sector_select)

            # Dropdown menu for first stock
            stockDrop1 = tk.Label(self.window, text="Select 1st Stock:")
            stockDrop1.grid(row=1, column=0)
            self.stock_combobox = ttk.Combobox(self.window, values=[], state="readonly")
            self.stock_combobox.set('Choose your 1st stock here!')
            self.stock_combobox.grid(row=1, column=1)
            self.stock_combobox.bind("<<ComboboxSelected>>", self.on_stock_select)

            # Dropdown menu for second stock
            stockDrop2 = tk.Label(self.window, text="Select 2nd Stock:")
            stockDrop2.grid(row=2, column=0)
            self.stock_combobox2 = ttk.Combobox(self.window, values=[], state="readonly")
            self.stock_combobox2.set('Choose your 2nd stock here!')
            self.stock_combobox2.grid(row=2, column=1)
            self.stock_combobox2.bind("<<ComboboxSelected>>", self.on_stock_select)

            # Stock information labels
            self.PE_label1 = tk.Label(self.window, text="PE Ratio1")
            self.PE_label1.grid(row=5, column=0)
            self.revenue_label1 = tk.Label(self.window, text="Revenue1")
            self.revenue_label1.grid(row=3, column=0)
            self.debt_label1 = tk.Label(self.window, text="Debt1")
            self.debt_label1.grid(row=4, column=0)
            self.CurrentRatio_label1 = tk.Label(self.window, text="Current Ratio1")
            self.CurrentRatio_label1.grid(row=6, column=0)
            self.PE_label2 = tk.Label(self.window, text="PE Ratio2")
            self.PE_label2.grid(row=5, column=1)
            self.revenue_label2 = tk.Label(self.window, text="Revenue2")
            self.revenue_label2.grid(row=3, column=1)
            self.debt_label2 = tk.Label(self.window, text="Debt2")
            self.debt_label2.grid(row=4, column=1)
            self.CurrentRatio_label2 = tk.Label(self.window, text="Current Ratio2")
            self.CurrentRatio_label2.grid(row=6, column=1)

        def stockStats(self, stkTicker):
            '''This function gathers, stores, and returns the PE Ratio, Revenue, Debt, and Current Ratio values for a stock as an input and returns those values.'''
            stock = Ticker(stkTicker)
            PERatio = stock.info['forwardPE'] if stock.info['forwardPE'] else "N/A"
            Revenue = stock.info['totalRevenue'] if stock.info['totalRevenue'] else "N/A"
            Debt = stock.info['totalDebt'] if stock.info['totalDebt'] else "N/A"
            CurrentRatio = stock.info['currentRatio'] if stock.info['currentRatio'] else "N/A"
            return PERatio, CurrentRatio, Revenue, Debt

        def stockGraph(self, stkTicker1, stkTicker2):
            '''This function takes two stocks as inputs and then graphs the prices of both those stocks over the maximum available period.'''
            stock1 = download(stkTicker1, period="max")
            stock2 = download(stkTicker2, period="max")
            plt.figure(figsize=(8, 5))
            plt.plot(stock1['Open'], label=stkTicker1)
            plt.plot(stock2['Open'], label=stkTicker2)
            plt.xlabel('Years')
            plt.ylabel('Stock Price ($)')
            plt.title('Stock Price Over Available Period')
            plt.grid(True)
            plt.legend()
            plt.show()

        def on_sector_select(self, event):
            selected_sector = self.sector_combobox.get()
            if selected_sector != '':
                stocks = sector_stocks.get(selected_sector)
                self.stock_combobox['values'] = stocks
                self.stock_combobox2['values'] = stocks

        def on_stock_select(self, event):
            selected_stock1 = self.stock_combobox.get()
            selected_stock2 = self.stock_combobox2.get()
            if selected_stock1 != 'Choose your 1st stock here!' and selected_stock2 != 'Choose your 2nd stock here!':
                PERatio1, Revenue1, Debt1, CurrentRatio1 = self.stockStats(selected_stock1)
                self.PE_label1.config(text='PE Ratio1 = ' + str(PERatio1))
                self.revenue_label1.config(text='Revenue1 = ' + str(Revenue1))
                self.debt_label1.config(text='Debt1 = ' + str(Debt1))
                self.CurrentRatio_label1.config(text='Current Ratio1 = ' + str(CurrentRatio1))
                PERatio2, Revenue2, Debt2, CurrentRatio2 = self.stockStats(selected_stock2)
                self.PE_label2.config(text='PE Ratio2 = ' + str(PERatio2))
                self.revenue_label2.config(text='Revenue2 = ' + str(Revenue2))
                self.debt_label2.config(text='Debt2 = ' + str(Debt2))
                self.CurrentRatio_label2.config(text='Current Ratio2 = ' + str(CurrentRatio2))
                self.stockGraph(selected_stock1, selected_stock2)

        def run(self):
            self.window.mainloop()

    myGui = Interface()
    myGui.run()

if __name__ == "__main__":
    wholeProject()




