from vendas_under import cabecalho
import mysql.connector

banco_de_dados = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='vendas'

)

cursor = banco_de_dados.cursor()

while True:

    cabecalho('VENDAS.PDV')

    print('1 - VENDAS')
    print('2 - CADASTRO DE VENDEDORES')
    print(f'3 - ENCERRAR')
    print('-' * 30)

    opcao_menu_principal = str(input('Digite sua opção:'))

    if opcao_menu_principal == '1':
        while True:
            print('1 - INCLUIR VENDA')
            print('2 - CONSULTAR VENDAS')
            print('3 - VOLTAR AO MENU ANTERIOR')

            opcao_menu_vendas = str(input('Digite sua opção:'))

            if opcao_menu_vendas == '1':
                #implantar verificaçao para ver se o vendedor já foi cadastrado

                data_da_venda = str(input('Data da venda:'))
                produto = str(input('PRODUTO:'))
                valor = float(input('VALOR: R$ '))
                nome_vendedor = str(input('VENDEDOR:'))

                comando_SQL = f"""INSERT INTO vendas_corrigidas2 (Data), (Produto), (Valor), (Vendedor) VALUES 
                                ('{data_da_venda}', '{produto}', {valor}, '{nome_vendedor}')"""

                cursor.execute(comando_SQL)
                banco_de_dados.commit()
                banco_de_dados.close()

                with open(f'{nome_vendedor}.txt', mode='a+') as arquivo_vendedores:
                    arquivo_vendedores.write(f'{data_da_venda} - {produto} - {valor}\n')

            if opcao_menu_vendas == '2':
                vendas_do_vendedor = str(input('Nome do vendedor: '))
                with open(f'{vendas_do_vendedor}.txt', mode='r') as arquivo_vendedor:
                    print(arquivo_vendedor.read())



            if opcao_menu_vendas == '3':
                break

    if opcao_menu_principal == '2':
        while True:
            print('1 - CADASTRAR VENDEDOR')
            print('2 - EXCLUIR VENDEDOR')
            print('3 - VOLTAR AO MENU ANTERIOR')
            opcao_cadastro_vendedores = str(input('Digite sua opção:'))

            if opcao_cadastro_vendedores == '1':
                nome_vendedor = input('Nome do vendedor:')
                comando_SQL = f"""INSERT INTO vendedores (nome) VALUES 
                ('{nome_vendedor}')"""

                cursor.execute(comando_SQL, nome_vendedor)
                banco_de_dados.commit()
                banco_de_dados.close()

            if opcao_cadastro_vendedores == '3':
                break

    if opcao_menu_principal == '3':
        print('Encerrando sistema...')
        break