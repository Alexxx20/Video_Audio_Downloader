try:
    from pytube import YouTube
    #from moviepy.editor import VideoFileClip, AudioFileClip
except ModuleNotFoundError:
        import subprocess
        result = subprocess.run(['pip', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode != 0:
            print("O pip não foi encontrado. Por favor, instale o pip manualmente.")

        else:
            result = subprocess.run(['pip', 'install', 'pytube'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            result2 = subprocess.run(['pip', 'install', 'moviepy'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            if result.returncode == 0:
                print("A biblioteca pytube foi instalada com sucesso!")
            else:
                print("Ocorreu um erro ao instalar a biblioteca pytube, tente instalá-la manualmente")
                print(result.stderr.decode('utf-8'))

            #if result2.returncode == 0:
            #    print("A biblioteca moviepy foi instalada com sucesso!")
            #else:
            #    print("Ocorreu um erro ao instalar a biblioteca moviepy, tente instalá-la manualmente")
            #    print(result2.stderr.decode('utf-8'))
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
    try:
        for i in links:
            yt = YouTube(i)

            print('Título = ', yt.title)

            resolucoes = yt.streams.filter(progressive=True)
            cont = 1
            for i in resolucoes:
                # if hasattr(i, 'res'):
                #     print(f"{cont}. itag: {i.itag}, res: {i.res}")
                # else:
                #     print(f"{cont}. itag: {i.itag}, resolução não disponível")
                print(i)
                cont += 1

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
    except Exception as e:
        print(e)
        input = input()
