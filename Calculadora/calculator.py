import PySimpleGUI as sg


sg.theme('LightBlue3')


layout = [[sg.Input('0',size=(31,30),key='tela',justification='right')],

          [sg.Button('7',key='sete',size=(4,2)),
           sg.Button('8',key='oito',size=(4,2)),
           sg.Button('9',key='nove',size=(4,2)),
           sg.Button('C',key='limpar_numero',size=(3,2),button_color=('black','lightblue')),
           sg.Button('AC',key='limpar_tudo',size=(3,2),button_color=('black','lightblue'))],
          
          [sg.Button('4',key='quatro',size=(4,2)),
           sg.Button('5',key='cinco',size=(4,2)),
           sg.Button('6',key='seis',size=(4,2)),
           sg.Button('+',key='mais',size=(3,2),button_color=('black','lightblue')),
           sg.Button('*',key='vezes',size=(3,2),button_color=('black','lightblue'))],
          
          [sg.Button('1',key='One',size=(4,2)),
           sg.Button('2',key='dois',size=(4,2)),
           sg.Button('3',key='tres',size=(4,2)),
           sg.Button('-',key='menos',size=(3,2),button_color=('black','lightblue')),
           sg.Button('/',key='dividir',size=(3,2),button_color=('black','lightblue'))],
         
          [sg.Button('0',key='zero',size=(10,2)),
           sg.Button('.',key='ponto',size=(4,2)),
           sg.Button('=',key='igual',size=(9,2),button_color=('black','lightblue'))]]     
          

class App():
    def __init__(self):
        self.window = sg.Window('Calculadora',layout,margins=(0,0))
        self.result = 0
        self.oper = ''
        self.window.read(timeout=1)
        
    def resultados(self):
        if self.oper == '+':
            return float(self.result) + float(self.values['tela'])
        if self.oper == '-':
            return float(self.result) - float(self.values['tela'])
        if self.oper == '*':
            return float(self.result) * float(self.values['tela'])
        if self.oper == '/':
            return float(self.result) / float(self.values['tela'])

    def inicia(self):
        while True:
            event, self.values = self.window.read()
            if event == sg.WIN_CLOSED:
                break
            
            ##Botões numeros
            if event in ('zero'):
                if self.values['tela'] == '0':
                    self.window['tela'].update(value='0')
                else:
                    self.window['tela'].update(value=self.values['tela'] + '0')
                    
            if event in ('One'):
                if self.values['tela'] == '0':
                    self.window['tela'].update(value='1')
                else:
                    self.window['tela'].update(value=self.values['tela'] + '1')
            
            if event in ('dois'):
                if self.values['tela'] == '0':
                    self.window['tela'].update(value='2')
                else:
                    self.window['tela'].update(value=self.values['tela'] + '2')
                    
            if event in ('tres'):
                if self.values['tela'] == '0':
                    self.window['tela'].update(value='3')
                else:
                    self.window['tela'].update(value=self.values['tela'] + '3')
                    
            if event in ('quatro'):
                if self.values['tela'] == '0':
                    self.window['tela'].update(value='4')
                else:
                    self.window['tela'].update(value=self.values['tela'] + '4')
                    
            if event in ('cinco'):
                if self.values['tela'] == '0':
                    self.window['tela'].update(value='5')
                else:
                    self.window['tela'].update(value=self.values['tela'] + '5')
            
            if event in ('seis'):
                if self.values['tela'] == '0':
                    self.window['tela'].update(value='6')
                else:
                    self.window['tela'].update(value=self.values['tela'] + '6')
                    
            if event in ('sete'):
                if self.values['tela'] == '0':
                    self.window['tela'].update(value='7')
                else:
                    self.window['tela'].update(value=self.values['tela'] + '7')
                    
            if event in ('oito'):
                if self.values['tela'] == '0':
                    self.window['tela'].update(value='8')
                else:
                    self.window['tela'].update(value=self.values['tela'] + '8')
                    
            if event in ('nove'):
                if self.values['tela'] == '0':
                    self.window['tela'].update(value='9')
                else:
                    self.window['tela'].update(value=self.values['tela'] + '9')
                    
            if event in ('ponto'):
                if self.values['tela'] == '0':
                    self.window['tela'].update(value='.')
                else:
                    self.window['tela'].update(value=self.values['tela'] + '.')
           
            ## Botões C e AC
            if event in ('limpar_tudo'):
                self.result = 0
                self.window['tela'].update(value=self.result)
            
            if event in ('limpar_numero'):
                self.window['tela'].update(value=self.values['tela'][:-1])
                
                
            ##Botões operadores
            if event in ('mais'):
                if self.oper != '':
                    self.result = self.resultados()
                else:
                    self.oper = '+'
                    self.result = self.values['tela']
                self.window['tela'].update(value='')
                             
            if event in ('menos'):
                if self.oper != '':
                    self.result = self.resultados()
                else:
                    self.oper = '-'
                    self.result = self.values['tela']
                self.window['tela'].update(value='')
                
            if event in ('vezes'):
                if self.oper != '':
                    self.result = self.resultados()
                else:
                    self.oper = '*'
                    self.result = self.values['tela']
                self.window['tela'].update(value='')
                
            if event in ('dividir'):
                if self.oper != '':
                    self.result = self.resultados()
                else:
                    self.oper = '/'
                    self.result = self.values['tela']
                self.window['tela'].update(value='')
                
            if event in ('igual'):
                self.result = self.resultados()
                x = str(self.result)
                y = len(x)
                if y > 8:
                    self.window['tela'].update(value='Operação tem mais que 8 dígitos')
                    self.result = 0
                    self.oper = ''
                else:
                    self.window['tela'].update(value=self.result)
                    self.result = 0
                    self.oper = ''





App().inicia()