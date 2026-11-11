import sys
import os

# Read the NEW mod script
with open('combat_mod.js', 'r') as f:
    mod_script = f.read()

# Read the HTML file
with open('EaglercraftZ_1.20_Offline_International.html', 'rb') as f:
    html = f.read()

# Find the start of the existing block
start_marker = b'// COMBAT MOD - ATTACK COOLDOWNS LIKE JAVA 1.9+'
start_idx = html.find(start_marker)

if start_idx == -1:
    print('ERROR: Could not find existing Combat Mod block to replace!')
    sys.exit(1)

# Find the end of the script block
# It ends with `</script>`.
end_idx = html.find(b'</script>', start_idx)

if end_idx == -1:
    print('ERROR: Could not find end of script block!')
    sys.exit(1)

print(f'Found block from {start_idx} to {end_idx}')
print(f'Old block size: {end_idx - start_idx} bytes')

# Replace
new_content = mod_script.encode('utf-8')
new_html = html[:start_idx] + new_content + html[end_idx:]

with open('EaglercraftZ_1.20_Offline_International.html', 'wb') as f:
    f.write(new_html)

print(f'Replaced Combat Mod script! New size: {len(new_html)}')
print('Injection successful.')
