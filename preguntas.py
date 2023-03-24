"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
import csv
f = open('data.csv')

def pregunta_01():
    sumat = 0
    for row in f:
        temp = int(row.split('\t')[1])
        sumat += temp
    return sumat


def pregunta_02():
    count = {}
    count_list = []
    #Recorre la lista y llena el diccionario contando
    for row in f:
        letter = row.split('\t')[0]
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    #Ordenar el diccionario alfabeticamente
    order_keys = sorted(count.keys())
    sorted_count = {}
    for key in order_keys:
        sorted_count[key] = count[key]
    #Convertir el diccionario en una lista de tuplas
    for letter, quant in sorted_count.items():
        count_list.append((letter, quant))
    return count_list


def pregunta_03():
    count = {}
    count_list = []
    for row in f:
        letter = row.split('\t')[0]
        number = int(row.split('\t')[1])
        if letter in count:
            count[letter] += number
        else:
            count[letter] = number
    ordered_keys = sorted(count.keys())
    sorted_count = {}
    for key in ordered_keys:
        sorted_count[key] = count[key]
    for letter, summ in sorted_count.items():
        count_list.append((letter, summ))
    return count_list


def pregunta_04():
    count = {}
    count_list = []
    for row in f:
        month = row.split('\t')[2].split('-')[1]
        if month in count:
            count[month] += 1
        else:
            count[month] = 1
    ordered_keys = sorted(count.keys())
    sorted_count = {}
    for key in ordered_keys:
        sorted_count[key] = count[key]
    for letter, summ in sorted_count.items():
        count_list.append((letter, summ))
    return count_list


def pregunta_05():
    count = {}
    count_list = []
    for row in f:
        letter = row.split('\t')[0]
        number = int(row.split('\t')[1])
        if (letter in count):
            if number > count[letter]['max']:
                count[letter]['max'] = number
            elif number < count[letter]['min']:
                count[letter]['min'] = number
        else:
            count[letter] = {'max' : number, 'min' : number}
    ordered_keys = sorted(count.keys())
    sorted_count = {}
    for key in ordered_keys:
        sorted_count[key] = count[key]
    for letter, values in sorted_count.items():
        max_value = values['max']
        min_value = values['min']
        count_list.append((letter, max_value, min_value))
    return count_list


def pregunta_06():
    count = {}
    count_list = []
    for row in f:
        line = row.split('\t')[4].strip().split(',')
        for item in line:
            sep = item.split(':')
            clave = sep[0]
            num = int(sep[1])
            if clave in count:
                if num > count[clave]['max']:
                    count[clave]['max'] = num
                if num < count[clave]['min']:
                    count[clave]['min'] = num
            else:
                count[clave] = {'max': num, 'min': num} 
    ordered_keys = sorted(count.keys())
    ordered = {}
    for key in ordered_keys:
        ordered[key] = count[key]
    for letter, values in ordered.items():
        max_value = values['max']
        min_value = values['min']
        count_list.append((letter, min_value, max_value))
    return count_list


def pregunta_07():
    count = {}
    count_list = []
    for row in f:
        col_0 = row.split('\t')[0]
        col_1 = int(row.split('\t')[1])
        if col_1 in count:
            #if col_0 not in count[col_1]:
            count[col_1].append(col_0)
            #print('Nueva registro de letra',count)
        else:
            count[col_1] = [col_0]
            #print('Nueva registro de numero',count)
    ordered_keys = sorted(count.keys())
    ordered = {}
    for key in ordered_keys:
        ordered[key] = count[key]
    for number, letters in ordered.items():
        count_list.append((number, letters))
    return count_list


def pregunta_08():
    count = {}
    count_list = []
    for row in f:
        col_0 = row.split('\t')[0]
        col_1 = int(row.split('\t')[1])
        if col_1 in count:
            if col_0 not in count[col_1]:
                count[col_1].append(col_0)
        else:
            count[col_1] = [col_0]
    ordered_keys = sorted(count.keys())
    ordered = {}
    for key in ordered_keys:
        ordered[key] = count[key]
        ordered[key] = sorted(ordered[key])
    for number, letters in ordered.items():
        count_list.append((number, letters))
    return count_list


def pregunta_09():
    count = {}
    for row in f:
        line = row.split('\t')[4].strip().split(',')
        for i in line:
            pwd = i.split(':')[0]
            if pwd in count:
                count[pwd] += 1
            else:
                count[pwd] = 1
    ordered_keys = sorted(count.keys())
    ordered = {}
    for key in ordered_keys:
        ordered[key] = count[key]
    return ordered


def pregunta_10():
    count = []
    for row in f:
        col_0 = row.split('\t')[0]
        col_3 = row.split('\t')[3].strip().split(',')
        col_4 = row.split('\t')[4].strip().split(',')
        count_3 = 0
        count_4 = 0
        for i in col_3:
            count_3 += 1
            #print(count_3)
        for j in col_4:
            count_4 += 1
            #print(count_4)
        count.append((col_0, count_3, count_4))
    return count


def pregunta_11():
    count = {}
    for row in f:
        col_1 = int(row.strip().split('\t')[1])
        col_4 = row.strip().split('\t')[3].split(',')
        for i in col_4:
            if i in count:
                count[i] += col_1
            else:
                count[i] = col_1
    ordered_keys = sorted(count.keys())
    ordered = {}
    for key in ordered_keys:
        ordered[key] = count[key]
    return ordered


def pregunta_12():
    count = {}
    for row in f:
        col_0 = row.strip().split('\t')[0]
        col_4 = row.strip().split('\t')[4].split(',')
        for i in col_4:
            num = int(i.split(':')[1])
            if col_0 in count:
                count[col_0] += num
            else:
                count[col_0] = num
    ordered_keys = sorted(count.keys())
    ordered = {}
    for key in ordered_keys:
        ordered[key] = count[key]
    return ordered
