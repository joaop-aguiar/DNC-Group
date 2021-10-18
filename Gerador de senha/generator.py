import PySimpleGUI as sg
import random
import os

char_list_maiu = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
char_list_minu = 'abcdefghijklmnopqrstuvwxyz'
numero_list = '1234567890'
especial = '!@#$%&*'

def nova_senha():
    chars = random.choices(char_list_minu+char_list_maiu+numero_list+especial,k=int(values['n_char']))
    senha_nova = ''.join(chars)
    return senha_nova

def nova_senha_letrasMm_numeros():
    chars = random.choices(char_list_minu+char_list_maiu+numero_list,k=int(values['n_char']))
    senha_nova = ''.join(chars)
    return senha_nova

def nova_senha_letrasMm_especial():
    chars = random.choices(char_list_maiu+char_list_minu+especial,k=int(values['n_char']))
    senha_nova = ''.join(chars)
    return senha_nova

def nova_senha_letrasM_numeros_especial():
    chars = random.choices(char_list_maiu+numero_list+especial,k=int(values['n_char']))
    senha_nova = ''.join(chars)
    return senha_nova

def nova_senha_letrasm_numeros_especial():
    chars = random.choices(char_list_minu+numero_list+especial,k=int(values['n_char']))
    senha_nova = ''.join(chars)
    return senha_nova

def nova_senha_maiu_minu():
    chars = random.choices(char_list_minu+char_list_maiu,k=int(values['n_char']))
    senha_nova = ''.join(chars)
    return senha_nova

def nova_senha_maiu_num():
    chars = random.choices(char_list_maiu+numero_list,k=int(values['n_char']))
    senha_nova = ''.join(chars)
    return senha_nova

def nova_senha_maiu_esp():
    chars = random.choices(char_list_maiu+especial,k=int(values['n_char']))
    senha_nova = ''.join(chars)
    return senha_nova

def nova_senha_minu_num():
    chars = random.choices(char_list_minu+numero_list,k=int(values['n_char']))
    senha_nova = ''.join(chars)
    return senha_nova

def nova_senha_minu_esp():
    chars = random.choices(char_list_minu+especial,k=int(values['n_char']))
    senha_nova = ''.join(chars)
    return senha_nova

def nova_senha_num_esp():
    chars = random.choices(numero_list+especial,k=int(values['n_char']))
    senha_nova = ''.join(chars)
    return senha_nova

def nova_senha_minu():
    chars = random.choices(char_list_minu,k=int(values['n_char']))
    senha_nova = ''.join(chars)
    return senha_nova

def nova_senha_maiu():
    chars = random.choices(char_list_maiu,k=int(values['n_char']))
    senha_nova = ''.join(chars)
    return senha_nova

def nova_senha_numero():
    chars = random.choices(numero_list,k=int(values['n_char']))
    senha_nova = ''.join(chars)
    return senha_nova

def nova_senha_especial():
    chars = random.choices(especial,k=int(values['n_char']))
    senha_nova = ''.join(chars)
    return senha_nova

def copiar_senha(text):
    command = 'echo | set /p nul=' + text.strip() + '| clip'
    os.system(command)





sg.theme('DarkBlue13')
layout = [  [sg.Text('Gerador de senha')],
            [sg.Checkbox(text='Incluir Maiusculas',key='Maiu')],
            [sg.Checkbox(text='Incluir Minusculas',key='Minu')],
            [sg.Checkbox(text='Incluir Números',key='Num')],
            [sg.Checkbox(text='Incluir Caracteres especiais',key='Esp')],
            [sg.Combo(values=list(range(1,41)),key='n_char',default_value=1),sg.Text('Números de Caracteres')],
            [sg.Output(size=(50,2),key='saida')],
            [sg.Button('Gerar senha'), sg.Button('Copiar senha')] ]


window = sg.Window('Gerador de senhas', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Gerar senha':
        window.FindElement('saida').Update('')
        if values['Minu'] is True and values['Maiu'] is True and values['Num'] is True and values['Esp'] is True:
            senha = nova_senha()
            print(senha)
        elif values['Minu'] is True and values['Maiu'] is True and values['Num'] is True:
            senha = nova_senha_letrasMm_numeros()
            print(senha)
        elif values['Minu'] is True and values['Maiu'] is True and values['Esp'] is True:
            senha = nova_senha_letrasMm_especial()
            print(senha)
        elif values['Maiu'] is True and values['Num'] is True and values['Esp'] is True:
            senha = nova_senha_letrasM_numeros_especial()
            print(senha)
        elif values['Minu'] is True and values['Num'] is True and values['Esp'] is True:
            senha = nova_senha_letrasm_numeros_especial()
            print(senha)
        elif values['Minu'] is True and values['Maiu'] is True:
            senha = nova_senha_maiu_minu()
            print(senha)
        elif values['Num'] is True and values['Maiu'] is True:
            senha = nova_senha_maiu_num()
            print(senha)
        elif values['Esp'] is True and values['Maiu'] is True:
            senha = nova_senha_maiu_esp()
            print(senha)
        elif values['Minu'] is True and values['Num'] is True:
            senha = nova_senha_minu_num()
            print(senha)
        elif values['Minu'] is True and values['Esp'] is True:
            senha = nova_senha_minu_esp()
            print(senha)
        elif values['Num'] is True and values['Esp'] is True:
            senha = nova_senha_num_esp()
            print(senha)
        elif values['Minu'] is True:
            senha = nova_senha_minu()
            print(senha)
        elif values['Maiu'] is True:
            senha = nova_senha_maiu()
            print(senha)
        elif values['Num'] is True:
            senha = nova_senha_numero()
            print(senha)
        elif values['Esp'] is True:
            senha = nova_senha_especial()
            print(senha)
        else:
            print('Escolher pelo menos um campo acima')
    if event == 'Copiar senha':
        copiar_senha(senha)
        print('Senha copiada para área de transferência')

window.close()