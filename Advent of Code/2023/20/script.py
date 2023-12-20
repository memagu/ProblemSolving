from collections import deque


def part1():
    with open("data.in", 'r') as f:
        modules = {}
        for line in f.read().splitlines():
            module, destinations = line.split(" -> ")
            destinations = destinations.split(", ")

            if module.startswith('%'):
                modules[module.removeprefix('%')] = ['%', False, destinations]
            elif module.startswith('&'):
                modules[module.removeprefix('&')] = ['&', {}, destinations]
            else:
                modules[module] = [None, None, destinations]

        for module, (_, _, destinations) in modules.items():
            for destination in destinations:
                if destination not in modules:
                    continue
                destination_module_type, destination_state, _ = modules[destination]
                if destination_module_type == '&':
                    destination_state[module] = False

    lows = highs = 0
    for _ in range(1000):
        queue = deque(((False, "broadcaster"),))
        while queue:
            for _ in range(len(queue)):
                incoming_signal, module = queue.popleft()

                highs += incoming_signal
                lows += not incoming_signal

                if module not in modules:
                    continue

                module_type, state, destinations = modules[module]

                match module_type:
                    case None:
                        output = [(module, incoming_signal, d) for d in destinations]
                    case '%':
                        if not incoming_signal:
                            modules[module][1] = state = not state
                            output = [(module, state, d) for d in destinations]
                        else:
                            output = []
                    case '&':
                        output = [(module, not all(state.values()), d) for d in destinations]
                    case _:
                        raise ValueError

                for source, incoming_signal, destination in output:
                    if destination in modules:
                        module_type, state, _ = modules[destination]
                        if module_type == '&':
                            state[source] = incoming_signal

                    queue.append((incoming_signal, destination))

    return lows * highs


def part2():
    with open("data.in", 'r') as f:
        modules = {}
        for line in f.read().splitlines():
            module, destinations = line.split(" -> ")
            destinations = destinations.split(", ")

            if module.startswith('%'):
                modules[module.removeprefix('%')] = ['%', False, destinations]
            elif module.startswith('&'):
                modules[module.removeprefix('&')] = ['&', {}, destinations]
            else:
                modules[module] = [None, None, destinations]

        for module, (_, _, destinations) in modules.items():
            for destination in destinations:
                if destination not in modules:
                    continue
                destination_module_type, destination_state, _ = modules[destination]
                if destination_module_type == '&':
                    destination_state[module] = False

    pairs = (("hd", "cq"), ("zj", "vp"), ("sq", "rv"), ("jz", "dc"))

    result = 1
    for source_module, destination_module in pairs:
        button_presses = 0
        while True:
            button_presses += 1
            queue = deque(((False, source_module),))
            while queue:
                for _ in range(len(queue)):
                    incoming_signal, module = queue.popleft()

                    if module == destination_module and not incoming_signal:
                        result *= button_presses
                        break

                    if module not in modules:
                        continue

                    module_type, state, destinations = modules[module]

                    match module_type:
                        case None:
                            output = [(module, incoming_signal, d) for d in destinations]
                        case '%':
                            if not incoming_signal:
                                modules[module][1] = state = not state
                                output = [(module, state, d) for d in destinations]
                            else:
                                output = []
                        case '&':
                            output = [(module, not all(state.values()), d) for d in destinations]
                        case _:
                            raise ValueError

                    for source, incoming_signal, destination in output:
                        if destination in modules:
                            module_type, state, _ = modules[destination]
                            if module_type == '&':
                                state[source] = incoming_signal

                        queue.append((incoming_signal, destination))

                else:
                    continue
                break
            else:
                continue
            break

    return result


if __name__ == "__main__":
    print(part1())
    print(part2())
