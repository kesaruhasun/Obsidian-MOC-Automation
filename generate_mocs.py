import os

def generate_mocs(vault_root_path):
    for root, dirs, files in os.walk(vault_root_path):
        # Exclude .git and .obsidian directories from MOC generation
        dirs[:] = [d for d in dirs if d not in ['.git', '.obsidian']]

        md_files = [f for f in files if f.endswith('.md') and not f.endswith('_MOC.md')]
        
        # Check if there are any markdown files or subdirectories to warrant an MOC
        if not md_files and not dirs:
            continue

        moc_content = f"# {os.path.basename(root).replace('_', ' ').title()} Map of Content\n\n"
        
        if md_files:
            moc_content += "## Files\n"
            for md_file in sorted(md_files):
                # Remove .md extension for Obsidian link
                file_name_without_ext = os.path.splitext(md_file)[0]
                moc_content += f"- [[{file_name_without_ext}]]\n"
            moc_content += "\n"

        if dirs:
            moc_content += "## Subfolders\n"
            for directory in sorted(dirs):
                moc_content += f"- [[{directory}]]\n"
            moc_content += "\n"

        moc_file_name = f"{os.path.basename(root).replace(' ', '_')}_MOC.md"
        moc_file_path = os.path.join(root, moc_file_name)

        # Avoid overwriting the script itself if it's in the root
        if os.path.abspath(moc_file_path) == os.path.abspath(__file__):
            continue

        with open(moc_file_path, 'w', encoding='utf-8') as f:
            f.write(moc_content)

if __name__ == "__main__":
    # Determine the vault root dynamically based on script location
    # This assumes the script is placed within the Obsidian vault
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Navigate up to find the vault root (assuming MOC_Automation is in Journal/Projects)
    # You might need to adjust this path based on where you place MOC_Automation
    # For this setup, it's 3 levels up from MOC_Automation:
    # MOC_Automation/ -> Projects/ -> Journal/ -> obsidian-vault/
    vault_root = os.path.abspath(os.path.join(script_dir, '..', '..', '..'))
    
    # If the script is placed directly in the vault root, use script_dir
    # If you want to be super robust, you could search for a .obsidian folder
    # For now, let's assume the MOC_Automation folder is within the vault.

    generate_mocs(vault_root)
