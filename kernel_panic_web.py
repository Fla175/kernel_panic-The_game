import os
import time
import random
# Importações do 'rich'
from rich.console import Console
from rich.panel import Panel
# from rich.prompt import Prompt  <-- REMOVIDO, pois não funciona no PyScript
from rich.table import Table
from rich.text import Text

# --- Configuração Inicial ---
# O Console do Rich funciona perfeitamente para SAÍDA no PyScript
console = Console()
# clear_screen = lambda: os.system('cls' if os.name == 'nt' else 'clear') <-- REMOVIDO
# 'os.system' não funciona no navegador.

def clear_screen():
    """Substitui o 'os.system' por um código de 'limpar tela' que o terminal PyScript entende."""
    print("\033c", end="", flush=True)

# --- Funções Utilitárias com 'rich' ---

def press_enter_to_continue():
    """Pausa o jogo e espera o usuário pressionar Enter para avançar. Limpa a tela em seguida."""
    # Substituído 'console.input' por 'input' padrão
    input("\n[Pressione Enter para continuar]...")
    clear_screen()

def print_narrative(text):
    """Imprime o texto da narrativa."""
    styled_text = Text(text, style="italic grey70")
    console.print(styled_text)
    time.sleep(0.5)

def print_dialog(personagem, texto, cor="cyan"):
    """Formata e imprime um diálogo."""
    console.print(Panel(f"{texto}", title=f"[b {cor}]{personagem}[/b {cor}]", border_style=cor, width=90))

# --- Definições de Personagens (Stats Iniciais) ---
player = {
    "nome": "Bob", 
    "hp": 100, 
    "hp_max": 100, 
    "ataques": {"Tapas Múltiplos": 10}
}
wizard = {
    "nome": "Wizard", 
    "hp": 80, 
    "hp_max": 80, 
    "ataques": {"Bola de Fogo": 25}
}
querubim = {
    "nome": "Querubim", 
    "hp": 120, 
    "hp_max": 120, 
    "ataques": {"Espada de Códigos": 30}
}

# --- Tela de Título ---

def title_screen():
    """Exibe a tela inicial do jogo."""
    clear_screen()
    console.print(Panel(
        "[bold red blink]K E R N E L   P A N I C ![/bold red blink]",
        title="[bold yellow]O RPG dos Desenvolvedores[/bold yellow]",
        border_style="red",
        padding=(2, 10),
        expand=False
    ))
    press_enter_to_continue()


# --- Funções da História (Capítulos) ---

def intro():
    """Capítulo de introdução: Bob é sugado para o servidor e encontra Maus."""
    clear_screen()
    print_narrative("Bob, um desenvolvedor desempregado, estava criando um jogo em um site...")
    print_narrative("De repente, ele faz um código tão grotesco que abre um portal.")
    press_enter_to_continue()
    
    print_dialog("Bob", "O que é isso?!", "green")
    print_narrative("*Ele tenta se afastar, só que é sugado para dentro.*")
    print_dialog("Bob", "Aaaaaaaaaa, onde eu estou?", "green")
    press_enter_to_continue()
    
    print_dialog("?", "Olá Bob. Seja bem-vindo ao mundo dos desenvolvedores.", "yellow")
    print_dialog("?", "Aqui você pode fazer o que vc quiser para melhorar seu jogo.", "yellow")
    print_dialog("Bob", "Entendi... mas o que é esse lugar?", "green")
    print_dialog("?", "Eu já disse... Vc por acaso tem algum vírus em seu computador?", "yellow")
    print_dialog("Bob", "Eu acho que sim, por quê?", "green")
    print_dialog("?", "Só para saber, pois isso pode comprometer seu jogo. Então é melhor você baixar um anti-víru...", "yellow")
    press_enter_to_continue()
    
    print_narrative("*De repente, o ar congela. Uma sombra grotesca se materializa.*")
    print_dialog("Maus", "Você sabe quem eu sou?", "red")
    print_dialog("Bob", "Não, ehh.. pra mim você não passa de um mito...", "green")
    
    maus_extended_dialogue = (
        "Tabom, vou me apresentar... Eu sou [bold underline]MAUS[/bold underline]! "
        "O maior vírus do mundo!! E eu vou destruir o [bold cyan]ChatGPT[/bold cyan] e o [bold blue]Google[/bold blue]!! "
        "Além de outros sites de pesquisa!! Todo mundo vai ter que usar o cérebro pra resolver uma questão de matemática!! "
        "hahahahaahah (risada maligna). "
        "[i]Cof.. cof.. desculpe[/i] (tosse de fumante), hahahah..."
    )
    print_dialog("Maus", maus_extended_dialogue, "red")
    print_dialog("Bob", "Ah, legal.", "green")
    press_enter_to_continue()
    
    print_narrative("*Em um momento inesperado, surge um monstro das sombras e ataca o ser misterioso.*")
    print_dialog("Bob", "O QUE FOI ISSO?!", "green")
    print_narrative("*Bob fica horrorizado.*")
    press_enter_to_continue()

def capitulo_2_intro():
    """Capítulo 2: Apresentação de Maus, a história do vírus e o encontro com Wizard."""
    console.rule("[bold red]CAPÍTULO 2: A ASCENSÃO DO CAÍDO", style="red")
    time.sleep(2)
    
    print_narrative("\nA um tempo atrás, um vírus foi criado por um russo, chamado de Maus.")
    print_narrative("Ele foi feito para matar e destruir todos os computadores que entrasse.")
    press_enter_to_continue()
    
    print_dialog("Maus", "Eu finalmente estou livre!", "red")
    print_narrative("*Maus começa a se transformar em um ser misto, metade humano, metade glitch.*")
    print_narrative("*Mas surge um antivírus já pré-baixado. O nome dele é Wizard.*")
    press_enter_to_continue()
    
    print_dialog("Wizard", "Humano! Isso é um vírus banido! Eu vou precisar de sua ajuda.")
    print_narrative("*Wizard dá poderes de Administrador para Bob.*")
    player["hp"] = 150 
    player["hp_max"] = 150
    player["ataques"]["Debug Rápido"] = 20
    console.print(Panel("[bold green]Você recebeu poderes de ADM![/bold green]\nHP aumentado para 150!\nNovo ataque: 'Debug Rápido'", title="LEVEL UP!"))
    press_enter_to_continue()

def battle_1_maus_intro():
    """Batalha curta (scripted) contra Maus."""
    print_dialog("Maus", "Vocês não podem me parar! Poder I-LI-MI-TA-DO! MORRAM!", "red")
    print_narrative("*Maus corrompe o Wizard e paralisa ele por alguns segundos.*")
    print_dialog("Wizard", "Argh...!")
    print_dialog("Bob", "Não! Maldito!", "green")
    press_enter_to_continue()
    
    console.rule("[bold magenta]BATALHA (SCRIPTED)", style="magenta")
    maus_hp = 200
    print_narrative(f"Maus HP: {maus_hp}")
    
    print_narrative("*Bob corre pra cima do Maus e usa seu golpe Tapas Múltiplos!*")
    dano = player["ataques"]["Tapas Múltiplos"]
    maus_hp -= dano
    print_narrative(f"Maus sofreu {dano} de dano. (HP: {maus_hp})")
    print_narrative("Não faz muita coisa, mas foi o tempo para o Wizard se mover novamente.")
    press_enter_to_continue()
    
    print_dialog("Wizard", "Obrigado, Bob!")
    print_narrative("*Ele canaliza sua energia e usa sua BOLA DE FOGO!*")
    dano_wizard = wizard["ataques"]["Bola de Fogo"] * 3
    maus_hp -= dano_wizard
    console.print(f"Maus sofreu [bold red]{dano_wizard}[/bold red] de dano massivo! (HP: {maus_hp})")
    press_enter_to_continue()

    print_narrative("*Maus se assusta e foge para longe.*")
    console.rule("[bold magenta]FIM DA BATALHA", style="magenta")
    press_enter_to_continue()
    
    print_dialog("Bob", "Vamos pegá-lo!", "green")
    print_dialog("Wizard", "ESPERA! A gente precisa de mais pessoas, ele é muito forte.")
    print_dialog("Wizard", "Vamos até a base do sistema, vamos até o Navegador. Precisamos de mais força.")
    press_enter_to_continue()

def recrutar_querubim():
    """Cena para adicionar o personagem Querubim ao grupo."""
    print_narrative("*Eles caminharam por aquela terra que antes era bela, agora hostil.*")
    print_dialog("Wizard", "Vem rápido, eu tenho um amigo aqui, ele pode nos ajudar nisso.")
    print_dialog("Bob", "Tá.", "green")
    press_enter_to_continue()

    print_dialog("Wizard", "Fala Querubim! Precisamos de sua ajuda. Tem um vírus aí que tá muito forte.")
    print_dialog("Wizard", "Precisamos pará-lo antes que ele corrompa todo o servidor.")
    print_dialog("Querubim", "O quê?! Isso é impossível! Vocês sabem onde esse vírus tá?", "blue")
    print_dialog("Querubim", "Tá. Precisamos achar ele, e rápido, antes dele matar o servidor.", "blue")
    print_narrative("*Ele saca a Espada de Códigos.*")
    print_dialog("Querubim", "Vamos!", "blue")
    
    console.print(Panel("[bold blue]QUERUBIM ENTROU NO GRUPO![/bold blue]", padding=(1, 4)))
    press_enter_to_continue()

def print_battle_status(party, enemies):
    """Exibe o HP atual da party e dos inimigos em uma tabela organizada do Rich."""
    table = Table(title="Status da Batalha", border_style="magenta", padding=(0, 2))
    table.add_column("Heróis", style="green", justify="right")
    table.add_column("HP", style="bold green", justify="left")
    table.add_column("Inimigos", style="red", justify="right")
    table.add_column("HP", style="bold red", justify="left")

    party_vivos = [h for h in party if h["hp"] > 0]
    enemies_vivos = [e for e in enemies if e["hp"] > 0]
    
    max_rows = max(len(party_vivos), len(enemies_vivos))
    
    for i in range(max_rows):
        heroi_nome = party_vivos[i]['nome'] if i < len(party_vivos) else ""
        heroi_hp = f"{party_vivos[i]['hp']}/{party_vivos[i]['hp_max']}" if i < len(party_vivos) else ""
        
        inimigo_nome = enemies_vivos[i]['nome'] if i < len(enemies_vivos) else ""
        inimigo_hp = f"{enemies_vivos[i]['hp']}/{enemies_vivos[i]['hp_max']}" if i < len(enemies_vivos) else ""
        
        table.add_row(heroi_nome, heroi_hp, inimigo_nome, inimigo_hp)
        
    console.print(table)

def battle_2_glitchs():
    """Batalha de RPG por turnos contra inimigos genéricos (Glitchs)."""
    print_narrative("*Todos seguem Querubim até uma floresta.*")
    print_dialog("Querubim", "Vamos matar o vírus aqui.", "blue")
    press_enter_to_continue()
    
    print_narrative("*Maus de repente aparece!*")
    print_dialog("Maus", "Avancem, meus filhos!", "red")
    press_enter_to_continue()
    
    console.rule("[bold red]INÍCIO DA BATALHA", style="red")
    glitchs = [{"nome": f"Glitch {i+1}", "hp": 30, "hp_max": 30, "dano": 10} for i in range(3)]
    party = [player, wizard, querubim]
    
    while any(g["hp"] > 0 for g in glitchs) and any(h["hp"] > 0 for h in party):
        print_battle_status(party, glitchs)
        
        # --- Turno do Jogador (Bob) ---
        console.rule("Turno de Bob", style="green")
        if player["hp"] <= 0:
            console.print(Panel("Bob foi derrotado. O servidor foi corrompido.", title="[b red]GAME OVER[/b red]", border_style="red"))
            return # 'exit()' pode travar o PyScript, 'return' é mais seguro
            
        ataques_bob = list(player["ataques"].items())
        choices_ataque = {f"{i+1}": f"{nome} (Dano: {dano})" for i, (nome, dano) in enumerate(ataques_bob)}
        
        print("Escolha seu ataque:")
        for key, value in choices_ataque.items():
            print(f"  [b]{key}[/b]: {value}")
        
        # --- MODIFICAÇÃO PRINCIPAL: 'rich.prompt' -> 'input()' ---
        escolha_ataque_key = ""
        while escolha_ataque_key not in choices_ataque:
            escolha_ataque_key = input(f"Escolha (1-{len(choices_ataque)}): ")
        
        ataque_idx = int(escolha_ataque_key) - 1
        nome_ataque, dano_ataque = ataques_bob[ataque_idx]
        
        alvos_vivos = [g for g in glitchs if g["hp"] > 0]
        if not alvos_vivos: break
            
        choices_alvo = {f"{i+1}": g["nome"] for i, g in enumerate(alvos_vivos)}
        
        print("Escolha o alvo:")
        for key, value in choices_alvo.items():
            print(f"  [b]{key}[/b]: {value}")
            
        # --- MODIFICAÇÃO PRINCIPAL: 'rich.prompt' -> 'input()' ---
        escolha_alvo_key = ""
        while escolha_alvo_key not in choices_alvo:
            escolha_alvo_key = input(f"Escolha (1-{len(choices_alvo)}): ")
            
        alvo = alvos_vivos[int(escolha_alvo_key) - 1]
        
        dano_real = dano_ataque + random.randint(-2, 5)
        alvo["hp"] -= dano_real
        console.print(f"\nBob usa [b]'{nome_ataque}'[/b] em {alvo['nome']} causando [b red]{dano_real}[/b red] de dano!")
        
        if alvo["hp"] <= 0:
            alvo["hp"] = 0
            console.print(f"[b red]{alvo['nome']} foi deletado![/b red]")
        
        time.sleep(1)

        if not any(g["hp"] > 0 for g in glitchs): break

        # --- Turnos dos Aliados (Auto) ---
        console.rule("Turnos Aliados", style="cyan")
        alvos_vivos = [g for g in glitchs if g["hp"] > 0]
        
        if wizard["hp"] > 0 and alvos_vivos:
            alvo_wizard = random.choice(alvos_vivos)
            dano_wizard = wizard["ataques"]["Bola de Fogo"] + random.randint(-5, 5)
            alvo_wizard["hp"] -= dano_wizard
            console.print(f"Wizard usa [b]'Bola de Fogo'[/b] em {alvo_wizard['nome']} causando [b red]{dano_wizard}[/b red] de dano.")
            if alvo_wizard["hp"] <= 0:
                alvo_wizard["hp"] = 0
                console.print(f"[b red]{alvo_wizard['nome']} foi deletado![/b red]")
                alvos_vivos = [g for g in glitchs if g["hp"] > 0]
            time.sleep(1)

        if not any(g["hp"] > 0 for g in glitchs): break

        if querubim["hp"] > 0 and alvos_vivos:
            alvo_querubim = random.choice(alvos_vivos)
            dano_querubim = querubim["ataques"]["Espada de Códigos"] + random.randint(-5, 10)
            alvo_querubim["hp"] -= dano_querubim
            console.print(f"Querubim usa [b]'Espada de Códigos'[/b] em {alvo_querubim['nome']} causando [b red]{dano_querubim}[/b red] de dano.")
            if alvo_querubim["hp"] <= 0:
                alvo_querubim["hp"] = 0
                console.print(f"[b red]{alvo_querubim['nome']} foi deletado![/b red]")
            time.sleep(1)

        if not any(g["hp"] > 0 for g in glitchs): break
            
        # --- Turno dos Inimigos ---
        console.rule("Turnos Inimigos", style="red")
        
        party_viva = [h for h in party if h["hp"] > 0]
        if not party_viva: break
            
        for g in glitchs:
            if g["hp"] > 0:
                if not party_viva: break
                alvo_inimigo = random.choice(party_viva)
                dano_inimigo = g["dano"] + random.randint(-2, 2)
                alvo_inimigo["hp"] -= dano_inimigo
                console.print(f"{g['nome']} ataca {alvo_inimigo['nome']} causando [b red]{dano_inimigo}[/b red] de dano.")
                
                if alvo_inimigo["hp"] <= 0:
                    alvo_inimigo["hp"] = 0
                    console.print(f"[b red]{alvo_inimigo['nome']} foi derrotado![/b red]")
                    party_viva = [h for h in party if h["hp"] > 0]
                    if not party_viva:
                        break
                time.sleep(0.5)

        if player["hp"] <= 0:
            console.print(Panel("Bob foi derrotado. O servidor foi corrompido.", title="[b red]GAME OVER[/b red]", border_style="red"))
            return
            
        press_enter_to_continue()

    # Fim da batalha
    if any(g["hp"] > 0 for g in glitchs):
        if player["hp"] <= 0:
            console.print(Panel("Bob foi derrotado. O servidor foi corrompido.", title="[b red]GAME OVER[/b red]", border_style="red"))
            return
    else:
        console.print(Panel("[bold green]VITÓRIA![/bold green]\nTodos os Glitchs foram derrotados!", padding=(1, 4)))
        player["hp"] = min(player["hp_max"], player["hp"] + 20)
        wizard["hp"] = min(wizard["hp_max"], wizard["hp"] + 10)
        querubim["hp"] = min(querubim["hp_max"], querubim["hp"] + 10)
        console.print("[yellow]Algum HP foi restaurado após a batalha.[/yellow]")
        press_enter_to_continue()


def battle_3_maus_main():
    """Cena scriptada onde Maus elimina Wizard e Querubim."""
    print_narrative("*Maus, furioso, assume sua forma completa...*")
    print_dialog("Maus", "Vou apagar vocês do mapa antes de acabar com este servidor!", "red")
    press_enter_to_continue()

    console.rule("[bold red]BATALHA FINAL (SCRIPTED)", style="red")
    
    if wizard["hp"] > 0:
        print_narrative("*Maus avança com velocidade impossível e corta Wizard ao meio.*")
        wizard["hp"] = 0
        print_dialog("Bob", "WIZARD! NÃO!", "green")
        console.print(Panel("[bold red]Wizard foi deletado.[/bold red]", border_style="red"))
        press_enter_to_continue()

    if querubim["hp"] > 0:
        print_dialog("Querubim", "MALDITO! Vou limpar você do mapa!", "blue")
        print_narrative("*Maus estende a mão e paralisa Querubim... e perfura seu rosto.*")
        print_dialog("Maus", "MORRAAAAA!", "red")
        querubim["hp"] = 0
        console.print(Panel("[bold red]Querubim foi deletado.[/bold red]", border_style="red"))
        press_enter_to_continue()
    
    print_dialog("Bob", "Maldito... EU VOU MATAR VOCÊ!", "green")
    print_narrative("*Bob corre para cima do Maus.*")
    press_enter_to_continue()

def battle_4_bob_vs_maus():
    """Turno scriptado onde Bob ganha o poder final de ADM."""
    print_dialog("Maus", "Você vai morrer como os outros.", "red")
    print_narrative("*Maus paralisa Bob e invoca Glitchs para espancá-lo.*")
    
    dano_glitchs = 50
    player["hp"] -= dano_glitchs
    if player["hp"] < 1: player["hp"] = 1
        
    console.print(f"Os Glitchs atacam Bob! Ele sofre [b red]{dano_glitchs}[/b red] de dano. (HP: {player['hp']})")
    press_enter_to_continue()
    
    print_narrative("*Bob lembra de sua vida e família... Essa vontade de viver desperta algo...*")
    press_enter_to_continue()
    
    print_dialog("Bob", "É verdade... Eu sou o desenvolvedor. EU SOU O DONO DE TUDO!", "green")
    print_narrative("*Bob se solta dos Glitchs e seu HP é totalmente restaurado!*")
    player["hp"] = player["hp_max"]
    console.print(f"[bold green]Bob HP: {player['hp']}/{player['hp_max']}[/bold green]")
    
    player["ataques"]["[PODER ADM SUPREMO] APAGAR"] = 99999
    
    console.rule("Turno Final de Bob", style="green")
    console.print("O que fazer?\n  [b]1[/b]: [PODER ADM SUPREMO] APAGAR")
    
    # --- MODIFICAÇÃO PRINCIPAL: 'rich.prompt' -> 'input()' ---
    escolha = ""
    while escolha != "1":
        escolha = input("Escolha (1): ")
        
    console.print("\nBob: [bold]PEREÇA![/bold]")
    print_narrative("*Bob estende a mão e apaga Maus do computador.*")
    press_enter_to_continue()

def battle_5_final_boss():
    """O final da batalha: Maus invoca seu filho antes de ser apagado."""
    print_dialog("Maus", "...eu retornarei... mais forte... eu sempre volto... melhor!", "red")
    print_narrative("*Ele usa suas últimas energias para invocar seu filho mais forte.*")
    print_narrative("*Cai um relâmpago em cima do Maus e ele é apagado.*")
    press_enter_to_continue()
    
    print_dialog("Filho de Maus", "Você matou meu pai... EU JURO ANIQUILAR VOCÊ!", "magenta")
    print_narrative("*O ser misterioso corre pra cima de Bob e morde seu pescoço!*")
    
    dano_filho = 75
    player["hp"] -= dano_filho
    console.print(f"Bob sofre [b red]{dano_filho}[/b red] de dano crítico! (HP: {player['hp']})")
    press_enter_to_continue()
    
    console.rule("Turno Final de Bob", style="green")
    console.print("O que fazer?\n  [b]1[/b]: [PODER ADM SUPREMO] APAGAR")
    
    # --- MODIFICAÇÃO PRINCIPAL: 'rich.prompt' -> 'input()' ---
    escolha = ""
    while escolha != "1":
        escolha = input("Escolha (1): ")

    print_narrative("*Bob estala o dedo, apagando o filho do Maus da existência.*")
    print_narrative("...")
    time.sleep(2)
    press_enter_to_continue()

def ending():
    """A cena final e a conclusão da história de Bob."""
    print_narrative("O cansaço toma conta de Bob...")
    print_narrative("Ele sente uma sensação de vertigem...")
    time.sleep(2)
    clear_screen()
    print_narrative("Bob acorda em sua cadeira. Ele está de volta ao mundo real.")
    print_narrative("O jogo no site perdeu toda a programação.")
    print_narrative("Ele terá que fazer tudo de novo...")
    print_narrative("...mas as lembranças do Servidor dos Desenvolvedores jamais sairão de suas memórias.")
    time.sleep(3)
    
    console.print(Panel("[bold yellow]FIM[/bold yellow]", title="Obrigado por jogar!", padding=(1, 4)))

# --- Função Principal ---
def main():
    """Função principal que executa a sequência de eventos do jogo."""
    try:
        title_screen()
        intro()
        capitulo_2_intro()
        battle_1_maus_intro()
        recrutar_querubim()
        battle_2_glitchs()
        # A checagem de "Game Over" está dentro de battle_2_glitchs
        if player["hp"] > 0: 
            battle_3_maus_main()
            battle_4_bob_vs_maus()
            battle_5_final_boss()
            ending()
    except (KeyboardInterrupt, EOFError):
        console.print("\n\n[yellow]Jogo interrompido. Saindo.[/yellow]")
    except Exception as e:
        # Captura erros para depuração no terminal web
        console.print(f"\n\n[bold red]UM ERRO INESPERADO OCORREU:[/bold red]\n{e}")
        console.print("Por favor, recarregue a página para tentar novamente.")

if __name__ == "__main__":
    main()
