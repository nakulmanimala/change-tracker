import os
import git
import subprocess


get_tag_cmd= "git log --simplify-by-decoration --decorate --tags --oneline master | grep 'tag:' | sed -E 's/.*tag: ([^,)]+).*/\\1/' | head -n1"
old_git_tag = subprocess.check_output(get_tag_cmd, shell=True, text=True).strip()
#git_diff_cmd = 'git log '+old_git_tag+'..HEAD --no-merges --pretty=format:"%s%n%b- %aN (%h)%n"'
#result = subprocess.check_output(git_diff_cmd, shell=True, text=True)

#print(result)

repo = git.Repo('.')
changed = False

# Get the diff between HEAD and specified commit/tag
diff = repo.git.diff('HEAD', old_git_tag, '--', 'entri/ui/static_design_revamp/north_south/sass/')

if diff:
    # Changes exist in the directory
    print("There are changes in the sass directory between HEAD and specified commit:")
    
    # Parse diff output to show specific changes
    for line in diff.split('\n'):
        if line.startswith('diff --git'):
            file_path = line.split(' b/')[1]
            print(f"Changed: {file_path}")
            changed = True

if not changed:
    print("No changes detected in the sass directory between HEAD and specified commit")
