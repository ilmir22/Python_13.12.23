#Массив - это переменная которая может принимать в себя несколько значений 
op_data = []
test = "test"
while True:   
    input("Это приложение калькулятор ")
    start = input("Если вы хотите начать работу с калькулятором введите: start:  Если вы хотите просмотреть историю введите: history: ")
    if start == "start":
        try:
            calculate=input('Список операций калькулятора: "+" - сложение\n "-" - вычитание \n "*" - умножение\n "/"- деление\n'
                        'Введите нужную вам операцию:')

            a=float(input('Введите первое число: '))
            b=float(input('Введите второе число: '))

            if calculate not in ('+' , '-' , '*' , '/'):
                raise Exception ("Вы ввели неккореткную операцию, введите операцию из списка")


            if calculate == '+':
                print(f'Результат вычесления: {a+b}')
                op_data.append (f"{a} + {b} = {a + b}")
            elif calculate == '-':
                print(f'Результат вычесления: {a-b}')
                op_data.append (f"{a} - {b} = {a - b}")
            elif calculate == '*':
                print(f'Результат вычесления: {a*b}')
                op_data.append (f"{a} * {b} = {a * b}")
            elif calculate == '/':
                print(f'Результат вычесления: {a/b}')
                op_data.append (f"{a} / {b} = {a / b}")    
        except ZeroDivisionError: 
            print("Вы не можете делить на ноль!!!")    
        except ValueError:
            print ("Вы должны ввести цифры")
        except Exception as peremennaya:
            print(peremennaya)    
        except:
            print ("Неизвестная ошибка")
    elif start == "history":
        for i in op_data:
            print(i)
    else:
        print("Приложение калькулятор заверишило работу")
        break        
        