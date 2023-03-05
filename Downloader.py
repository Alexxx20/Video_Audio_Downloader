import os

links = input('Insira os links: ').split()
print('Deseja salvar o vídeo como áudio?')
resposta = input("")

if resposta.lower() in ["yes",'sim','s']:  
    try:
        if resposta.lower() in ["yes", 'sim', 's']:
            for link in links:
                try:
                    from pytube import YouTube
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
else:
    try:
        from pytube import YouTube
        import os

        for i in links:
            yt = YouTube(i)

            print('Título = ', yt.title)

            print('Baixando...')
            ys = yt.streams.get_highest_resolution()

            download_dir = os.path.join(os.path.expanduser("~"), "Videos", "Videos baixados")

            if not os.path.exists(download_dir):
                os.makedirs(download_dir)

            ys.download(download_dir)

        print('Downloads concluídos!')
        print('\nAperte "Enter" para finalizar o programa')
        input = input()

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
        input = input("")

 
