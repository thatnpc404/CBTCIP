from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle


class GenerateReceipt:
    def __init__(self):
        self.c = canvas.Canvas("receipt.pdf","C:\\Users\\shrey\\OneDrive\\Desktop")
        self.c.setPageSize((300, 500))
        self.c.rect(10, 10, 280, 480)
        self.c.setTitle("Computer Generated Receipt")
        self.c.drawString(120, 400,'Ratiborus.inc')
        self.c.setFontSize(8)
        self.c.drawString(128, 390,'Kempegowda')
        self.c.drawString(132, 380,'Bangalore')
        self.c.setFontSize(12)

        self.style = TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),         
        ('GRID', (0, 0), (-1, -1), 1, colors.black)  ,
        ('FONTSIZE', (0, 0), (-1, -1), 12),    
        ])

    def defaultReceipt(self):
        data =[
            ['Receipt number', '12345678'],
            ['Transaction id', '21353737'],
            ['Merchant id', '8844448DDS'],
            ['Amount', 'Rs. 489/-'],
            ['Mode of payment', 'UPI'],
            ['Date', '01/01/2001'],
            ]

        
        table = Table(data)
        table.setStyle(self.style)
        table.wrapOn(self.c,60,190)
        table.drawOn(self.c, 60, 190)
        self.c.drawString(70, 120, "Thank you for shopping with us :)")
        self.c.setFontSize(8)
        self.c.drawString(85, 100, "This is a computer generated receipt")
        self.c.save()
        print("Receipt stored as 'receipt.pdf'")

    def userReceipt(self):
        rno=input("Enter receipt number :")
        tid=input("Enter transaction id : ")
        mid=input("Enter merchant id : ")
        amount='Rs. '+input("Enter amount : ")+'/-'
        mop=input("Enter mode of payment : ")
        date=input("Enter date : ")

        data =[
            ['Receipt number', rno],
            ['Transaction id', tid],
            ['Merchant id', mid],
            ['Amount', amount],
            ['Mode of payment',mop],
            ['Date', date],
            ]


        table = Table(data)
        table.setStyle(self.style)
        table.wrapOn(self.c,60,190)
        table.drawOn(self.c, 60, 190)
        self.c.drawString(70, 120, "Thank you for shopping with us :)")
        self.c.setFontSize(8)
        self.c.drawString(85, 100, "This is a computer generated receipt")
        self.c.save()
        print("Receipt stored as 'receipt.pdf'")



R=GenerateReceipt()
print("1: Default receipt\n2: User defined receipt")
i=input("Enter 1 for default receipt and 2 for user defined receipt : ")
if i=='1':
    R.defaultReceipt()
elif i=='2':
    R.userReceipt()
else:
    print("Enter a valid input")








