# Undo/redo with logs

state = {}
undo_log = []
redo_log = []

def update(change):
    key = change[0]
    val = change[1].strip()
    state[key] = val
    undo_log.append((key, val))
    redo_log.clear()

def update_internal(change):
    key = change[0]
    val = change[1]
    state[key] = val
    undo_log.append((key, val))

def undo():
    if len(undo_log) == 0:
        return
    redo_log.append(undo_log.pop())
    if len(undo_log) == 0:
        state.clear()
    else:
        update_internal(undo_log.pop())

def redo():
    if len(redo_log) == 0:
        return
    update_internal(redo_log.pop())

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
