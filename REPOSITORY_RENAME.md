# Repository Rename Guidance

This repository was renamed from 'file_commander' to 'sp-file-commander' on 2026-04-29 17:24:25 +02:00.

## Existing Clones

1. Save or commit local work before pulling the rename changes.
2. Update your remote URL: git remote set-url origin https://github.com/SP-202102/sp-file-commander.git
3. Fetch and fast-forward: git fetch origin --prune; git pull --ff-only
4. Optionally rename your local clone folder after you leave the repo directory.

## Rollback

- Backup ZIP: D:\Develop\GitHub\_rename-artifacts\file_commander-to-sp-file-commander-20260429-171028\file_commander-to-sp-file-commander-20260429-171028-backup.zip
- Backup scope: working tree snapshot only. The ZIP does not include `.git` metadata.
- Safety tag: pre-repo-rename/file_commander-to-sp-file-commander-20260429-171028
- Restore the ZIP into a separate folder or reset to the safety tag before pushing if you need a full rollback. Use the safety tag or remote clone if you also need Git history.

## Review Notes

- Secrets were skipped by default; inspect skipped files manually when needed.
- Review CI, badges, registries, and other repo-coupled integrations before pushing.
