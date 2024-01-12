# previousandnext.py

class HistoryManager:
    def __init__(self):
        self.history = []
        self.current_state = -1

    def add_state(self, elements, current_element):
        self.current_state += 1
        self.history = self.history[:self.current_state]  # Discard future history
        self.history.append((elements, current_element))

    def undo(self):
        if self.current_state > 0:
            self.current_state -= 1
            return self.history[self.current_state]
        return None

    def redo(self):
        if self.current_state < len(self.history) - 1:
            self.current_state += 1
            return self.history[self.current_state]
        return None

