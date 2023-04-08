import datetime
import sqlite3
from tkinter import *
from tkinter import messagebox
from fpdf import FPDF
from tkcalendar import DateEntry
from PIL import Image, ImageTk
from tkinter import filedialog

hotel_exemplo1 = {
    "titulo": "ORÇAMENTO",
    "nome_empresa": "HOTEL MAR ABERTO",
    "site_empresa": "www.hotelmaraberto.com",
    "whatsapp_empresa": "(88) 8888-8888",
    "email_empresa": "reservas@hotelmaraberto.com",
    "end_empresa": "Rua das Flores, Centro",
    "cidade_estado": "Cidade - ES"
}
hotel_exemplo2 = {
    "titulo": "ORÇAMENTO",
    "nome_empresa": "HOTEL PARADISE FLAT",
    "site_empresa": "www.hotelparadiseflat.com",
    "whatsapp_empresa": "(88) 9999-9999",
    "email_empresa": "reservas@hotelparadiseflat.com",
    "end_empresa": "Rua das Pedras, Centro",
    "cidade_estado": "Cidade - ES"
}

root = Tk()


class LinhasDeEntrada:
    def __init__(self):
        self.entry_diaria_l5 = None
        self.entry_qtd_l5 = None
        self.bt_nova_linha4 = None
        self.entry_diaria_l4 = None
        self.entry_qtd_l4 = None
        self.lb_diaria_l4 = None
        self.lb_quarto_l4 = None
        self.lb_qtd_l4 = None
        self.bt_nova_linha3 = None
        self.entry_diaria_l3 = None
        self.entry_qtd_l3 = None
        self.lb_diaria_l3 = None
        self.lb_quarto_l3 = None
        self.lb_qtd_l3 = None
        self.bt_nova_linha = None
        self.bt_nova_linha2 = None
        self.entry_diaria_l2 = None
        self.entry_qtd_l2 = None
        self.lb_diaria_l2 = None
        self.lb_quarto_l2 = None
        self.lb_qtd_l2 = None

    def linha2_hotel1(self):
        self.entry_qtd_l2 = Entry(self.hotel1)
        self.entry_qtd_l2.place(relx=0.025, rely=0.50, relwidth=0.12, relheight=0.06)
        self.quarto_select_l2.place(relx=0.17, rely=0.50, relwidth=0.45, relheight=0.06)
        self.entry_diaria_l2 = Entry(self.hotel1)
        self.entry_diaria_l2.place(relx=0.65, rely=0.50, relwidth=0.15, relheight=0.06)
        self.bt_nova_linha2 = Button(self.hotel1, text='+', font=('Aria', 12, 'bold'), command=self.linha3_hotel1)
        self.bt_nova_linha2.place(relx=0.85, rely=0.50, relwidth=0.04, relheight=0.06)
        self.bt_nova_linha = Button(self.hotel1, text='+', font=('Aria', 12, 'bold'), state=DISABLED)
        self.bt_nova_linha.place(relx=0.85, rely=0.41, relwidth=0.04, relheight=0.06)

    def linha3_hotel1(self):
        self.entry_qtd_l3 = Entry(self.hotel1)
        self.entry_qtd_l3.place(relx=0.025, rely=0.59, relwidth=0.12, relheight=0.06)
        self.quarto_select_l3.place(relx=0.17, rely=0.59, relwidth=0.45, relheight=0.06)
        self.entry_diaria_l3 = Entry(self.hotel1)
        self.entry_diaria_l3.place(relx=0.65, rely=0.59, relwidth=0.15, relheight=0.06)
        self.bt_nova_linha3 = Button(self.hotel1, text='+', font=('Aria', 12, 'bold'), command=self.linha4_hotel1)
        self.bt_nova_linha3.place(relx=0.85, rely=0.59, relwidth=0.04, relheight=0.06)
        self.bt_nova_linha2 = Button(self.hotel1, text='+', font=('Aria', 12, 'bold'), state=DISABLED)
        self.bt_nova_linha2.place(relx=0.85, rely=0.50, relwidth=0.04, relheight=0.06)

    def linha4_hotel1(self):
        self.entry_qtd_l4 = Entry(self.hotel1)
        self.entry_qtd_l4.place(relx=0.025, rely=0.68, relwidth=0.12, relheight=0.06)
        self.quarto_select_l4.place(relx=0.17, rely=0.68, relwidth=0.45, relheight=0.06)
        self.entry_diaria_l4 = Entry(self.hotel1)
        self.entry_diaria_l4.place(relx=0.65, rely=0.68, relwidth=0.15, relheight=0.06)
        self.bt_nova_linha4 = Button(self.hotel1, text='+', font=('Aria', 12, 'bold'), command=self.linha5_hotel1)
        self.bt_nova_linha4.place(relx=0.85, rely=0.68, relwidth=0.04, relheight=0.06)
        self.bt_nova_linha3 = Button(self.hotel1, text='+', font=('Aria', 12, 'bold'), state=DISABLED)
        self.bt_nova_linha3.place(relx=0.85, rely=0.59, relwidth=0.04, relheight=0.06)

    def linha5_hotel1(self):
        self.entry_qtd_l5 = Entry(self.hotel1)
        self.entry_qtd_l5.place(relx=0.025, rely=0.77, relwidth=0.12, relheight=0.06)
        self.quarto_select_l5.place(relx=0.17, rely=0.77, relwidth=0.45, relheight=0.06)
        self.entry_diaria_l5 = Entry(self.hotel1)
        self.entry_diaria_l5.place(relx=0.65, rely=0.77, relwidth=0.15, relheight=0.06)
        self.bt_nova_linha4 = Button(self.hotel1, text='+', font=('Aria', 12, 'bold'), state=DISABLED)
        self.bt_nova_linha4.place(relx=0.85, rely=0.68, relwidth=0.04, relheight=0.06)


class Funcoes(LinhasDeEntrada):
    def __init__(self):
        super().__init__()
        self.nome_arquivo_padrao = None
        self.lb_logo_hotel = None
        self.logo_aberta_hotel = None
        self.logo_hotel = None
        self.email_empresa = None
        self.end_empresa = None
        self.telefone_empresa = None
        self.nome_hotel = None
        self.pdf = None
        self.totalfinal = None
        self.subtotal = None
        self.texto_total1 = None
        self.texto_total2 = None
        self.texto_total3 = None
        self.texto_total4 = None
        self.texto_total5 = None
        self.soma_totais = None
        self.total_l1 = None
        self.total_l2 = None
        self.total_l3 = None
        self.total_l4 = None
        self.total_l5 = None
        self.resultado_data = None
        self.data_checkout_texto = None
        self.data_checkin_texto = None
        self.data_checkout = None
        self.data_checkin = None
        self.texto_valor_diaria5 = None
        self.texto_valor_diaria4 = None
        self.texto_valor_diaria3 = None
        self.texto_valor_diaria2 = None
        self.texto_valor_diaria1 = None
        self.valor_diaria1 = None
        self.valor_diaria2 = 0
        self.valor_diaria3 = 0
        self.valor_diaria4 = 0
        self.valor_diaria5 = 0
        self.nome_quarto1 = None
        self.nome_quarto2 = ""
        self.nome_quarto3 = ""
        self.nome_quarto4 = ""
        self.nome_quarto5 = ""
        self.quantidade1 = None
        self.quantidade2 = 0
        self.quantidade3 = 0
        self.quantidade4 = 0
        self.quantidade5 = 0
        self.nome_cli = None
        self.hoje = None
        self.numero_formatado = None
        self.numero = None
        self.linha_db = None
        self.cursor = None
        self.banco = None
        self.opcao_hotel = None
        self.dados_hotel = None
        self.entry_quarto_l1 = None
        self.entry_quarto_l2 = None
        self.entry_quarto_l3 = None
        self.entry_quarto_l4 = None
        self.entry_quarto_l5 = None
        self.quarto_select_l1 = None
        self.quarto_select_l2 = None
        self.quarto_select_l3 = None
        self.quarto_select_l4 = None
        self.quarto_select_l5 = None

    def incui_dados_empresa(self):
        if self.opcao_hotel == 'Hotel Mar Aberto':
            self.bt_nova_linha = Button(self.hotel1, text='+', font=('Aria', 12, 'bold'), command=self.linha2_hotel1)
            self.bt_nova_linha.place(relx=0.85, rely=0.41, relwidth=0.04, relheight=0.06)
            self.dados_hotel = Label(self.hotel1, text=f'''                                                                                                            
                                                {hotel_exemplo1["nome_empresa"]}
                                                {hotel_exemplo1["site_empresa"]}
                                                {hotel_exemplo1["email_empresa"]}
                                                {hotel_exemplo1["end_empresa"]}
                                                {hotel_exemplo1["cidade_estado"]}
                                                ''', justify=LEFT)
            self.dados_hotel.place(relx=0.5, rely=0.025, relwidth=0.4, relheight=0.25)
            self.entry_quarto_l1 = StringVar(self.hotel1)
            self.entry_quarto_l1.set('Escolha a Categoria de Quarto')
            self.quarto_select_l1 = OptionMenu(self.hotel1, self.entry_quarto_l1,
                                               "Single Com Varanda Térreo",
                                               "Duplo Com varanda Térreo",
                                               "Triplo Com varanda Térreo",
                                               "Quadruplo Com varanda Térreo",
                                               "Single Com Varanda Superior",
                                               "Duplo Com varanda Superior",
                                               "Triplo Com varanda Superior",
                                               "Quadruplo Com varanda Superior"
                                               )
            self.quarto_select_l1.place(relx=0.17, rely=0.41, relwidth=0.45, relheight=0.06)
            self.entry_quarto_l2 = StringVar(self.hotel1)
            self.entry_quarto_l2.set('Escolha a Categoria de Quarto')
            self.quarto_select_l2 = OptionMenu(self.hotel1, self.entry_quarto_l2,
                                               "Single Com Varanda Térreo",
                                               "Duplo Com varanda Térreo",
                                               "Triplo Com varanda Térreo",
                                               "Quadruplo Com varanda Térreo",
                                               "Single Com Varanda Superior",
                                               "Duplo Com varanda Superior",
                                               "Triplo Com varanda Superior",
                                               "Quadruplo Com varanda Superior"
                                               )
            self.entry_quarto_l3 = StringVar(self.hotel1)
            self.entry_quarto_l3.set('Escolha a Categoria de Quarto')
            self.quarto_select_l3 = OptionMenu(self.hotel1, self.entry_quarto_l3,
                                               "Single Com Varanda Térreo",
                                               "Duplo Com varanda Térreo",
                                               "Triplo Com varanda Térreo",
                                               "Quadruplo Com varanda Térreo",
                                               "Single Com Varanda Superior",
                                               "Duplo Com varanda Superior",
                                               "Triplo Com varanda Superior",
                                               "Quadruplo Com varanda Superior"
                                               )
            self.entry_quarto_l4 = StringVar(self.hotel1)
            self.entry_quarto_l4.set('Escolha a Categoria de Quarto')
            self.quarto_select_l4 = OptionMenu(self.hotel1, self.entry_quarto_l4,
                                               "Single Com Varanda Térreo",
                                               "Duplo Com varanda Térreo",
                                               "Triplo Com varanda Térreo",
                                               "Quadruplo Com varanda Térreo",
                                               "Single Com Varanda Superior",
                                               "Duplo Com varanda Superior",
                                               "Triplo Com varanda Superior",
                                               "Quadruplo Com varanda Superior"
                                               )
            self.entry_quarto_l5 = StringVar(self.hotel1)
            self.entry_quarto_l5.set('Escolha a Categoria de Quarto')
            self.quarto_select_l5 = OptionMenu(self.hotel1, self.entry_quarto_l5,
                                               "Single Com Varanda Térreo",
                                               "Duplo Com varanda Térreo",
                                               "Triplo Com varanda Térreo",
                                               "Quadruplo Com varanda Térreo",
                                               "Single Com Varanda Superior",
                                               "Duplo Com varanda Superior",
                                               "Triplo Com varanda Superior",
                                               "Quadruplo Com varanda Superior"
                                               )
            self.nome_hotel = hotel_exemplo1["nome_empresa"]
            self.telefone_empresa = hotel_exemplo1["whatsapp_empresa"]
            self.end_empresa = hotel_exemplo1["end_empresa"]
            self.email_empresa = hotel_exemplo1["email_empresa"]
            self.logo_hotel = Image.open("icons/logo_mar_aberto.png")
            self.logo_aberta_hotel = ImageTk.PhotoImage(self.logo_hotel)
            self.lb_logo_hotel = Label(image=self.logo_aberta_hotel)
            self.lb_logo_hotel.place(relx=0.48, rely=0.06, relwidth=0.18, relheight=0.2)

        if self.opcao_hotel == 'Hotel Paradise Flat':
            self.bt_nova_linha = Button(self.hotel1, text='+', font=('Aria', 12, 'bold'), command=self.linha2_hotel1)
            self.bt_nova_linha.place(relx=0.85, rely=0.41, relwidth=0.04, relheight=0.06)
            self.dados_hotel = Label(self.hotel1, text=f'''                                                                                                            
                                                {hotel_exemplo2["nome_empresa"]}
                                                {hotel_exemplo2["site_empresa"]}
                                                {hotel_exemplo2["email_empresa"]}
                                                {hotel_exemplo2["end_empresa"]}
                                                {hotel_exemplo2["cidade_estado"]}
                                                ''', justify=LEFT)
            self.dados_hotel.place(relx=0.5, rely=0.025, relwidth=0.4, relheight=0.25)
            self.entry_quarto_l1 = StringVar(self.hotel1)
            self.entry_quarto_l1.set('Escolha a Categoria de Quarto')
            self.quarto_select_l1 = OptionMenu(self.hotel1, self.entry_quarto_l1,
                                               "Single Com Varanda Térreo",
                                               "Duplo Com varanda Térreo",
                                               "Triplo Com varanda Térreo",
                                               "Quadruplo Com varanda Térreo",
                                               "Single Com Varanda Superior",
                                               "Duplo Com varanda Superior",
                                               "Triplo Com varanda Superior",
                                               "Quadruplo Com varanda Superior"
                                               )
            self.quarto_select_l1.place(relx=0.17, rely=0.41, relwidth=0.45, relheight=0.06)
            self.entry_quarto_l2 = StringVar(self.hotel1)
            self.entry_quarto_l2.set('Escolha a Categoria de Quarto')
            self.quarto_select_l2 = OptionMenu(self.hotel1, self.entry_quarto_l2,
                                               "Single Com Varanda Térreo",
                                               "Duplo Com varanda Térreo",
                                               "Triplo Com varanda Térreo",
                                               "Quadruplo Com varanda Térreo",
                                               "Single Com Varanda Superior",
                                               "Duplo Com varanda Superior",
                                               "Triplo Com varanda Superior",
                                               "Quadruplo Com varanda Superior"
                                               )
            self.entry_quarto_l3 = StringVar(self.hotel1)
            self.entry_quarto_l3.set('Escolha a Categoria de Quarto')
            self.quarto_select_l3 = OptionMenu(self.hotel1, self.entry_quarto_l3,
                                               "Single Com Varanda Térreo",
                                               "Duplo Com varanda Térreo",
                                               "Triplo Com varanda Térreo",
                                               "Quadruplo Com varanda Térreo",
                                               "Single Com Varanda Superior",
                                               "Duplo Com varanda Superior",
                                               "Triplo Com varanda Superior",
                                               "Quadruplo Com varanda Superior"
                                               )
            self.entry_quarto_l4 = StringVar(self.hotel1)
            self.entry_quarto_l4.set('Escolha a Categoria de Quarto')
            self.quarto_select_l4 = OptionMenu(self.hotel1, self.entry_quarto_l4,
                                               "Single Com Varanda Térreo",
                                               "Duplo Com varanda Térreo",
                                               "Triplo Com varanda Térreo",
                                               "Quadruplo Com varanda Térreo",
                                               "Single Com Varanda Superior",
                                               "Duplo Com varanda Superior",
                                               "Triplo Com varanda Superior",
                                               "Quadruplo Com varanda Superior"
                                               )
            self.entry_quarto_l5 = StringVar(self.hotel1)
            self.entry_quarto_l5.set('Escolha a Categoria de Quarto')
            self.quarto_select_l5 = OptionMenu(self.hotel1, self.entry_quarto_l5,
                                               "Single Com Varanda Térreo",
                                               "Duplo Com varanda Térreo",
                                               "Triplo Com varanda Térreo",
                                               "Quadruplo Com varanda Térreo",
                                               "Single Com Varanda Superior",
                                               "Duplo Com varanda Superior",
                                               "Triplo Com varanda Superior",
                                               "Quadruplo Com varanda Superior"
                                               )
            self.nome_hotel = hotel_exemplo2["nome_empresa"]
            self.telefone_empresa = hotel_exemplo2["whatsapp_empresa"]
            self.end_empresa = hotel_exemplo2["end_empresa"]
            self.email_empresa = hotel_exemplo2["email_empresa"]
            self.logo_hotel = Image.open("icons/logo_paradise_flat.png")
            self.logo_aberta_hotel = ImageTk.PhotoImage(self.logo_hotel)
            self.lb_logo_hotel = Label(image=self.logo_aberta_hotel)
            self.lb_logo_hotel.place(relx=0.48, rely=0.06, relwidth=0.18, relheight=0.2)

    def pegar_hotel(self):
        try:
            self.opcao_hotel = self.entry_hotel.get()

        except Exception:
            pass
        try:
            self.incui_dados_empresa()
        except Exception:
            messagebox.showerror("Erro", "Erro ao Incluir os dados")

    def numero_orcamento_db(self):
        self.banco = sqlite3.connect('bd/numero_do_orcamento.db')
        self.cursor = self.banco.cursor()
        self.cursor.execute('SELECT numero FROM num_orcamento')
        self.linha_db = self.cursor.fetchone()
        self.numero = self.linha_db[0] + 1
        self.numero_formatado = f"{self.numero:05}"
        # Salva o novo número no banco de dados
        self.banco.execute('UPDATE num_orcamento SET numero = ?', (self.numero,))
        self.banco.commit()
        return self.numero_formatado

    def data_atual(self):
        """Retorna a data atual no formato brasileiro"""
        # Obtém a data atual e formata a data no formato brasileiro (dd/mm/aaaa)
        self.hoje = datetime.date.today().strftime('%d/%m/%Y')

        return self.hoje

    def limpa_tela(self):
        try:
            self.entry_cliente.delete(0, END)
            self.entry_checkin.delete(0, END)
            self.entry_checkout.delete(0, END)
            self.entry_qtd_l1.delete(0, END)
            self.entry_diaria_l1.delete(0, END)
            self.entry_qtd_l2.delete(0, END)
            self.entry_diaria_l2.delete(0, END)
            self.entry_qtd_l3.delete(0, END)
            self.entry_diaria_l3.delete(0, END)
            self.entry_qtd_l4.delete(0, END)
            self.entry_diaria_l4.delete(0, END)
        except Exception:
            pass

    def gerar_orcamento(self):
        try:
            self.nome_cli = self.entry_cliente.get()
            self.quantidade1 = int(self.entry_qtd_l1.get())
            self.nome_quarto1 = self.entry_quarto_l1.get()
            self.valor_diaria1 = self.entry_diaria_l1.get().replace(".", "_").replace(",", ".")
            self.valor_diaria1 = float(self.valor_diaria1)
        except Exception:
            messagebox.showerror("Erro", "Algumas informações não foram fornecidas!")
        try:
            self.valor_diaria2 = self.entry_diaria_l2.get().replace(".", "_").replace(",", ".")
            if self.valor_diaria2 == "":
                self.valor_diaria2 = 0
            self.valor_diaria2 = float(self.valor_diaria2)
            self.nome_quarto2 = self.entry_quarto_l2.get()
            self.quantidade2 = int(self.entry_qtd_l2.get())
        except Exception:
            pass

        try:
            self.valor_diaria3 = self.entry_diaria_l3.get().replace(".", "_").replace(",", ".")
            if self.valor_diaria3 == "":
                self.valor_diaria3 = 0
            self.valor_diaria3 = float(self.valor_diaria3)
            self.nome_quarto3 = self.entry_quarto_l3.get()
            self.quantidade3 = int(self.entry_qtd_l3.get())
        except Exception:
            pass
        try:
            self.valor_diaria4 = self.entry_diaria_l4.get().replace(".", "_").replace(",", ".")
            if self.valor_diaria4 == "":
                self.valor_diaria4 = 0
            self.valor_diaria4 = float(self.valor_diaria4)
            self.nome_quarto4 = self.entry_quarto_l4.get()
            self.quantidade4 = int(self.entry_qtd_l4.get())
        except Exception:
            pass
        try:
            self.valor_diaria5 = self.entry_diaria_l5.get().replace(".", "_").replace(",", ".")
            if self.valor_diaria5 == "":
                self.valor_diaria5 = 0
            self.valor_diaria5 = float(self.valor_diaria5)
            self.nome_quarto5 = self.entry_quarto_l5.get()
            self.quantidade5 = int(self.entry_qtd_l5.get())
        except Exception:
            pass
        try:
            self.texto_valor_diaria1 = f'R$ {self.valor_diaria1:_.2f}'
            self.texto_valor_diaria1 = self.texto_valor_diaria1.replace(".", ",").replace("_", ".")
            self.texto_valor_diaria2 = f'R$ {self.valor_diaria2:_.2f}'
            self.texto_valor_diaria2 = self.texto_valor_diaria2.replace(".", ",").replace("_", ".")
            self.texto_valor_diaria3 = f'R$ {self.valor_diaria3:_.2f}'
            self.texto_valor_diaria3 = self.texto_valor_diaria3.replace(".", ",").replace("_", ".")
            self.texto_valor_diaria4 = f'R$ {self.valor_diaria4:_.2f}'
            self.texto_valor_diaria4 = self.texto_valor_diaria4.replace(".", ",").replace("_", ".")
            self.texto_valor_diaria5 = f'R$ {self.valor_diaria5:_.2f}'
            self.texto_valor_diaria5 = self.texto_valor_diaria5.replace(".", ",").replace("_", ".")
        except Exception:
            pass
        # DATAS E CALCULOS DE DATA
        self.data_checkin = datetime.datetime.strptime(self.entry_checkin.get(), '%d/%m/%Y')
        self.data_checkout = datetime.datetime.strptime(self.entry_checkout.get(), '%d/%m/%Y')
        self.data_checkin_texto = self.entry_checkin.get()
        self.data_checkout_texto = self.entry_checkout.get()
        self.resultado_data = (self.data_checkout - self.data_checkin).days

        # CALCULOS DOS TOTAIS
        self.total_l1 = self.quantidade1 * self.resultado_data * self.valor_diaria1
        self.total_l2 = self.quantidade2 * self.resultado_data * self.valor_diaria2
        self.total_l3 = self.quantidade3 * self.resultado_data * self.valor_diaria3
        self.total_l4 = self.quantidade4 * self.resultado_data * self.valor_diaria4
        self.total_l5 = self.quantidade5 * self.resultado_data * self.valor_diaria5
        self.soma_totais = self.total_l1 + self.total_l2 + self.total_l3 + self.total_l4 + self.total_l5
        self.texto_total1 = f'R$ {self.total_l1:_.2f}'
        self.texto_total1 = self.texto_total1.replace(".", ",").replace("_", ".")
        self.texto_total2 = f'R$ {self.total_l2:_.2f}'
        self.texto_total2 = self.texto_total2.replace(".", ",").replace("_", ".")
        self.texto_total3 = f'R$ {self.total_l3:_.2f}'
        self.texto_total3 = self.texto_total3.replace(".", ",").replace("_", ".")
        self.texto_total4 = f'R$ {self.total_l4:_.2f}'
        self.texto_total4 = self.texto_total4.replace(".", ",").replace("_", ".")
        self.texto_total5 = f'R$ {self.total_l5:_.2f}'
        self.texto_total5 = self.texto_total5.replace(".", ",").replace("_", ".")
        self.subtotal = f'R$ {self.soma_totais:_.2f}'
        self.subtotal = self.subtotal.replace(".", ",").replace("_", ".")
        self.totalfinal = self.subtotal

        self.pdf = FPDF('P', 'mm', (210, 297))
        self.pdf.add_page()
        self.pdf.set_font('Arial', 'B', 26)
        try:
            if self.opcao_hotel == 'Hotel Mar Aberto':
                self.pdf.image("templates/template_hotel_mar_aberto.jpeg", x=0, y=0, w=210, h=297)
                self.nome_arquivo_padrao = f"ORCAMENTO {self.nome_hotel}.pdf"
                self.root.filename = filedialog.asksaveasfilename(initialdir="/", initialfile=self.nome_arquivo_padrao,
                                                                  title="Salvar PDF", filetypes=(("PDF files", "*.pdf"),
                                                                                                 ("all files", "*.*")))
            if self.opcao_hotel == 'Hotel Paradise Flat':
                self.pdf.image("templates/template_hotel_paradise_flat.jpeg", x=0, y=0, w=210, h=297)
                self.nome_arquivo_padrao = f"ORCAMENTO {self.nome_hotel}.pdf"
                self.root.filename = filedialog.asksaveasfilename(initialdir="/", initialfile=self.nome_arquivo_padrao,
                                                                  title="Salvar PDF", filetypes=(("PDF files", "*.pdf"),
                                                                                                 ("all files", "*.*")))
        except Exception:
            messagebox.showerror("Erro", "Template não encontrado!")
            exit()

        self.pdf.text(85, 25, hotel_exemplo1["titulo"])
        self.pdf.set_font('Arial', 'B', 10)
        self.pdf.text(110, 50, str(self.telefone_empresa))
        self.pdf.text(110, 60, str(self.end_empresa))
        self.pdf.text(110, 70, str(self.email_empresa))
        self.pdf.text(47, 86, self.nome_cli.upper())
        self.pdf.text(47, 95, self.data_checkin_texto)
        self.pdf.text(47, 104, self.data_checkout_texto)
        self.pdf.text(160, 96, str(self.numero_orcamento_db()))
        self.pdf.text(160, 104, self.data_atual())
        self.pdf.text(26, 133, str(self.quantidade1))
        self.pdf.text(42, 133, self.entry_quarto_l1.get())
        self.pdf.text(109, 133, str(self.resultado_data))
        self.pdf.text(127, 133, self.texto_valor_diaria1)
        self.pdf.text(160, 133, self.texto_total1)
        if self.texto_total2 != "R$ 0,00":
            self.pdf.text(160, 146, self.texto_total2)
            self.pdf.text(26, 146, str(self.quantidade2))
            self.pdf.text(42, 146, self.entry_quarto_l2.get())
            self.pdf.text(127, 146, self.texto_valor_diaria2)
            self.pdf.text(109, 146, str(self.resultado_data))
        else:
            pass
        if self.texto_total3 != "R$ 0,00":
            self.pdf.text(160, 158, self.texto_total3)
            self.pdf.text(26, 158, str(self.quantidade3))
            self.pdf.text(42, 158, self.entry_quarto_l3.get())
            self.pdf.text(127, 158, self.texto_valor_diaria3)
            self.pdf.text(109, 158, str(self.resultado_data))
        else:
            pass
        if self.texto_total4 != "R$ 0,00":
            self.pdf.text(160, 171, self.texto_total4)
            self.pdf.text(26, 171, str(self.quantidade4))
            self.pdf.text(42, 171, self.entry_quarto_l4.get())
            self.pdf.text(127, 171, self.texto_valor_diaria4)
            self.pdf.text(109, 171, str(self.resultado_data))
        else:
            pass
        if self.texto_total5 != "R$ 0,00":
            self.pdf.text(160, 183, self.texto_total5)
            self.pdf.text(26, 183, str(self.quantidade5))
            self.pdf.text(42, 183, self.entry_quarto_l5.get())
            self.pdf.text(127, 183, self.texto_valor_diaria5)
            self.pdf.text(109, 183, str(self.resultado_data))
        else:
            pass
        self.pdf.text(160, 211, str(self.subtotal))
        self.pdf.set_font('Arial', 'I', 10)
        self.pdf.text(160, 222, "0%")
        self.pdf.set_font('Arial', 'B', 14)
        self.pdf.text(152, 240, str(self.totalfinal))
        self.pdf.output(self.root.filename)
        messagebox.showinfo("Sucesso!", "Orçamento finalizado com sucesso.")


class Application(Funcoes):
    def __init__(self):
        super().__init__()
        self.bt_selecionar = None
        self.entry_checkout = None
        self.entry_checkin = None
        self.entry_diaria_l1 = None
        self.entry_qtd_l1 = None
        self.entry_cliente = None
        self.hotel_select = None
        self.entry_hotel = None
        self.lb_checkout = None
        self.lb_checkin = None
        self.lb_diaria = None
        self.lb_quarto = None
        self.lb_qtd = None
        self.lb_cliente = None
        self.bt_limpar = None
        self.bt_salvar = None
        self.hotel1 = None
        self.root = root
        self.tela()
        self.app_hotel()
        root.mainloop()

    def tela(self):
        self.root.title('Gerador de Orçamentos v1.0')
        self.root.configure(background='gray')
        self.root.geometry('800x500')
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=600)
        self.root.minsize(width=800, height=500)
        self.hotel1 = Frame(self.root)
        self.hotel1.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

    def app_hotel(self):
        # ------------ BOTÕES ------------------
        self.bt_salvar = Button(self.hotel1, text='Salvar',
                                font=('Arial', 12, 'bold'), command=self.gerar_orcamento)
        self.bt_salvar.place(relx=0.01, rely=0.9, relwidth=0.1, relheight=0.06)
        self.bt_limpar = Button(self.hotel1, text='Limpar', font=('Arial', 11), command=self.limpa_tela)
        self.bt_limpar.place(relx=0.15, rely=0.9, relwidth=0.1, relheight=0.06)
        self.bt_nova_linha = Button(self.hotel1, text='+', font=('Aria', 12, 'bold'))
        self.bt_nova_linha.place(relx=0.85, rely=0.41, relwidth=0.04, relheight=0.06)
        self.bt_selecionar = Button(self.hotel1, text='SELECIONAR', font=('Arial', 8), command=self.pegar_hotel)
        self.bt_selecionar.place(relx=0.27, rely=0.05, relwidth=0.15, relheight=0.055)
        # ------------- TEXTOS  - LABEL ---------------
        self.lb_cliente = Label(self.hotel1, text='CLIENTE:')
        self.lb_cliente.place(relx=0.01, rely=0.3, relwidth=0.1, relheight=0.06)
        self.lb_qtd = Label(self.hotel1, text='QTD QUARTOS')
        self.lb_qtd.place(relx=0.01, rely=0.36, relwidth=0.15, relheight=0.06)
        self.lb_quarto = Label(self.hotel1, text='QUARTO')
        self.lb_quarto.place(relx=0.33, rely=0.36, relwidth=0.1, relheight=0.06)
        self.lb_diaria = Label(self.hotel1, text='VALOR DIÁRIA')
        self.lb_diaria.place(relx=0.68, rely=0.36, relwidth=0.11, relheight=0.06)
        self.lb_checkin = Label(self.hotel1, text='CHECK-IN')
        self.lb_checkin.place(relx=0.164, rely=0.13, relwidth=0.1, relheight=0.06)
        self.lb_checkout = Label(self.hotel1, text='CHECK-OUT')
        self.lb_checkout.place(relx=0.157, rely=0.2, relwidth=0.1, relheight=0.06)
        # --------------- CAIXAS DE ENTRADA DE DADOS - ENTRY ------------------
        self.entry_hotel = StringVar(self.hotel1)
        self.entry_hotel.set('HOTEL')
        self.hotel_select = OptionMenu(self.hotel1, self.entry_hotel, 'Hotel Mar Aberto', 'Hotel Paradise Flat')
        self.hotel_select.place(relx=0.025, rely=0.05, relwidth=0.23, relheight=0.06)
        self.entry_cliente = Entry(self.hotel1)
        self.entry_cliente.place(relx=0.12, rely=0.3, relwidth=0.68, relheight=0.06)
        self.entry_qtd_l1 = Entry(self.hotel1)
        self.entry_qtd_l1.place(relx=0.025, rely=0.41, relwidth=0.12, relheight=0.06)
        self.entry_quarto_l1 = StringVar(self.hotel1)
        self.entry_quarto_l1.set('Escolha a Categoria de Quarto')
        self.quarto_select_l1 = OptionMenu(self.hotel1, self.entry_quarto_l1, '')
        self.quarto_select_l1.place(relx=0.17, rely=0.41, relwidth=0.45, relheight=0.06)
        self.entry_diaria_l1 = Entry(self.hotel1)
        self.entry_diaria_l1.place(relx=0.65, rely=0.41, relwidth=0.15, relheight=0.06)
        self.entry_checkin = DateEntry(self.hotel1, selectmode='day', date_pattern='dd/mm/y')
        self.entry_checkin.place(relx=0.27, rely=0.13, relwidth=0.15, relheight=0.06)
        self.entry_checkout = DateEntry(self.hotel1, selectmode='day', date_pattern='dd/mm/y')
        self.entry_checkout.place(relx=0.27, rely=0.2, relwidth=0.15, relheight=0.06)


Application()
