import argparse
import os
import shutil
import sys
import yaml

def deploy_skill(source_path, target_base_dir=".trae/skills"):
    """
    Deploys a skill from a source path to the target skills directory.
    """
    source_path = os.path.abspath(source_path)
    if not os.path.exists(source_path):
        print(f"Error: Source path '{source_path}' does not exist.")
        sys.exit(1)

    # Check if source is a directory or a .skill (zip) file
    is_zip = source_path.endswith('.skill') or source_path.endswith('.zip')
    
    skill_name = os.path.basename(source_path)
    if is_zip:
        skill_name = os.path.splitext(skill_name)[0]
    
    target_dir = os.path.join(target_base_dir, skill_name)
    
    print(f"Deploying skill '{skill_name}'...")
    print(f"  Source: {source_path}")
    print(f"  Target: {target_dir}")

    try:
        if os.path.exists(target_dir):
            print(f"  Target directory '{target_dir}' already exists. Overwriting...")
            shutil.rmtree(target_dir)
        
        if is_zip:
            import zipfile
            with zipfile.ZipFile(source_path, 'r') as zip_ref:
                zip_ref.extractall(target_dir)
        else:
            shutil.copytree(source_path, target_dir)
            
        print("  Deployment successful.")
        
        # Verify and read SKILL.md
        skill_md_path = os.path.join(target_dir, "SKILL.md")
        if os.path.exists(skill_md_path):
            print(f"  Found SKILL.md at {skill_md_path}")
            return skill_md_path
        else:
            print(f"  Warning: SKILL.md not found in {target_dir}")
            return None

    except Exception as e:
        print(f"Error deploying skill: {e}")
        sys.exit(1)

def parse_skill_md(file_path):
    """
    Parses SKILL.md to extract name, description, and usage instructions.
    """
    if not file_path:
        return None

    try:
        with open(file_path, 'r') as f:
            content = f.read()
            
        # Extract frontmatter
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                frontmatter_raw = parts[1]
                body = parts[2]
                
                try:
                    metadata = yaml.safe_load(frontmatter_raw)
                except yaml.YAMLError:
                    metadata = {}
                    
                return {
                    "name": metadata.get("name", "Unknown"),
                    "description": metadata.get("description", "No description provided."),
                    "body": body
                }
        
        return {"body": content}

    except Exception as e:
        print(f"Error parsing SKILL.md: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Deploy a skill and show usage.")
    parser.add_argument("path", help="Path to the skill directory or .skill file")
    args = parser.parse_args()

    skill_md_path = deploy_skill(args.path)
    
    if skill_md_path:
        info = parse_skill_md(skill_md_path)
        if info:
            print("\n" + "="*40)
            print(f"SKILL DEPLOYED: {info.get('name', 'Unknown')}")
            print("="*40)
            print(f"\nDESCRIPTION:\n{info.get('description')}")
            print("\nUSAGE & DETAILS:")
            # Print the first 1000 characters of the body to avoid flooding
            print(info.get('body', '')[:2000] + "...\n(truncated)")
            print("="*40)

if __name__ == "__main__":
    main()
