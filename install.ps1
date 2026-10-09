# Installs the shared skills and global guidance for Codex, Claude Code, and
# GitHub Copilot on Windows, where symlinks need admin rights or Developer Mode.
# Copies instead of linking; re-run after changes. Unchanged targets are left alone.
#
#   powershell -ExecutionPolicy Bypass -File .\install.ps1
#
# Pulls the repository first when run from a git clone. Skills removed from the
# repository are not removed from the targets.

$ErrorActionPreference = 'Stop'
$repo = $PSScriptRoot

if ((Test-Path (Join-Path $repo '.git')) -and (Get-Command git -ErrorAction SilentlyContinue)) {
    git -C $repo pull --ff-only
    if ($LASTEXITCODE -ne 0) { Write-Warning 'git pull failed; installing the current checkout.' }
}

function Get-TreeFingerprint($dir) {
    if (-not (Test-Path $dir)) { return '' }
    $root = (Resolve-Path $dir).Path
    (Get-ChildItem $root -Recurse -File | Where-Object Name -ne '.DS_Store' | Sort-Object FullName | ForEach-Object {
        $_.FullName.Substring($root.Length) + ':' + (Get-FileHash $_.FullName -Algorithm SHA256).Hash
    }) -join "`n"
}

function Sync-Dir($source, $target) {
    if ((Get-TreeFingerprint $source) -eq (Get-TreeFingerprint $target)) {
        Write-Host "  unchanged  $target"
        return
    }
    if (Test-Path $target) { Remove-Item $target -Recurse -Force }
    New-Item -ItemType Directory -Path (Split-Path $target) -Force | Out-Null
    Copy-Item $source $target -Recurse
    Write-Host "  updated    $target"
}

function Sync-File($source, $target) {
    if ((Test-Path $target) -and (Get-FileHash $source).Hash -eq (Get-FileHash $target).Hash) {
        Write-Host "  unchanged  $target"
        return
    }
    New-Item -ItemType Directory -Path (Split-Path $target) -Force | Out-Null
    Copy-Item $source $target -Force
    Write-Host "  updated    $target"
}

# Codex and Copilot read ~/.agents/skills; Claude Code reads only ~/.claude/skills.
Write-Host 'Skills'
foreach ($skill in Get-ChildItem (Join-Path $repo 'skills') -Directory) {
    foreach ($root in '.agents\skills', '.claude\skills') {
        Sync-Dir $skill.FullName (Join-Path $HOME (Join-Path $root $skill.Name))
    }
}

# One guidance file, copied to each harness's user-level instructions.
# Overwrites ~/.claude/CLAUDE.md; keep machine-specific Claude notes elsewhere.
Write-Host 'Guidance'
$guidance = Join-Path $repo 'context\AGENTS.md'
foreach ($target in '.codex\AGENTS.md', '.claude\CLAUDE.md', '.copilot\copilot-instructions.md') {
    Sync-File $guidance (Join-Path $HOME $target)
}
