---
name: skill-deployer
description: Deploys a skill from a given file path to the skills directory and displays its usage information. Use when the user provides a path to a skill folder or .skill file and asks to "deploy", "install", or "import" it.
---

# Skill Deployer

This skill automates the process of installing new skills into the Trae environment.

## Usage

When the user provides a path to a skill (either a directory or a `.skill` zip file), run the deployment script:

```bash
python3 {baseDir}/scripts/deploy.py <path_to_skill>
```

The script will:
1.  **Validate** the source path.
2.  **Copy/Extract** the skill to `.trae/skills/<skill_name>`.
3.  **Read** the `SKILL.md` file.
4.  **Output** the skill's name, description, and usage instructions.

## Output

The script prints the skill's metadata and a preview of its documentation. You should summarize this information for the user, highlighting:
*   **Skill Name**: The name of the installed skill.
*   **Description**: What the skill does.
*   **How to Use**: Key commands or triggers mentioned in the documentation.

## Example

**User**: "Deploy the skill at /Users/me/Downloads/my-new-skill"

**Action**:
```bash
python3 .trae/skills/skill-deployer/scripts/deploy.py /Users/me/Downloads/my-new-skill
```

**Response**:
"Successfully deployed **my-new-skill**!
**Description**: ...
**Usage**: ..."
