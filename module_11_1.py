import requests
import pandas as pd
import matplotlib.pyplot as plt


# requests
def date():
    print('Введите год (например: 2002):', end=' ')
    y = input()
    print('Введите месяц (например: 05):', end=' ')
    m = input()
    print('Введите день (например: 01):', end=' ')
    d = input()
    return y, m, d

def answer(url, params):
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            xml_data = response.text
            print("XML-данные успешно получены и отформатированы:")
            return xml_data
        else:
            print(f"Ошибка: сервер вернул статус-код {response.status_code}")
    except requests.RequestException as e:
        print(f"Ошибка при выполнении запроса: {e}")

def write_in_file(answer):
    with open('Values.xml', 'w') as test:
        test.write(answer)

def result():
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    y, m, d = date()
    params = {'date_req': f'{d}/{m}/{y}'}
    write_in_file(answer(url, params))
    return y, m, d

y, m, d = result()


# pandas
df = pd.read_xml('./Values.xml', parser='etree', encoding='windows-1251') # Преобразование формата данных из XML в DataFrame

df['Value'] = df['Value'].str.replace(',', '.').astype(float)
max_value = df.loc[df['Value'].idxmax()]
min_value = df.loc[df['Value'].idxmin()]
print('\n', max_value, '\n\n', min_value, sep='')


# matplotlib
plt.figure(figsize=(10, 6))
plt.bar(df['CharCode'], df['Value'], color='skyblue')
plt.title(f"Курсы валют (ЦБ РФ) на {d}.{m}.{y}", fontsize=16)
plt.xlabel("Валюты", fontsize=12)
plt.ylabel("Курс (рубли)", fontsize=12)
plt.xticks(rotation=45, fontsize=10)
plt.tight_layout()
plt.show()