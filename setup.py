import requests
import os

def download_file_from_github(file_name):
  try:
    autor = 'Basefilespython'
    dictgit = 'DiscordBotMafia'
    url = f"https://raw.githubusercontent.com/{autor}/{dictgit}/main/{file_name}"

    def download_file(url):
      local_filename = url.split('/')[-1]
      with requests.get(url, stream=True, allow_redirects=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
          for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)
      return local_filename

    file_name = download_file(url)
    pass
  except Exception as err:
    return err


def update():
  file_names = ['ping.gif', 'main.py', 'README.md','LICENSE','baza.py']
  er = ''
  for file_name in file_names:
    er = er + "\n" + file_name + "\n" + str(
      download_file_from_github(file_name))
    #er = download_file_from_github(file_name)
  #print(er)
  import time
  time.sleep(2)
  return er

update()
with open("start.bat", "w") as outfile:
    outfile.write(f"cd {os.getcwd()} \npython main.py")
    pass
print("Установка завершена!")
