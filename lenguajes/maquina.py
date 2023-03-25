from collections import defaultdict, deque


class Tape:
    def __init__(self, blank, string='', head=0):
        self.blank = blank
        self.loadString(string, head)

    def loadString(self, string, head):
        self.symbols = list(string)
        self.head = head

    def readSymbol(self):
        if self.head < len(self.symbols):
            return self.symbols[self.head]
        else:
            return self.blank

    def writeSymbol(self, symbol):
        if self.head < len(self.symbols):
            self.symbols[self.head] = symbol
        else:
            self.symbols.append(symbol)

    def moveHead(self, direction):
        if direction == 'L':
            inc = -1
        elif direction == 'R':
            inc = 1
        else:
            inc = 0
        self.head += inc

    def clone(self):
        return Tape(self.blank, self.symbols, self.head)

    def __str__(self):
        return str(self.symbols[:self.head]) + \
            str(self.symbols[self.head:])


class TuringMachine:
    def __init__(self, start, final, blank='#', ntapes=1):
        self.start = self.state = start
        self.final = final
        self.tapes = [Tape(blank) for _ in range(ntapes)]
        self.trans = defaultdict(list)

    def restart(self, string):
        self.state = self.start
        self.tapes[0].loadString(string, 0)
        for tape in self.tapes[1:]:
            tape.loadString('', 0)

    def readSymbols(self):
        return tuple(tape.readSymbol() for tape in self.tapes)

    def addTrans(self, state, read_sym, new_state, moves):
        self.trans[(state, read_sym)].append((new_state, moves))

    def getTrans(self):
        key = (self.state, self.readSymbols())
        return self.trans[key] if key in self.trans else None

    def execTrans(self, trans):
        self.state, moves = trans
        for tape, move in zip(self.tapes, moves):
            symbol, direction = move
            tape.writeSymbol(symbol)
            tape.moveHead(direction)
        return self

    def clone(self):
        tm = TuringMachine(self.start, self.final)
        tm.state = self.state
        tm.tapes = [tape.clone() for tape in self.tapes]
        tm.trans = self.trans
        return tm

    def accepts(self, string):
        self.restart(string)
        queue = deque([self])
        while len(queue) > 0:
            tm = queue.popleft()
            transitions = tm.getTrans()

            if transitions is None:
                for end in self.final:
                    if tm.state == end:
                        return tm
            else:
                for trans in transitions[1:]:
                    queue.append(tm.clone().execTrans(trans))
                queue.append(tm.execTrans(transitions[0]))
        return None

    def __str__(self):
        out = ''
        for tape in self.tapes:
            out += self.state + ': ' + str(tape) + '\n'
        return out

    @staticmethod
    def parse(filename):
        tm = None
        with open(filename) as file:
            for line in file:
                spec = line.strip()
                if len(spec) == 0 or spec[0] == '%':
                    continue
                if tm is None:
                    start, final, blank, ntapes = spec.split()
                    ntapes = int(ntapes)
                    final = tuple(final.split('.'))
                    tm = TuringMachine(start, final, blank, ntapes)
                else:
                    fields = line.split()
                    state = fields[0]
                    symbols = tuple(fields[1].split('.'))
                    new_st = fields[2]
                    moves = tuple(tuple(m.split('.'))
                                for m in fields[3:])
                    tm.addTrans(state, symbols, new_st, moves)
        return tm
