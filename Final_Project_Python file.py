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
            self.window.title(
                "Comparative Stock Data")  # Titles the window that the user interacts with: "Comparative Stock Data

            # This section of code creates a dropdown menu of stock sectors for the user to select a sector.
            sectorDrop = ttk.Label(self.window, text="Select Sector")
            sectorDrop.grid(row=0, column=0)
            self.sector_combobox = ttk.Combobox(self.window, values=list(sector_stocks.keys()),
                                                state="readonly")  # Sets the value of the dropdown menu to be a list of stock sectors; also sets the dropdown menu to only be changed by selecting a sector.
            self.sector_combobox.set(
                'Choose your sector here!')  # Makes the original value of the dropdown menu say "Choose your sector here!"
            self.sector_combobox.grid(row=0,
                                      column=1)  # Sets placement of this dropdown menu in the window that the user interacts with.
            self.sector_combobox.bind("<<ComboboxSelected>>",
                                      self.on_sector_select)  # Calls the on_sector_select function when a sector is selected

            # This section of code creates a dropdown menu of stocks for the user to select a stock from a particular sector that they already selected above.
            stockDrop1 = tk.Label(self.window, text="Select 1st Stock:")
            stockDrop1.grid(row=1, column=0)
            self.stock_combobox = ttk.Combobox(self.window, values=[],
                                               state="readonly")  # Sets the value of this dropdown menu to be a list of stocks from the already-chosen sector; also sets this dropdown menu to only be changed by selecting a stock.
            self.stock_combobox.set(
                'Choose your 1st stock here!')  # Makes the orginal value of this dropdown menu say "Choose your 1st stock here!"
            self.stock_combobox.grid(row=1,
                                     column=1)  # Sets placement of this dropdown menu in the window that the user interacts with.
            self.stock_combobox.bind("<<ComboboxSelected>>",
                                     self.on_stock_select)  # Calls the on_stock_select function when a stock is selected

            # This section of code creates another dropdown menu of stocks for the user to select a stock from a particular sector that they already selected above. It should be noted that they can choose a stock from another sector if they select another sector from the sector dropdown menu.
            stockDrop2 = tk.Label(self.window, text="Select 2nd Stock:")
            stockDrop2.grid(row=2, column=0)
            self.stock_combobox2 = ttk.Combobox(self.window, values=[],
                                                state="readonly")  # Sets the value of this dropdown menu to be a list of stocks from the already-chosen sector; also sets this dropdown menu to only be changed by selecting a stock.
            self.stock_combobox2.set(
                'Choose your 2nd stock here!')  # Makes the orginal value of this dropdown menu say "Choose your 2nd stock here!"
            self.stock_combobox2.grid(row=2,
                                      column=1)  # Sets placement of this dropdown menu in the window that the user interacts with.
            self.stock_combobox2.bind("<<ComboboxSelected>>",
                                      self.on_stock_select)  # Calls the on_stock_select function when a stock is selected

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
            stock = Ticker(stkTicker)  # Stores the stock ticker passed in as a parameter as a variable called 'stock'
            PERatio = stock.info['forwardPE']  # Stores the stock's forward PE Ratio in a variable called 'PERatio'
            Revenue = stock.info['totalRevenue']  # Stores the stock's total revenue in a variable called 'Revenue'
            Debt = stock.info['totalDebt']  # Stores the stock's total debt in a variable called 'Debt'
            CurrentRatio = stock.info[
                'currentRatio']  # Stores the stock's current ratio in a variable called 'CurrentRatio'
            return PERatio, CurrentRatio, Revenue, Debt  # Returns variables: PERatio, Revenue, Debt, and CurrentRatio

        def stockGraph(self, stkTicker1, stkTicker2):
            '''This function takes two stocks as inputs and then graphs the prices of both those stocks over 50 years
            It should be noted that this particular function had significant help from AI in being defined.'''
            stock1 = download(stkTicker1,
                              period="50y")  # Downloads data for first stock input over 50 years and stores it a variable called 'stock1'
            stock2 = download(stkTicker2,
                              period="50y")  # Downloads data for second stock input over 50 years and stores it a variable called 'stock2'
            plt.figure(figsize=(8, 5))  # Creates graph plane with width level 8 and height level 5
            plt.plot(stock1['Open'], label=stkTicker1)  # Plots a line graph of stock1's opening price over 50 years
            plt.plot(stock2['Open'], label=stkTicker2)  # Plots a line graph of stock2's opening price over 50 years
            plt.xlabel('Years')  # Titles the x-axis of the graph to 'Years'
            plt.ylabel('Stock Price ($)')  # Titles the y-axis of the graph to 'Stock Price ($)'
            plt.title('Stock Price Over 50 Years')  # Titles the entire graph to 'Stock Price Over 50 Years'
            plt.grid(True)  # Creates a grid on the graph plane
            plt.legend()  # Creates a colored key for each stock
            plt.show()  # Shows the graph

        def on_sector_select(self, event):
            '''This function sets the values of the 2 stock dropdown menus to the stocks within the sector selected from the sector dropdown menu.
            It should be noted that this particular function had significant help from AI in being defined.'''
            selected_sector = self.sector_combobox.get()  # Sets a variable 'selected_sector' equal to the sector selected on the sector dropdown menu
            if selected_sector != '':  # Checks to make sure that a sector is selected from the sector dropdown menu
                stocks = sector_stocks.get(
                    selected_sector)  # Sets a variable 'stocks' equal to the list of stocks within the sector selected from the sector dropdown menu
                self.stock_combobox[
                    'values'] = stocks  # Sets the first stock dropdown menu equal to the list of stocks within the sector selected from the sector dropdown menu
                self.stock_combobox2[
                    'values'] = stocks  # Sets the list of stocks within the sector selected from the sector dropdown menu

        def on_stock_select(self, event):
            '''This function retrieves relevant data from yahoo finance for the two stocks selected from the dropdown menus. It resets the pre-defined labels for such data to now show the data. It also calls the stockGraph function at the end.'''
            selected_stock1 = self.stock_combobox.get()  # Sets a variable 'selected_stock1' equal to the stock selected on the first stock dropdown menu.
            selected_stock2 = self.stock_combobox2.get()  # Sets a variable 'selected_stock2' equal to the stock selected on the second stock dropdown menu.
            if selected_stock1 != 'Choose your 1st stock here!' and selected_stock2 != 'Choose your 2nd stock here!':  # Checks to make sure that stocks are selected on both stock dropdown menus.
                PERatio1, Revenue1, Debt1, CurrentRatio1 = self.stockStats(
                    selected_stock1)  # Calls the stockStats function to gather and then store the PE Ratio, Total Revenue, Total Debt, and Current Ratio statistics in variables for the stock selected in the first stock dropdown menu.
                self.PE_label1.config(text='PE Ratio1 = ' + str(
                    PERatio1))  # Adds the PE Ratio value retrieved above to the PE label for the stock selected in the first dropdown menu.
                self.revenue_label1.config(text='Revenue1 = ' + str(
                    Revenue1))  # Adds the revenue value retrieved above to the revenue label for the stock selected in the first dropdown menu.
                self.debt_label1.config(text='Debt1 = ' + str(
                    Debt1))  # Adds the debt value retrieved above to the debt label for the stock selected in the first dropdown menu.
                self.CurrentRatio_label1.config(text='Current Ratio1 = ' + str(
                    CurrentRatio1))  # Adds the CurrentRatio value retrieved above to the CurrentRatio label for the stock selected in the first dropdown menu.
                PERatio2, Revenue2, Debt2, CurrentRatio2 = self.stockStats(
                    selected_stock2)  # Calls the stockStats function to gather and store the PE Ratio, Total Revenue, Total Debt, and Current Ratio statistics in variables for the stock selected in the second stock dropdown menu.
                self.PE_label2.config(text='PE Ratio2 = ' + str(
                    PERatio2))  # Adds the PE Ratio value retrieved above to the PE label for the stock selected in the second dropdown menu.
                self.revenue_label2.config(text='Revenue2 = ' + str(
                    Revenue2))  # Adds the revenue value retrieved above to the revenue label for the stock selected in the second dropdown menu.
                self.debt_label2.config(text='Debt2 = ' + str(
                    Debt2))  # Adds the debt value retrieved above to the debt label for the stock selected in the second dropdown menu.
                self.CurrentRatio_label2.config(text='Current Ratio2 = ' + str(
                    CurrentRatio2))  # Adds the CurrentRatio value retrieved above to the CurrentRatio label for the stock selected in the second dropdown menu.
                self.stockGraph(selected_stock1,
                                selected_stock2)  # Calls the stockGraph function to graph the prices of the stocks selected in both stock dropdown menus

        def run(self):
            self.window.mainloop()

    myGui = Interface()
    myGui.run()


if __name__ == "__main__":
    wholeProject()




