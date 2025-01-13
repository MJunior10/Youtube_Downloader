import yt_dlp
import os

def download_playlist_yt_dlp(playlist_url, download_path="downloads", audio_only=False):
    """
    Baixa todos os vídeos de uma playlist do YouTube usando yt-dlp, ignorando erros.

    Args:
        playlist_url (str): URL da playlist.
        download_path (str): Caminho onde os vídeos serão salvos.
        audio_only (bool): Define se deve baixar apenas o áudio.
    """
    # Configurações do yt-dlp
    ydl_opts = {
        'outtmpl': f'{download_path}/%(title)s.%(ext)s',
        'format': 'bestaudio/best' if audio_only else 'best',
        'noplaylist': True,  # Vamos processar manualmente cada vídeo na playlist
    }

    # Criar o diretório de destino, se necessário
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    try:
        # Obter informações da playlist
        with yt_dlp.YoutubeDL({'extract_flat': True, 'quiet': True}) as ydl:
            playlist_info = ydl.extract_info(playlist_url, download=False)
            video_urls = [entry['url'] for entry in playlist_info.get('entries', [])]

        print(f"Playlist detectada com {len(video_urls)} vídeos.")

        # Processar cada vídeo da playlist
        for index, video_url in enumerate(video_urls, start=1):
            print(f"\nBaixando vídeo {index}/{len(video_urls)}: {video_url}")
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([video_url])
                print(f"Vídeo {index} baixado com sucesso!")
            except Exception as e:
                print(f"Erro ao baixar o vídeo {index}: {e}. Pulando para o próximo.")
    except Exception as e:
        print(f"Erro ao processar a playlist: {e}")

# Exemplo de uso:
if __name__ == "__main__":
    playlist_url = input("Insira a URL da playlist: ")
    download_path = "C:\Users\marti\Downloads\musica"
    audio_only = input("Deseja baixar apenas o áudio? (s/n): ").strip().lower() == 's'

    download_playlist_yt_dlp(playlist_url, download_path, audio_only)
