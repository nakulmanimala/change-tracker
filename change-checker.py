import os
import git

repo = git.Repo('.')
changed = False

# Get the diff between HEAD and specified commit/tag
diff = repo.git.diff('HEAD', '4436b2bbe08f1a18fc25c15e7b73f01cf524e3ec', '--', 'entri/ui/static_design_revamp/north_south/sass/')

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
