from itertools import chain
version = '0.0.4'

def alive_or_dead(ste, members_roles):
    with open("members_roles.py") as my_file:
       data = my_file.read()
       if ste == 1:
           for mem in members_roles:
                print(mem)
           pass
    pass




def len_maf_and_mirn(maf,che,mirn,doni,doci,phutan):
    len_maf_command = int(len(maf.split())) + int(len(doni.split()))
    len_mir_command = int(len(che.split())) + int(len(mirn.split())) + int(len(doci.split())) + int(len(phutan.split()))
    return len_maf_command, len_mir_command



def download_the_module(module):
   try: 
    if os.uname()[0]== "Linux":
        print(f"{red} Введите пароль администратора для продолжения скачивания модуля ({module}).")
        system(f"sudo pip install {module} -U")
        print(f"{white}")
        try:
            import aiohttp
        except ImportError:
            cls()
            print(f"Установка модуля {module}  не была завершена.")

    else:
        system(f"pip3 install {module} -U")
   except:    
        system(f"pip install {module} -U")

def main(members_in_room):
    members_spicok = members_in_room
    count_in_list_members = len(members_spicok)
    from baza import role_names
    members_roles = list()
    member_role_none = []
    members_roles.append({f'day_or_night': 'day'})

    def mafia(members_roles):
            count_mafia_in_list_members = round(int(count_in_list_members / 4))
            if count_mafia_in_list_members == 0:
                count_mafia_in_list_members = 1
        #    print(type(members_roles))
            i=0
            mafia_id_list = ""
            while i != count_mafia_in_list_members:
                i=i+1
                member_in_role = random.choice(members_spicok)
                mafia_id_list = mafia_id_list + f"{member_in_role}  "
                role_id = 5

                members_roles.append({f'{member_in_role}': {'role': f'{role_id}', 'alive': True, 'vote' : 0}})
            return mafia_id_list
    maf = mafia(members_roles)



    def don(members_roles):

            i=0
            don_id_list = ""
            member_in_role = random.choice(members_spicok)
            role_id = 6
            if member_in_role in list(chain(*members_roles)):
                pass
            else:
                if randint(1, 2) == 1: 
                    don_id_list = don_id_list + f"{member_in_role}  "
                    i=i+1
                    members_roles.append({f'{member_in_role}': {'role': f'{role_id}', 'alive': True, 'vote' : 0}})
                else:
                    pass
            return don_id_list
    doni = don(members_roles)



    def cher(members_roles):
        count_cher_in_list_members  = round(int(count_in_list_members / 4.5))
        i=0
        cher_id_list = ""
        role_id = 3
        while i != count_cher_in_list_members:
            member_in_role = random.choice(members_spicok)
            if member_in_role in list(chain(*members_roles)):
                pass
            else:
                cher_id_list = cher_id_list + f"{member_in_role}  "
                i=i+1
                members_roles.append({f'{member_in_role}': {'role': f'{role_id}', 'alive': True, 'vote' : 0}})
        return cher_id_list
    che = cher(members_roles)



    def phutana(members_roles):
        x=int(count_in_list_members)
        count_phutana_in_list_members = round((x/x+(0.25*x)))
        i=0
        err_count = 0
        phutana_id_list = ""
        while i < count_phutana_in_list_members:
            member_in_role = random.choice(members_spicok)
            if member_in_role in list(chain(*members_roles)):
                err_count = err_count + 1
                if err_count > 50:
                  break
                
                pass
            else:
                if randint(1, 2) == 1:
                    phutana_id_list = phutana_id_list + f"{member_in_role}  "
                    
                    role_id = 2
                    ttt = {"role": f"{role_id}",
                                   "alive": True}
                    members_roles.append({f'{member_in_role}': {'role': f'{role_id}', 'alive': True, 'vote' : 0}})
                else:
                    pass
                i=i+1
        return phutana_id_list

    phutan = phutana(members_roles)




    def doc(members_roles):
        x=int(count_in_list_members)
        count_doc_in_list_members = round((x/x+(0.1*x)))
        i=0
        err_count = 0
        doc_id_list = ""
        while i < count_doc_in_list_members:
            member_in_role = random.choice(members_spicok)
            if member_in_role in list(chain(*members_roles)):
                ###print(f"Участник с id {member_in_role} уже в списке.")
                err_count = err_count + 1
                if err_count > 50:

                  break
                
                pass
            else:

                    doc_id_list = doc_id_list + f"{member_in_role}  "
                    i=i+1
                    role_id = 4
                    members_roles.append({f'{member_in_role}': {'role': f'{role_id}', 'alive': True, 'vote' : 0}})


            return doc_id_list
    doci = doc(members_roles)



    def mir(members_spicok):
        mir_id_list = ""
        for member_id in members_in_room: 
            if member_id in list(chain(*members_roles)):
                pass
            else:
                print(f"{member_id} не в списке.")
                members_roles.append({f'{member_id}': {'role': f'4', 'alive': True, 'vote' : 0}})
                mir_id_list = mir_id_list + f"{member_id}  "
        print(f"members_roles: {members_roles}")    
        return mir_id_list

            
    mirn = mir(members_spicok)
    print(members_roles)
    print(f'''
    mafia: {maf}
    cher: {che}
    mirny: {mirn}
    don: {doni}
    doc: {doci}
    phutan: {phutan}
    
    ''')

    len_maf_command, len_mir_command = len_maf_and_mirn(maf, che, mirn, doni, doci, phutan)

                # def raspredelenie(mafia,cher,mirny,don_maf,doc_mirn,phutan):
                #     x = discord.Embed(title = "Роли", color= colors['write'])
                #
                #     mafia = mafia.split()
                #     i = 0
                #     joj = ""
                #     for r in mafia:
                #                 i = i + 1
                #                 joj = joj + f"{i}) <@{r}>\n"
                #     x.add_field(name=f'Мафия:',value=f"{joj}", inline=True)
                #     cher = cher.split()
                #     i = 0
                #     joj = ""
                #     for r in cher:
                #                 i = i + 1
                #                 joj = joj + f"{i}) <@{r}>\n"
                #     x.add_field(name=f'Шериф:',value=f"{joj}", inline=True)
                #     mirny = mirny.split()
                #     i = 0
                #     joj = ""
                #     for r in mirny:
                #                 i = i + 1
                #                 joj = joj + f"{i}) <@{r}>\n"
                #     x.add_field(name=f'Мирный:',value=f"{joj}", inline=True)
                #     don_maf = don_maf.split()
                #     i = 0
                #     joj = ""
                #     for r in don_maf:
                #                 i = i + 1
                #                 joj = joj + f"{i}) <@{r}>\n"
                #     x.add_field(name=f'Дон:',value=f"{joj}", inline=True)
                #     doc_mirn = doc_mirn.split()
                #     i = 0
                #     joj = ""
                #     for r in doc_mirn:
                #                 i = i + 1
                #                 joj = joj + f"{i}) <@{r}>\n"
                #     x.add_field(name=f'Доктор:',value=f"{joj}", inline=True)
                #     phutan = phutan.split()
                #     i = 0
                #     joj = ""
                #     for r in phutan:
                #                 i = i + 1
                #                 joj = joj + f"{i}) <@{r}>\n"
                #     x.add_field(name=f'Путана:',value=f"{joj}", inline=True)
                #     return mafia,cher,mirny,don_maf,doc_mirn,phutan
                #
                # maf,che,mirn,doni,doci,phutan = raspredelenie(maf,che,mirn,doni,doci,phutan)
    
    with open("members_roles.json", "w") as file:
        json.dump(members_roles, file)
    with open("members_roles.py", "w") as file:
        file.write(str(json.dumps(members_roles, indent = 4) ))

    return maf,che,mirn,doni,doci,phutan,members_roles,len_maf_command, len_mir_command
















black = "\033[30m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
violet = "\033[35m"
turquoise = "\033[36m"
white = "\033[37m"
st = "\033[37"

print('*'*80 + '\nStarting')
from os import system

errs_in_import_module = []

try:
    from tkinter import *
except ImportError:
    system("pip install tkinter")




try:
    import getpass
except ImportError:
    errs_in_import_module.append('getpass')

try:
    import aiohttp
except ImportError:
    errs_in_import_module.append('aiohttp')


try:
    import requests
except ImportError:
    errs_in_import_module.append('requests')

try:
    import psutil
except ImportError:
    download_the_module("psutil")
    try:
        import psutil
    except ImportError:
        pass

try:
    import platform
except ImportError:
    errs_in_import_module.append('platform')

from os import system

try:
    import asyncio
except ImportError:
    errs_in_import_module.append('asyncio')
import os
try:
    import socket
except ImportError:
    errs_in_import_module.append('socket')

try:
    import subprocess
except ImportError:
    errs_in_import_module.append('subprocess')

try:
    from pypresence import Presence
except ImportError:
    errs_in_import_module.append('pypresence')


import time
from time import sleep
try:
    import random
    from random import randint
except ImportError:
    errs_in_import_module.append('random')


if len(errs_in_import_module) == 0:
    pass
else:
    for failing_module in errs_in_import_module:
        download_the_module(failing_module) 




title = "[DB] Discord Bot by BSNIKYT"
try:
    os.system(f'title {title}  ^|  the last version actual in 2023 ^| v{version}' if os.name == "nt" else "clear")
except:
    pass



def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%d:%02d:%02d" % (hh, mm, ss)


def download_file_from_github(file_name):
#  try:
    autor = 'Basefilespython'
    dictgit = 'DiscordBotMafia'
    url = f"https://raw.githubusercontent.com/{autor}/{dictgit}/main/{file_name}"

    def download_file(url):
        try:
            local_filename = url.split('/')[-1]
            #while not os.path.exists(local_filename):
            with requests.get(url, stream=True, allow_redirects=True) as r:
                    r.raise_for_status()
                    with open(local_filename, 'wb') as f:
                        for chunk in r.iter_content(chunk_size=8192):
                            f.write(chunk)
            return f'Loaded file [{local_filename}]'
        except Exception as err:
            return f'Failed load file [{local_filename}][{err.code}]'
    return download_file(url)



def update():
  file_names = ['main.py','baza.py','ping.gif','LICENSE','README.md']
  er = ''
  for file_name in file_names:
    er = er + "\n" + str(download_file_from_github(file_name))
    #er = download_file_from_github(file_name)
  print(er)
  import time
  time.sleep(2)
update()

def get_info_by_ip(ip):
    # ip = str(input())
    # ip = " ".join()
   try: 
    if not ip:
        print(f"{red}| Не получен ip/ домен                |{white}")
        data = "Не получен ip/ домен"
    else:
        try:
            try:    
                response = requests.get(
                    url=f'http://ip-api.com/json/{ip}?lang=ru').json()
            except:
                data = "❌Информация не найдена. Проверьте данные!"
            if psutil.sensors_battery() is not None:
                ps_sen_batt = str(psutil.sensors_battery().percent)+"%"
            else:
                ps_sen_batt = "Ошибка в получении заряда ПК"
            if response.get("status") == "fail":
                data = "❌Информация не найдена. Проверьте данные!"
            else:
                import datetime
                data = f'''
                ⚙Айпи чекер⚙
        
                🔎IP: {response.get('query') if response.get('query') != "" else "Не найдено"}
                🤖Провайдер: {response.get('isp') if response.get('isp') != "" else "Не найдено"}
                🌇Страна: {response.get('country') if response.get('country') != "" else "Не найдено"}
                🏙Регион: {response.get('regionName') if response.get('regionName') != "" else "Не найдено"}
                🏙Город: {response.get('city') if response.get('city') != "" else "Не найдено"}
                🔑Индекс: {response.get('zip') if response.get('zip') != "" else "Не найдено"}
                ✏Координаты: {response.get('lat') if response.get('lat') != "" else "Не найдено"}:{response.get('lon') if response.get('lon') != "" else "Не найдено"}
                
                🖥Процент заряда - {ps_sen_batt}
                🕋Имя пользователя: {getpass.getuser()}
                🚀Время загрузки системы: {datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")}
                🏁Нагрузка системы: {psutil.cpu_percent(interval=1)}
                '''.replace(
                    "                ", "")
                # print(data)
        except Exception as err:
            print(err)
    return data
   except:
       import datetime
       data = f'''
       Не получен ip/ домен
       🖥Процент заряда - {ps_sen_batt}
       🕋Имя пользователя: {getpass.getuser()}
       🚀Время загрузки системы: {datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")}
       🏁Нагрузка системы: {psutil.cpu_percent(interval=1)}'''
       return data




def cls():
    import subprocess
    try:
        if os.name()[0] == "Linux":
            print("\033c")
            #subprocess.call("cls", shell=True)
        else:
            os.system('cls')
            #os.system('clear')

    except:
       try:
            subprocess.call("cls")  # linux/mac
       except:
            os.system('cls')

hostname = "www.google.com"
def is_connected(hostname):
    try:
        host = socket.gethostbyname(hostname)
        socket.create_connection((host, 80), 2)
        return True
    except Exception:
        return False
    
# if is_connected(hostname) == True:
#     pass
# else:
#     cls()
#     print(f"{red}Подключитесь к Интернету!{white}")
#     while is_connected(hostname) == False:
#         pass


def is_pip():
    try:
        download_the_module("progress")

        try:
            import progress
            from progress.bar import Bar, IncrementalBar
            return True
        except:
            return False

    except:
        return False

# is_connected(hostname)

def cls():
    import subprocess
    try:
        if os.name()[0] == "Linux":
            print("\033c")
            #subprocess.call("cls", shell=True)
        else:
            os.system('cls')
            #os.system('clear')

    except:
       try:
            subprocess.call("cls")  # linux/mac
       except:
            os.system('cls')




if is_pip() ==True:
    pass
else:
    cls()
    print(f"{red}Установите pip{white}")
    i = 0
    while is_pip() == False:
        i = i +1
        if i > 50:
            break
        pass
    print(f"{green}Продолжение работы скрипта{white}")


try:
    import progress
    from progress.bar import Bar, IncrementalBar
except:
    try:
        system("pip3 install progress")
        import progress
        from progress.bar import Bar, IncrementalBar
    except:
        print(f"{red}Установите pip.{white}")
        ystanowlen = False



try:
    from progress.bar import Bar, IncrementalBar
except Exception as err:
    print(f"{red}{err}{white}")



try:
    my_file1 = open('log.txt', 'a', encoding='utf-8')
    my_file1.close()
except FileNotFoundError:
    print("Локальный файл записи не обнаружен!\n")

try:
    my_file2 = open('config.py', 'r', encoding='utf-8')
    my_file2.close()
except FileNotFoundError:
    pass


try:
    my_file3 = open('baze.py', 'r', encoding="utf-8")
    my_file3.close()
except FileNotFoundError:
    print("Локальный файл базы не обнаружен!\n")



# imports = {
#         "wget",
#         "pypresence",
#         "psutil",
#         "Button",
#         "discord.py -U",
#         "discord_webhook",
#         "discord",
#         "discord-py-slash-command"}
try:
    import wget
except ImportError:
    errs_in_import_module.append('wget')

try:
    import Button
except ImportError:
    errs_in_import_module.append('Button')

try:
    import discord_webhook
except ImportError:
    errs_in_import_module.append('discord_webhook')




from os import system
try:

    try:
        system("python.exe -m pip install --upgrade pip")
    except:
        pass
    bar = IncrementalBar('Установка / Обновление модулей', max=len(errs_in_import_module))
    for module in errs_in_import_module:
        download_the_module(module)
        cls()
        bar.next()
        print(f"\nМодуль {module} успешно импортирован!\n\n")
    bar.finish()
    import subprocess

   
    cls()

    try:
        pass
        subprocess.call("clear")  # linux/mac
    except:
        pass
        subprocess.call("cls", shell=True)

    print(f"{green}+-------------------------------------+{white}")
    try:
        my_file = open('log.txt', 'a')
        my_file.write(f'\n[Доступ к локальному файлу записи получен]')
        my_file.close()

        print(f"{green}| Доступ к файлу записи получен!      |{white}")
    except FileNotFoundError:
        print(f"{red}| Локальный файл записи не обнаружен! |{white}")

    print(f"{green}+-------------------------------------+{white}")
    try:
        from config import settings
        print(f"{green}| settings загружен из config!        |{white}")
    except:

        print(f"{red}| ERROR: settings                     |{white}")
    try:
        from config import autor_info
        print(f"{green}| autor_info загружен из config!      |{white}")
    except:
        
        print(f"{red}| ERROR: autor_info                   |{white}")
    try:
        from config import colors
        print(f"{green}| colors загружен из config!          |{white}")
    except:
        print(f"{red}| ERROR: colors                       |{white}")
    try:
        from keep_alive import keep_alive
        print(f"{green}| keep_alive загружен из keep_alive!  |{white}")
    except:
        print(f"{red}| ERROR: keep_alive                   |{white}")
    try:
        from baza import role_names
        print(f"{green}| roles_in_game загружен из roles!    |{white}")
    except:
        print(f"{red}| ERROR: imgs                         |{white}")
    print(f"{green}+-------------------------------------+{white}")
    try:
        try:
         import wget
        except ImportError:
            system("pip install wget")
        try:
            import discord
        except ImportError:
            system("pip install discord")
        try:
            import logging
        except ImportError:
            system("pip install logging")
        try:
            import json
        except ImportError:
            system("pip install json")
        try:    
            import requests
        except ImportError:
            system("pip install requests")
        import datetime
        from discord.ext import commands
        import discord.utils
        try:
            import platform
        except ImportError:
            system("pip install pip")

        from discord.utils import get
        try:
            from Cybernator import Paginator
        except ImportError:
            system("pip install Cybernator")
        
        from urllib.error import HTTPError
        from discord.ext.commands import Bot
        from discord.utils import get


    except Exception as err:
        print("Произошла ошибка при импорте:", str(err))
except Exception as err:
    print("Произошла ошибка при импорте:", str(err))


def file_info_def():
    #file_info = (f"{str(os.getcwd()) + f"\{__name__}"}")
    file_name = __name__.replace("__","")
    file_info = f"{green} Рабочая дирректория: {str(os.getcwd())}\{file_name}.py  |{white}"

    if __name__ != "__main__":
        file_info= file_info + f'''{red}Внимение! Этот файл является главным!{white}'''
    print(f'''{green}|{file_info}\n{green}+-------------------------------------+{white}''')    



def ply(titl,msg):
   try:
      try:
        import plyer
      except ImportError:
        system("pip3 install plyer")  
        import plyer
    #"Успешно запущено!", f"Бот запущен!({settings['bot']})\nТокен:\n{settings['token']}"
      plyer.notification.notify(message=msg, app_name=f'DiscordBot( {settings["bot"]} )',    # app_icon='ok.png',
                              title= titl)#,app_icon = r"icon.ico")
   except Exception as err:
      print(err)
      

import json
import requests


try:
    ip = json.loads(requests.get("https://api.ipify.org/?format=json").text)['ip']
except:
    ip = None
    ply("Запуск бота не удался.","Проверьте доступ в Интернет!")

# site = json.loads(requests.get(f"https://ipinfo.io/{str(ip)}/geo").text)
# info_lokal_pc_ip_and_more = f'''IP:{site['ip']}\nHostname:{site['hostname']}\nCity:{site['city']}\nRegion:{site['region']}\nCountry:{site['country']}\nTimezone:{site['timezone']}\n'''
info_lokal_pc_ip_and_more = get_info_by_ip(ip)#+ f"\nПроцент заряда - {str(psutil.sensors_battery().percent)}%"


if "Windows" in platform.platform():
    os_name = "Windows"
if "Linux" in platform.platform():
    os_name  = "Linux"
else:
    os_name = "Mac"



try:
    try:
        intents = intents = discord.Intents.all()
        yes = f"{green}| INTENTS- ALL{white}"
    except:
        yes = f"{red}| INTENTS- NO{white}"
    try:
        bot = commands.Bot(command_prefix=settings['prefix'],
                           intents=discord.Intents.all(),
                           case_insensitive=True)
        yes = yes + f"{green}, PREFIX - .            |{white}"
    except NameError as err:
            print(err)
            print(f"{red}Локальный файл запуска бота не обнаружен!")
            while True:
                pass

    print(yes)

except Exception as err:

    print(f"{red}| ERROR: INTENTS OR BOT ERROR         |\n{white}", str(err))
print(f"{green}+-------------------------------------+{white}")

bot.remove_command('help')




token = settings['token']



@bot.event
async def status_task():
    members = 0
    my_file = open(r'guilds.txt', 'a', encoding="utf-8")
    i = 0
    for guild in bot.guilds:
        i = i + 1
        my_file = open(r'guilds.txt', 'a', encoding="utf-8")
        my_file.write(f'\n{i}) {guild.name}')

        for member in guild.members:
            members += 1
    my_file.close()

    #        await bot.wait_until_ready()
    await bot.change_presence(status=discord.Status.idle,
                              activity=discord.Game('▁ ▂ ▃ ▄ ▅ ▆ ▇ █'))
    await asyncio.sleep(6)
    await bot.change_presence(status=discord.Status.idle,
                              activity=discord.Game(f".help"))
    await asyncio.sleep(6)
    await bot.change_presence(
        status=discord.Status.idle,
        activity=discord.Game(f'Следит за {members} участниками')
    )  # https://discord.gg/4WKjy5gdBP
    await asyncio.sleep(6)
    await bot.change_presence(
        status=discord.Status.idle,
        activity=discord.Game(
            f"Этот бот находится на {len(bot.guilds)} server`s"))
    await asyncio.sleep(6)
    await bot.wait_until_ready()

@bot.event
async def on_ready():
    ply("Успешно запущено!",f"Бот запущен!  {settings['bot']}")   
    #ply("Успешно запущено!",f"Бот запущен!({settings['bot']}")   
    
    print(f'''{turquoise}
        █۞███████]▄▄▄▄▄▄▄▄▄▄▄ ★★★★★
        ▄▅█████████▅▄▃▂
        █★★-  -★★█ █ ████
        ◥ ⊙▲⊙▲⊙▲⊙▲⊙▲⊙ ◤ SR{st}''')
    try:
        os.system(f'title {title}  ^|  Успешно запущено!')  # if os.name == "nt" else "clear")
    except:
        pass
    my_file = open('guilds.txt', 'a', encoding="utf-8")
    i = 0

    for guild in bot.guilds:
        i = i + 1
        my_file = open('guilds.txt', 'a', encoding="utf-8")
        my_file.write(f'\n{i}) {guild.name}')
        memb_txt = open('members.txt', 'a', encoding="utf-8")
        memb_txt.write(f'████████████ - {guild} - ███████████████████')
        memb_count = 1
        for member in guild.members:
            #    for r in range(len(guild.members)):

            memb_txt.write(f'\n{memb_count}) {member}')
            memb_count += 1
        memb_txt.write(f'\n\n')
        memb_txt.close()
    my_file.close()

    # asyncio.run_coroutine_threadsafe(console_commands(), bot.loop)
    owner = bot.get_user(485085685565620234)
    print(f"███████████████████████████████")
    print(f"Прочая информация:\n{info_lokal_pc_ip_and_more}")
    print("███████████████████████████████")
    print("ЗАПУСК БОТА")
    print(f"IP: {ip}")
    print("БОТ: {0.user}".format(bot))
    print(f"PING: {round(bot.latency * 1000)}ms")
    print(f"ID: {bot.user.id}")
    print(f"OS: {platform.platform()}")

    print(f"{green}███████████████████████████████{white}")

    await bot.change_presence(status=discord.Status.dnd,
                              activity=discord.Game('Перезапуск бота'))
    await owner.send("**█████████████████████████████████████████████**")
    x = discord.Embed(title='**Запуск бота!**', colour=colors['write'])
    x.add_field(name='<:15:1057749352287834154>Бот:', value="**{0.user}**".format(bot), inline=False)
    x.add_field(name='Пинг:',
                value=f"```{round(bot.latency * 1000)}ms```",
                inline=True)
    x.add_field(name='ID:', value="```{0.user.id}```".format(bot), inline=True)
    x.add_field(name='OS:', value=f"```{platform.platform()}```", inline=True)
    x.add_field(name='TOKEN:', value=f"\n```{token}```", inline=False)
    x.add_field(name='Прочая информация:',
                value=f"\n```{info_lokal_pc_ip_and_more}```",
                inline=False)
    x.timestamp = datetime.datetime.utcnow()
    #  await owner.send(embed=x)
    bot.loop.create_task(status_task())

    view = discord.ui.View()
    buttonSign = discord.ui.Button(label="click me",
                                   style=discord.ButtonStyle.green)
    buttonSign2 = discord.ui.Button(label="click me",
                                    style=discord.ButtonStyle.red)

    #    buttonSign2 = discord.ui.Button(label = "click me", style= discord.ButtonStyle.blue)
    async def buttonSign_callback(interaction):
        userName = interaction.user.id
        embedText = f"test test test"
        embed = discord.Embed(title="Test",
                              description=embedText,
                              color=0xffffff)
        await interaction.response.send_message(f"Hi <@{userName}>")

    async def buttonSign2_callback(interaction):
        userName = interaction.user.id
        embedText = f"test test test"
        embed = discord.Embed(title="Test",
                              description=embedText,
                              color=0xffffff)
        await interaction.response.send_message(f"Hep <@{userName}>")

    buttonSign.callback = buttonSign_callback
    buttonSign2.callback = buttonSign2_callback
    view.add_item(item=buttonSign)
    view.add_item(item=buttonSign2)
    await owner.send(embed=x, view=view)
    try:
        my_file = open('log.txt', 'a', encoding="utf-8")
        my_file.write(f'\n[БОТ Запущен!][Время: {datetime.datetime.now()}]')
        my_file.close()

      
        guilds = open('guilds.txt', 'w')
        rt = 0
        for r in bot.guilds:
            rt += 1
            guilds.write(f'{rt}) {r}\n')
        guilds.close()  
    except Exception as err:
        print("Произошла ошибка при записи логов:", err)

    try:
        pass
        #tray()
    except Exception:
        pass

@bot.command()
async def vote(ctx, member: discord.Member = None):
    try:
        f = open('data_file.json')
        r = json.load(f)
        f.close()
        if member == None:
                await ctx.reply(embed=discord.Embed(title=f"Ошибка!",description=f"Вы не ввели имя пользователя!",color=colors['write']))
                return
        else:
                in_room = 0
                len_users_in_room = 0
                for i in r:
                        len_users_in_room = len_users_in_room + 1
                for e in r:
                        
                        if (list(e.keys()))[0] in str(ctx.author.id):
                            print((list(e.keys()))[0])
                            print(e)
                            pass
                        else:
                            in_room +=1
                            pass
                if len_users_in_room == in_room:
                    await ctx.reply(embed=discord.Embed(title=f"Ошибка!",description=f"Вы не играете ни в одной игре!\nВы не можете голосовать не находясь в комнате с другими игроками!",color=colors['write']))
                    pass

                else:
                    f = open('data_file45.json')
                    sd = json.load(f)

                    for e in sd:
                            member_role = 0
                            member_role_in_comand = 0
                            for dfg in sd:
                              if list(dfg.keys())[0] != "day_or_night": 
                                print(f"list(dfg.keys())[0]_0: {list(dfg.keys())[0]}")
                                if  (e[f"{(list(e.keys()))[0]}"] != 'night') or (e[f"{(list(e.keys()))[0]}"] != 'day') or (e[f"{(list(e.keys()))[0]}"] != 'golos_day') or (e[f"{(list(e.keys()))[0]}"] != 'golos_night'):
                                    if (list(dfg.keys()))[0] in str(ctx.author.id):


                                        print('e[f"{(list(e.keys()))[0]}"]_1 :',e[f"{(list(e.keys()))[0]}"],'\n')
                                        if e[f"{(list(e.keys()))[0]}"]  == 'night':
                                            pass
                                        else:
                                            if e[f"{(list(e.keys()))[0]}"]  == 'day':
                                                pass
                                            else:
                                                if e[f"{(list(e.keys()))[0]}"]  == 'golos_day':
                                                    pass
                                                else:
                                                    if e[f"{(list(e.keys()))[0]}"]  == 'golos_night':
                                                        pass
                                                    else:
                                                        member_role = e[f"{(list(e.keys()))[0]}"]['role']
                                                        print("Роль прописавшего команду:",e[f"{(list(e.keys()))[0]}"]['role'])
                                                        await ctx.reply(f"Роль прописавшего команду:{member_role}")


                                        pass
                                    else:
                                        pass
                                else:
                                   pass 
                              else:
                                pass
                              
                              if list(dfg.keys())[0] != "day_or_night": 
                               if  (e[f"{(list(e.keys()))[0]}"] != 'night') or (e[f"{(list(e.keys()))[0]}"] != 'day') or (e[f"{(list(e.keys()))[0]}"] != 'golos_day') or (e[f"{(list(e.keys()))[0]}"] != 'golos_night'): 
                                if (list(dfg.keys()))[0] in str(member.id):
                                        print('e[f"{(list(e.keys()))[0]}"]_1 :',e[f"{(list(e.keys()))[0]}"],'\n')
                                        if e[f"{(list(e.keys()))[0]}"]  == 'night':
                                            pass
                                        else:
                                            if e[f"{(list(e.keys()))[0]}"]  == 'day':
                                                pass
                                            else:
                                                if e[f"{(list(e.keys()))[0]}"]  == 'golos_day':
                                                    pass
                                                else:
                                                    if e[f"{(list(e.keys()))[0]}"]  == 'golos_night':
                                                        pass
                                                    else:
                                                        member_role_in_comand = e[f"{(list(e.keys()))[0]}"]['role']
                                           #             print("Роль прописавшего команду:",e[f"{(list(e.keys()))[0]}"]['role'])
                                                        print("Роль человека в команде :",e[f"{(list(e.keys()))[0]}"]['role'])
                                                        await ctx.reply(f"Роль человека в команде:{member_role_in_comand}")
                                        pass
                                else:
                                        pass
                              else:
                                 pass
                              

                            if member_role:
                                await ctx.reply(f"Роль прописавшего команду:{member_role}")
                            if member_role_in_comand:
                                await ctx.reply(f"Роль человека в команде:{member_role_in_comand}")






                            if (list(e.keys()))[0]  == "day_or_night":
                                if e["day_or_night"] == 'night':
                                    print("Сейчас ночь...")
                                    await ctx.reply("Сейчас ночь!\nГолосовать можно только когда дневное голосование или ночное голосование...")

                                if e["day_or_night"] == 'day':
                                    print("Сейчас день...")
                                    await ctx.reply("Сейчас ночь!\nГолосовать можно только когда дневное голосование или ночное голосование...")
                                if e["day_or_night"] == 'golos_day':
                                    print("Сейчас дневное голосование...")
                                    ttt = []
                                    for e in r:
                                        if (list(e.keys()))[0] in str(member.id):
                                            e[f"{(list(e.keys()))[0]}"]["vote"] = 1
                                            await ctx.reply(f"Ваш голос отдан за {member.id}")
                                            #print(f"Ваш голос отдан за {member.id}")
                                            pass
                                        else:
                                            pass
                                        ttt.append(e)
                                #  f.close()
                                    try:
                                        os.remove("data_file45.json")
                                    except FileNotFoundError:
                                        pass

                                    with open("data_file45.json", "a") as outfile:
                                        json.dump(ttt, outfile)


                                if e["day_or_night"] == 'golos_night':
                                    print("Сейчас ночное голосование...")
                                    if (member_role == 5) or (member_role == 6):
                                        ttt = []
                                        for e in r:
                                            if (list(e.keys()))[0] in str(member.id):
                                                e[f"{(list(e.keys()))[0]}"]["vote"] = 1
                                                await ctx.reply(f"Ваш голос отдан за {member.id}")

                                                pass
                                            else:
                                                pass
                                            ttt.append(e)

                                        try:
                                            os.remove("data_file45.json")
                                        except FileNotFoundError:
                                            pass

                                        with open("data_file45.json", "a") as outfile:
                                            json.dump(ttt, outfile)
                                    else:
                                        await ctx.reply("Сейчас голосуют только мафия и дон!")

                                pass
                            else:
                                pass





                #     ttt = []
                #     for e in r:
                #         if (list(e.keys()))[0] in str(member.id):
                #             e[f"{(list(e.keys()))[0]}"]["vote"] = 1
                #             await ctx.reply(f"Ваш голос отдан за {member.id}")
                #             #print(f"Ваш голос отдан за {member.id}")
                #             pass
                #         else:
                #             pass
                #         ttt.append(e)
                # #  f.close()
                #     try:
                #         os.remove("data_file45.json")
                #     except FileNotFoundError:
                #         pass

                #     with open("data_file45.json", "a") as outfile:
                #         json.dump(ttt, outfile)
    except FileNotFoundError:
        await ctx.reply(embed=discord.Embed(title=f"Ошибка!",description=f"Пока никто не играет!\nВы можете исправить это прописав команду =play ```@Игрок1``````@Игрок2```.",color=colors['write']))



@bot.command()
async def cat(ctx):
    failed = []
    counter = 0
    for category in ctx.guild.categories:
       try:
        if "Комната" in category.name:
            await category.delete(reason='"комната" in category.name')
        else:
            #print(category.name)
            pass

       except Exception as err:
           await ctx.reply(f"{err}")
           failed.append(category.name)
       else: counter += 1
    fmt = ", ".join(failed)
    await ctx.author.send(f"Удалено {counter} категорий. {f'Не удалил: {fmt}' if len(failed) > 0 else ''}")



@bot.command()
async def cha(ctx):
    failed = []
    counter = 0
    for category in ctx.guild.categories:
       try:
        if "Комната" in category.name:
            await category.delete(reason='"комната" in category.name')
        else:
            pass

       except Exception as err:
           await ctx.reply(f"{err}")
           failed.append(channel.name)
       else: counter += 1
    fmt = ", ".join(failed)
    await ctx.author.send(f"Удалено {counter} категорий. {f'Не удалил: {fmt}' if len(failed) > 0 else ''}")

    failed = []
    counter = 0
    for channel in ctx.guild.channels:
       try:
        if "комната" in channel.name:
            await channel.delete(reason='"комната" in channel.name')
        else:
            pass

       except: failed.append(channel.name)
       else: counter += 1
    fmt = ", ".join(failed)
    await ctx.author.send(f"Удалено {counter} каналов. {f'Не удалил: {fmt}' if len(failed) > 0 else ''}")

@bot.command()
async def role(ctx):
    failed = []
    counter = 0
    for role in ctx.guild.roles:
       try:
        if "Комната" in role.name:
            await role.delete(reason='"комната" in role.name')
        else:
            pass
       except Exception as err:
           await ctx.reply(f"{err}")
           failed.append(role.name)
       else: counter += 1
    fmt = ", ".join(failed)
    await ctx.author.send(f"Удалено {counter} ролей. {f'Не удалил: {fmt}' if len(failed) > 0 else ''}")


@bot.command()
async def ping(ctx):
      await ctx.reply("Pong!")
      net_blet  = bot.get_emoji(946362122458234920)
      await ctx.message.add_reaction(net_blet)


@bot.command()
async def кусь(ctx):


      embed = discord.Embed(color=colors['write'])
      embed.set_image(url= "https://cs4.pikabu.ru/images/big_size_comm_an/2016-08_2/1470580009180657914.gif")
      await ctx.reply(embed = embed)
      net_blet  = bot.get_emoji(946362122458234920)
      await ctx.message.add_reaction(net_blet)



@bot.command()
async def hack(ctx):
  await ctx.reply("█████████▀▀▀▀▀▀▀██████████████▌\n████████▀⠀⠀⠀⠀⠀⠀⠀⠀⠀▀████████████▌\n███████▀⠀⠀⠀▄▀▀▀▀▀▀▀███████████▌\n██████▌⠀⠀ ⠀▌⠀⠀⠀⠀⠀⠀⠀⠀  █████████▌\n██████▌⠀⠀⠀⠀▌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀██████████\n██▀⠀⠀█▌⠀⠀⠀⠀█▄▄▄▄▄▄▄▄▄██████████\n█▌⠀⠀⠀█▌⠀⠀⠀⠀⠀⠀▀▀▀▀▀▀▀⠀██████████▌\n█▌⠀⠀⠀█▌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ██████████▌\n█▌⠀⠀⠀█▌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀███████████▌\n█▌⠀⠀⠀█▌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀███████████▌\n██▄▄▄█▌⠀⠀⠀⠀▄▄▄▄▄ ⠀⠀ ███████████▌\n██████▌⠀⠀⠀⠀⠀███▌⠀⠀⠀  ██████████▌\n██████▌⠀⠀⠀⠀⠀████▄   ▄██████████▌\n███████▄▄▄████████████████████▌\n▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁\n  Хм, похоже ты знаешь эту команду.")




@bot.command()
async def play(ctx,*args):
    guild_id = ctx.message.guild.id
    lobby = discord.Embed(title='Лобби комнаты', colour=colors['write'])
    members_in_room = []
    for member in args:
        
        y = member
        member_id = member.replace("<", "").replace(">", "").replace("@", "".replace("&", "",2))
        member_id = member_id.replace("&","")
        try:
         member = bot.get_user(int(member_id))
         name  = member.name
        except AttributeError:
            await ctx.reply(f"{y} не является участником.")
        except ValueError:
            await ctx.reply(f"{y} не является участником.")
        try:
            if member == None:
                pass
                #await ctx.reply(f"{y} не является участником.")
            if member == ctx.message.author.id:
                await ctx.reply("Вы уже в комнате!")
                pass
            else:
                #try:
                    
                    view = discord.ui.View()
                    refuse = discord.ui.Button(style=discord.ButtonStyle.red,label=f"Отказать",emoji="❌",disabled=False)
                    accept = discord.ui.Button(style=discord.ButtonStyle.green,label=f"Принять",emoji="✅",disabled=False)

                    async def accept_callback(interaction):
                        #members_in_room.extend(str(interaction.user.id))
                        embed = discord.Embed(title=interaction.user.name,description="Вы приняли запрос на совместную игру!",color=colors['write'])
                        await interaction.response.send_message(f"Hi <@{interaction.user.id}>", embed = embed)


                    async def refuse_callback(interaction):
                        embed = discord.Embed(title=interaction.user.name,description="Вы отказали запрос на совместную игру!",color=colors['write'])
                        await interaction.response.send_message(f"Hi <@{interaction.user.id}>", embed = embed)

                    accept.callback = accept_callback
                    refuse.callback = refuse_callback
                   # buttonSign2.callback = buttonSign2_callback
                    view.add_item(item=accept)
                    view.add_item(item=refuse)
                  #  await owner.send(embed=x, view=view)

                    join_req = discord.Embed(title='**Приглашение!**',description="Вас пригласили в совместную игру!", colour=colors['write'])
                    join_req.add_field(name='Кто пригласил:', value=f"**{ctx.message.author.mention}**", inline=False)
                    join_req.add_field(name='Сервер',
                                value=f"Отправленно из ▶{ctx.guild.name}◀",
                                inline=True)

                    join_req.timestamp = datetime.datetime.utcnow()
             #       await ctx.reply(embed = join_req)
                    await member.send(embed = join_req, view=view)
                
                    print(f"{str(member.id)} - {member.name}")
                    members_in_room.append(str(member.id))
                    await member.send(f'Участник {ctx.message.author.name} пригласил вас в совместную игру!')
                    lobby.add_field(name=f"{member.name}" + "#" +
                      f"{member.discriminator}", value="**✅**", inline=True)
                #except Exception as err:


        except ValueError:
            pass
        except:
            try:
                if member.bot and member != None:
                 lobby.add_field(name=name, value="**❌(BOT)**", inline=True)
                 await ctx.reply(f"Нельзя добавить бота!({member.name})")
                else:  
                 pass 
            except:
                pass

        #####print(member)
    if len(members_in_room) > 1:
        id_room = random.randint(0,1111111)
        name_room = f"Комната - {str(id_room)}"
        role = await ctx.guild.create_role(name=name_room, color=colors['write'], mentionable=True, reason="Создана новая комната.",hoist =False)
        lobby.add_field(name="Вам была добавлена данная роль.", value=role.mention, inline=False)
        await ctx.reply(embed = lobby)
    else:
        await ctx.reply("Лобби не должно быть пустым!")

    if args == "()":
        await ctx.reply("Вы не упомянули участника!")
    if args != None:
        pass
    role = discord.utils.get(ctx.guild.roles, name=name_room) #находим роль по имени
    overwrites_role_comnata={
                    ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False,send_messages = False),
                    role: discord.PermissionOverwrite(read_messages=True,send_messages = True)}
    overwrites_role_srytny={
                    ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False,send_messages = False),
                    role: discord.PermissionOverwrite(read_messages=False,send_messages = False) 
                    }

    from werkzeug.exceptions import HTTPException
    try:
        categori_lob = await ctx.guild.create_category_channel(name = name_room, reason="Создана новая комната.",overwrites=overwrites_role_comnata)
        osnowa_ch = await ctx.guild.create_text_channel(name = f"Основной - {name_room}", reason="Создана новая комната.", overwrites=overwrites_role_comnata, category = categori_lob)
        doc_ch = await ctx.guild.create_text_channel(name = f"Доктор - {name_room}", reason="Создана новая комната.", overwrites=overwrites_role_srytny, category = categori_lob)
        love_ch = await ctx.guild.create_text_channel(name = f"Любовница - {name_room}", reason="Создана новая комната.", overwrites=overwrites_role_comnata, category = categori_lob)
        mafiozy_and_don_ch = await ctx.guild.create_text_channel(name = f"Мафия и Дон - {name_room}", reason="Создана новая комната.", overwrites=overwrites_role_srytny, category = categori_lob)
        cherif_ch = await ctx.guild.create_text_channel(name = f"Шериф - {name_room}", reason="Создана новая комната.", overwrites=overwrites_role_srytny, category = categori_lob)
        
        
        
        await ctx.channel.send("Категория и каналы созданны!")
        await ctx.message.author.add_roles(role)
    except HTTPException:
        await ctx.reply("Ошибка! Превышено максимальное количество каналов в группе!")

    #print(members_in_room)
    i =0
    for member_id in members_in_room:
        i = i +1
        guild = bot.get_guild(guild_id)
        if guild == None:
            guild = await bot.fetch_guild(guild_id)
        member_in_room = guild.get_member(int(member_id))
        try:
            await member_in_room.add_roles(role)
        except discord.errors.HTTPException:
            print(member_id, "не получил роль")
   
    
    lobb_emb = discord.Embed(title=f'Лобби игры {ctx.message.author.name}. ID:{name_room}', colour=colors['write'])
    stre = ""
    sd = ""
    for r in members_in_room:
        stre = stre + f"<@{r}>\n" 
        sd = sd  + f"<@{r}>" 
    asg = await osnowa_ch.send(f"{sd}\n**Лобби игры находится здесь!**")
    await ctx.channel.send(embed = discord.Embed(title = "Категория и каналы созданны!", color=colors['write'],description=f"Лобби игры находится по [**ЭТОЙ**](https://discord.com/channels/{guild.id}/{osnowa_ch.id}/{asg.id}) ссылке."))
    lobb_emb.add_field(name="Игроки находящиеся в лобби:", value=stre, inline=False)
    msg = await osnowa_ch.send(embed = lobb_emb)
    import time

    timer = 90
    gg = False
    if gg == True:
        for k in range(timer):
            time.sleep(1)
            mm, ss = divmod(timer, 60)
            hh, mm = divmod(mm, 60)
            if timer > 60:
                ele = "%d минут %02d секунд" % (mm, ss)
            else:
                ele = "%d секунд" % ( ss)
            
            lobb343 = discord.Embed(title=f'Лобби игры {ctx.message.author.name}        ID: {name_room}', colour=colors['write'])
            lobb343.add_field(name="Игроки находящиеся в лобби:", value=stre, inline=False)
            lobb343.add_field(name="Игра начнется через", value=f"{ele}", inline=False)
            
            await msg.edit(embed=lobb343)
            timer = timer -  1
            if timer == 0:
                break
    lobb345 = discord.Embed(title=f'Лобби игры {ctx.message.author.name}        ID: {name_room}', colour=colors['write'])
    lobb345.add_field(name="Игроки находящиеся в лобби:", value=stre, inline=False)
    message = await msg.edit(embed=lobb345)
    await message.pin()

    await asg.delete()
    #await msg.delete()
    await osnowa_ch.send(f"**Настройка параметров**")
    print(f"Настройка параметров")
    maf,che,mirn,doni,doci,phutan,members_roles,len_maf_com, len_mir_com = main(members_in_room)


    st =1
    if st == 1:
                for mem in members_roles:
                   if list(mem.keys())[0] != "day_or_night":
                    guild = bot.get_guild(guild_id)
                    if guild == None:
                            guild = await bot.fetch_guild(guild_id)
                    member_in_room = guild.get_member(int(list(mem.keys())[0]))
                    
                    a = int(mem[f"{list(mem.keys())[0]}"][f"{(list(mem[f'{list(mem.keys())[0]}'].keys())[0])}"])
                    
                    await osnowa_ch.set_permissions(member_in_room, read_message_history = True, send_messages = True, attach_files = True, embed_links = True,read_messages = True)
                    await mafiozy_and_don_ch.set_permissions(member_in_room, read_messages=False, send_messages=False,mention_everyone = False)
                    await love_ch.set_permissions(member_in_room, read_messages=False, send_messages= False,mention_everyone = False)
                    await doc_ch.set_permissions(member_in_room, read_messages=False, send_messages=False,mention_everyone = False)
                    await cherif_ch.set_permissions(member_in_room, read_messages=False, send_messages=False,mention_everyone = False)
                    if (a == 5) or (a== 6):
                        await mafiozy_and_don_ch.set_permissions(member_in_room, read_messages=True, send_messages=True,mention_everyone = True)
                    if a == 3:
                        await cherif_ch.set_permissions(member_in_room, read_messages=True, send_messages=True,mention_everyone = True)

                    if a == 4:
                        await doc_ch.set_permissions(member_in_room, read_messages=True, send_messages=True,mention_everyone = True)

                    if a == 2:
                        await love_ch.set_permissions(member_in_room, read_messages=True, send_messages= True,mention_everyone = True)

                    if a == 1:
                        pass
                   else:
                       pass

    else:
            pass

#     with open("data_file.py", 'w') as outfile:
#         outfile.write(f'''
# room{str(id_room)} = {members_roles}''')
   # json_object = json.dumps(members_roles, indent = 4) 



    with open("data_file.json", "w") as outfile:
        json.dump(members_roles, outfile, indent = 4)

    names_ch_role = ['phutana','cher', 'doc','maf']
    for name_ch in names_ch_role:
        embed = discord.Embed(title=f'{role_names[name_ch]["name"]}',
                              description=f"{role_names[name_ch]['description']}", 
                              colour=colors['write'])
        embed.add_field(name="Активность ночью",
                        value=f"{role_names[name_ch]['activnost_night']}", 
                        inline=False)
        embed.set_image(url=role_names[name_ch]["url"])

        if name_ch == "phutana":
            stre = ""
            for r in phutan:
                stre = stre + f"<@{r}>\n" 
            embed.add_field(name="Игроки у вас в команде:", value=f"{stre}", inline=False)
            await love_ch.send(embed = embed) 
        if name_ch == "cher":
            stre = ""
            for r in che:
                stre = stre + f"<@{r}>\n" 
            embed.add_field(name="Игроки у вас в команде:", value=f"{stre}", inline=False)
            await cherif_ch.send(embed = embed)
        if name_ch == "maf":
            stre = ""
            for r in maf:
                stre = stre + f"<@{r}>\n" 
            for r in doni:
                stre = stre + f"<@{r}>\n" 
            embed.add_field(name="Игроки у вас в команде:", value=f"{stre}", inline=False)
            await mafiozy_and_don_ch.send(embed = embed)
        if name_ch == "doc":
            stre = ""
            for r in doci:
                stre = stre + f"<@{r}>\n" 
            embed.add_field(name="Игроки у вас в команде:", value=f"{stre}", inline=False)
            await doc_ch.send(embed = embed)
            




    while (len_maf_com != len_mir_com) or (len_maf_com != 0):
                await osnowa_ch.send(embed = discord.Embed(title = 'Ночь',description = f'Сейчас ночь.\nМафия общается в чате.\n >>> {mafiozy_and_don_ch.mention}'))
                
                for mem in members_roles:
                    if list(mem.keys())[0] != "day_or_night":
                        guild = bot.get_guild(guild_id)
                        if guild == None:
                                guild = await bot.fetch_guild(guild_id)
                        member_in_room = guild.get_member(int(list(mem.keys())[0]))
                        await osnowa_ch.set_permissions(member_in_room, read_message_history = True, send_messages = False, attach_files = False, embed_links = False,read_messages = True)
                        
                        a = int(mem[f"{list(mem.keys())[0]}"][f"{(list(mem[f'{list(mem.keys())[0]}'].keys())[0])}"])
                        await mafiozy_and_don_ch.set_permissions(member_in_room, read_messages=True, send_messages=True,mention_everyone = True)
                        await love_ch.set_permissions(member_in_room, read_messages=False, send_messages=False,mention_everyone = False)
                        await doc_ch.set_permissions(member_in_room, read_messages=False, send_messages=False,mention_everyone = False)
                        await cherif_ch.set_permissions(member_in_room, read_messages=False, send_messages=False,mention_everyone = False)

                        if (a == 5) or (a== 6):
                            await mafiozy_and_don_ch.set_permissions(member_in_room, read_messages=True, send_messages=True,mention_everyone = True)
                        if a == 3:
                            await cherif_ch.set_permissions(member_in_room, read_messages=True, send_messages=True,mention_everyone = True)
                        if a == 4:
                            await doc_ch.set_permissions(member_in_room, read_messages=True, send_messages=True,mention_everyone = True)
                        if a == 2:
                            await love_ch.set_permissions(member_in_room, read_messages=True, send_messages= True,mention_everyone = True)
                        if a == 1:
                            pass

                    else:
                      pass

                

                print('Ночь')

                f = open('data_file.json')
                sd = json.load(f)
                ttt = []
                for e in sd:
                        #print((list(e.keys()))[0])
                        if (list(e.keys()))[0]  == "day_or_night":
                            e["day_or_night"] = "night"
                            #print(f"Ваш голос отдан за {member.id}")
                            pass
                        else:
                            pass
                        ttt.append(e)
                try:
                        os.remove("data_file45.json")
                except FileNotFoundError:
                        pass

                with open("data_file45.json", "a") as outfile:
                        json.dump(ttt, outfile)




                await osnowa_ch.send("**Ночь!**\nМафии переписываются в чате.")
                timer= 60
                for k in range(timer):
                    time.sleep(1)
                    mm, ss = divmod(timer, 60)
                    hh, mm = divmod(mm, 60)
                    if timer > 60:
                        ele = "%d минут %02d секунд" % (mm, ss)
                    else:
                        ele = "%d секунд" % (ss)
                    
                    lobb343 = discord.Embed(title=f'Ночь!',description="Мафии переписываются в чате.", colour=colors['write'])
                    lobb343.add_field(name="Переход к следующему ходу через", value=f"{ele}", inline=False)
                    
                    await msg.edit(embed=lobb343)
                    timer = timer -  1
                    if timer == -1:
                        break
                timer = 60
                #await osnowa_ch.send("**Ночь!**\nМафия делает свой выбор.")

                f = open('data_file.json')
                sd = json.load(f)
                ttt = []
                for e in sd:
                        #print((list(e.keys()))[0])
                        if (list(e.keys()))[0]  == "day_or_night":
                            e["day_or_night"] = "golos_night"
                            #print(f"Ваш голос отдан за {member.id}")
                            pass
                        else:
                            pass
                        ttt.append(e)
                try:
                        os.remove("data_file45.json")
                except FileNotFoundError:
                        pass

                with open("data_file45.json", "a") as outfile:
                        json.dump(ttt, outfile)

                for k in range(timer):
                    time.sleep(1)
                    mm, ss = divmod(timer, 60)
                    hh, mm = divmod(mm, 60)
                    if timer > 60:
                        ele = "%d минут %02d секунд" % (mm, ss)
                    else:
                        ele = "%d секунд" % (ss)
                        
                    lobb343 = discord.Embed(title=f'Ночь!',description="Мафия делает свой выбор", colour=colors['write'])
                    lobb343.add_field(name="Утро настанет через", value=f"{ele}", inline=False)
                        
                    await msg.edit(embed=lobb343)
                    timer = timer -  1
                    if timer == -1:
                        break

                maf = (str(maf)).replace("[", "").replace("]", "")
                doni = (str(doni)).replace("[", "").replace("]", "")
                che =  (str(che)).replace("[", "").replace("]", "")
                mirn = (str(mirn)).replace("[", "").replace("]", "")
                doci =  (str(doci)).replace("[", "").replace("]", "")
                phutan = (str(phutan)).replace("[", "").replace("]", "")
                len_maf_com = int(len(maf.split())) + int(len(doni.split()))
                len_mir_com = int(len(che.split())) + int(len(mirn.split())) + int(len(doci.split())) + int(len(phutan.split()))
                print(len_maf_com, len_mir_com)


                for mem in members_roles:
                  if list(mem.keys())[0] != "day_or_night": 
                    guild = bot.get_guild(guild_id)
                    if guild == None:
                            guild = await bot.fetch_guild(guild_id)
                    member_in_room = guild.get_member(int(list(mem.keys())[0]))
                    await osnowa_ch.set_permissions(member_in_room, read_message_history = True, send_messages = True, attach_files = True, embed_links = True,read_messages = True)
                    
                    a = int(mem[f"{list(mem.keys())[0]}"][f"{(list(mem[f'{list(mem.keys())[0]}'].keys())[0])}"])
                    await mafiozy_and_don_ch.set_permissions(member_in_room, read_messages=False, send_messages=False,mention_everyone = False)
                    await love_ch.set_permissions(member_in_room, read_messages=False, send_messages= False,mention_everyone = False)
                    await doc_ch.set_permissions(member_in_room, read_messages=False, send_messages=False,mention_everyone = False)
                    await cherif_ch.set_permissions(member_in_room, read_messages=False, send_messages=False,mention_everyone = False)

                    if (a == 5) or (a== 6):
                        await mafiozy_and_don_ch.set_permissions(member_in_room, read_messages=True, send_messages=False,mention_everyone = False)
                        
                    if a == 3:
                        await cherif_ch.set_permissions(member_in_room, read_messages=True, send_messages=False,mention_everyone = False)

                    if a == 4:
                        await doc_ch.set_permissions(member_in_room, read_messages=True, send_messages=False,mention_everyone = False)

                    if a == 2:
                        await love_ch.set_permissions(member_in_room, read_messages=True, send_messages= False,mention_everyone = True)
                        

                    if a == 1:
                       pass
                  else:
                      pass


                f = open('data_file.json')
                sd = json.load(f)
                ttt = []
                for e in sd:
                        #print((list(e.keys()))[0])
                        if (list(e.keys()))[0]  == "day_or_night":
                            e["day_or_night"] = "day"
                            #print(f"Ваш голос отдан за {member.id}")
                            pass
                        else:
                            pass
                        ttt.append(e)
                try:
                        os.remove("data_file45.json")
                except FileNotFoundError:
                        pass

                with open("data_file45.json", "a") as outfile:
                        json.dump(ttt, outfile)



                print('День')
                await osnowa_ch.send("**День!**\nИгроки переписываются в чате.")
                timer= 90
                for k in range(timer):
                    time.sleep(1)
                    mm, ss = divmod(timer, 60)
                    hh, mm = divmod(mm, 60)
                    if timer > 60:
                        ele = "%d минут %02d секунд" % (mm, ss)
                    else:
                        ele = "%d секунд" % ( ss)
                    
                    lobb343 = discord.Embed(title=f'День!',description="Игроки переписываются в чате.", colour=colors['write'])
                    lobb343.add_field(name="Голосование начнется через", value=f"{ele}", inline=False)
                    
                    await msg.edit(embed=lobb343)
                    timer = timer -  1
                    if timer == 0:
                        break

                f = open('data_file.json')
                sd = json.load(f)
                ttt = []
                for e in sd:
                        #print((list(e.keys()))[0])
                        if (list(e.keys()))[0]  == "day_or_night":
                            e["day_or_night"] = "golos_day"
                            #print(f"Ваш голос отдан за {member.id}")
                            pass
                        else:
                            pass
                        ttt.append(e)
                try:
                        os.remove("data_file45.json")
                except FileNotFoundError:
                        pass

                with open("data_file45.json", "a") as outfile:
                        json.dump(ttt, outfile)

                await osnowa_ch.send("**Голосование!!**\nВыберите игрока, который по вашему мнению является мафией.")
                timer = 30
                for k in range(timer):
                    time.sleep(1)
                    mm, ss = divmod(timer, 60)
                    hh, mm = divmod(mm, 60)
                    if timer > 60:
                        elem = "%d минут %02d секунд" % (mm, ss)
                    else:
                        elem = "%d секунд" % ( ss)
                    
                    lobb343 = discord.Embed(title=f'Голосование!',description="Выберите игрока, который по вашему мнению является мафией.", colour=colors['write'])
                    lobb343.add_field(name="Команда голоса", value=f"=vote", inline=False)
                    lobb343.add_field(name="Ночь начнется через", value=f"{elem}", inline=True)
                    
                    await msg.edit(embed=lobb343)
                    timer = timer -  1
                    if timer == -1:
                        break
                    await osnowa_ch.send('Время вышло!')


    if len_maf_com == len_mir_com:
        itog_name = "mafia"
        itog = discord.Embed(title=f'Игра окончена!',
                                description="Победа за мафией!",
                                colour=colors['write'])
        await osnowa_ch.send(embed = itog)
    if len_maf_com == 0:
        itog_name = "mirny"
        itog = discord.Embed(title=f'Игра окончена!',
                                description="Победа за мирными!",
                                colour=colors['write'])
        await osnowa_ch.send(embed = itog)
    time.sleep(10)
    role = discord.utils.get(ctx.guild.roles, name=name_room)
    await role.delete(reason=f'Игра завершена! - ({itog_name})')
    await cherif_ch.delete(reason=f'Игра завершена! - ({itog_name})')
    await osnowa_ch.delete(reason=f'Игра завершена! - ({itog_name})')
    await doc_ch.delete(reason=f'Игра завершена! - ({itog_name})')
    await love_ch.delete(reason=f'Игра завершена! - ({itog_name})')
    await mafiozy_and_don_ch.delete(reason=f'Игра завершена! - ({itog_name})')
     #   itog.add_field(name="Команда голоса", value=f"=vote", inline=False)
     #   itog.add_field(name="Ночь начнется через", value=f"{elem}", inline=True)






def pres_py():
    try:

        from pypresence import Presence
        import time
        from time import sleep

        RPC = Presence("937294505093267507")
        RPC.connect()
        RPC.update(state=f"Хост активен! ({settings['bot']})",
                   details="Бот успешно запущен!",
                   buttons=[{
                                "label": "GITHUB",
                                "url": "https://github.com/BSNIKYT"
                            }, {
                                "label": "VK",
                                "url": "https://vk.com/serving_antifem"
                            }],
                   large_image="logo_2_1024",
                   small_image="ok",
                   large_text="VK: Бот-Мейкеры",
                   small_text="Хост активен!")
        flag_pres_py = True
        return flag_pres_py
    except Exception as err:
        flag_pres_py = False
        #print(err)
        return flag_pres_py,err


def check_press_py():
    try:
        stat, err = pres_py()
    except TypeError:
        stat = pres_py()
    if stat == False:
        print(f"{red}| ERROR: PRESS_PY                     | {err}{white}")
        print(f"{green}+-------------------------------------+{white}")
    else:
        print(f"{green}| PRESS_PY                            | {white}")
        print(f"{green}+-------------------------------------+{white}")
        pass
check_press_py()
#keep_alive_run()


def img_two_to_one(img_file_1,img_file_2):
  from PIL import Image
  im_1 = Image.open(img_file_1)
  im_2 = Image.open(img_file_2)

  img_1 = im_1.resize((400, 400))
  img_1.size
  img_2 = im_2.resize((400, 400))
  img_2.size

  new_image = Image.new('RGB',(2*img_1.size[0], img_1.size[1]), (250,250,250))

  new_image.paste(img_1,(0,0))
  new_image.paste(img_2,(img_1.size[0],0))

  name_img = random.randrange(999999999)

  new_image.save(f"{name_img}.png","PNG")
  new_image.show()
  return name_img






def tray():
    from os import system
    try:
        import pystray
    except:
        system('pip3 install pystray')
        import pystray
    import PIL.Image


    #logo.png
    image = PIL.Image.open("ok.png")

    def on_clicked(icon,item):
        if str(item) == "Нажми на меня":
            print("Вы нажали на пункт меню")
        if str(item) == "Выход":
            icon.stop()



    icon = pystray.Icon('ITStart',image,menu = pystray.Menu(
        pystray.MenuItem('Нажми на меня',pystray.Menu(
            pystray.MenuItem('Привет!', on_clicked),
            pystray.MenuItem('Пока!', on_clicked),
        )),
        pystray.MenuItem('Нажми на меня',on_clicked),
        pystray.MenuItem('Пример',on_clicked),
        pystray.MenuItem('Выход',on_clicked)
    ))

    icon.run()
file_info_def()

import urllib3
while True:

    try:

        try:

            bot.run(token=settings['token'], reconnect=True)  # , log_handler="log.txt")

        except discord.errors.LoginFailure:
            ply("Запуск бота не удался.","Токен устарел! Смените его!")
            print("Токен устарел! Смените его!")
            while True:
                pass
        except RuntimeError:
            print("Session is closed")
            ply("Запуск бота не удался.",f"Session is closed")
            while True:
                pass
        except discord.errors.ConnectionClosed:
            ply("Запуск бота не удался.","Ошибка с подключением к API Discord.")
            print("Ошибка с подключением к API Discord.")
        except TimeoutError:
            ply("Запуск бота не удался.","Timeouterror")
            print("Timeouterror")
        except urllib3.exceptions.NewConnectionError:
            ply("Запуск бота не удался.","Проверьте доступ в Интернет!")
            print("Проверьте доступ в Интернет!")
        except Exception as err:
              ply("Запуск бота не удался.",f"ERR: {err}")

              if is_connected(hostname) == True:
                  bot.run(token=settings['token'], reconnect=True)
                    #ply("Запуск бота не удался.",f"ERR: {err}")
                    #print(err)
                    #pass
              else:
                    #cls()
                    ply("Запуск бота не удался.",f"ERR: {err}")
                    print(f"{red}Подключитесь к Интернету!{white}")
                    while is_connected(hostname) == False:
                        pass 

    except Exception as error:
        print(error)
