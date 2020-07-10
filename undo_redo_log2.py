# Undo/redo with linked list

state = {}
changes = []
idx = -1

def update(change):
    global idx
    key = change[0]
    val = change[1].strip()
    state[key] = val
    del changes[idx+1:]
    changes.append(change)
    idx += 1

def update_internal(change):
    key = change[0]
    val = change[1]
    state[key] = val

def undo():
    global idx
    if idx > 0:
        idx -= 1
        update_internal(changes[idx])
    else:
        idx = -1
        state.clear()  
        
def redo():
    global idx
    if idx < (len(changes)-1):
        idx += 1
        update_internal(changes[idx])

while True:
    raw = input("> ")
    rawl = raw.lower()
    if rawl == 'u':
        undo()
    elif rawl == 'r':
        redo()
    else:
        change = raw.split('=')
        if len(change) != 2:
            print("invalid operation")
            continue
        update(change)
    print(state)
