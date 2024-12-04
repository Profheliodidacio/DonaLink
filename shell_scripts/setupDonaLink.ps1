[System.Console]::OutputEncoding = [System.Text.Encoding]::UTF8

# setupDonaLink.ps1


# Verifica se o Python estao instalado
if (-not (Get-Command -Name python -ErrorAction SilentlyContinue)) {
    Write-Error "Python não está instalado. Por favor, instale o Python antes de executar este script."
    exit
}

# Definindo o nome do ambiente virtual
$venvName = '.venv'

# Criando o ambiente virtual
Write-Host "Criando ambiente virtual..."
python -m venv $venvName

# Ativando o ambiente virtual
Write-Host "Ativando ambiente virtual..."
if ($env:OS -like "*Windows*") {
    .\$venvName\Scripts\Activate.ps1
} else {
    ./$venvName/bin/activate
}

# Criando o arquivo requirements.txt
Write-Host "Criando arquivo requirements.txt..."
New-Item -ItemType File -Path "requirements.txt"
New-Item -ItemType File -Path ".gitignore"
New-Item -ItemType File -Path ".gitignore"


# Criando diretÃ³rios
# Write-Host "Criando diretÃ³rios..."
# New-Item -ItemType Directory -Path "data"
# New-Item -ItemType Directory -Path "docs"
# New-Item -ItemType Directory -Path "config"
# New-Item -ItemType Directory -Path "assets"
# New-Item -ItemType Directory -Path "src"
# New-Item -ItemType Directory -Path "src\screens"
# New-Item -ItemType Directory -Path "src\api"
# New-Item -ItemType Directory -Path "src\routes"
# Criando arquivos dentro do diretÃ³rio src
# Write-Host "Criando arquivos no diretório src..."
# New-Item -ItemType File -Path "main.py"
# New-Item -ItemType File -Path "docs\README.md"
# New-Item -ItemType File -Path "docs\INSTALLATION.md"
# New-Item -ItemType File -Path "src\main_app.py"
# New-Item -ItemType File -Path "src\screens\login_screen.py"
# New-Item -ItemType File -Path "src\screens\donate_screen.py"
# New-Item -ItemType File -Path "src\screens\info_screen.py"
# New-Item -ItemType File -Path "src\screens\sobre_screen.py"
# New-Item -ItemType File -Path "src\routes\router.py"

# InstruÃ§Ãµes finais
Write-Host "Setup concluído. Lembre-se de instalar as dependências usando `pip install -r requirements.txt` e configurar os arquivos conforme necessário."
