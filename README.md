# autofarm_tft
Um bot de tft para quem quiser tirar o máximo de proveito dos passes no lolzinho

Esta ferramenta foi criada para auxiliar no farm de Emblemas nos passes da Riot para quem não tem tempo (ou paciência) de farmar manualmente.
O bot é capaz de farmar tokens automaticamente, burlando a detecção de AFK's da Riot. O bot foi desenvolvido por mim, Weoah, e inspirado no joseBot, este criado pelo José Ricardo e seu amigo José Ricardo (isso mesmo).

## Instalação
Primeiramente é necessário baixar e instalar a linguagem de programação Python. A ultima versão pode ser baixada no [site oficial](https://www.python.org/downloads/). Durante o processo de instalação tenha certeza de marcar a opção "ADD TO PATH".

Em seguida baixe os arquivos que estão no repositório, crie uma pasta somente para eles e os deixe lá.

Para executá-los é necessario que as bibliotecas estejam instaladas, para isso, dentro da pasta abra um terminal (ou prompt de comando) clicando com o (shift + botão direito) e na opção "Abrir no Terminal/PowerShell". Execute o seguinte comando:
```
pip install -r requirements.txt
```

## Execução
O intuito da ferramente é ser o mais intuitivo possível, por conta disso há pouquíssimas configurações a serem feitas para a execução do bot. 
Para executar é preciso abrir um terminal na pasta onde está o arquivo:
```
bot.py
```
e digitar o seguinte comando:
```
python bot.py
```
A partir deste momento o bot já vai estar funcionando e farmando os seus emblemas automaticamente!
Para parar a execução basta dar um (Ctrl + C) dentro do terminal onde o bot foi iniciado.

## O jogo deve estar em modo janela na resolução 1024x768
Essa decisão foi tomada por conta de ser a menor resolução, logo a mais viavel para a maioria das pessoas, caso o bot tenha sido iniciado com o jogo em outra resolução, pare-o e o inicie novamente (tanto dentro de jogo ou no client).