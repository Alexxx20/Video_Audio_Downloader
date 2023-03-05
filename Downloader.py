try:
    from pytube import YouTube
except ModuleNotFoundError:
        import subprocess
        result = subprocess.run(['pip', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode != 0:
            print("O pip não foi encontrado. Por favor, instale o pip manualmente.")

        else:
            result = subprocess.run(['pip', 'install', 'pytube'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result.returncode == 0:
                print("A biblioteca pytube foi instalada com sucesso!")
            else:
                print("Ocorreu um erro ao instalar a biblioteca pytube, tente instalá-la manualmente")
                print(result.stderr.decode('utf-8'))
        print("Reinicie o programa")
import os

links = input('Insira os links: ').split()
print('Deseja salvar o vídeo como áudio?')
resposta = input("")    

if resposta.lower() in ["yes", 'sim', 's']:
    for link in links:
            try: 
                yt = YouTube(link)
                print('Título = ', yt.title)
                print('Baixando...')
                stream = yt.streams.filter(only_audio=True).first()
                download_dir = os.path.join(os.path.expanduser("~"), "Downloads", "Musicas baixadas")

                if not os.path.exists(download_dir):
                    os.makedirs(download_dir)

                stream.download(download_dir)


                print(f'O arquivo de áudio {yt.title} foi salvo com sucesso!')
            except Exception as e:
                print(f'Ocorreu um erro durante o download de {yt.title}: {e}')

    print('\nAperte "Enter" para finalizar o programa')
    input("")


        
else:
    for i in links:
        yt = YouTube(i)

        print('Título = ', yt.title)

        resolucoes = yt.streams.filter(progressive=True)
        for i in resolucoes:
            print(i)

        x = int(input("Digite a 'itag' das configurações desejadas "))

        ys = yt.streams.get_by_itag(x)
        
        print('Baixando...')

        download_dir = os.path.join(os.path.expanduser("~"), "Videos", "Videos baixados")

        if not os.path.exists(download_dir):
            os.makedirs(download_dir)

        ys.download(download_dir)

    print('Downloads concluídos!')
    print('\nAperte "Enter" para finalizar o programa')
    input = input()
