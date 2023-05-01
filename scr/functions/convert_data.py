def format_data(list_city):
    for i in range(len(list_city)):
        data_formating = {
            'id_cidade': list_city[i]['id'],
            'nome': list_city[i]['name'],
            'estado': list_city[i]['state'],
            'pais': list_city[i]['country'],
            'temperatura': list_city[i]['data']['temperature'],
            'humidade': list_city[i]['data']['humidity'],
            'condicao': list_city[i]['data']['condition'],
            'sensacao_termica': list_city[i]['data']['sensation'],
            'dia': list_city[i]['data']['date']
        }
        return data_formating
