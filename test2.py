from tkinter import *
# testlist = ['   0013', '   4', '  0', '  7', '  2', '  11', '  17', '  9', '  1', '  0', '  0', '  5', '  2', '  1', '  0', '  0', '  0', '  0', '  0', '  0', '  3', '  0', '  21', '  0', '  1', '  0', '  0', '  0', '  0', '  0', '  2', '  7', '  0', '  0', ' 1  5', ' 2  40', ' 3  4', ' 4  0', ' 5  0', ' 6  0', ' 7  0', ' 8  0', ' 9  0', '10  0', '11  0', '12  0', '13  0', '14  0', '15  0', '16  0', ' 1  4', ' 2  23', ' 3  32', ' 4  50', ' 5  1', ' 6  0', '  0', '    760', '  10', ' 1  0', ' 2  0', ' 3  0', ' 4  0', ' 5  0', ' 6  2', ' 7  0', ' 8  0', ' 9  0', '10  1', '11  0', '12  0', '13  0', '14  0', '15  1', '16  0']
# print(testlist[34],testlist[49],'\n',testlist[50],testlist[55],'\n',testlist[59],testlist[74])

# vlx50 = ['   0056', '   1', ' 35', ' 0', ' 196', ' 0', ' 49', ' 0', ' 6', ' 0', ' 9', ' 0', ' 42', ' 0', ' 2', ' 0', ' 8', ' 0', ' 0', ' 0', ' 0', ' 0', ' 1  231', ' 2  114', ' 3  2', ' 4  0', ' 5  0', ' 6  0', ' 7  0', ' 8  0', ' 1  35', ' 2  77', ' 3  77', ' 4  342', ' 5  3', ' 6  0', '  0', '    4144', '  84', ' 1  0', ' 2  0', ' 3  0', ' 4  0', ' 5  0', ' 6  0', ' 7  0', ' 8  0', ' 9  0', '10  0', '11  0']
# brio46 = ['   0081', '   12', ' 0', ' 0', ' 0', ' 0', ' 0', ' 0', ' 0', ' 0', ' 0', ' 0', ' 0', ' 0', ' 0', ' 0', ' 0', ' 0', ' 1  0', ' 2  0', ' 3  0', ' 4  0', ' 5  0', ' 6  0', ' 7  0', ' 8  0', ' 1  0', ' 2  0', ' 3  0', ' 4  0', ' 5  0', ' 6  0', '  0', '    000', '  000', ' 1  0', ' 2  0', ' 3  0', ' 4  0', ' 5  0', ' 6  0', ' 7  0', ' 8  0', ' 9  0', '10  0', '11  0']
# colibri47 = ['  0125', '   1', ' 0', ' 0', ' 0', ' 0', ' 61', ' 6', ' 44', ' 0', ' 0', ' 0', ' 1', ' 0', ' 15', ' 0', ' 8', ' 0', ' 1  61', ' 2  59', ' 3  9', ' 4  0', ' 5  0', ' 6  0', ' 7  0', ' 8  0', ' 1  0', ' 2  0', ' 3  0', ' 4  0', ' 5  0', ' 6  0', ' 7  0', ' 8  0', ' 9  0', '10  0', '11  0', '12  0', '13  0', ' 1  15', ' 2  22', ' 3  26', ' 4  101', ' 5  10', ' 6  0', '         1699', '    0']
# class nes():
#     def __init__(self,code):
#         self.code=code
#         print(self.code)

# Brio, Venezia
# records = 0
# count =0
# for record in records:
#     if count % 2 == 0:
#         my_tree.insert(parent='', index='end', iid=count, text='',
#                        values=(record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10],
#                                record[11], record[12], record[13], record[14], record[15], record[16], record[17], record[18], record[19], record[20],
#                                record[21], record[22], record[23], record[24], record[25], record[26], record[27], record[28], record[29], record[30],
#                                record[31], record[32], record[33], record[34], record[35], record[36], record[37], record[38], record[39], record[40],
#                                record[41], record[42], record[43], record[44], record[45], record[46], record[47], record[48], record[49], record[50],
#                                record[51], record[52], record[53], record[54], record[55], record[56], record[57], record[58], record[59], record[60],
#                                record[61], record[62], record[63], record[64], record[65], record[66], record[67], record[68], record[69], record[70],
#                                record[71], record[72], record[73], record[74], record[75], record[76], record[77], record[78], record[79], record[80]),
#                        tags=('evenrow',))
#     else:
#         my_tree.insert(parent='', index='end', iid=count, text='',
#                        values=(record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10],
#                                record[11], record[12], record[13], record[14], record[15], record[16], record[17], record[18], record[19], record[20],
#                                record[21], record[22], record[23], record[24], record[25], record[26], record[27], record[28], record[29], record[30],
#                                record[31], record[32], record[33], record[34], record[35], record[36], record[37], record[38], record[39], record[40],
#                                record[41], record[42], record[43], record[44], record[45], record[46], record[47], record[48], record[49], record[50],
#                                record[51], record[52], record[53], record[54], record[55], record[56], record[57], record[58], record[59], record[60],
#                                record[61], record[62], record[63], record[64], record[65], record[66], record[67], record[68], record[69], record[70],
#                                record[71], record[72], record[73], record[74], record[75], record[76]),
#                        tags=('evenrow',))
# (od+\S*\s+\S{0,4}\s*=\s+\d{1,4})|([P,p]+\w{0,7}\s\w{1,2}.\s=\s\d{0,6})|(Pa\D{4,7}\d{1,6})|(Test\s*=\s\d{1,6})|(Pr\D{1,2}\s*\d{1,2}\s*=\s\d{1,6})|([C,M]o\D{1,2}\s*\d{1,6}\s*=\s\d{1,6})|(et.\s*=\s\d{1,6})|(CA\S{2,4}\s*\D{0,7}\s=\s\d{1,9})|(I\S{1,5}\s*=\s\d{1,6})|(Er\D{0,2}\d{1,2}\s*=\s\d{1,6})
# (Cod. = \d{8})|(TOTAL COUNT\s\d{6,10})|(norm.o.Total =\s\d{1,8})|(mainten.Total = \d{1,8})|(SELECTION NUM.\s*\d{1,2})|(Band \d Total = \d{1,8})|(Coin N. \d Total = \d{1,8})|(TOTAL CASH Tot. = \d{1,6})|(TOTAL CASH x CRED. Tot. = \d{1,8})|(Counter = \d{1,6})
def unique_tree(name,my_tree):
    if name == 'FSE':
        my_tree['columns'] = (
        "Date", "Email", "Print", "Pay1", "Test1", "Pay2", "Test2", "Pay3", "Test3", "Pay4", "Test4", "Pay5", "Test5",
        "Pay6", "Test6", "Pay7", "Test7", "Pay8", "Test8", "Pay9", "Test9", "Pay10", "Test10", "Pay11", "Test11",
        "Pay12", "Test12", "Pay13", "Test13", "Pay14", "Test14", "Pay15", "Test15", "Pay16", "Test16", "Price1",
        "Price2", "Price3", "Price4", "Price5", "Price6", "Price7", "Price8", "Price9", "Price10", "Price11", "Price12",
        "Price13", "Price14", "Price15", "Price16", "Coin1", "Coin2", "Coin3", "Coin4", "Coin5", "Coin6", "Token",
        "Total Cash", 'Total Credit', "Error1", "Error2", "Error3", "Error4", "Error5", "Error6", "Error7", "Error8",
        "Error9", "Error10", "Error11", "Error12", "Error13", "Error14", "Error15", "Error16")

        # Format Our Columns
        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("Date", anchor=W, width=50)
        my_tree.column("Email", anchor=W, width=50)
        my_tree.column("Print", anchor=W, width=50)
        my_tree.column("Pay1", anchor=W, width=50)
        my_tree.column("Test1", anchor=W, width=50)
        my_tree.column("Pay2", anchor=W, width=50)
        my_tree.column("Test2", anchor=W, width=50)
        my_tree.column("Pay3", anchor=W, width=50)
        my_tree.column("Test3", anchor=W, width=50)
        my_tree.column("Pay4", anchor=W, width=50)
        my_tree.column("Test4", anchor=W, width=50)
        my_tree.column("Pay5", anchor=W, width=50)
        my_tree.column("Test5", anchor=W, width=50)
        my_tree.column("Pay6", anchor=W, width=50)
        my_tree.column("Test6", anchor=W, width=50)
        my_tree.column("Pay7", anchor=W, width=50)
        my_tree.column("Test7", anchor=W, width=50)
        my_tree.column("Pay8", anchor=W, width=50)
        my_tree.column("Test8", anchor=W, width=50)
        my_tree.column("Pay9", anchor=W, width=50)
        my_tree.column("Test9", anchor=W, width=50)
        my_tree.column("Pay10", anchor=W, width=50)
        my_tree.column("Test10", anchor=W, width=50)
        my_tree.column("Pay11", anchor=W, width=50)
        my_tree.column("Test11", anchor=W, width=50)
        my_tree.column("Pay12", anchor=W, width=50)
        my_tree.column("Test12", anchor=W, width=50)
        my_tree.column("Pay13", anchor=W, width=50)
        my_tree.column("Test13", anchor=W, width=50)
        my_tree.column("Pay14", anchor=W, width=50)
        my_tree.column("Test14", anchor=W, width=50)
        my_tree.column("Pay15", anchor=W, width=50)
        my_tree.column("Test15", anchor=W, width=50)
        my_tree.column("Pay16", anchor=W, width=50)
        my_tree.column("Test16", anchor=W, width=50)
        my_tree.column("Price1", anchor=W, width=50)
        my_tree.column("Price2", anchor=W, width=50)
        my_tree.column("Price3", anchor=W, width=50)
        my_tree.column("Price4", anchor=W, width=50)
        my_tree.column("Price5", anchor=W, width=50)
        my_tree.column("Price6", anchor=W, width=50)
        my_tree.column("Price7", anchor=W, width=50)
        my_tree.column("Price8", anchor=W, width=50)
        my_tree.column("Price9", anchor=W, width=50)
        my_tree.column("Price10", anchor=W, width=50)
        my_tree.column("Price11", anchor=W, width=50)
        my_tree.column("Price12", anchor=W, width=50)
        my_tree.column("Price13", anchor=W, width=50)
        my_tree.column("Price14", anchor=W, width=50)
        my_tree.column("Price15", anchor=W, width=50)
        my_tree.column("Price16", anchor=W, width=50)
        my_tree.column("Coin1", anchor=W, width=50)
        my_tree.column("Coin2", anchor=W, width=50)
        my_tree.column("Coin3", anchor=W, width=50)
        my_tree.column("Coin4", anchor=W, width=50)
        my_tree.column("Coin5", anchor=W, width=50)
        my_tree.column("Coin6", anchor=W, width=50)
        my_tree.column("Token", anchor=W, width=50)
        my_tree.column("Total Cash", anchor=W, width=50)
        my_tree.column("Total Credit", anchor=W, width=50)
        my_tree.column("Error1", anchor=W, width=50)
        my_tree.column("Error2", anchor=W, width=50)
        my_tree.column("Error3", anchor=W, width=50)
        my_tree.column("Error4", anchor=W, width=50)
        my_tree.column("Error5", anchor=W, width=50)
        my_tree.column("Error6", anchor=W, width=50)
        my_tree.column("Error7", anchor=W, width=50)
        my_tree.column("Error8", anchor=W, width=50)
        my_tree.column("Error9", anchor=W, width=50)
        my_tree.column("Error10", anchor=W, width=50)
        my_tree.column("Error11", anchor=W, width=50)
        my_tree.column("Error12", anchor=W, width=50)
        my_tree.column("Error13", anchor=W, width=50)
        my_tree.column("Error14", anchor=W, width=50)
        my_tree.column("Error15", anchor=W, width=50)
        my_tree.column("Error16", anchor=W, width=50)

        # Create Headings
        my_tree.heading("#0", text="", anchor=W)
        my_tree.heading("Date", text="Date", anchor=W)
        my_tree.heading("Email", text="Email", anchor=W)
        my_tree.heading("Print", text="Print", anchor=W)
        my_tree.heading("Pay1", text="Pay1", anchor=W)
        my_tree.heading("Test1", text="Test1", anchor=W)
        my_tree.heading("Pay2", text="Pay2", anchor=W)
        my_tree.heading("Test2", text="Test2", anchor=W)
        my_tree.heading("Pay3", text="Pay3", anchor=W)
        my_tree.heading("Test3", text="Test3", anchor=W)
        my_tree.heading("Pay4", text="Pay4", anchor=W)
        my_tree.heading("Test4", text="Test4", anchor=W)
        my_tree.heading("Pay5", text="Pay5", anchor=W)
        my_tree.heading("Test5", text="Test5", anchor=W)
        my_tree.heading("Pay6", text="Pay6", anchor=W)
        my_tree.heading("Test6", text="Test6", anchor=W)
        my_tree.heading("Pay7", text="Pay7", anchor=W)
        my_tree.heading("Test7", text="Test7", anchor=W)
        my_tree.heading("Pay8", text="Pay8", anchor=W)
        my_tree.heading("Test8", text="Test8", anchor=W)
        my_tree.heading("Pay9", text="Pay9", anchor=W)
        my_tree.heading("Test9", text="Test9", anchor=W)
        my_tree.heading("Pay10", text="Pay10", anchor=W)
        my_tree.heading("Test10", text="Test10", anchor=W)
        my_tree.heading("Pay11", text="Pay11", anchor=W)
        my_tree.heading("Test11", text="Test11", anchor=W)
        my_tree.heading("Pay12", text="Pay12", anchor=W)
        my_tree.heading("Test12", text="Test12", anchor=W)
        my_tree.heading("Pay13", text="Pay13", anchor=W)
        my_tree.heading("Test13", text="Test13", anchor=W)
        my_tree.heading("Pay14", text="Pay14", anchor=W)
        my_tree.heading("Test14", text="Test14", anchor=W)
        my_tree.heading("Pay15", text="Pay15", anchor=W)
        my_tree.heading("Test15", text="Test15", anchor=W)
        my_tree.heading("Pay16", text="Pay16", anchor=W)
        my_tree.heading("Test16", text="Test16", anchor=W)
        my_tree.heading("Price1", text="Price1", anchor=W)
        my_tree.heading("Price2", text="Price2", anchor=W)
        my_tree.heading("Price3", text="Price3", anchor=W)
        my_tree.heading("Price4", text="Price4", anchor=W)
        my_tree.heading("Price5", text="Price5", anchor=W)
        my_tree.heading("Price6", text="Price6", anchor=W)
        my_tree.heading("Price7", text="Price7", anchor=W)
        my_tree.heading("Price8", text="Price8", anchor=W)
        my_tree.heading("Price9", text="Price9", anchor=W)
        my_tree.heading("Price10", text="Price10", anchor=W)
        my_tree.heading("Price11", text="Price11", anchor=W)
        my_tree.heading("Price12", text="Price12", anchor=W)
        my_tree.heading("Price13", text="Price13", anchor=W)
        my_tree.heading("Price14", text="Price14", anchor=W)
        my_tree.heading("Price15", text="Price15", anchor=W)
        my_tree.heading("Price16", text="Price16", anchor=W)
        my_tree.heading("Coin1", text="Coin1", anchor=W)
        my_tree.heading("Coin2", text="Coin2", anchor=W)
        my_tree.heading("Coin3", text="Coin3", anchor=W)
        my_tree.heading("Coin4", text="Coin4", anchor=W)
        my_tree.heading("Coin5", text="Coin5", anchor=W)
        my_tree.heading("Coin6", text="Coin6", anchor=W)
        my_tree.heading("Token", text="Token", anchor=W)
        my_tree.heading("Total Cash", text="Total Cash", anchor=W)
        my_tree.heading("Total Credit", text="Total Credit", anchor=W)
        my_tree.heading("Error1", text="Error1", anchor=W)
        my_tree.heading("Error2", text="Error2", anchor=W)
        my_tree.heading("Error3", text="Error3", anchor=W)
        my_tree.heading("Error4", text="Error4", anchor=W)
        my_tree.heading("Error5", text="Error5", anchor=W)
        my_tree.heading("Error6", text="Error6", anchor=W)
        my_tree.heading("Error7", text="Error7", anchor=W)
        my_tree.heading("Error8", text="Error8", anchor=W)
        my_tree.heading("Error9", text="Error9", anchor=W)
        my_tree.heading("Error10", text="Error10", anchor=W)
        my_tree.heading("Error11", text="Error11", anchor=W)
        my_tree.heading("Error12", text="Error12", anchor=W)
        my_tree.heading("Error13", text="Error13", anchor=W)
        my_tree.heading("Error14", text="Error14", anchor=W)
        my_tree.heading("Error15", text="Error15", anchor=W)
        my_tree.heading("Error16", text="Error16", anchor=W)
    elif name == 'Brio' or name == 'Venezia':
        my_tree['columns'] = (
            "Date", "Email", "Print", "Pay1", "Test1", "Pay2", "Test2", "Pay3", "Test3", "Pay4", "Test4", "Pay5",
            "Test5", "Pay6", "Test6", "Pay7", "Test7", "Pay8", "Test8", "Price1", "Price2", "Price3", "Price4",
            "Price5",
            "Price6", "Price7", "Price8", "Coin1", "Coin2", "Coin3",
            "Coin4", "Coin5", "Coin6", "Token", "Total Cash", 'Total Credit', "Error1", "Error2", "Error3", "Error4",
            "Error5", "Error6", "Error7", "Error8", "Error9", "Error10", "Error11")

        # Format Our Columns
        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("Date", anchor=W, width=50)
        my_tree.column("Email", anchor=W, width=50)
        my_tree.column("Print", anchor=W, width=50)
        my_tree.column("Pay1", anchor=W, width=50)
        my_tree.column("Test1", anchor=W, width=50)
        my_tree.column("Pay2", anchor=W, width=50)
        my_tree.column("Test2", anchor=W, width=50)
        my_tree.column("Pay3", anchor=W, width=50)
        my_tree.column("Test3", anchor=W, width=50)
        my_tree.column("Pay4", anchor=W, width=50)
        my_tree.column("Test4", anchor=W, width=50)
        my_tree.column("Pay5", anchor=W, width=50)
        my_tree.column("Test5", anchor=W, width=50)
        my_tree.column("Pay6", anchor=W, width=50)
        my_tree.column("Test6", anchor=W, width=50)
        my_tree.column("Pay7", anchor=W, width=50)
        my_tree.column("Test7", anchor=W, width=50)
        my_tree.column("Pay8", anchor=W, width=50)
        my_tree.column("Test8", anchor=W, width=50)
        my_tree.column("Price1", anchor=W, width=50)
        my_tree.column("Price2", anchor=W, width=50)
        my_tree.column("Price3", anchor=W, width=50)
        my_tree.column("Price4", anchor=W, width=50)
        my_tree.column("Price5", anchor=W, width=50)
        my_tree.column("Price6", anchor=W, width=50)
        my_tree.column("Price7", anchor=W, width=50)
        my_tree.column("Price8", anchor=W, width=50)
        my_tree.column("Coin1", anchor=W, width=50)
        my_tree.column("Coin2", anchor=W, width=50)
        my_tree.column("Coin3", anchor=W, width=50)
        my_tree.column("Coin4", anchor=W, width=50)
        my_tree.column("Coin5", anchor=W, width=50)
        my_tree.column("Coin6", anchor=W, width=50)
        my_tree.column("Token", anchor=W, width=50)
        my_tree.column("Total Cash", anchor=W, width=50)
        my_tree.column("Total Credit", anchor=W, width=50)
        my_tree.column("Error1", anchor=W, width=50)
        my_tree.column("Error2", anchor=W, width=50)
        my_tree.column("Error3", anchor=W, width=50)
        my_tree.column("Error4", anchor=W, width=50)
        my_tree.column("Error5", anchor=W, width=50)
        my_tree.column("Error6", anchor=W, width=50)
        my_tree.column("Error7", anchor=W, width=50)
        my_tree.column("Error8", anchor=W, width=50)
        my_tree.column("Error9", anchor=W, width=50)
        my_tree.column("Error10", anchor=W, width=50)
        my_tree.column("Error11", anchor=W, width=50)

        # Create Headings
        my_tree.heading("#0", text="", anchor=W)
        my_tree.heading("Date", text="Date", anchor=W)
        my_tree.heading("Email", text="Email", anchor=W)
        my_tree.heading("Print", text="Print", anchor=W)
        my_tree.heading("Pay1", text="Pay1", anchor=W)
        my_tree.heading("Test1", text="Test1", anchor=W)
        my_tree.heading("Pay2", text="Pay2", anchor=W)
        my_tree.heading("Test2", text="Test2", anchor=W)
        my_tree.heading("Pay3", text="Pay3", anchor=W)
        my_tree.heading("Test3", text="Test3", anchor=W)
        my_tree.heading("Pay4", text="Pay4", anchor=W)
        my_tree.heading("Test4", text="Test4", anchor=W)
        my_tree.heading("Pay5", text="Pay5", anchor=W)
        my_tree.heading("Test5", text="Test5", anchor=W)
        my_tree.heading("Pay6", text="Pay6", anchor=W)
        my_tree.heading("Test6", text="Test6", anchor=W)
        my_tree.heading("Pay7", text="Pay7", anchor=W)
        my_tree.heading("Test7", text="Test7", anchor=W)
        my_tree.heading("Pay8", text="Pay8", anchor=W)
        my_tree.heading("Test8", text="Test8", anchor=W)
        my_tree.heading("Price1", text="Price1", anchor=W)
        my_tree.heading("Price2", text="Price2", anchor=W)
        my_tree.heading("Price3", text="Price3", anchor=W)
        my_tree.heading("Price4", text="Price4", anchor=W)
        my_tree.heading("Price5", text="Price5", anchor=W)
        my_tree.heading("Price6", text="Price6", anchor=W)
        my_tree.heading("Price7", text="Price7", anchor=W)
        my_tree.heading("Price8", text="Price8", anchor=W)
        my_tree.heading("Coin1", text="Coin1", anchor=W)
        my_tree.heading("Coin2", text="Coin2", anchor=W)
        my_tree.heading("Coin3", text="Coin3", anchor=W)
        my_tree.heading("Coin4", text="Coin4", anchor=W)
        my_tree.heading("Coin5", text="Coin5", anchor=W)
        my_tree.heading("Coin6", text="Coin6", anchor=W)
        my_tree.heading("Token", text="Token", anchor=W)
        my_tree.heading("Total Cash", text="Total Cash", anchor=W)
        my_tree.heading("Total Credit", text="Total Credit", anchor=W)
        my_tree.heading("Error1", text="Error1", anchor=W)
        my_tree.heading("Error2", text="Error2", anchor=W)
        my_tree.heading("Error3", text="Error3", anchor=W)
        my_tree.heading("Error4", text="Error4", anchor=W)
        my_tree.heading("Error5", text="Error5", anchor=W)
        my_tree.heading("Error6", text="Error6", anchor=W)
        my_tree.heading("Error7", text="Error7", anchor=W)
        my_tree.heading("Error8", text="Error8", anchor=W)
        my_tree.heading("Error9", text="Error9", anchor=W)
        my_tree.heading("Error10", text="Error10", anchor=W)
        my_tree.heading("Error11", text="Error11", anchor=W)

    elif name == 'VeneziaLX':
        my_tree['columns'] = (
            "Date", "Email", "Print", "Pay1", "Test1", "Pay2", "Test2", "Pay3", "Test3", "Pay4", "Test4", "Pay5",
            "Test5", "Pay6", "Test6", "Pay7", "Test7", "Pay8", "Test8", "Pay9", "Test9", "Pay10", "Test10",
            "Price1", "Price2", "Price3", "Price4", "Price5", "Price6", "Price7", "Price8", "Coin1", "Coin2", "Coin3",
            "Coin4", "Coin5", "Coin6", "Token", "Total Cash", 'Total Credit', "Error1", "Error2", "Error3", "Error4",
            "Error5", "Error6", "Error7", "Error8", "Error9", "Error10", "Error11")

        # Format Our Columns
        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("Date", anchor=W, width=50)
        my_tree.column("Email", anchor=W, width=50)
        my_tree.column("Print", anchor=W, width=50)
        my_tree.column("Pay1", anchor=W, width=50)
        my_tree.column("Test1", anchor=W, width=50)
        my_tree.column("Pay2", anchor=W, width=50)
        my_tree.column("Test2", anchor=W, width=50)
        my_tree.column("Pay3", anchor=W, width=50)
        my_tree.column("Test3", anchor=W, width=50)
        my_tree.column("Pay4", anchor=W, width=50)
        my_tree.column("Test4", anchor=W, width=50)
        my_tree.column("Pay5", anchor=W, width=50)
        my_tree.column("Test5", anchor=W, width=50)
        my_tree.column("Pay6", anchor=W, width=50)
        my_tree.column("Test6", anchor=W, width=50)
        my_tree.column("Pay7", anchor=W, width=50)
        my_tree.column("Test7", anchor=W, width=50)
        my_tree.column("Pay8", anchor=W, width=50)
        my_tree.column("Test8", anchor=W, width=50)
        my_tree.column("Pay9", anchor=W, width=50)
        my_tree.column("Test9", anchor=W, width=50)
        my_tree.column("Pay10", anchor=W, width=50)
        my_tree.column("Test10", anchor=W, width=50)
        my_tree.column("Price1", anchor=W, width=50)
        my_tree.column("Price2", anchor=W, width=50)
        my_tree.column("Price3", anchor=W, width=50)
        my_tree.column("Price4", anchor=W, width=50)
        my_tree.column("Price5", anchor=W, width=50)
        my_tree.column("Price6", anchor=W, width=50)
        my_tree.column("Price7", anchor=W, width=50)
        my_tree.column("Price8", anchor=W, width=50)
        my_tree.column("Coin1", anchor=W, width=50)
        my_tree.column("Coin2", anchor=W, width=50)
        my_tree.column("Coin3", anchor=W, width=50)
        my_tree.column("Coin4", anchor=W, width=50)
        my_tree.column("Coin5", anchor=W, width=50)
        my_tree.column("Coin6", anchor=W, width=50)
        my_tree.column("Token", anchor=W, width=50)
        my_tree.column("Total Cash", anchor=W, width=50)
        my_tree.column("Total Credit", anchor=W, width=50)
        my_tree.column("Error1", anchor=W, width=50)
        my_tree.column("Error2", anchor=W, width=50)
        my_tree.column("Error3", anchor=W, width=50)
        my_tree.column("Error4", anchor=W, width=50)
        my_tree.column("Error5", anchor=W, width=50)
        my_tree.column("Error6", anchor=W, width=50)
        my_tree.column("Error7", anchor=W, width=50)
        my_tree.column("Error8", anchor=W, width=50)
        my_tree.column("Error9", anchor=W, width=50)
        my_tree.column("Error10", anchor=W, width=50)
        my_tree.column("Error11", anchor=W, width=50)

        # Create Headings
        my_tree.heading("#0", text="", anchor=W)
        my_tree.heading("Date", text="Date", anchor=W)
        my_tree.heading("Email", text="Email", anchor=W)
        my_tree.heading("Print", text="Print", anchor=W)
        my_tree.heading("Pay1", text="Pay1", anchor=W)
        my_tree.heading("Test1", text="Test1", anchor=W)
        my_tree.heading("Pay2", text="Pay2", anchor=W)
        my_tree.heading("Test2", text="Test2", anchor=W)
        my_tree.heading("Pay3", text="Pay3", anchor=W)
        my_tree.heading("Test3", text="Test3", anchor=W)
        my_tree.heading("Pay4", text="Pay4", anchor=W)
        my_tree.heading("Test4", text="Test4", anchor=W)
        my_tree.heading("Pay5", text="Pay5", anchor=W)
        my_tree.heading("Test5", text="Test5", anchor=W)
        my_tree.heading("Pay6", text="Pay6", anchor=W)
        my_tree.heading("Test6", text="Test6", anchor=W)
        my_tree.heading("Pay7", text="Pay7", anchor=W)
        my_tree.heading("Test7", text="Test7", anchor=W)
        my_tree.heading("Pay8", text="Pay8", anchor=W)
        my_tree.heading("Test8", text="Test8", anchor=W)
        my_tree.heading("Pay9", text="Pay9", anchor=W)
        my_tree.heading("Test9", text="Test9", anchor=W)
        my_tree.heading("Pay10", text="Pay10", anchor=W)
        my_tree.heading("Test10", text="Test10", anchor=W)
        my_tree.heading("Price1", text="Price1", anchor=W)
        my_tree.heading("Price2", text="Price2", anchor=W)
        my_tree.heading("Price3", text="Price3", anchor=W)
        my_tree.heading("Price4", text="Price4", anchor=W)
        my_tree.heading("Price5", text="Price5", anchor=W)
        my_tree.heading("Price6", text="Price6", anchor=W)
        my_tree.heading("Price7", text="Price7", anchor=W)
        my_tree.heading("Price8", text="Price8", anchor=W)
        my_tree.heading("Coin1", text="Coin1", anchor=W)
        my_tree.heading("Coin2", text="Coin2", anchor=W)
        my_tree.heading("Coin3", text="Coin3", anchor=W)
        my_tree.heading("Coin4", text="Coin4", anchor=W)
        my_tree.heading("Coin5", text="Coin5", anchor=W)
        my_tree.heading("Coin6", text="Coin6", anchor=W)
        my_tree.heading("Token", text="Token", anchor=W)
        my_tree.heading("Total Cash", text="Total Cash", anchor=W)
        my_tree.heading("Total Credit", text="Total Credit", anchor=W)
        my_tree.heading("Error1", text="Error1", anchor=W)
        my_tree.heading("Error2", text="Error2", anchor=W)
        my_tree.heading("Error3", text="Error3", anchor=W)
        my_tree.heading("Error4", text="Error4", anchor=W)
        my_tree.heading("Error5", text="Error5", anchor=W)
        my_tree.heading("Error6", text="Error6", anchor=W)
        my_tree.heading("Error7", text="Error7", anchor=W)
        my_tree.heading("Error8", text="Error8", anchor=W)
        my_tree.heading("Error9", text="Error9", anchor=W)
        my_tree.heading("Error10", text="Error10", anchor=W)
        my_tree.heading("Error11", text="Error11", anchor=W)
    elif name == 'Colibri':
        my_tree['columns'] = (
            "Date", "Email", "Print",
            "Pay1", "Test1", "Pay2", "Test2", "Pay3", "Test3", "Pay4", "Test4",
            "Pay5", "Test5", "Pay6", "Test6", "Pay7", "Test7", "Pay8", "Test8",
            "Price1", "Price2", "Price3", "Price4", "Price5", "Price6", "Price7", "Price8",
            "Coin1", "Coin2", "Coin3", "Coin4", "Coin5", "Coin6",
            "Total Cash", 'Total Credit',
            "Error1", "Error2", "Error3", "Error4",
            "Error5", "Error6", "Error7", "Error8",
            "Error9", "Error10", "Error11", "Error12", "Error13")

        # Format Our Columns
        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("Date", anchor=W, width=50)
        my_tree.column("Email", anchor=W, width=50)
        my_tree.column("Print", anchor=W, width=50)
        my_tree.column("Pay1", anchor=W, width=50)
        my_tree.column("Test1", anchor=W, width=50)
        my_tree.column("Pay2", anchor=W, width=50)
        my_tree.column("Test2", anchor=W, width=50)
        my_tree.column("Pay3", anchor=W, width=50)
        my_tree.column("Test3", anchor=W, width=50)
        my_tree.column("Pay4", anchor=W, width=50)
        my_tree.column("Test4", anchor=W, width=50)
        my_tree.column("Pay5", anchor=W, width=50)
        my_tree.column("Test5", anchor=W, width=50)
        my_tree.column("Pay6", anchor=W, width=50)
        my_tree.column("Test6", anchor=W, width=50)
        my_tree.column("Pay7", anchor=W, width=50)
        my_tree.column("Test7", anchor=W, width=50)
        my_tree.column("Pay8", anchor=W, width=50)
        my_tree.column("Test8", anchor=W, width=50)
        my_tree.column("Price1", anchor=W, width=50)
        my_tree.column("Price2", anchor=W, width=50)
        my_tree.column("Price3", anchor=W, width=50)
        my_tree.column("Price4", anchor=W, width=50)
        my_tree.column("Price5", anchor=W, width=50)
        my_tree.column("Price6", anchor=W, width=50)
        my_tree.column("Price7", anchor=W, width=50)
        my_tree.column("Price8", anchor=W, width=50)
        my_tree.column("Coin1", anchor=W, width=50)
        my_tree.column("Coin2", anchor=W, width=50)
        my_tree.column("Coin3", anchor=W, width=50)
        my_tree.column("Coin4", anchor=W, width=50)
        my_tree.column("Coin5", anchor=W, width=50)
        my_tree.column("Coin6", anchor=W, width=50)
        my_tree.column("Total Cash", anchor=W, width=50)
        my_tree.column("Total Credit", anchor=W, width=50)
        my_tree.column("Error1", anchor=W, width=50)
        my_tree.column("Error2", anchor=W, width=50)
        my_tree.column("Error3", anchor=W, width=50)
        my_tree.column("Error4", anchor=W, width=50)
        my_tree.column("Error5", anchor=W, width=50)
        my_tree.column("Error6", anchor=W, width=50)
        my_tree.column("Error7", anchor=W, width=50)
        my_tree.column("Error8", anchor=W, width=50)
        my_tree.column("Error9", anchor=W, width=50)
        my_tree.column("Error10", anchor=W, width=50)
        my_tree.column("Error11", anchor=W, width=50)
        my_tree.column("Error12", anchor=W, width=50)
        my_tree.column("Error13", anchor=W, width=50)

        # Create Headings
        my_tree.heading("#0", text="", anchor=W)
        my_tree.heading("Date", text="Date", anchor=W)
        my_tree.heading("Email", text="Email", anchor=W)
        my_tree.heading("Print", text="Print", anchor=W)
        my_tree.heading("Pay1", text="Pay1", anchor=W)
        my_tree.heading("Test1", text="Test1", anchor=W)
        my_tree.heading("Pay2", text="Pay2", anchor=W)
        my_tree.heading("Test2", text="Test2", anchor=W)
        my_tree.heading("Pay3", text="Pay3", anchor=W)
        my_tree.heading("Test3", text="Test3", anchor=W)
        my_tree.heading("Pay4", text="Pay4", anchor=W)
        my_tree.heading("Test4", text="Test4", anchor=W)
        my_tree.heading("Pay5", text="Pay5", anchor=W)
        my_tree.heading("Test5", text="Test5", anchor=W)
        my_tree.heading("Pay6", text="Pay6", anchor=W)
        my_tree.heading("Test6", text="Test6", anchor=W)
        my_tree.heading("Pay7", text="Pay7", anchor=W)
        my_tree.heading("Test7", text="Test7", anchor=W)
        my_tree.heading("Pay8", text="Pay8", anchor=W)
        my_tree.heading("Test8", text="Test8", anchor=W)
        my_tree.heading("Price1", text="Price1", anchor=W)
        my_tree.heading("Price2", text="Price2", anchor=W)
        my_tree.heading("Price3", text="Price3", anchor=W)
        my_tree.heading("Price4", text="Price4", anchor=W)
        my_tree.heading("Price5", text="Price5", anchor=W)
        my_tree.heading("Price6", text="Price6", anchor=W)
        my_tree.heading("Price7", text="Price7", anchor=W)
        my_tree.heading("Price8", text="Price8", anchor=W)
        my_tree.heading("Coin1", text="Coin1", anchor=W)
        my_tree.heading("Coin2", text="Coin2", anchor=W)
        my_tree.heading("Coin3", text="Coin3", anchor=W)
        my_tree.heading("Coin4", text="Coin4", anchor=W)
        my_tree.heading("Coin5", text="Coin5", anchor=W)
        my_tree.heading("Coin6", text="Coin6", anchor=W)
        my_tree.heading("Total Cash", text="Total Cash", anchor=W)
        my_tree.heading("Total Credit", text="Total Credit", anchor=W)
        my_tree.heading("Error1", text="Error1", anchor=W)
        my_tree.heading("Error2", text="Error2", anchor=W)
        my_tree.heading("Error3", text="Error3", anchor=W)
        my_tree.heading("Error4", text="Error4", anchor=W)
        my_tree.heading("Error5", text="Error5", anchor=W)
        my_tree.heading("Error6", text="Error6", anchor=W)
        my_tree.heading("Error7", text="Error7", anchor=W)
        my_tree.heading("Error8", text="Error8", anchor=W)
        my_tree.heading("Error9", text="Error9", anchor=W)
        my_tree.heading("Error10", text="Error10", anchor=W)
        my_tree.heading("Error11", text="Error11", anchor=W)
        my_tree.heading("Error12", text="Error12", anchor=W)
        my_tree.heading("Error13", text="Error13", anchor=W)

    elif name == 'Colibri(1e)':
        my_tree['columns'] = (
            "Date", "Email", "Print",
            "Pay1", "Test1", "Pay2", "Test2", "Pay3", "Test3", "Pay4", "Test4",
            "Pay5", "Test5", "Pay6", "Test6", "Pay7", "Test7", "Pay8", "Test8",
            "Price1", "Price2", "Price3", "Price4", "Price5", "Price6", "Price7", "Price8",
            "Coin1", "Coin2", "Coin3", "Coin4", "Coin5", "Coin6",
            "Total Cash", 'Total Credit',
            "Error1", "Error2", "Error3", "Error4",
            "Error5", "Error6", "Error7", "Error8",
            "Error9", "Error10", "Error11", "Error12", "Error13", "Error14")
        # Format Our Columns
        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("Date", anchor=W, width=50)
        my_tree.column("Email", anchor=W, width=50)
        my_tree.column("Print", anchor=W, width=50)
        my_tree.column("Pay1", anchor=W, width=50)
        my_tree.column("Test1", anchor=W, width=50)
        my_tree.column("Pay2", anchor=W, width=50)
        my_tree.column("Test2", anchor=W, width=50)
        my_tree.column("Pay3", anchor=W, width=50)
        my_tree.column("Test3", anchor=W, width=50)
        my_tree.column("Pay4", anchor=W, width=50)
        my_tree.column("Test4", anchor=W, width=50)
        my_tree.column("Pay5", anchor=W, width=50)
        my_tree.column("Test5", anchor=W, width=50)
        my_tree.column("Pay6", anchor=W, width=50)
        my_tree.column("Test6", anchor=W, width=50)
        my_tree.column("Pay7", anchor=W, width=50)
        my_tree.column("Test7", anchor=W, width=50)
        my_tree.column("Pay8", anchor=W, width=50)
        my_tree.column("Test8", anchor=W, width=50)
        my_tree.column("Price1", anchor=W, width=50)
        my_tree.column("Price2", anchor=W, width=50)
        my_tree.column("Price3", anchor=W, width=50)
        my_tree.column("Price4", anchor=W, width=50)
        my_tree.column("Price5", anchor=W, width=50)
        my_tree.column("Price6", anchor=W, width=50)
        my_tree.column("Price7", anchor=W, width=50)
        my_tree.column("Price8", anchor=W, width=50)
        my_tree.column("Coin1", anchor=W, width=50)
        my_tree.column("Coin2", anchor=W, width=50)
        my_tree.column("Coin3", anchor=W, width=50)
        my_tree.column("Coin4", anchor=W, width=50)
        my_tree.column("Coin5", anchor=W, width=50)
        my_tree.column("Coin6", anchor=W, width=50)
        my_tree.column("Total Cash", anchor=W, width=50)
        my_tree.column("Total Credit", anchor=W, width=50)
        my_tree.column("Error1", anchor=W, width=50)
        my_tree.column("Error2", anchor=W, width=50)
        my_tree.column("Error3", anchor=W, width=50)
        my_tree.column("Error4", anchor=W, width=50)
        my_tree.column("Error5", anchor=W, width=50)
        my_tree.column("Error6", anchor=W, width=50)
        my_tree.column("Error7", anchor=W, width=50)
        my_tree.column("Error8", anchor=W, width=50)
        my_tree.column("Error9", anchor=W, width=50)
        my_tree.column("Error10", anchor=W, width=50)
        my_tree.column("Error11", anchor=W, width=50)
        my_tree.column("Error12", anchor=W, width=50)
        my_tree.column("Error13", anchor=W, width=50)
        my_tree.column("Error14", anchor=W, width=50)

        # Create Headings
        my_tree.heading("#0", text="", anchor=W)
        my_tree.heading("Date", text="Date", anchor=W)
        my_tree.heading("Email", text="Email", anchor=W)
        my_tree.heading("Print", text="Print", anchor=W)
        my_tree.heading("Pay1", text="Pay1", anchor=W)
        my_tree.heading("Test1", text="Test1", anchor=W)
        my_tree.heading("Pay2", text="Pay2", anchor=W)
        my_tree.heading("Test2", text="Test2", anchor=W)
        my_tree.heading("Pay3", text="Pay3", anchor=W)
        my_tree.heading("Test3", text="Test3", anchor=W)
        my_tree.heading("Pay4", text="Pay4", anchor=W)
        my_tree.heading("Test4", text="Test4", anchor=W)
        my_tree.heading("Pay5", text="Pay5", anchor=W)
        my_tree.heading("Test5", text="Test5", anchor=W)
        my_tree.heading("Pay6", text="Pay6", anchor=W)
        my_tree.heading("Test6", text="Test6", anchor=W)
        my_tree.heading("Pay7", text="Pay7", anchor=W)
        my_tree.heading("Test7", text="Test7", anchor=W)
        my_tree.heading("Pay8", text="Pay8", anchor=W)
        my_tree.heading("Test8", text="Test8", anchor=W)
        my_tree.heading("Price1", text="Price1", anchor=W)
        my_tree.heading("Price2", text="Price2", anchor=W)
        my_tree.heading("Price3", text="Price3", anchor=W)
        my_tree.heading("Price4", text="Price4", anchor=W)
        my_tree.heading("Price5", text="Price5", anchor=W)
        my_tree.heading("Price6", text="Price6", anchor=W)
        my_tree.heading("Price7", text="Price7", anchor=W)
        my_tree.heading("Price8", text="Price8", anchor=W)
        my_tree.heading("Coin1", text="Coin1", anchor=W)
        my_tree.heading("Coin2", text="Coin2", anchor=W)
        my_tree.heading("Coin3", text="Coin3", anchor=W)
        my_tree.heading("Coin4", text="Coin4", anchor=W)
        my_tree.heading("Coin5", text="Coin5", anchor=W)
        my_tree.heading("Coin6", text="Coin6", anchor=W)
        my_tree.heading("Total Cash", text="Total Cash", anchor=W)
        my_tree.heading("Total Credit", text="Total Credit", anchor=W)
        my_tree.heading("Error1", text="Error1", anchor=W)
        my_tree.heading("Error2", text="Error2", anchor=W)
        my_tree.heading("Error3", text="Error3", anchor=W)
        my_tree.heading("Error4", text="Error4", anchor=W)
        my_tree.heading("Error5", text="Error5", anchor=W)
        my_tree.heading("Error6", text="Error6", anchor=W)
        my_tree.heading("Error7", text="Error7", anchor=W)
        my_tree.heading("Error8", text="Error8", anchor=W)
        my_tree.heading("Error9", text="Error9", anchor=W)
        my_tree.heading("Error10", text="Error10", anchor=W)
        my_tree.heading("Error11", text="Error11", anchor=W)
        my_tree.heading("Error12", text="Error12", anchor=W)
        my_tree.heading("Error13", text="Error13", anchor=W)
        my_tree.heading("Error14", text="Error14", anchor=W)

    elif name == 'Canto':
        my_tree['columns'] = (
        "Date", "Email", "Print", "Sold", "Tested",
        "Pay2", "Pay3", "Pay4", "Pay5", "Pay6", "Pay7", "Pay8", "Pay9", "Pay10",
        "Pay12", "Pay13", "Pay14", "Pay15", "Pay16", "Pay17", "Pay18", "Pay19", "Pay20",
        "Pay21", "Pay22", "Pay23", "Pay24", "Pay25", "Pay26", "Pay27", "Pay29", "Pay30",
        "Pay31", "Pay32", "Pay33", "Pay34", "Pay35", "Pay36", "Pay37", "Pay38", "Pay39", "Pay40",
        "Price1", "Price2", "Price3", "Price4", "Price5",
        "Coin1", "Coin2", "Coin3", "Coin4", "Coin5", "Coin6",
        "Total Cash", 'Total Credit',
        "Error1", "Error2", "Error3", "Error4", "Error5", "Error6", "Error7", "Error8", "Error9", "Error10",
        "Error11", "Error12", "Error13", "Error14", "Error15", "Error16", "Error17", "Error18", "Error19", "Error20",
        "Error21", "Error22", "Error23", "Error24", "Error25", "Error26", "Error27", "Error28", "Error29", "Error30",
        "Error31", "Error32", "Error33", "Error34", "Error35", "Error36", "Error37", "Error38", "Error39", "Error40",
        "Error41", "Error42", "Error43", "Error44", "Error45", "Error46", "Error47", "Error48", "Error49", "Error50",
        "Error51", "Error52", "Error53", "Error54", "Error55", "Error56", "Error57", "Error58", "Error59", "Error60",
        "Error61", "Error62", "Error63", "Error64", "Error65", "Error66")

        # Format Our Columns
        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("Date", anchor=W, width=50)
        my_tree.column("Email", anchor=W, width=50)
        my_tree.column("Print", anchor=W, width=50)
        my_tree.column("Sold", anchor=W, width=50)
        my_tree.column("Tested", anchor=W, width=50)
        my_tree.column("Pay2", anchor=W, width=50)
        my_tree.column("Pay3", anchor=W, width=50)
        my_tree.column("Pay4", anchor=W, width=50)
        my_tree.column("Pay5", anchor=W, width=50)
        my_tree.column("Pay6", anchor=W, width=50)
        my_tree.column("Pay7", anchor=W, width=50)
        my_tree.column("Pay8", anchor=W, width=50)
        my_tree.column("Pay9", anchor=W, width=50)
        my_tree.column("Pay10", anchor=W, width=50)
        my_tree.column("Pay12", anchor=W, width=50)
        my_tree.column("Pay13", anchor=W, width=50)
        my_tree.column("Pay14", anchor=W, width=50)
        my_tree.column("Pay15", anchor=W, width=50)
        my_tree.column("Pay16", anchor=W, width=50)
        my_tree.column("Pay17", anchor=W, width=50)
        my_tree.column("Pay18", anchor=W, width=50)
        my_tree.column("Pay19", anchor=W, width=50)
        my_tree.column("Pay20", anchor=W, width=50)
        my_tree.column("Pay21", anchor=W, width=50)
        my_tree.column("Pay22", anchor=W, width=50)
        my_tree.column("Pay23", anchor=W, width=50)
        my_tree.column("Pay24", anchor=W, width=50)
        my_tree.column("Pay25", anchor=W, width=50)
        my_tree.column("Pay26", anchor=W, width=50)
        my_tree.column("Pay27", anchor=W, width=50)
        my_tree.column("Pay29", anchor=W, width=50)
        my_tree.column("Pay30", anchor=W, width=50)
        my_tree.column("Pay31", anchor=W, width=50)
        my_tree.column("Pay32", anchor=W, width=50)
        my_tree.column("Pay33", anchor=W, width=50)
        my_tree.column("Pay34", anchor=W, width=50)
        my_tree.column("Pay35", anchor=W, width=50)
        my_tree.column("Pay36", anchor=W, width=50)
        my_tree.column("Pay37", anchor=W, width=50)
        my_tree.column("Pay38", anchor=W, width=50)
        my_tree.column("Pay39", anchor=W, width=50)
        my_tree.column("Pay40", anchor=W, width=50)
        my_tree.column("Price1", anchor=W, width=50)
        my_tree.column("Price2", anchor=W, width=50)
        my_tree.column("Price3", anchor=W, width=50)
        my_tree.column("Price4", anchor=W, width=50)
        my_tree.column("Price5", anchor=W, width=50)
        my_tree.column("Coin1", anchor=W, width=50)
        my_tree.column("Coin2", anchor=W, width=50)
        my_tree.column("Coin3", anchor=W, width=50)
        my_tree.column("Coin4", anchor=W, width=50)
        my_tree.column("Coin5", anchor=W, width=50)
        my_tree.column("Coin6", anchor=W, width=50)
        my_tree.column("Total Cash", anchor=W, width=50)
        my_tree.column("Total Credit", anchor=W, width=50)
        my_tree.column("Error1", anchor=W, width=50)
        my_tree.column("Error2", anchor=W, width=50)
        my_tree.column("Error3", anchor=W, width=50)
        my_tree.column("Error4", anchor=W, width=50)
        my_tree.column("Error5", anchor=W, width=50)
        my_tree.column("Error6", anchor=W, width=50)
        my_tree.column("Error7", anchor=W, width=50)
        my_tree.column("Error8", anchor=W, width=50)
        my_tree.column("Error9", anchor=W, width=50)
        my_tree.column("Error10", anchor=W, width=50)
        my_tree.column("Error11", anchor=W, width=50)
        my_tree.column("Error12", anchor=W, width=50)
        my_tree.column("Error13", anchor=W, width=50)
        my_tree.column("Error14", anchor=W, width=50)
        my_tree.column("Error15", anchor=W, width=50)
        my_tree.column("Error16", anchor=W, width=50)
        my_tree.column("Error17", anchor=W, width=50)
        my_tree.column("Error18", anchor=W, width=50)
        my_tree.column("Error19", anchor=W, width=50)
        my_tree.column("Error20", anchor=W, width=50)
        my_tree.column("Error21", anchor=W, width=50)
        my_tree.column("Error22", anchor=W, width=50)
        my_tree.column("Error23", anchor=W, width=50)
        my_tree.column("Error24", anchor=W, width=50)
        my_tree.column("Error25", anchor=W, width=50)
        my_tree.column("Error26", anchor=W, width=50)
        my_tree.column("Error27", anchor=W, width=50)
        my_tree.column("Error28", anchor=W, width=50)
        my_tree.column("Error29", anchor=W, width=50)
        my_tree.column("Error30", anchor=W, width=50)
        my_tree.column("Error31", anchor=W, width=50)
        my_tree.column("Error32", anchor=W, width=50)
        my_tree.column("Error33", anchor=W, width=50)
        my_tree.column("Error34", anchor=W, width=50)
        my_tree.column("Error35", anchor=W, width=50)
        my_tree.column("Error36", anchor=W, width=50)
        my_tree.column("Error37", anchor=W, width=50)
        my_tree.column("Error38", anchor=W, width=50)
        my_tree.column("Error39", anchor=W, width=50)
        my_tree.column("Error40", anchor=W, width=50)
        my_tree.column("Error41", anchor=W, width=50)
        my_tree.column("Error42", anchor=W, width=50)
        my_tree.column("Error43", anchor=W, width=50)
        my_tree.column("Error44", anchor=W, width=50)
        my_tree.column("Error45", anchor=W, width=50)
        my_tree.column("Error46", anchor=W, width=50)
        my_tree.column("Error47", anchor=W, width=50)
        my_tree.column("Error48", anchor=W, width=50)
        my_tree.column("Error49", anchor=W, width=50)
        my_tree.column("Error50", anchor=W, width=50)
        my_tree.column("Error51", anchor=W, width=50)
        my_tree.column("Error52", anchor=W, width=50)
        my_tree.column("Error53", anchor=W, width=50)
        my_tree.column("Error54", anchor=W, width=50)
        my_tree.column("Error55", anchor=W, width=50)
        my_tree.column("Error56", anchor=W, width=50)
        my_tree.column("Error57", anchor=W, width=50)
        my_tree.column("Error58", anchor=W, width=50)
        my_tree.column("Error59", anchor=W, width=50)
        my_tree.column("Error60", anchor=W, width=50)
        my_tree.column("Error61", anchor=W, width=50)
        my_tree.column("Error62", anchor=W, width=50)
        my_tree.column("Error63", anchor=W, width=50)
        my_tree.column("Error64", anchor=W, width=50)
        my_tree.column("Error65", anchor=W, width=50)
        my_tree.column("Error66", anchor=W, width=50)

        # Create Headings
        my_tree.heading("#0", text="", anchor=W)
        my_tree.heading("Date", text="Date", anchor=W)
        my_tree.heading("Email", text="Email", anchor=W)
        my_tree.heading("Print", text="Print", anchor=W)
        my_tree.heading("Sold", text="Sold", anchor=W)
        my_tree.heading("Tested", text="Tested", anchor=W)
        my_tree.heading("Pay2", text="Pay2", anchor=W)
        my_tree.heading("Pay3", text="Pay3", anchor=W)
        my_tree.heading("Pay4", text="Pay4", anchor=W)
        my_tree.heading("Pay5", text="Pay5", anchor=W)
        my_tree.heading("Pay6", text="Pay6", anchor=W)
        my_tree.heading("Pay7", text="Pay7", anchor=W)
        my_tree.heading("Pay8", text="Pay8", anchor=W)
        my_tree.heading("Pay9", text="Pay9", anchor=W)
        my_tree.heading("Pay10", text="Pay10", anchor=W)
        my_tree.heading("Pay12", text="Pay12", anchor=W)
        my_tree.heading("Pay13", text="Pay13", anchor=W)
        my_tree.heading("Pay14", text="Pay14", anchor=W)
        my_tree.heading("Pay15", text="Pay15", anchor=W)
        my_tree.heading("Pay16", text="Pay16", anchor=W)
        my_tree.heading("Pay17", text="Pay17", anchor=W)
        my_tree.heading("Pay18", text="Pay18", anchor=W)
        my_tree.heading("Pay19", text="Pay19", anchor=W)
        my_tree.heading("Pay20", text="Pay20", anchor=W)
        my_tree.heading("Pay21", text="Pay21", anchor=W)
        my_tree.heading("Pay22", text="Pay22", anchor=W)
        my_tree.heading("Pay23", text="Pay23", anchor=W)
        my_tree.heading("Pay24", text="Pay24", anchor=W)
        my_tree.heading("Pay25", text="Pay25", anchor=W)
        my_tree.heading("Pay26", text="Pay26", anchor=W)
        my_tree.heading("Pay27", text="Pay27", anchor=W)
        my_tree.heading("Pay29", text="Pay29", anchor=W)
        my_tree.heading("Pay30", text="Pay30", anchor=W)
        my_tree.heading("Pay31", text="Pay31", anchor=W)
        my_tree.heading("Pay32", text="Pay32", anchor=W)
        my_tree.heading("Pay33", text="Pay33", anchor=W)
        my_tree.heading("Pay34", text="Pay34", anchor=W)
        my_tree.heading("Pay35", text="Pay35", anchor=W)
        my_tree.heading("Pay36", text="Pay36", anchor=W)
        my_tree.heading("Pay37", text="Pay37", anchor=W)
        my_tree.heading("Pay38", text="Pay38", anchor=W)
        my_tree.heading("Pay39", text="Pay39", anchor=W)
        my_tree.heading("Pay40", text="Pay40", anchor=W)
        my_tree.heading("Price1", text="Price1", anchor=W)
        my_tree.heading("Price2", text="Price2", anchor=W)
        my_tree.heading("Price3", text="Price3", anchor=W)
        my_tree.heading("Price4", text="Price4", anchor=W)
        my_tree.heading("Price5", text="Price5", anchor=W)
        my_tree.heading("Coin1", text="Coin1", anchor=W)
        my_tree.heading("Coin2", text="Coin2", anchor=W)
        my_tree.heading("Coin3", text="Coin3", anchor=W)
        my_tree.heading("Coin4", text="Coin4", anchor=W)
        my_tree.heading("Coin5", text="Coin5", anchor=W)
        my_tree.heading("Coin6", text="Coin6", anchor=W)
        my_tree.heading("Total Cash", text="Total Cash", anchor=W)
        my_tree.heading("Total Credit", text="Total Credit", anchor=W)
        my_tree.heading("Error1", text="Error1", anchor=W)
        my_tree.heading("Error2", text="Error2", anchor=W)
        my_tree.heading("Error3", text="Error3", anchor=W)
        my_tree.heading("Error4", text="Error4", anchor=W)
        my_tree.heading("Error5", text="Error5", anchor=W)
        my_tree.heading("Error6", text="Error6", anchor=W)
        my_tree.heading("Error7", text="Error7", anchor=W)
        my_tree.heading("Error8", text="Error8", anchor=W)
        my_tree.heading("Error9", text="Error9", anchor=W)
        my_tree.heading("Error10", text="Error10", anchor=W)
        my_tree.heading("Error11", text="Error11", anchor=W)
        my_tree.heading("Error12", text="Error12", anchor=W)
        my_tree.heading("Error13", text="Error13", anchor=W)
        my_tree.heading("Error14", text="Error14", anchor=W)
        my_tree.heading("Error15", text="Error15", anchor=W)
        my_tree.heading("Error16", text="Error16", anchor=W)
        my_tree.heading("Error17", text="Error17", anchor=W)
        my_tree.heading("Error18", text="Error18", anchor=W)
        my_tree.heading("Error19", text="Error19", anchor=W)
        my_tree.heading("Error20", text="Error20", anchor=W)
        my_tree.heading("Error21", text="Error21", anchor=W)
        my_tree.heading("Error22", text="Error22", anchor=W)
        my_tree.heading("Error23", text="Error23", anchor=W)
        my_tree.heading("Error24", text="Error24", anchor=W)
        my_tree.heading("Error25", text="Error25", anchor=W)
        my_tree.heading("Error26", text="Error26", anchor=W)
        my_tree.heading("Error27", text="Error27", anchor=W)
        my_tree.heading("Error28", text="Error28", anchor=W)
        my_tree.heading("Error29", text="Error29", anchor=W)
        my_tree.heading("Error30", text="Error30", anchor=W)
        my_tree.heading("Error31", text="Error31", anchor=W)
        my_tree.heading("Error32", text="Error32", anchor=W)
        my_tree.heading("Error33", text="Error33", anchor=W)
        my_tree.heading("Error34", text="Error34", anchor=W)
        my_tree.heading("Error35", text="Error35", anchor=W)
        my_tree.heading("Error36", text="Error36", anchor=W)
        my_tree.heading("Error37", text="Error37", anchor=W)
        my_tree.heading("Error38", text="Error38", anchor=W)
        my_tree.heading("Error39", text="Error39", anchor=W)
        my_tree.heading("Error40", text="Error40", anchor=W)
        my_tree.heading("Error41", text="Error41", anchor=W)
        my_tree.heading("Error42", text="Error42", anchor=W)
        my_tree.heading("Error43", text="Error43", anchor=W)
        my_tree.heading("Error44", text="Error44", anchor=W)
        my_tree.heading("Error45", text="Error45", anchor=W)
        my_tree.heading("Error46", text="Error46", anchor=W)
        my_tree.heading("Error47", text="Error47", anchor=W)
        my_tree.heading("Error48", text="Error48", anchor=W)
        my_tree.heading("Error49", text="Error49", anchor=W)
        my_tree.heading("Error50", text="Error50", anchor=W)
        my_tree.heading("Error51", text="Error51", anchor=W)
        my_tree.heading("Error52", text="Error52", anchor=W)
        my_tree.heading("Error53", text="Error53", anchor=W)
        my_tree.heading("Error54", text="Error54", anchor=W)
        my_tree.heading("Error55", text="Error55", anchor=W)
        my_tree.heading("Error56", text="Error56", anchor=W)
        my_tree.heading("Error57", text="Error57", anchor=W)
        my_tree.heading("Error58", text="Error58", anchor=W)
        my_tree.heading("Error59", text="Error59", anchor=W)
        my_tree.heading("Error60", text="Error60", anchor=W)
        my_tree.heading("Error61", text="Error61", anchor=W)
        my_tree.heading("Error62", text="Error62", anchor=W)
        my_tree.heading("Error63", text="Error63", anchor=W)
        my_tree.heading("Error64", text="Error64", anchor=W)
        my_tree.heading("Error65", text="Error65", anchor=W)
        my_tree.heading("Error66", text="Error66", anchor=W)
    elif name == 'Astro40(1e)':
        my_tree['columns'] = (
        "Date", "Email", "Print", "Sold", "Tested",
        "Pay1", "Pay2", "Pay3", "Pay4", "Pay5", "Pay6", "Pay7", "Pay8", "Pay9", "Pay10",
        "Pay11", "Pay12", "Pay13", "Pay14", "Pay15", "Pay16", "Pay17", "Pay18",
        "Pay21", "Pay22", "Pay23", "Pay24", "Pay25", "Pay26", "Pay27", "Pay28", "Pay29", "Pay30",
        "Pay31", "Pay32", "Pay33", "Pay34", "Pay35", "Pay36", "Pay37", "Pay38", "Pay39", "Pay40",
        "Coin1", "Coin2", "Coin3", "Coin4", "Coin5", "Coin6",
        "Total Cash", 'Total Credit',
        "Error1", "Error2", "Error3", "Error4", "Error5", "Error6", "Error7", "Error8", "Error9", "Error10",
        "Error11", "Error12", "Error13", "Error14", "Error15", "Error16", "Error17", "Error18", "Error19", "Error20",
        "Error21", "Error22", "Error23", "Error24", "Error25", "Error26", "Error27", "Error28", "Error29")

        # Format Our Columns
        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("Date", anchor=W, width=50)
        my_tree.column("Email", anchor=W, width=50)
        my_tree.column("Print", anchor=W, width=50)
        my_tree.column("Sold", anchor=W, width=50)
        my_tree.column("Tested", anchor=W, width=50)
        my_tree.column("Pay1", anchor=W, width=50)
        my_tree.column("Pay2", anchor=W, width=50)
        my_tree.column("Pay3", anchor=W, width=50)
        my_tree.column("Pay4", anchor=W, width=50)
        my_tree.column("Pay5", anchor=W, width=50)
        my_tree.column("Pay6", anchor=W, width=50)
        my_tree.column("Pay7", anchor=W, width=50)
        my_tree.column("Pay8", anchor=W, width=50)
        my_tree.column("Pay9", anchor=W, width=50)
        my_tree.column("Pay10", anchor=W, width=50)
        my_tree.column("Pay11", anchor=W, width=50)
        my_tree.column("Pay12", anchor=W, width=50)
        my_tree.column("Pay13", anchor=W, width=50)
        my_tree.column("Pay14", anchor=W, width=50)
        my_tree.column("Pay15", anchor=W, width=50)
        my_tree.column("Pay16", anchor=W, width=50)
        my_tree.column("Pay17", anchor=W, width=50)
        my_tree.column("Pay18", anchor=W, width=50)
        my_tree.column("Pay21", anchor=W, width=50)
        my_tree.column("Pay22", anchor=W, width=50)
        my_tree.column("Pay23", anchor=W, width=50)
        my_tree.column("Pay24", anchor=W, width=50)
        my_tree.column("Pay25", anchor=W, width=50)
        my_tree.column("Pay26", anchor=W, width=50)
        my_tree.column("Pay27", anchor=W, width=50)
        my_tree.column("Pay28", anchor=W, width=50)
        my_tree.column("Pay29", anchor=W, width=50)
        my_tree.column("Pay30", anchor=W, width=50)
        my_tree.column("Pay31", anchor=W, width=50)
        my_tree.column("Pay32", anchor=W, width=50)
        my_tree.column("Pay33", anchor=W, width=50)
        my_tree.column("Pay34", anchor=W, width=50)
        my_tree.column("Pay35", anchor=W, width=50)
        my_tree.column("Pay36", anchor=W, width=50)
        my_tree.column("Pay37", anchor=W, width=50)
        my_tree.column("Pay38", anchor=W, width=50)
        my_tree.column("Pay39", anchor=W, width=50)
        my_tree.column("Pay40", anchor=W, width=50)
        my_tree.column("Coin1", anchor=W, width=50)
        my_tree.column("Coin2", anchor=W, width=50)
        my_tree.column("Coin3", anchor=W, width=50)
        my_tree.column("Coin4", anchor=W, width=50)
        my_tree.column("Coin5", anchor=W, width=50)
        my_tree.column("Coin6", anchor=W, width=50)
        my_tree.column("Total Cash", anchor=W, width=50)
        my_tree.column("Total Credit", anchor=W, width=50)
        my_tree.column("Error1", anchor=W, width=50)
        my_tree.column("Error2", anchor=W, width=50)
        my_tree.column("Error3", anchor=W, width=50)
        my_tree.column("Error4", anchor=W, width=50)
        my_tree.column("Error5", anchor=W, width=50)
        my_tree.column("Error6", anchor=W, width=50)
        my_tree.column("Error7", anchor=W, width=50)
        my_tree.column("Error8", anchor=W, width=50)
        my_tree.column("Error9", anchor=W, width=50)
        my_tree.column("Error10", anchor=W, width=50)
        my_tree.column("Error11", anchor=W, width=50)
        my_tree.column("Error12", anchor=W, width=50)
        my_tree.column("Error13", anchor=W, width=50)
        my_tree.column("Error14", anchor=W, width=50)
        my_tree.column("Error15", anchor=W, width=50)
        my_tree.column("Error16", anchor=W, width=50)
        my_tree.column("Error17", anchor=W, width=50)
        my_tree.column("Error18", anchor=W, width=50)
        my_tree.column("Error19", anchor=W, width=50)
        my_tree.column("Error20", anchor=W, width=50)
        my_tree.column("Error21", anchor=W, width=50)
        my_tree.column("Error22", anchor=W, width=50)
        my_tree.column("Error23", anchor=W, width=50)
        my_tree.column("Error24", anchor=W, width=50)
        my_tree.column("Error25", anchor=W, width=50)
        my_tree.column("Error26", anchor=W, width=50)
        my_tree.column("Error27", anchor=W, width=50)
        my_tree.column("Error28", anchor=W, width=50)
        my_tree.column("Error29", anchor=W, width=50)

        # Create Headings
        my_tree.heading("#0", text="", anchor=W)
        my_tree.heading("Date", text="Date", anchor=W)
        my_tree.heading("Email", text="Email", anchor=W)
        my_tree.heading("Print", text="Print", anchor=W)
        my_tree.heading("Sold", text="Sold", anchor=W)
        my_tree.heading("Tested", text="Tested", anchor=W)
        my_tree.heading("Pay1", text="Pay1", anchor=W)
        my_tree.heading("Pay2", text="Pay2", anchor=W)
        my_tree.heading("Pay3", text="Pay3", anchor=W)
        my_tree.heading("Pay4", text="Pay4", anchor=W)
        my_tree.heading("Pay5", text="Pay5", anchor=W)
        my_tree.heading("Pay6", text="Pay6", anchor=W)
        my_tree.heading("Pay7", text="Pay7", anchor=W)
        my_tree.heading("Pay8", text="Pay8", anchor=W)
        my_tree.heading("Pay9", text="Pay9", anchor=W)
        my_tree.heading("Pay10", text="Pay10", anchor=W)
        my_tree.heading("Pay11", text="Pay11", anchor=W)
        my_tree.heading("Pay12", text="Pay12", anchor=W)
        my_tree.heading("Pay13", text="Pay13", anchor=W)
        my_tree.heading("Pay14", text="Pay14", anchor=W)
        my_tree.heading("Pay15", text="Pay15", anchor=W)
        my_tree.heading("Pay16", text="Pay16", anchor=W)
        my_tree.heading("Pay17", text="Pay17", anchor=W)
        my_tree.heading("Pay18", text="Pay18", anchor=W)
        my_tree.heading("Pay21", text="Pay21", anchor=W)
        my_tree.heading("Pay22", text="Pay22", anchor=W)
        my_tree.heading("Pay23", text="Pay23", anchor=W)
        my_tree.heading("Pay24", text="Pay24", anchor=W)
        my_tree.heading("Pay25", text="Pay25", anchor=W)
        my_tree.heading("Pay26", text="Pay26", anchor=W)
        my_tree.heading("Pay27", text="Pay27", anchor=W)
        my_tree.heading("Pay28", text="Pay28", anchor=W)
        my_tree.heading("Pay29", text="Pay29", anchor=W)
        my_tree.heading("Pay30", text="Pay30", anchor=W)
        my_tree.heading("Pay31", text="Pay31", anchor=W)
        my_tree.heading("Pay32", text="Pay32", anchor=W)
        my_tree.heading("Pay33", text="Pay33", anchor=W)
        my_tree.heading("Pay34", text="Pay34", anchor=W)
        my_tree.heading("Pay35", text="Pay35", anchor=W)
        my_tree.heading("Pay36", text="Pay36", anchor=W)
        my_tree.heading("Pay37", text="Pay37", anchor=W)
        my_tree.heading("Pay38", text="Pay38", anchor=W)
        my_tree.heading("Pay39", text="Pay39", anchor=W)
        my_tree.heading("Pay40", text="Pay40", anchor=W)
        my_tree.heading("Coin1", text="Coin1", anchor=W)
        my_tree.heading("Coin2", text="Coin2", anchor=W)
        my_tree.heading("Coin3", text="Coin3", anchor=W)
        my_tree.heading("Coin4", text="Coin4", anchor=W)
        my_tree.heading("Coin5", text="Coin5", anchor=W)
        my_tree.heading("Coin6", text="Coin6", anchor=W)
        my_tree.heading("Total Cash", text="Total Cash", anchor=W)
        my_tree.heading("Total Credit", text="Total Credit", anchor=W)
        my_tree.heading("Error1", text="Error1", anchor=W)
        my_tree.heading("Error2", text="Error2", anchor=W)
        my_tree.heading("Error3", text="Error3", anchor=W)
        my_tree.heading("Error4", text="Error4", anchor=W)
        my_tree.heading("Error5", text="Error5", anchor=W)
        my_tree.heading("Error6", text="Error6", anchor=W)
        my_tree.heading("Error7", text="Error7", anchor=W)
        my_tree.heading("Error8", text="Error8", anchor=W)
        my_tree.heading("Error9", text="Error9", anchor=W)
        my_tree.heading("Error10", text="Error10", anchor=W)
        my_tree.heading("Error11", text="Error11", anchor=W)
        my_tree.heading("Error12", text="Error12", anchor=W)
        my_tree.heading("Error13", text="Error13", anchor=W)
        my_tree.heading("Error14", text="Error14", anchor=W)
        my_tree.heading("Error15", text="Error15", anchor=W)
        my_tree.heading("Error16", text="Error16", anchor=W)
        my_tree.heading("Error17", text="Error17", anchor=W)
        my_tree.heading("Error18", text="Error18", anchor=W)
        my_tree.heading("Error19", text="Error19", anchor=W)
        my_tree.heading("Error20", text="Error20", anchor=W)
        my_tree.heading("Error21", text="Error21", anchor=W)
        my_tree.heading("Error22", text="Error22", anchor=W)
        my_tree.heading("Error23", text="Error23", anchor=W)
        my_tree.heading("Error24", text="Error24", anchor=W)
        my_tree.heading("Error25", text="Error25", anchor=W)
        my_tree.heading("Error26", text="Error26", anchor=W)
        my_tree.heading("Error27", text="Error27", anchor=W)
        my_tree.heading("Error28", text="Error28", anchor=W)
        my_tree.heading("Error29", text="Error29", anchor=W)
    elif name == 'Astro40':
        my_tree['columns'] = (
        "Date", "Email", "Print", "Sold", "Tested",
        "Pay1", "Pay2", "Pay3", "Pay4", "Pay5", "Pay6", "Pay7", "Pay8", "Pay9", "Pay10",
        "Pay11", "Pay12", "Pay13", "Pay14", "Pay15", "Pay16", "Pay17", "Pay18",
        "Pay21", "Pay22", "Pay23", "Pay24", "Pay25", "Pay26", "Pay27", "Pay28", "Pay29", "Pay30",
        "Pay31", "Pay32", "Pay33", "Pay34", "Pay35", "Pay36", "Pay37", "Pay38", "Pay39", "Pay40",
        "Coin1", "Coin2", "Coin3", "Coin4", "Coin5", "Coin6",
        "Total Cash", 'Total Credit',
        "Error1", "Error2", "Error3", "Error4", "Error5", "Error6", "Error7", "Error8", "Error9", "Error10",
        "Error11", "Error12", "Error13", "Error14", "Error15", "Error16", "Error17", "Error18", "Error19", "Error20",
        "Error21", "Error22", "Error23", "Error24", "Error25", "Error26", "Error27", "Error28", "Error29", "Error30")

        # Format Our Columns
        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("Date", anchor=W, width=50)
        my_tree.column("Email", anchor=W, width=50)
        my_tree.column("Print", anchor=W, width=50)
        my_tree.column("Sold", anchor=W, width=50)
        my_tree.column("Tested", anchor=W, width=50)
        my_tree.column("Pay1", anchor=W, width=50)
        my_tree.column("Pay2", anchor=W, width=50)
        my_tree.column("Pay3", anchor=W, width=50)
        my_tree.column("Pay4", anchor=W, width=50)
        my_tree.column("Pay5", anchor=W, width=50)
        my_tree.column("Pay6", anchor=W, width=50)
        my_tree.column("Pay7", anchor=W, width=50)
        my_tree.column("Pay8", anchor=W, width=50)
        my_tree.column("Pay9", anchor=W, width=50)
        my_tree.column("Pay10", anchor=W, width=50)
        my_tree.column("Pay11", anchor=W, width=50)
        my_tree.column("Pay12", anchor=W, width=50)
        my_tree.column("Pay13", anchor=W, width=50)
        my_tree.column("Pay14", anchor=W, width=50)
        my_tree.column("Pay15", anchor=W, width=50)
        my_tree.column("Pay16", anchor=W, width=50)
        my_tree.column("Pay17", anchor=W, width=50)
        my_tree.column("Pay18", anchor=W, width=50)
        my_tree.column("Pay21", anchor=W, width=50)
        my_tree.column("Pay22", anchor=W, width=50)
        my_tree.column("Pay23", anchor=W, width=50)
        my_tree.column("Pay24", anchor=W, width=50)
        my_tree.column("Pay25", anchor=W, width=50)
        my_tree.column("Pay26", anchor=W, width=50)
        my_tree.column("Pay27", anchor=W, width=50)
        my_tree.column("Pay28", anchor=W, width=50)
        my_tree.column("Pay29", anchor=W, width=50)
        my_tree.column("Pay30", anchor=W, width=50)
        my_tree.column("Pay31", anchor=W, width=50)
        my_tree.column("Pay32", anchor=W, width=50)
        my_tree.column("Pay33", anchor=W, width=50)
        my_tree.column("Pay34", anchor=W, width=50)
        my_tree.column("Pay35", anchor=W, width=50)
        my_tree.column("Pay36", anchor=W, width=50)
        my_tree.column("Pay37", anchor=W, width=50)
        my_tree.column("Pay38", anchor=W, width=50)
        my_tree.column("Pay39", anchor=W, width=50)
        my_tree.column("Pay40", anchor=W, width=50)
        my_tree.column("Coin1", anchor=W, width=50)
        my_tree.column("Coin2", anchor=W, width=50)
        my_tree.column("Coin3", anchor=W, width=50)
        my_tree.column("Coin4", anchor=W, width=50)
        my_tree.column("Coin5", anchor=W, width=50)
        my_tree.column("Coin6", anchor=W, width=50)
        my_tree.column("Total Cash", anchor=W, width=50)
        my_tree.column("Total Credit", anchor=W, width=50)
        my_tree.column("Error1", anchor=W, width=50)
        my_tree.column("Error2", anchor=W, width=50)
        my_tree.column("Error3", anchor=W, width=50)
        my_tree.column("Error4", anchor=W, width=50)
        my_tree.column("Error5", anchor=W, width=50)
        my_tree.column("Error6", anchor=W, width=50)
        my_tree.column("Error7", anchor=W, width=50)
        my_tree.column("Error8", anchor=W, width=50)
        my_tree.column("Error9", anchor=W, width=50)
        my_tree.column("Error10", anchor=W, width=50)
        my_tree.column("Error11", anchor=W, width=50)
        my_tree.column("Error12", anchor=W, width=50)
        my_tree.column("Error13", anchor=W, width=50)
        my_tree.column("Error14", anchor=W, width=50)
        my_tree.column("Error15", anchor=W, width=50)
        my_tree.column("Error16", anchor=W, width=50)
        my_tree.column("Error17", anchor=W, width=50)
        my_tree.column("Error18", anchor=W, width=50)
        my_tree.column("Error19", anchor=W, width=50)
        my_tree.column("Error20", anchor=W, width=50)
        my_tree.column("Error21", anchor=W, width=50)
        my_tree.column("Error22", anchor=W, width=50)
        my_tree.column("Error23", anchor=W, width=50)
        my_tree.column("Error24", anchor=W, width=50)
        my_tree.column("Error25", anchor=W, width=50)
        my_tree.column("Error26", anchor=W, width=50)
        my_tree.column("Error27", anchor=W, width=50)
        my_tree.column("Error28", anchor=W, width=50)
        my_tree.column("Error29", anchor=W, width=50)
        my_tree.column("Error30", anchor=W, width=50)

        # Create Headings
        my_tree.heading("#0", text="", anchor=W)
        my_tree.heading("Date", text="Date", anchor=W)
        my_tree.heading("Email", text="Email", anchor=W)
        my_tree.heading("Print", text="Print", anchor=W)
        my_tree.heading("Sold", text="Sold", anchor=W)
        my_tree.heading("Tested", text="Tested", anchor=W)
        my_tree.heading("Pay1", text="Pay1", anchor=W)
        my_tree.heading("Pay2", text="Pay2", anchor=W)
        my_tree.heading("Pay3", text="Pay3", anchor=W)
        my_tree.heading("Pay4", text="Pay4", anchor=W)
        my_tree.heading("Pay5", text="Pay5", anchor=W)
        my_tree.heading("Pay6", text="Pay6", anchor=W)
        my_tree.heading("Pay7", text="Pay7", anchor=W)
        my_tree.heading("Pay8", text="Pay8", anchor=W)
        my_tree.heading("Pay9", text="Pay9", anchor=W)
        my_tree.heading("Pay10", text="Pay10", anchor=W)
        my_tree.heading("Pay11", text="Pay11", anchor=W)
        my_tree.heading("Pay12", text="Pay12", anchor=W)
        my_tree.heading("Pay13", text="Pay13", anchor=W)
        my_tree.heading("Pay14", text="Pay14", anchor=W)
        my_tree.heading("Pay15", text="Pay15", anchor=W)
        my_tree.heading("Pay16", text="Pay16", anchor=W)
        my_tree.heading("Pay17", text="Pay17", anchor=W)
        my_tree.heading("Pay18", text="Pay18", anchor=W)
        my_tree.heading("Pay21", text="Pay21", anchor=W)
        my_tree.heading("Pay22", text="Pay22", anchor=W)
        my_tree.heading("Pay23", text="Pay23", anchor=W)
        my_tree.heading("Pay24", text="Pay24", anchor=W)
        my_tree.heading("Pay25", text="Pay25", anchor=W)
        my_tree.heading("Pay26", text="Pay26", anchor=W)
        my_tree.heading("Pay27", text="Pay27", anchor=W)
        my_tree.heading("Pay28", text="Pay28", anchor=W)
        my_tree.heading("Pay29", text="Pay29", anchor=W)
        my_tree.heading("Pay30", text="Pay30", anchor=W)
        my_tree.heading("Pay31", text="Pay31", anchor=W)
        my_tree.heading("Pay32", text="Pay32", anchor=W)
        my_tree.heading("Pay33", text="Pay33", anchor=W)
        my_tree.heading("Pay34", text="Pay34", anchor=W)
        my_tree.heading("Pay35", text="Pay35", anchor=W)
        my_tree.heading("Pay36", text="Pay36", anchor=W)
        my_tree.heading("Pay37", text="Pay37", anchor=W)
        my_tree.heading("Pay38", text="Pay38", anchor=W)
        my_tree.heading("Pay39", text="Pay39", anchor=W)
        my_tree.heading("Pay40", text="Pay40", anchor=W)
        my_tree.heading("Coin1", text="Coin1", anchor=W)
        my_tree.heading("Coin2", text="Coin2", anchor=W)
        my_tree.heading("Coin3", text="Coin3", anchor=W)
        my_tree.heading("Coin4", text="Coin4", anchor=W)
        my_tree.heading("Coin5", text="Coin5", anchor=W)
        my_tree.heading("Coin6", text="Coin6", anchor=W)
        my_tree.heading("Total Cash", text="Total Cash", anchor=W)
        my_tree.heading("Total Credit", text="Total Credit", anchor=W)
        my_tree.heading("Error1", text="Error1", anchor=W)
        my_tree.heading("Error2", text="Error2", anchor=W)
        my_tree.heading("Error3", text="Error3", anchor=W)
        my_tree.heading("Error4", text="Error4", anchor=W)
        my_tree.heading("Error5", text="Error5", anchor=W)
        my_tree.heading("Error6", text="Error6", anchor=W)
        my_tree.heading("Error7", text="Error7", anchor=W)
        my_tree.heading("Error8", text="Error8", anchor=W)
        my_tree.heading("Error9", text="Error9", anchor=W)
        my_tree.heading("Error10", text="Error10", anchor=W)
        my_tree.heading("Error11", text="Error11", anchor=W)
        my_tree.heading("Error12", text="Error12", anchor=W)
        my_tree.heading("Error13", text="Error13", anchor=W)
        my_tree.heading("Error14", text="Error14", anchor=W)
        my_tree.heading("Error15", text="Error15", anchor=W)
        my_tree.heading("Error16", text="Error16", anchor=W)
        my_tree.heading("Error17", text="Error17", anchor=W)
        my_tree.heading("Error18", text="Error18", anchor=W)
        my_tree.heading("Error19", text="Error19", anchor=W)
        my_tree.heading("Error20", text="Error20", anchor=W)
        my_tree.heading("Error21", text="Error21", anchor=W)
        my_tree.heading("Error22", text="Error22", anchor=W)
        my_tree.heading("Error23", text="Error23", anchor=W)
        my_tree.heading("Error24", text="Error24", anchor=W)
        my_tree.heading("Error25", text="Error25", anchor=W)
        my_tree.heading("Error26", text="Error26", anchor=W)
        my_tree.heading("Error27", text="Error27", anchor=W)
        my_tree.heading("Error28", text="Error28", anchor=W)
        my_tree.heading("Error29", text="Error29", anchor=W)
        my_tree.heading("Error30", text="Error30", anchor=W)
    elif name == 'Astro40(s)':
        my_tree['columns'] = (
        "Date", "Email", "Print", "Sold", "Tested",
        "Pay1", "Pay2", "Pay3", "Pay4", "Pay5", "Pay6", "Pay7", "Pay8", "Pay9", "Pay10",
        "Pay11", "Pay12", "Pay13", "Pay14", "Pay15", "Pay16", "Pay17", "Pay18",
        "Coin1", "Coin2", "Coin3", "Coin4", "Coin5", "Coin6",
        "Total Cash", 'Total Credit',
        "Error1", "Error2", "Error3", "Error4", "Error5", "Error6", "Error7", "Error8", "Error9", "Error10",
        "Error11", "Error12", "Error13", "Error14", "Error15", "Error16", "Error17", "Error18", "Error19", "Error20",
        "Error21", "Error22", "Error23", "Error24", "Error25", "Error26", "Error27", "Error28", "Error29")

        # Format Our Columns
        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("Date", anchor=W, width=50)
        my_tree.column("Email", anchor=W, width=50)
        my_tree.column("Print", anchor=W, width=50)
        my_tree.column("Sold", anchor=W, width=50)
        my_tree.column("Tested", anchor=W, width=50)
        my_tree.column("Pay1", anchor=W, width=50)
        my_tree.column("Pay2", anchor=W, width=50)
        my_tree.column("Pay3", anchor=W, width=50)
        my_tree.column("Pay4", anchor=W, width=50)
        my_tree.column("Pay5", anchor=W, width=50)
        my_tree.column("Pay6", anchor=W, width=50)
        my_tree.column("Pay7", anchor=W, width=50)
        my_tree.column("Pay8", anchor=W, width=50)
        my_tree.column("Pay9", anchor=W, width=50)
        my_tree.column("Pay10", anchor=W, width=50)
        my_tree.column("Pay11", anchor=W, width=50)
        my_tree.column("Pay12", anchor=W, width=50)
        my_tree.column("Pay13", anchor=W, width=50)
        my_tree.column("Pay14", anchor=W, width=50)
        my_tree.column("Pay15", anchor=W, width=50)
        my_tree.column("Pay16", anchor=W, width=50)
        my_tree.column("Pay17", anchor=W, width=50)
        my_tree.column("Pay18", anchor=W, width=50)
        my_tree.column("Coin1", anchor=W, width=50)
        my_tree.column("Coin2", anchor=W, width=50)
        my_tree.column("Coin3", anchor=W, width=50)
        my_tree.column("Coin4", anchor=W, width=50)
        my_tree.column("Coin5", anchor=W, width=50)
        my_tree.column("Coin6", anchor=W, width=50)
        my_tree.column("Total Cash", anchor=W, width=50)
        my_tree.column("Total Credit", anchor=W, width=50)
        my_tree.column("Error1", anchor=W, width=50)
        my_tree.column("Error2", anchor=W, width=50)
        my_tree.column("Error3", anchor=W, width=50)
        my_tree.column("Error4", anchor=W, width=50)
        my_tree.column("Error5", anchor=W, width=50)
        my_tree.column("Error6", anchor=W, width=50)
        my_tree.column("Error7", anchor=W, width=50)
        my_tree.column("Error8", anchor=W, width=50)
        my_tree.column("Error9", anchor=W, width=50)
        my_tree.column("Error10", anchor=W, width=50)
        my_tree.column("Error11", anchor=W, width=50)
        my_tree.column("Error12", anchor=W, width=50)
        my_tree.column("Error13", anchor=W, width=50)
        my_tree.column("Error14", anchor=W, width=50)
        my_tree.column("Error15", anchor=W, width=50)
        my_tree.column("Error16", anchor=W, width=50)
        my_tree.column("Error17", anchor=W, width=50)
        my_tree.column("Error18", anchor=W, width=50)
        my_tree.column("Error19", anchor=W, width=50)
        my_tree.column("Error20", anchor=W, width=50)
        my_tree.column("Error21", anchor=W, width=50)
        my_tree.column("Error22", anchor=W, width=50)
        my_tree.column("Error23", anchor=W, width=50)
        my_tree.column("Error24", anchor=W, width=50)
        my_tree.column("Error25", anchor=W, width=50)
        my_tree.column("Error26", anchor=W, width=50)
        my_tree.column("Error27", anchor=W, width=50)
        my_tree.column("Error28", anchor=W, width=50)
        my_tree.column("Error29", anchor=W, width=50)

        # Create Headings
        my_tree.heading("#0", text="", anchor=W)
        my_tree.heading("Date", text="Date", anchor=W)
        my_tree.heading("Email", text="Email", anchor=W)
        my_tree.heading("Print", text="Print", anchor=W)
        my_tree.heading("Sold", text="Sold", anchor=W)
        my_tree.heading("Tested", text="Tested", anchor=W)
        my_tree.heading("Pay1", text="Pay1", anchor=W)
        my_tree.heading("Pay2", text="Pay2", anchor=W)
        my_tree.heading("Pay3", text="Pay3", anchor=W)
        my_tree.heading("Pay4", text="Pay4", anchor=W)
        my_tree.heading("Pay5", text="Pay5", anchor=W)
        my_tree.heading("Pay6", text="Pay6", anchor=W)
        my_tree.heading("Pay7", text="Pay7", anchor=W)
        my_tree.heading("Pay8", text="Pay8", anchor=W)
        my_tree.heading("Pay9", text="Pay9", anchor=W)
        my_tree.heading("Pay10", text="Pay10", anchor=W)
        my_tree.heading("Pay11", text="Pay11", anchor=W)
        my_tree.heading("Pay12", text="Pay12", anchor=W)
        my_tree.heading("Pay13", text="Pay13", anchor=W)
        my_tree.heading("Pay14", text="Pay14", anchor=W)
        my_tree.heading("Pay15", text="Pay15", anchor=W)
        my_tree.heading("Pay16", text="Pay16", anchor=W)
        my_tree.heading("Pay17", text="Pay17", anchor=W)
        my_tree.heading("Pay18", text="Pay18", anchor=W)
        my_tree.heading("Coin1", text="Coin1", anchor=W)
        my_tree.heading("Coin2", text="Coin2", anchor=W)
        my_tree.heading("Coin3", text="Coin3", anchor=W)
        my_tree.heading("Coin4", text="Coin4", anchor=W)
        my_tree.heading("Coin5", text="Coin5", anchor=W)
        my_tree.heading("Coin6", text="Coin6", anchor=W)
        my_tree.heading("Total Cash", text="Total Cash", anchor=W)
        my_tree.heading("Total Credit", text="Total Credit", anchor=W)
        my_tree.heading("Error1", text="Error1", anchor=W)
        my_tree.heading("Error2", text="Error2", anchor=W)
        my_tree.heading("Error3", text="Error3", anchor=W)
        my_tree.heading("Error4", text="Error4", anchor=W)
        my_tree.heading("Error5", text="Error5", anchor=W)
        my_tree.heading("Error6", text="Error6", anchor=W)
        my_tree.heading("Error7", text="Error7", anchor=W)
        my_tree.heading("Error8", text="Error8", anchor=W)
        my_tree.heading("Error9", text="Error9", anchor=W)
        my_tree.heading("Error10", text="Error10", anchor=W)
        my_tree.heading("Error11", text="Error11", anchor=W)
        my_tree.heading("Error12", text="Error12", anchor=W)
        my_tree.heading("Error13", text="Error13", anchor=W)
        my_tree.heading("Error14", text="Error14", anchor=W)
        my_tree.heading("Error15", text="Error15", anchor=W)
        my_tree.heading("Error16", text="Error16", anchor=W)
        my_tree.heading("Error17", text="Error17", anchor=W)
        my_tree.heading("Error18", text="Error18", anchor=W)
        my_tree.heading("Error19", text="Error19", anchor=W)
        my_tree.heading("Error20", text="Error20", anchor=W)
        my_tree.heading("Error21", text="Error21", anchor=W)
        my_tree.heading("Error22", text="Error22", anchor=W)
        my_tree.heading("Error23", text="Error23", anchor=W)
        my_tree.heading("Error24", text="Error24", anchor=W)
        my_tree.heading("Error25", text="Error25", anchor=W)
        my_tree.heading("Error26", text="Error26", anchor=W)
        my_tree.heading("Error27", text="Error27", anchor=W)
        my_tree.heading("Error28", text="Error28", anchor=W)
        my_tree.heading("Error29", text="Error29", anchor=W)

    elif name == 'Astro35':
        my_tree['columns'] = (
        "Date", "Email", "Print", "Sold", "Tested",
        "Pay1", "Pay2", "Pay3", "Pay4", "Pay5", "Pay6", "Pay7", "Pay8", "Pay9", "Pay10",
        "Pay11", "Pay12", "Pay13", "Pay14", "Pay15", "Pay16", "Pay17", "Pay18",
        "Pay21", "Pay22", "Pay23", "Pay24", "Pay25", "Pay26", "Pay27", "Pay28", "Pay29", "Pay30",
        "Pay31", "Pay32", "Pay33", "Pay34", "Pay35",
        "Price1", "Price2", "Price3", "Price4", "Price5",
        "Coin1", "Coin2", "Coin3", "Coin4", "Coin5", "Coin6",
        "Total Cash", 'Total Credit',
        "Error1", "Error2", "Error3", "Error4", "Error5", "Error6", "Error7", "Error8", "Error9", "Error10",
        "Error11", "Error12", "Error13", "Error14", "Error15", "Error16", "Error17", "Error18", "Error19", "Error20",
        "Error21", "Error22", "Error23", "Error24", "Error25", "Error26", "Error27", "Error28", "Error29")

        # Format Our Columns
        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("Date", anchor=W, width=50)
        my_tree.column("Email", anchor=W, width=50)
        my_tree.column("Print", anchor=W, width=50)
        my_tree.column("Sold", anchor=W, width=50)
        my_tree.column("Tested", anchor=W, width=50)
        my_tree.column("Pay1", anchor=W, width=50)
        my_tree.column("Pay2", anchor=W, width=50)
        my_tree.column("Pay3", anchor=W, width=50)
        my_tree.column("Pay4", anchor=W, width=50)
        my_tree.column("Pay5", anchor=W, width=50)
        my_tree.column("Pay6", anchor=W, width=50)
        my_tree.column("Pay7", anchor=W, width=50)
        my_tree.column("Pay8", anchor=W, width=50)
        my_tree.column("Pay9", anchor=W, width=50)
        my_tree.column("Pay10", anchor=W, width=50)
        my_tree.column("Pay11", anchor=W, width=50)
        my_tree.column("Pay12", anchor=W, width=50)
        my_tree.column("Pay13", anchor=W, width=50)
        my_tree.column("Pay14", anchor=W, width=50)
        my_tree.column("Pay15", anchor=W, width=50)
        my_tree.column("Pay16", anchor=W, width=50)
        my_tree.column("Pay17", anchor=W, width=50)
        my_tree.column("Pay18", anchor=W, width=50)
        my_tree.column("Pay21", anchor=W, width=50)
        my_tree.column("Pay22", anchor=W, width=50)
        my_tree.column("Pay23", anchor=W, width=50)
        my_tree.column("Pay24", anchor=W, width=50)
        my_tree.column("Pay25", anchor=W, width=50)
        my_tree.column("Pay26", anchor=W, width=50)
        my_tree.column("Pay27", anchor=W, width=50)
        my_tree.column("Pay28", anchor=W, width=50)
        my_tree.column("Pay29", anchor=W, width=50)
        my_tree.column("Pay30", anchor=W, width=50)
        my_tree.column("Pay31", anchor=W, width=50)
        my_tree.column("Pay32", anchor=W, width=50)
        my_tree.column("Pay33", anchor=W, width=50)
        my_tree.column("Pay34", anchor=W, width=50)
        my_tree.column("Pay35", anchor=W, width=50)
        my_tree.column("Price1", anchor=W, width=50)
        my_tree.column("Price2", anchor=W, width=50)
        my_tree.column("Price3", anchor=W, width=50)
        my_tree.column("Price4", anchor=W, width=50)
        my_tree.column("Price5", anchor=W, width=50)
        my_tree.column("Coin1", anchor=W, width=50)
        my_tree.column("Coin2", anchor=W, width=50)
        my_tree.column("Coin3", anchor=W, width=50)
        my_tree.column("Coin4", anchor=W, width=50)
        my_tree.column("Coin5", anchor=W, width=50)
        my_tree.column("Coin6", anchor=W, width=50)
        my_tree.column("Total Cash", anchor=W, width=50)
        my_tree.column("Total Credit", anchor=W, width=50)
        my_tree.column("Error1", anchor=W, width=50)
        my_tree.column("Error2", anchor=W, width=50)
        my_tree.column("Error3", anchor=W, width=50)
        my_tree.column("Error4", anchor=W, width=50)
        my_tree.column("Error5", anchor=W, width=50)
        my_tree.column("Error6", anchor=W, width=50)
        my_tree.column("Error7", anchor=W, width=50)
        my_tree.column("Error8", anchor=W, width=50)
        my_tree.column("Error9", anchor=W, width=50)
        my_tree.column("Error10", anchor=W, width=50)
        my_tree.column("Error11", anchor=W, width=50)
        my_tree.column("Error12", anchor=W, width=50)
        my_tree.column("Error13", anchor=W, width=50)
        my_tree.column("Error14", anchor=W, width=50)
        my_tree.column("Error15", anchor=W, width=50)
        my_tree.column("Error16", anchor=W, width=50)
        my_tree.column("Error17", anchor=W, width=50)
        my_tree.column("Error18", anchor=W, width=50)
        my_tree.column("Error19", anchor=W, width=50)
        my_tree.column("Error20", anchor=W, width=50)
        my_tree.column("Error21", anchor=W, width=50)
        my_tree.column("Error22", anchor=W, width=50)
        my_tree.column("Error23", anchor=W, width=50)
        my_tree.column("Error24", anchor=W, width=50)
        my_tree.column("Error25", anchor=W, width=50)
        my_tree.column("Error26", anchor=W, width=50)
        my_tree.column("Error27", anchor=W, width=50)
        my_tree.column("Error28", anchor=W, width=50)
        my_tree.column("Error29", anchor=W, width=50)

        # Create Headings
        my_tree.heading("#0", text="", anchor=W)
        my_tree.heading("Date", text="Date", anchor=W)
        my_tree.heading("Email", text="Email", anchor=W)
        my_tree.heading("Print", text="Print", anchor=W)
        my_tree.heading("Sold", text="Sold", anchor=W)
        my_tree.heading("Tested", text="Tested", anchor=W)
        my_tree.heading("Pay1", text="Pay1", anchor=W)
        my_tree.heading("Pay2", text="Pay2", anchor=W)
        my_tree.heading("Pay3", text="Pay3", anchor=W)
        my_tree.heading("Pay4", text="Pay4", anchor=W)
        my_tree.heading("Pay5", text="Pay5", anchor=W)
        my_tree.heading("Pay6", text="Pay6", anchor=W)
        my_tree.heading("Pay7", text="Pay7", anchor=W)
        my_tree.heading("Pay8", text="Pay8", anchor=W)
        my_tree.heading("Pay9", text="Pay9", anchor=W)
        my_tree.heading("Pay10", text="Pay10", anchor=W)
        my_tree.heading("Pay11", text="Pay11", anchor=W)
        my_tree.heading("Pay12", text="Pay12", anchor=W)
        my_tree.heading("Pay13", text="Pay13", anchor=W)
        my_tree.heading("Pay14", text="Pay14", anchor=W)
        my_tree.heading("Pay15", text="Pay15", anchor=W)
        my_tree.heading("Pay16", text="Pay16", anchor=W)
        my_tree.heading("Pay17", text="Pay17", anchor=W)
        my_tree.heading("Pay18", text="Pay18", anchor=W)
        my_tree.heading("Pay21", text="Pay21", anchor=W)
        my_tree.heading("Pay22", text="Pay22", anchor=W)
        my_tree.heading("Pay23", text="Pay23", anchor=W)
        my_tree.heading("Pay24", text="Pay24", anchor=W)
        my_tree.heading("Pay25", text="Pay25", anchor=W)
        my_tree.heading("Pay26", text="Pay26", anchor=W)
        my_tree.heading("Pay27", text="Pay27", anchor=W)
        my_tree.heading("Pay28", text="Pay28", anchor=W)
        my_tree.heading("Pay29", text="Pay29", anchor=W)
        my_tree.heading("Pay30", text="Pay30", anchor=W)
        my_tree.heading("Pay31", text="Pay31", anchor=W)
        my_tree.heading("Pay32", text="Pay32", anchor=W)
        my_tree.heading("Pay33", text="Pay33", anchor=W)
        my_tree.heading("Pay34", text="Pay34", anchor=W)
        my_tree.heading("Pay35", text="Pay35", anchor=W)
        my_tree.heading("Price1", text="Price1", anchor=W)
        my_tree.heading("Price2", text="Price2", anchor=W)
        my_tree.heading("Price3", text="Price3", anchor=W)
        my_tree.heading("Price4", text="Price4", anchor=W)
        my_tree.heading("Price5", text="Price5", anchor=W)
        my_tree.heading("Coin1", text="Coin1", anchor=W)
        my_tree.heading("Coin2", text="Coin2", anchor=W)
        my_tree.heading("Coin3", text="Coin3", anchor=W)
        my_tree.heading("Coin4", text="Coin4", anchor=W)
        my_tree.heading("Coin5", text="Coin5", anchor=W)
        my_tree.heading("Coin6", text="Coin6", anchor=W)
        my_tree.heading("Total Cash", text="Total Cash", anchor=W)
        my_tree.heading("Total Credit", text="Total Credit", anchor=W)
        my_tree.heading("Error1", text="Error1", anchor=W)
        my_tree.heading("Error2", text="Error2", anchor=W)
        my_tree.heading("Error3", text="Error3", anchor=W)
        my_tree.heading("Error4", text="Error4", anchor=W)
        my_tree.heading("Error5", text="Error5", anchor=W)
        my_tree.heading("Error6", text="Error6", anchor=W)
        my_tree.heading("Error7", text="Error7", anchor=W)
        my_tree.heading("Error8", text="Error8", anchor=W)
        my_tree.heading("Error9", text="Error9", anchor=W)
        my_tree.heading("Error10", text="Error10", anchor=W)
        my_tree.heading("Error11", text="Error11", anchor=W)
        my_tree.heading("Error12", text="Error12", anchor=W)
        my_tree.heading("Error13", text="Error13", anchor=W)
        my_tree.heading("Error14", text="Error14", anchor=W)
        my_tree.heading("Error15", text="Error15", anchor=W)
        my_tree.heading("Error16", text="Error16", anchor=W)
        my_tree.heading("Error17", text="Error17", anchor=W)
        my_tree.heading("Error18", text="Error18", anchor=W)
        my_tree.heading("Error19", text="Error19", anchor=W)
        my_tree.heading("Error20", text="Error20", anchor=W)
        my_tree.heading("Error21", text="Error21", anchor=W)
        my_tree.heading("Error22", text="Error22", anchor=W)
        my_tree.heading("Error23", text="Error23", anchor=W)
        my_tree.heading("Error24", text="Error24", anchor=W)
        my_tree.heading("Error25", text="Error25", anchor=W)
        my_tree.heading("Error26", text="Error26", anchor=W)
        my_tree.heading("Error27", text="Error27", anchor=W)
        my_tree.heading("Error28", text="Error28", anchor=W)
        my_tree.heading("Error29", text="Error29", anchor=W)

    elif name == 'Kikko':
        my_tree['columns'] = (
        "Date", "Email", "Print", "Sold", "Tested",
        "Pay1", "Pay2", "Pay3", "Pay4", "Pay5", "Pay6", "Pay7", "Pay8", "Pay9", "Pay10",
        "Pay11", "Pay12", "Pay13", "Pay14", "Pay15", "Pay16",
        "Price1", "Price2", "Price3", "Price4", "Price5",
        "Coin1", "Coin2", "Coin3", "Coin4", "Coin5", "Coin6",
        "Total Cash", 'Total Credit',
        "Error1", "Error2", "Error3", "Error4", "Error5", "Error6", "Error7", "Error8", "Error9", "Error10",
        "Error11", "Error12", "Error13", "Error14")

        # Format Our Columns
        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("Date", anchor=W, width=50)
        my_tree.column("Email", anchor=W, width=50)
        my_tree.column("Print", anchor=W, width=50)
        my_tree.column("Sold", anchor=W, width=50)
        my_tree.column("Tested", anchor=W, width=50)
        my_tree.column("Pay1", anchor=W, width=50)
        my_tree.column("Pay2", anchor=W, width=50)
        my_tree.column("Pay3", anchor=W, width=50)
        my_tree.column("Pay4", anchor=W, width=50)
        my_tree.column("Pay5", anchor=W, width=50)
        my_tree.column("Pay6", anchor=W, width=50)
        my_tree.column("Pay7", anchor=W, width=50)
        my_tree.column("Pay8", anchor=W, width=50)
        my_tree.column("Pay9", anchor=W, width=50)
        my_tree.column("Pay10", anchor=W, width=50)
        my_tree.column("Pay11", anchor=W, width=50)
        my_tree.column("Pay12", anchor=W, width=50)
        my_tree.column("Pay13", anchor=W, width=50)
        my_tree.column("Pay14", anchor=W, width=50)
        my_tree.column("Pay15", anchor=W, width=50)
        my_tree.column("Pay16", anchor=W, width=50)
        my_tree.column("Price1", anchor=W, width=50)
        my_tree.column("Price2", anchor=W, width=50)
        my_tree.column("Price3", anchor=W, width=50)
        my_tree.column("Price4", anchor=W, width=50)
        my_tree.column("Price5", anchor=W, width=50)
        my_tree.column("Coin1", anchor=W, width=50)
        my_tree.column("Coin2", anchor=W, width=50)
        my_tree.column("Coin3", anchor=W, width=50)
        my_tree.column("Coin4", anchor=W, width=50)
        my_tree.column("Coin5", anchor=W, width=50)
        my_tree.column("Coin6", anchor=W, width=50)
        my_tree.column("Total Cash", anchor=W, width=50)
        my_tree.column("Total Credit", anchor=W, width=50)
        my_tree.column("Error1", anchor=W, width=50)
        my_tree.column("Error2", anchor=W, width=50)
        my_tree.column("Error3", anchor=W, width=50)
        my_tree.column("Error4", anchor=W, width=50)
        my_tree.column("Error5", anchor=W, width=50)
        my_tree.column("Error6", anchor=W, width=50)
        my_tree.column("Error7", anchor=W, width=50)
        my_tree.column("Error8", anchor=W, width=50)
        my_tree.column("Error9", anchor=W, width=50)
        my_tree.column("Error10", anchor=W, width=50)
        my_tree.column("Error11", anchor=W, width=50)
        my_tree.column("Error12", anchor=W, width=50)
        my_tree.column("Error13", anchor=W, width=50)
        my_tree.column("Error14", anchor=W, width=50)

        # Create Headings
        my_tree.heading("#0", text="", anchor=W)
        my_tree.heading("Date", text="Date", anchor=W)
        my_tree.heading("Email", text="Email", anchor=W)
        my_tree.heading("Print", text="Print", anchor=W)
        my_tree.heading("Sold", text="Sold", anchor=W)
        my_tree.heading("Tested", text="Tested", anchor=W)
        my_tree.heading("Pay1", text="Pay1", anchor=W)
        my_tree.heading("Pay2", text="Pay2", anchor=W)
        my_tree.heading("Pay3", text="Pay3", anchor=W)
        my_tree.heading("Pay4", text="Pay4", anchor=W)
        my_tree.heading("Pay5", text="Pay5", anchor=W)
        my_tree.heading("Pay6", text="Pay6", anchor=W)
        my_tree.heading("Pay7", text="Pay7", anchor=W)
        my_tree.heading("Pay8", text="Pay8", anchor=W)
        my_tree.heading("Pay9", text="Pay9", anchor=W)
        my_tree.heading("Pay10", text="Pay10", anchor=W)
        my_tree.heading("Pay11", text="Pay11", anchor=W)
        my_tree.heading("Pay12", text="Pay12", anchor=W)
        my_tree.heading("Pay13", text="Pay13", anchor=W)
        my_tree.heading("Pay14", text="Pay14", anchor=W)
        my_tree.heading("Pay15", text="Pay15", anchor=W)
        my_tree.heading("Pay16", text="Pay16", anchor=W)
        my_tree.heading("Price1", text="Price1", anchor=W)
        my_tree.heading("Price2", text="Price2", anchor=W)
        my_tree.heading("Price3", text="Price3", anchor=W)
        my_tree.heading("Price4", text="Price4", anchor=W)
        my_tree.heading("Price5", text="Price5", anchor=W)
        my_tree.heading("Coin1", text="Coin1", anchor=W)
        my_tree.heading("Coin2", text="Coin2", anchor=W)
        my_tree.heading("Coin3", text="Coin3", anchor=W)
        my_tree.heading("Coin4", text="Coin4", anchor=W)
        my_tree.heading("Coin5", text="Coin5", anchor=W)
        my_tree.heading("Coin6", text="Coin6", anchor=W)
        my_tree.heading("Total Cash", text="Total Cash", anchor=W)
        my_tree.heading("Total Credit", text="Total Credit", anchor=W)
        my_tree.heading("Error1", text="Error1", anchor=W)
        my_tree.heading("Error2", text="Error2", anchor=W)
        my_tree.heading("Error3", text="Error3", anchor=W)
        my_tree.heading("Error4", text="Error4", anchor=W)
        my_tree.heading("Error5", text="Error5", anchor=W)
        my_tree.heading("Error6", text="Error6", anchor=W)
        my_tree.heading("Error7", text="Error7", anchor=W)
        my_tree.heading("Error8", text="Error8", anchor=W)
        my_tree.heading("Error9", text="Error9", anchor=W)
        my_tree.heading("Error10", text="Error10", anchor=W)
        my_tree.heading("Error11", text="Error11", anchor=W)
        my_tree.heading("Error12", text="Error12", anchor=W)
        my_tree.heading("Error13", text="Error13", anchor=W)
        my_tree.heading("Error14", text="Error14", anchor=W)
def record_something(name,records,my_tree,count):
    if name == 'FSE':
        for record in records:
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10],
                               record[11], record[12], record[13], record[14], record[15], record[16], record[17], record[18], record[19], record[20],
                               record[21], record[22], record[23], record[24], record[25], record[26], record[27], record[28], record[29], record[30],
                               record[31], record[32], record[33], record[34], record[35], record[36], record[37], record[38], record[39], record[40],
                               record[41], record[42], record[43], record[44], record[45], record[46], record[47], record[48], record[49], record[50],
                               record[51], record[52], record[53], record[54], record[55], record[56], record[57], record[58], record[59], record[60],
                               record[61], record[62], record[63], record[64], record[65], record[66], record[67], record[68], record[69], record[70],
                               record[71], record[72], record[73], record[74], record[75], record[76]),
                               tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10],
                               record[11], record[12], record[13], record[14], record[15], record[16], record[17], record[18], record[19], record[20],
                               record[21], record[22], record[23], record[24], record[25], record[26], record[27], record[28], record[29], record[30],
                               record[31], record[32], record[33], record[34], record[35], record[36], record[37], record[38], record[39], record[40],
                               record[41], record[42], record[43], record[44], record[45], record[46], record[47], record[48], record[49], record[50],
                               record[51], record[52], record[53], record[54], record[55], record[56], record[57], record[58], record[59], record[60],
                               record[61], record[62], record[63], record[64], record[65], record[66], record[67], record[68], record[69], record[70],
                               record[71], record[72], record[73], record[74], record[75], record[76]),
                               tags=('oddrow',))
            # increment counter
            count += 1
    elif name =='Brio' or name=='Venezia':
        for record in records:
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10],
                               record[11], record[12], record[13], record[14], record[15], record[16], record[17], record[18], record[19], record[20],
                               record[21], record[22], record[23], record[24], record[25], record[26], record[27], record[28], record[29], record[30],
                               record[31], record[32], record[33], record[34], record[35], record[36], record[37], record[38], record[39], record[40],
                               record[41], record[42], record[43], record[44], record[45], record[46], record[47]),
                               tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10],
                               record[11], record[12], record[13], record[14], record[15], record[16], record[17], record[18], record[19], record[20],
                               record[21], record[22], record[23], record[24], record[25], record[26], record[27], record[28], record[29], record[30],
                               record[31], record[32], record[33], record[34], record[35], record[36], record[37], record[38], record[39], record[40],
                               record[41], record[42], record[43], record[44], record[45], record[46], record[47]),
                               tags=('oddrow',))
            # increment counter
            count += 1
    elif name =='VeneziaLX':
        for record in records:
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10],
                               record[11], record[12], record[13], record[14], record[15], record[16], record[17], record[18], record[19], record[20],
                               record[21], record[22], record[23], record[24], record[25], record[26], record[27], record[28], record[29], record[30],
                               record[31], record[32], record[33], record[34], record[35], record[36], record[37], record[38], record[39], record[40],
                               record[41], record[42], record[43], record[44], record[45], record[46], record[47], record[48], record[49], record[50],
                               record[51]),
                               tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10],
                               record[11], record[12], record[13], record[14], record[15], record[16], record[17], record[18], record[19], record[20],
                               record[21], record[22], record[23], record[24], record[25], record[26], record[27], record[28], record[29], record[30],
                               record[31], record[32], record[33], record[34], record[35], record[36], record[37], record[38], record[39], record[40],
                               record[41], record[42], record[43], record[44], record[45], record[46], record[47], record[48], record[49], record[50],
                               record[51]),
                               tags=('oddrow',))
            # increment counter
            count += 1
    elif name =='Colibri':
        for record in records:
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10],
                               record[11], record[12], record[13], record[14], record[15], record[16], record[17], record[18], record[19], record[20],
                               record[21], record[22], record[23], record[24], record[25], record[26], record[27], record[28], record[29], record[30],
                               record[31], record[32], record[33], record[34], record[35], record[36], record[37], record[38], record[39], record[40],
                               record[41], record[42], record[43], record[44], record[45], record[46], record[47], record[48]),
                               tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10],
                               record[11], record[12], record[13], record[14], record[15], record[16], record[17], record[18], record[19], record[20],
                               record[21], record[22], record[23], record[24], record[25], record[26], record[27], record[28], record[29], record[30],
                               record[31], record[32], record[33], record[34], record[35], record[36], record[37], record[38], record[39], record[40],
                               record[41], record[42], record[43], record[44], record[45], record[46], record[47], record[48]),
                               tags=('oddrow',))
            # increment counter
            count += 1
    elif name =='Colibri(1e)':
        for record in records:
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10],
                               record[11], record[12], record[13], record[14], record[15], record[16], record[17], record[18], record[19], record[20],
                               record[21], record[22], record[23], record[24], record[25], record[26], record[27], record[28], record[29], record[30],
                               record[31], record[32], record[33], record[34], record[35], record[36], record[37], record[38], record[39], record[40],
                               record[41], record[42], record[43], record[44], record[45], record[46], record[47], record[48], record[49]),
                               tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10],
                               record[11], record[12], record[13], record[14], record[15], record[16], record[17], record[18], record[19], record[20],
                               record[21], record[22], record[23], record[24], record[25], record[26], record[27], record[28], record[29], record[30],
                               record[31], record[32], record[33], record[34], record[35], record[36], record[37], record[38], record[39], record[40],
                               record[41], record[42], record[43], record[44], record[45], record[46], record[47], record[48], record[49]),
                               tags=('oddrow',))
            # increment counter
            count += 1
    elif name == 'Canto':
        for record in records:
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10],
                               record[11], record[12], record[13], record[14], record[15], record[16], record[17], record[18], record[19], record[20],
                               record[21], record[22], record[23], record[24], record[25], record[26], record[27], record[28], record[29], record[30],
                               record[31], record[32], record[33], record[34], record[35], record[36], record[37], record[38], record[39], record[40],
                               record[41], record[42], record[43], record[44], record[45], record[46], record[47], record[48], record[49], record[50],
                               record[51], record[52], record[53], record[54], record[55], record[56], record[57], record[58], record[59], record[60],
                               record[61], record[62], record[63], record[64], record[65], record[66], record[67], record[68], record[69], record[70],
                               record[71], record[72], record[73], record[74], record[75], record[76], record[77], record[78], record[79], record[80],
                               record[81], record[82], record[83], record[84], record[85], record[86], record[87], record[88], record[89], record[90],
                               record[91], record[92], record[93], record[94], record[95], record[96], record[97], record[98], record[99], record[100],
                               record[101], record[102], record[103], record[104], record[105], record[106], record[107], record[108], record[109], record[110],
                               record[111], record[112], record[113], record[114], record[115], record[116]),
                               tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10],
                               record[11], record[12], record[13], record[14], record[15], record[16], record[17], record[18], record[19], record[20],
                               record[21], record[22], record[23], record[24], record[25], record[26], record[27], record[28], record[29], record[30],
                               record[31], record[32], record[33], record[34], record[35], record[36], record[37], record[38], record[39], record[40],
                               record[41], record[42], record[43], record[44], record[45], record[46], record[47], record[48], record[49], record[50],
                               record[51], record[52], record[53], record[54], record[55], record[56], record[57], record[58], record[59], record[60],
                               record[61], record[62], record[63], record[64], record[65], record[66], record[67], record[68], record[69], record[70],
                               record[71], record[72], record[73], record[74], record[75], record[76], record[77], record[78], record[79], record[80],
                               record[81], record[82], record[83], record[84], record[85], record[86], record[87], record[88], record[89], record[90],
                               record[91], record[92], record[93], record[94], record[95], record[96], record[97], record[98], record[99], record[100],
                               record[101], record[102], record[103], record[104], record[105], record[106], record[107], record[108], record[109], record[110],
                               record[111], record[112], record[113], record[114], record[115], record[116]),
                               tags=('oddrow',))
            # increment counter
            count += 1
    elif name == 'Astro40':
        for record in records:
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10],
                               record[11], record[12], record[13], record[14], record[15], record[16], record[17], record[18], record[19], record[20],
                               record[21], record[22], record[23], record[24], record[25], record[26], record[27], record[28], record[29], record[30],
                               record[31], record[32], record[33], record[34], record[35], record[36], record[37], record[38], record[39], record[40],
                               record[41], record[42], record[43], record[44], record[45], record[46], record[47], record[48], record[49], record[50],
                               record[51], record[52], record[53], record[54], record[55], record[56], record[57], record[58], record[59], record[60],
                               record[61], record[62], record[63], record[64], record[65], record[66], record[67], record[68], record[69], record[70],
                               record[71], record[72], record[73], record[74], record[75], record[76], record[77], record[78], record[79], record[80],
                               record[81]),
                               tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10],
                               record[11], record[12], record[13], record[14], record[15], record[16], record[17], record[18], record[19], record[20],
                               record[21], record[22], record[23], record[24], record[25], record[26], record[27], record[28], record[29], record[30],
                               record[31], record[32], record[33], record[34], record[35], record[36], record[37], record[38], record[39], record[40],
                               record[41], record[42], record[43], record[44], record[45], record[46], record[47], record[48], record[49], record[50],
                               record[51], record[52], record[53], record[54], record[55], record[56], record[57], record[58], record[59], record[60],
                               record[61], record[62], record[63], record[64], record[65], record[66], record[67], record[68], record[69], record[70],
                               record[71], record[72], record[73], record[74], record[75], record[76], record[77], record[78], record[79], record[80],
                               record[81]),
                               tags=('oddrow',))
            # increment counter
            count += 1
    elif name == 'Astro40(1e)':
        for record in records:
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10],
                               record[11], record[12], record[13], record[14], record[15], record[16], record[17], record[18], record[19], record[20],
                               record[21], record[22], record[23], record[24], record[25], record[26], record[27], record[28], record[29], record[30],
                               record[31], record[32], record[33], record[34], record[35], record[36], record[37], record[38], record[39], record[40],
                               record[41], record[42], record[43], record[44], record[45], record[46], record[47], record[48], record[49], record[50],
                               record[51], record[52], record[53], record[54], record[55], record[56], record[57], record[58], record[59], record[60],
                               record[61], record[62], record[63], record[64], record[65], record[66], record[67], record[68], record[69], record[70],
                               record[71], record[72], record[73], record[74], record[75], record[76], record[77], record[78], record[79], record[80]),
                               tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10],
                               record[11], record[12], record[13], record[14], record[15], record[16], record[17], record[18], record[19], record[20],
                               record[21], record[22], record[23], record[24], record[25], record[26], record[27], record[28], record[29], record[30],
                               record[31], record[32], record[33], record[34], record[35], record[36], record[37], record[38], record[39], record[40],
                               record[41], record[42], record[43], record[44], record[45], record[46], record[47], record[48], record[49], record[50],
                               record[51], record[52], record[53], record[54], record[55], record[56], record[57], record[58], record[59], record[60],
                               record[61], record[62], record[63], record[64], record[65], record[66], record[67], record[68], record[69], record[70],
                               record[71], record[72], record[73], record[74], record[75], record[76], record[77], record[78], record[79], record[80]),
                               tags=('oddrow',))
            # increment counter
            count += 1
    elif name == 'Astro40(s)':
        for record in records:
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10],
                               record[11], record[12], record[13], record[14], record[15], record[16], record[17], record[18], record[19], record[20],
                               record[21], record[22], record[23], record[24], record[25], record[26], record[27], record[28], record[29], record[30],
                               record[31], record[32], record[33], record[34], record[35], record[36], record[37], record[38], record[39], record[40],
                               record[41], record[42], record[43], record[44], record[45], record[46], record[47], record[48], record[49], record[50],
                               record[51], record[52], record[53], record[54], record[55], record[56], record[57], record[58], record[59], record[60]),
                               tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10],
                               record[11], record[12], record[13], record[14], record[15], record[16], record[17], record[18], record[19], record[20],
                               record[21], record[22], record[23], record[24], record[25], record[26], record[27], record[28], record[29], record[30],
                               record[31], record[32], record[33], record[34], record[35], record[36], record[37], record[38], record[39], record[40],
                               record[41], record[42], record[43], record[44], record[45], record[46], record[47], record[48], record[49], record[50],
                               record[51], record[52], record[53], record[54], record[55], record[56], record[57], record[58], record[59], record[60]),
                               tags=('oddrow',))
            # increment counter
            count += 1
    elif name == 'Astro35':
        for record in records:
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10],
                               record[11], record[12], record[13], record[14], record[15], record[16], record[17], record[18], record[19], record[20],
                               record[21], record[22], record[23], record[24], record[25], record[26], record[27], record[28], record[29], record[30],
                               record[31], record[32], record[33], record[34], record[35], record[36], record[37], record[38], record[39], record[40],
                               record[41], record[42], record[43], record[44], record[45], record[46], record[47], record[48], record[49], record[50],
                               record[51], record[52], record[53], record[54], record[55], record[56], record[57], record[58], record[59], record[60],
                               record[61], record[62], record[63], record[64], record[65], record[66], record[67], record[68], record[69], record[70],
                               record[71], record[72], record[73], record[74], record[75], record[76], record[77], record[78], record[79], record[80]),
                               tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10],
                               record[11], record[12], record[13], record[14], record[15], record[16], record[17], record[18], record[19], record[20],
                               record[21], record[22], record[23], record[24], record[25], record[26], record[27], record[28], record[29], record[30],
                               record[31], record[32], record[33], record[34], record[35], record[36], record[37], record[38], record[39], record[40],
                               record[41], record[42], record[43], record[44], record[45], record[46], record[47], record[48], record[49], record[50],
                               record[51], record[52], record[53], record[54], record[55], record[56], record[57], record[58], record[59], record[60],
                               record[61], record[62], record[63], record[64], record[65], record[66], record[67], record[68], record[69], record[70],
                               record[71], record[72], record[73], record[74], record[75], record[76], record[77], record[78], record[79], record[80]),
                               tags=('oddrow',))
            # increment counter
            count += 1
    elif name == 'Kikko':
        for record in records:
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10],
                               record[11], record[12], record[13], record[14], record[15], record[16], record[17], record[18], record[19], record[20],
                               record[21], record[22], record[23], record[24], record[25], record[26], record[27], record[28], record[29], record[30],
                               record[31], record[32], record[33], record[34], record[35], record[36], record[37], record[38], record[39], record[40],
                               record[41], record[42], record[43]),
                               tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10],
                               record[11], record[12], record[13], record[14], record[15], record[16], record[17], record[18], record[19], record[20],
                               record[21], record[22], record[23], record[24], record[25], record[26], record[27], record[28], record[29], record[30],
                               record[31], record[32], record[33], record[34], record[35], record[36], record[37], record[38], record[39], record[40],
                               record[41], record[42], record[43]),
                               tags=('oddrow',))
            # increment counter
            count += 1
def record_something2(name,records,my_tree,count):
    if name == 'FSE':
        for record in records:
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10],
                               record[11], record[12], record[13], record[14], record[15], record[16]),
                               tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10],
                               record[11], record[12], record[13], record[14], record[15], record[16]),
                               tags=('oddrow',))
            # increment counter
            count += 1
    elif name =='Brio' or name=='Venezia':
        for record in records:
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]),
                               tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]),
                               tags=('oddrow',))
            # increment counter
            count += 1
    elif name =='VeneziaLX':
        for record in records:
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10]),
                               tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10]),
                               tags=('oddrow',))
            # increment counter
            count += 1
    elif name =='Colibri':
        for record in records:
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]),
                               tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]),
                               tags=('oddrow',))
            # increment counter
            count += 1
    elif name =='Colibri(1e)':
        for record in records:
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]),
                               tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]),
                               tags=('oddrow',))
            # increment counter
            count += 1
    elif name == 'Canto':
        for record in records:
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10],
                               record[11], record[12], record[13], record[14], record[15], record[16], record[17], record[18], record[19], record[20],
                               record[21], record[22], record[23], record[24], record[25], record[26], record[27], record[28], record[29], record[30],
                               record[31], record[32], record[33], record[34], record[35], record[36], record[37]),
                               tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10],
                               record[11], record[12], record[13], record[14], record[15], record[16], record[17], record[18], record[19], record[20],
                               record[21], record[22], record[23], record[24], record[25], record[26], record[27], record[28], record[29], record[30],
                               record[31], record[32], record[33], record[34], record[35], record[36], record[37]),
                               tags=('oddrow',))
            # increment counter
            count += 1
    elif name == 'Astro40':
        for record in records:
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10],
                               record[11], record[12], record[13], record[14], record[15], record[16], record[17], record[18], record[19], record[20],
                               record[21], record[22], record[23], record[24], record[25], record[26], record[27], record[28], record[29], record[30],
                               record[31], record[32], record[33], record[34], record[35], record[36], record[37], record[38]),
                               tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10],
                               record[11], record[12], record[13], record[14], record[15], record[16], record[17], record[18], record[19], record[20],
                               record[21], record[22], record[23], record[24], record[25], record[26], record[27], record[28], record[29], record[30],
                               record[31], record[32], record[33], record[34], record[35], record[36], record[37], record[38]),
                               tags=('oddrow',))
            # increment counter
            count += 1
    elif name == 'Astro40(1e)':
        for record in records:
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10],
                               record[11], record[12], record[13], record[14], record[15], record[16], record[17], record[18], record[19], record[20],
                               record[21], record[22], record[23], record[24], record[25], record[26], record[27], record[28], record[29], record[30],
                               record[31], record[32], record[33], record[34], record[35], record[36], record[37], record[38]),
                               tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10],
                               record[11], record[12], record[13], record[14], record[15], record[16], record[17], record[18], record[19], record[20],
                               record[21], record[22], record[23], record[24], record[25], record[26], record[27], record[28], record[29], record[30],
                               record[31], record[32], record[33], record[34], record[35], record[36], record[37], record[38]),
                               tags=('oddrow',))
            # increment counter
            count += 1
    elif name == 'Astro40(s)':
        for record in records:
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10],
                               record[11], record[12], record[13], record[14], record[15], record[16], record[17], record[18]),
                               tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10],
                               record[11], record[12], record[13], record[14], record[15], record[16], record[17], record[18]),
                               tags=('oddrow',))
            # increment counter
            count += 1
    elif name == 'Astro35':
        for record in records:
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10],
                               record[11], record[12], record[13], record[14], record[15], record[16], record[17], record[18], record[19], record[20],
                               record[21], record[22], record[23], record[24], record[25], record[26], record[27], record[28], record[29], record[30],
                               record[31], record[32], record[33]),
                               tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10],
                               record[11], record[12], record[13], record[14], record[15], record[16], record[17], record[18], record[19], record[20],
                               record[21], record[22], record[23], record[24], record[25], record[26], record[27], record[28], record[29], record[30],
                               record[31], record[32], record[33]),
                               tags=('oddrow',))
            # increment counter
            count += 1
    elif name == 'Kikko':
        for record in records:
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10],
                               record[11], record[12], record[13], record[14], record[15], record[16]),
                               tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               values=(record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10],
                               record[11], record[12], record[13], record[14], record[15], record[16]),
                               tags=('oddrow',))
            # increment counter
            count += 1
def unique_tree2(name,my_tree):
    if name == 'FSE' or name == "Kikko":
        my_tree['columns'] = (
        "Pay1", "Pay2", "Pay3", "Pay4", "Pay5",
        "Pay6", "Pay7", "Pay8", "Pay9", "Pay10", "Pay11",
        "Pay12", "Pay13", "Pay14", "Pay15", "Pay16")

        # Format Our Columns
        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("Pay1", anchor=W, width=50)
        my_tree.column("Pay2", anchor=W, width=50)
        my_tree.column("Pay3", anchor=W, width=50)
        my_tree.column("Pay4", anchor=W, width=50)
        my_tree.column("Pay5", anchor=W, width=50)
        my_tree.column("Pay6", anchor=W, width=50)
        my_tree.column("Pay7", anchor=W, width=50)
        my_tree.column("Pay8", anchor=W, width=50)
        my_tree.column("Pay9", anchor=W, width=50)
        my_tree.column("Pay10", anchor=W, width=50)
        my_tree.column("Pay11", anchor=W, width=50)
        my_tree.column("Pay12", anchor=W, width=50)
        my_tree.column("Pay13", anchor=W, width=50)
        my_tree.column("Pay14", anchor=W, width=50)
        my_tree.column("Pay15", anchor=W, width=50)
        my_tree.column("Pay16", anchor=W, width=50)


        # Create Headings
        my_tree.heading("#0", text="", anchor=W)
        my_tree.heading("Pay1", text="Pay1", anchor=W)
        my_tree.heading("Pay2", text="Pay2", anchor=W)
        my_tree.heading("Pay3", text="Pay3", anchor=W)
        my_tree.heading("Pay4", text="Pay4", anchor=W)
        my_tree.heading("Pay5", text="Pay5", anchor=W)
        my_tree.heading("Pay6", text="Pay6", anchor=W)
        my_tree.heading("Pay7", text="Pay7", anchor=W)
        my_tree.heading("Pay8", text="Pay8", anchor=W)
        my_tree.heading("Pay9", text="Pay9", anchor=W)
        my_tree.heading("Pay10", text="Pay10", anchor=W)
        my_tree.heading("Pay11", text="Pay11", anchor=W)
        my_tree.heading("Pay12", text="Pay12", anchor=W)
        my_tree.heading("Pay13", text="Pay13", anchor=W)
        my_tree.heading("Pay14", text="Pay14", anchor=W)
        my_tree.heading("Pay15", text="Pay15", anchor=W)
        my_tree.heading("Pay16", text="Pay16", anchor=W)

    elif name == 'Brio' or name == 'Venezia' or name =='Colibri' or name == 'Colibri(1e)':
        my_tree['columns'] = (
            "Pay1", "Pay2",  "Pay3", "Pay4",  "Pay5",
             "Pay6",  "Pay7", "Pay8")

        # Format Our Columns
        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("Pay1", anchor=W, width=50)
        my_tree.column("Pay2", anchor=W, width=50)
        my_tree.column("Pay3", anchor=W, width=50)
        my_tree.column("Pay4", anchor=W, width=50)
        my_tree.column("Pay5", anchor=W, width=50)
        my_tree.column("Pay6", anchor=W, width=50)
        my_tree.column("Pay7", anchor=W, width=50)
        my_tree.column("Pay8", anchor=W, width=50)


        # Create Headings
        my_tree.heading("#0", text="", anchor=W)
        my_tree.heading("Pay1", text="Pay1", anchor=W)
        my_tree.heading("Pay2", text="Pay2", anchor=W)
        my_tree.heading("Pay3", text="Pay3", anchor=W)
        my_tree.heading("Pay4", text="Pay4", anchor=W)
        my_tree.heading("Pay5", text="Pay5", anchor=W)
        my_tree.heading("Pay6", text="Pay6", anchor=W)
        my_tree.heading("Pay7", text="Pay7", anchor=W)
        my_tree.heading("Pay8", text="Pay8", anchor=W)


    elif name == 'VeneziaLX':
        my_tree['columns'] = (
            "Pay1",  "Pay2",  "Pay3",  "Pay4",  "Pay5",
             "Pay6",  "Pay7",  "Pay8", "Pay9", "Pay10")

        # Format Our Columns
        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("Pay1", anchor=W, width=50)
        my_tree.column("Pay2", anchor=W, width=50)
        my_tree.column("Pay3", anchor=W, width=50)
        my_tree.column("Pay4", anchor=W, width=50)
        my_tree.column("Pay5", anchor=W, width=50)
        my_tree.column("Pay6", anchor=W, width=50)
        my_tree.column("Pay7", anchor=W, width=50)
        my_tree.column("Pay8", anchor=W, width=50)
        my_tree.column("Pay9", anchor=W, width=50)
        my_tree.column("Pay10", anchor=W, width=50)


        # Create Headings
        my_tree.heading("#0", text="", anchor=W)
        my_tree.heading("Pay1", text="Pay1", anchor=W)
        my_tree.heading("Pay2", text="Pay2", anchor=W)
        my_tree.heading("Pay3", text="Pay3", anchor=W)
        my_tree.heading("Pay4", text="Pay4", anchor=W)
        my_tree.heading("Pay5", text="Pay5", anchor=W)
        my_tree.heading("Pay6", text="Pay6", anchor=W)
        my_tree.heading("Pay7", text="Pay7", anchor=W)
        my_tree.heading("Pay8", text="Pay8", anchor=W)
        my_tree.heading("Pay9", text="Pay9", anchor=W)
        my_tree.heading("Pay10", text="Pay10", anchor=W)


    elif name == 'Canto':
        my_tree['columns'] = (
        "Pay2", "Pay3", "Pay4", "Pay5", "Pay6", "Pay7", "Pay8", "Pay9", "Pay10",
        "Pay12", "Pay13", "Pay14", "Pay15", "Pay16", "Pay17", "Pay18", "Pay19", "Pay20",
        "Pay21", "Pay22", "Pay23", "Pay24", "Pay25", "Pay26", "Pay27", "Pay29", "Pay30",
        "Pay31", "Pay32", "Pay33", "Pay34", "Pay35", "Pay36", "Pay37", "Pay38", "Pay39", "Pay40")

        # Format Our Columns
        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("Pay2", anchor=W, width=50)
        my_tree.column("Pay3", anchor=W, width=50)
        my_tree.column("Pay4", anchor=W, width=50)
        my_tree.column("Pay5", anchor=W, width=50)
        my_tree.column("Pay6", anchor=W, width=50)
        my_tree.column("Pay7", anchor=W, width=50)
        my_tree.column("Pay8", anchor=W, width=50)
        my_tree.column("Pay9", anchor=W, width=50)
        my_tree.column("Pay10", anchor=W, width=50)
        my_tree.column("Pay12", anchor=W, width=50)
        my_tree.column("Pay13", anchor=W, width=50)
        my_tree.column("Pay14", anchor=W, width=50)
        my_tree.column("Pay15", anchor=W, width=50)
        my_tree.column("Pay16", anchor=W, width=50)
        my_tree.column("Pay17", anchor=W, width=50)
        my_tree.column("Pay18", anchor=W, width=50)
        my_tree.column("Pay19", anchor=W, width=50)
        my_tree.column("Pay20", anchor=W, width=50)
        my_tree.column("Pay21", anchor=W, width=50)
        my_tree.column("Pay22", anchor=W, width=50)
        my_tree.column("Pay23", anchor=W, width=50)
        my_tree.column("Pay24", anchor=W, width=50)
        my_tree.column("Pay25", anchor=W, width=50)
        my_tree.column("Pay26", anchor=W, width=50)
        my_tree.column("Pay27", anchor=W, width=50)
        my_tree.column("Pay29", anchor=W, width=50)
        my_tree.column("Pay30", anchor=W, width=50)
        my_tree.column("Pay31", anchor=W, width=50)
        my_tree.column("Pay32", anchor=W, width=50)
        my_tree.column("Pay33", anchor=W, width=50)
        my_tree.column("Pay34", anchor=W, width=50)
        my_tree.column("Pay35", anchor=W, width=50)
        my_tree.column("Pay36", anchor=W, width=50)
        my_tree.column("Pay37", anchor=W, width=50)
        my_tree.column("Pay38", anchor=W, width=50)
        my_tree.column("Pay39", anchor=W, width=50)
        my_tree.column("Pay40", anchor=W, width=50)

        # Create Headings
        my_tree.heading("#0", text="", anchor=W)
        my_tree.heading("Pay2", text="Pay2", anchor=W)
        my_tree.heading("Pay3", text="Pay3", anchor=W)
        my_tree.heading("Pay4", text="Pay4", anchor=W)
        my_tree.heading("Pay5", text="Pay5", anchor=W)
        my_tree.heading("Pay6", text="Pay6", anchor=W)
        my_tree.heading("Pay7", text="Pay7", anchor=W)
        my_tree.heading("Pay8", text="Pay8", anchor=W)
        my_tree.heading("Pay9", text="Pay9", anchor=W)
        my_tree.heading("Pay10", text="Pay10", anchor=W)
        my_tree.heading("Pay12", text="Pay12", anchor=W)
        my_tree.heading("Pay13", text="Pay13", anchor=W)
        my_tree.heading("Pay14", text="Pay14", anchor=W)
        my_tree.heading("Pay15", text="Pay15", anchor=W)
        my_tree.heading("Pay16", text="Pay16", anchor=W)
        my_tree.heading("Pay17", text="Pay17", anchor=W)
        my_tree.heading("Pay18", text="Pay18", anchor=W)
        my_tree.heading("Pay19", text="Pay19", anchor=W)
        my_tree.heading("Pay20", text="Pay20", anchor=W)
        my_tree.heading("Pay21", text="Pay21", anchor=W)
        my_tree.heading("Pay22", text="Pay22", anchor=W)
        my_tree.heading("Pay23", text="Pay23", anchor=W)
        my_tree.heading("Pay24", text="Pay24", anchor=W)
        my_tree.heading("Pay25", text="Pay25", anchor=W)
        my_tree.heading("Pay26", text="Pay26", anchor=W)
        my_tree.heading("Pay27", text="Pay27", anchor=W)
        my_tree.heading("Pay29", text="Pay29", anchor=W)
        my_tree.heading("Pay30", text="Pay30", anchor=W)
        my_tree.heading("Pay31", text="Pay31", anchor=W)
        my_tree.heading("Pay32", text="Pay32", anchor=W)
        my_tree.heading("Pay33", text="Pay33", anchor=W)
        my_tree.heading("Pay34", text="Pay34", anchor=W)
        my_tree.heading("Pay35", text="Pay35", anchor=W)
        my_tree.heading("Pay36", text="Pay36", anchor=W)
        my_tree.heading("Pay37", text="Pay37", anchor=W)
        my_tree.heading("Pay38", text="Pay38", anchor=W)
        my_tree.heading("Pay39", text="Pay39", anchor=W)
        my_tree.heading("Pay40", text="Pay40", anchor=W)
    elif name == 'Astro40(1e)' or name == 'Astro40':
        my_tree['columns'] = (
        "Pay1", "Pay2", "Pay3", "Pay4", "Pay5", "Pay6", "Pay7", "Pay8", "Pay9", "Pay10",
        "Pay11", "Pay12", "Pay13", "Pay14", "Pay15", "Pay16", "Pay17", "Pay18",
        "Pay21", "Pay22", "Pay23", "Pay24", "Pay25", "Pay26", "Pay27", "Pay28", "Pay29", "Pay30",
        "Pay31", "Pay32", "Pay33", "Pay34", "Pay35", "Pay36", "Pay37", "Pay38", "Pay39", "Pay40")

        # Format Our Columns
        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("Pay1", anchor=W, width=50)
        my_tree.column("Pay2", anchor=W, width=50)
        my_tree.column("Pay3", anchor=W, width=50)
        my_tree.column("Pay4", anchor=W, width=50)
        my_tree.column("Pay5", anchor=W, width=50)
        my_tree.column("Pay6", anchor=W, width=50)
        my_tree.column("Pay7", anchor=W, width=50)
        my_tree.column("Pay8", anchor=W, width=50)
        my_tree.column("Pay9", anchor=W, width=50)
        my_tree.column("Pay10", anchor=W, width=50)
        my_tree.column("Pay11", anchor=W, width=50)
        my_tree.column("Pay12", anchor=W, width=50)
        my_tree.column("Pay13", anchor=W, width=50)
        my_tree.column("Pay14", anchor=W, width=50)
        my_tree.column("Pay15", anchor=W, width=50)
        my_tree.column("Pay16", anchor=W, width=50)
        my_tree.column("Pay17", anchor=W, width=50)
        my_tree.column("Pay18", anchor=W, width=50)
        my_tree.column("Pay21", anchor=W, width=50)
        my_tree.column("Pay22", anchor=W, width=50)
        my_tree.column("Pay23", anchor=W, width=50)
        my_tree.column("Pay24", anchor=W, width=50)
        my_tree.column("Pay25", anchor=W, width=50)
        my_tree.column("Pay26", anchor=W, width=50)
        my_tree.column("Pay27", anchor=W, width=50)
        my_tree.column("Pay28", anchor=W, width=50)
        my_tree.column("Pay29", anchor=W, width=50)
        my_tree.column("Pay30", anchor=W, width=50)
        my_tree.column("Pay31", anchor=W, width=50)
        my_tree.column("Pay32", anchor=W, width=50)
        my_tree.column("Pay33", anchor=W, width=50)
        my_tree.column("Pay34", anchor=W, width=50)
        my_tree.column("Pay35", anchor=W, width=50)
        my_tree.column("Pay36", anchor=W, width=50)
        my_tree.column("Pay37", anchor=W, width=50)
        my_tree.column("Pay38", anchor=W, width=50)
        my_tree.column("Pay39", anchor=W, width=50)
        my_tree.column("Pay40", anchor=W, width=50)

        # Create Headings
        my_tree.heading("#0", text="", anchor=W)
        my_tree.heading("Pay1", text="Pay1", anchor=W)
        my_tree.heading("Pay2", text="Pay2", anchor=W)
        my_tree.heading("Pay3", text="Pay3", anchor=W)
        my_tree.heading("Pay4", text="Pay4", anchor=W)
        my_tree.heading("Pay5", text="Pay5", anchor=W)
        my_tree.heading("Pay6", text="Pay6", anchor=W)
        my_tree.heading("Pay7", text="Pay7", anchor=W)
        my_tree.heading("Pay8", text="Pay8", anchor=W)
        my_tree.heading("Pay9", text="Pay9", anchor=W)
        my_tree.heading("Pay10", text="Pay10", anchor=W)
        my_tree.heading("Pay11", text="Pay11", anchor=W)
        my_tree.heading("Pay12", text="Pay12", anchor=W)
        my_tree.heading("Pay13", text="Pay13", anchor=W)
        my_tree.heading("Pay14", text="Pay14", anchor=W)
        my_tree.heading("Pay15", text="Pay15", anchor=W)
        my_tree.heading("Pay16", text="Pay16", anchor=W)
        my_tree.heading("Pay17", text="Pay17", anchor=W)
        my_tree.heading("Pay18", text="Pay18", anchor=W)
        my_tree.heading("Pay21", text="Pay21", anchor=W)
        my_tree.heading("Pay22", text="Pay22", anchor=W)
        my_tree.heading("Pay23", text="Pay23", anchor=W)
        my_tree.heading("Pay24", text="Pay24", anchor=W)
        my_tree.heading("Pay25", text="Pay25", anchor=W)
        my_tree.heading("Pay26", text="Pay26", anchor=W)
        my_tree.heading("Pay27", text="Pay27", anchor=W)
        my_tree.heading("Pay28", text="Pay28", anchor=W)
        my_tree.heading("Pay29", text="Pay29", anchor=W)
        my_tree.heading("Pay30", text="Pay30", anchor=W)
        my_tree.heading("Pay31", text="Pay31", anchor=W)
        my_tree.heading("Pay32", text="Pay32", anchor=W)
        my_tree.heading("Pay33", text="Pay33", anchor=W)
        my_tree.heading("Pay34", text="Pay34", anchor=W)
        my_tree.heading("Pay35", text="Pay35", anchor=W)
        my_tree.heading("Pay36", text="Pay36", anchor=W)
        my_tree.heading("Pay37", text="Pay37", anchor=W)
        my_tree.heading("Pay38", text="Pay38", anchor=W)
        my_tree.heading("Pay39", text="Pay39", anchor=W)
        my_tree.heading("Pay40", text="Pay40", anchor=W)
    elif name == 'Astro40(s)':
        my_tree['columns'] = (
        "Pay1", "Pay2", "Pay3", "Pay4", "Pay5", "Pay6", "Pay7", "Pay8", "Pay9", "Pay10",
        "Pay11", "Pay12", "Pay13", "Pay14", "Pay15", "Pay16", "Pay17", "Pay18")

        # Format Our Columns
        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("Pay1", anchor=W, width=50)
        my_tree.column("Pay2", anchor=W, width=50)
        my_tree.column("Pay3", anchor=W, width=50)
        my_tree.column("Pay4", anchor=W, width=50)
        my_tree.column("Pay5", anchor=W, width=50)
        my_tree.column("Pay6", anchor=W, width=50)
        my_tree.column("Pay7", anchor=W, width=50)
        my_tree.column("Pay8", anchor=W, width=50)
        my_tree.column("Pay9", anchor=W, width=50)
        my_tree.column("Pay10", anchor=W, width=50)
        my_tree.column("Pay11", anchor=W, width=50)
        my_tree.column("Pay12", anchor=W, width=50)
        my_tree.column("Pay13", anchor=W, width=50)
        my_tree.column("Pay14", anchor=W, width=50)
        my_tree.column("Pay15", anchor=W, width=50)
        my_tree.column("Pay16", anchor=W, width=50)
        my_tree.column("Pay17", anchor=W, width=50)
        my_tree.column("Pay18", anchor=W, width=50)

        # Create Headings
        my_tree.heading("#0", text="", anchor=W)
        my_tree.heading("Pay1", text="Pay1", anchor=W)
        my_tree.heading("Pay2", text="Pay2", anchor=W)
        my_tree.heading("Pay3", text="Pay3", anchor=W)
        my_tree.heading("Pay4", text="Pay4", anchor=W)
        my_tree.heading("Pay5", text="Pay5", anchor=W)
        my_tree.heading("Pay6", text="Pay6", anchor=W)
        my_tree.heading("Pay7", text="Pay7", anchor=W)
        my_tree.heading("Pay8", text="Pay8", anchor=W)
        my_tree.heading("Pay9", text="Pay9", anchor=W)
        my_tree.heading("Pay10", text="Pay10", anchor=W)
        my_tree.heading("Pay11", text="Pay11", anchor=W)
        my_tree.heading("Pay12", text="Pay12", anchor=W)
        my_tree.heading("Pay13", text="Pay13", anchor=W)
        my_tree.heading("Pay14", text="Pay14", anchor=W)
        my_tree.heading("Pay15", text="Pay15", anchor=W)
        my_tree.heading("Pay16", text="Pay16", anchor=W)
        my_tree.heading("Pay17", text="Pay17", anchor=W)
        my_tree.heading("Pay18", text="Pay18", anchor=W)

    elif name == 'Astro35':
        my_tree['columns'] = (
        "Pay1", "Pay2", "Pay3", "Pay4", "Pay5", "Pay6", "Pay7", "Pay8", "Pay9", "Pay10",
        "Pay11", "Pay12", "Pay13", "Pay14", "Pay15", "Pay16", "Pay17", "Pay18",
        "Pay21", "Pay22", "Pay23", "Pay24", "Pay25", "Pay26", "Pay27", "Pay28", "Pay29", "Pay30",
        "Pay31", "Pay32", "Pay33", "Pay34", "Pay35")

        # Format Our Columns
        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("Pay1", anchor=W, width=50)
        my_tree.column("Pay2", anchor=W, width=50)
        my_tree.column("Pay3", anchor=W, width=50)
        my_tree.column("Pay4", anchor=W, width=50)
        my_tree.column("Pay5", anchor=W, width=50)
        my_tree.column("Pay6", anchor=W, width=50)
        my_tree.column("Pay7", anchor=W, width=50)
        my_tree.column("Pay8", anchor=W, width=50)
        my_tree.column("Pay9", anchor=W, width=50)
        my_tree.column("Pay10", anchor=W, width=50)
        my_tree.column("Pay11", anchor=W, width=50)
        my_tree.column("Pay12", anchor=W, width=50)
        my_tree.column("Pay13", anchor=W, width=50)
        my_tree.column("Pay14", anchor=W, width=50)
        my_tree.column("Pay15", anchor=W, width=50)
        my_tree.column("Pay16", anchor=W, width=50)
        my_tree.column("Pay17", anchor=W, width=50)
        my_tree.column("Pay18", anchor=W, width=50)
        my_tree.column("Pay21", anchor=W, width=50)
        my_tree.column("Pay22", anchor=W, width=50)
        my_tree.column("Pay23", anchor=W, width=50)
        my_tree.column("Pay24", anchor=W, width=50)
        my_tree.column("Pay25", anchor=W, width=50)
        my_tree.column("Pay26", anchor=W, width=50)
        my_tree.column("Pay27", anchor=W, width=50)
        my_tree.column("Pay28", anchor=W, width=50)
        my_tree.column("Pay29", anchor=W, width=50)
        my_tree.column("Pay30", anchor=W, width=50)
        my_tree.column("Pay31", anchor=W, width=50)
        my_tree.column("Pay32", anchor=W, width=50)
        my_tree.column("Pay33", anchor=W, width=50)
        my_tree.column("Pay34", anchor=W, width=50)
        my_tree.column("Pay35", anchor=W, width=50)

        # Create Headings
        my_tree.heading("#0", text="", anchor=W)
        my_tree.heading("Pay1", text="Pay1", anchor=W)
        my_tree.heading("Pay2", text="Pay2", anchor=W)
        my_tree.heading("Pay3", text="Pay3", anchor=W)
        my_tree.heading("Pay4", text="Pay4", anchor=W)
        my_tree.heading("Pay5", text="Pay5", anchor=W)
        my_tree.heading("Pay6", text="Pay6", anchor=W)
        my_tree.heading("Pay7", text="Pay7", anchor=W)
        my_tree.heading("Pay8", text="Pay8", anchor=W)
        my_tree.heading("Pay9", text="Pay9", anchor=W)
        my_tree.heading("Pay10", text="Pay10", anchor=W)
        my_tree.heading("Pay11", text="Pay11", anchor=W)
        my_tree.heading("Pay12", text="Pay12", anchor=W)
        my_tree.heading("Pay13", text="Pay13", anchor=W)
        my_tree.heading("Pay14", text="Pay14", anchor=W)
        my_tree.heading("Pay15", text="Pay15", anchor=W)
        my_tree.heading("Pay16", text="Pay16", anchor=W)
        my_tree.heading("Pay17", text="Pay17", anchor=W)
        my_tree.heading("Pay18", text="Pay18", anchor=W)
        my_tree.heading("Pay21", text="Pay21", anchor=W)
        my_tree.heading("Pay22", text="Pay22", anchor=W)
        my_tree.heading("Pay23", text="Pay23", anchor=W)
        my_tree.heading("Pay24", text="Pay24", anchor=W)
        my_tree.heading("Pay25", text="Pay25", anchor=W)
        my_tree.heading("Pay26", text="Pay26", anchor=W)
        my_tree.heading("Pay27", text="Pay27", anchor=W)
        my_tree.heading("Pay28", text="Pay28", anchor=W)
        my_tree.heading("Pay29", text="Pay29", anchor=W)
        my_tree.heading("Pay30", text="Pay30", anchor=W)
        my_tree.heading("Pay31", text="Pay31", anchor=W)
        my_tree.heading("Pay32", text="Pay32", anchor=W)
        my_tree.heading("Pay33", text="Pay33", anchor=W)
        my_tree.heading("Pay34", text="Pay34", anchor=W)
        my_tree.heading("Pay35", text="Pay35", anchor=W)
def record_something3(records,my_tree,count):
    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(record[1], record[2]),
                           tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(record[1], record[2]),
                           tags=('oddrow',))
        # increment counter
        count += 1
def unique_tree3(my_tree):
    my_tree['columns'] = ("Day", "Promet")

    # Format Our Columns
    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("Day", anchor=W, width=50)
    my_tree.column("Promet", anchor=W, width=50)

    # Create Headings
    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("Day", text="Day", anchor=W)
    my_tree.heading("Promet", text="Promet", anchor=W)