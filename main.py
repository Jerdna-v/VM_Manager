import datetime
import email
import imaplib
import mimetypes
import os
import re
from tkinter import Toplevel, Label, Entry, Button, messagebox

from bs4 import BeautifulSoup

from test import Machine

username = 'kafematisan@gmail.com'
password = 'KafematiSan120'

mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(username, password)
def everything():
    top = Toplevel()
    l = Label(top,text="Mail")
    l.pack()
    e = Entry(top)
    e.pack()
    def neshto():
        if e.get() == '':
            mail.select('Inbox')
        else:
            mail.select(e.get())
        top.destroy()
        result, data = mail.uid('search', None, "ALL")
        inbox_item_list = data[0].split()

        for item in inbox_item_list:
            result2, email_data = mail.uid('fetch', item, '(RFC822)')
            raw_email = email_data[0][1].decode("utf-8")
            email_message = email.message_from_string((raw_email))
            subject_ = email_message['Subject']
            from_ = email_message['From']
            date_ = email_message['Date']
            datefrom = date_ + from_
            datefrom_tupl = re.compile(r'(\d{2}:\d{2}:\d{2})|(\d{1,2}\s\w{3}\s\d{4})|(\w+\D{1}\w+@\w+.com)').findall(
                datefrom)
            for tupl in datefrom_tupl:
                if tupl[0] != '':
                    time_ = datetime.datetime.strptime(tupl[0], '%H:%M:%S').strftime('%H:%M:%S').replace(':', '-')
                if tupl[1] != '':
                    date_ = tupl[1]
                if tupl[2] != '':
                    from_ = tupl[2]
            counter = 1
            for part in email_message.walk():
                if part.get_content_maintype() == 'multipart':
                    continue
                filename = part.get_filename()
                content_type = part.get_content_type()
                if not filename:
                    ext = mimetypes.guess_extension(content_type)
                    if not ext:
                        ext = 'bin'
                    if 'text' in content_type:
                        ext = '.txt'
                    elif 'html' in content_type:
                        ext = '.html'
                    filename = f'{time_}-{from_}{ext}'
                counter += 1
            save_path = os.path.join(os.getcwd(), "emails", date_)
            if not os.path.exists(save_path):
                os.makedirs(save_path)
            with open(os.path.join(save_path, filename), 'wb') as fp:
                fp.write(part.get_payload(decode=True))
            with open(os.path.join(save_path, filename)) as markup:
                try:
                    soup= BeautifulSoup(markup.read(), features="html.parser").get_text()
                except UnicodeError:
                    messagebox.showerror(title="Error", message='Ima mejl so problemi')
                    continue
            with open(os.path.join(save_path, filename), "w") as f:
                for char in '@', '^M', '\n', '^', ' ', 'Â', '�', '#', '�':
                    soup = soup.replace(char, '')
                f.write(soup)
            Tester = Machine(from_, date_, soup)
            try:
                Tester.size_identifier()
                Tester.data_sorter()
                Tester.table_auth()
                Tester.table_machine()
                Tester.table_email()
                Tester.price_setter()
                Tester.promet_setter()
            except Exception:
                messagebox.showerror(title="Error", message=f'Ima mashina so problemi: {subject_}')
                continue
    b = Button(top,text="Start", command = neshto)
    b.pack()
    # mail.create('new')

