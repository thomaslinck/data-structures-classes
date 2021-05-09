def is_queue_empty(queue):
    return not queue


def number_of_elements_in(queue):
    return len(queue)


def add_element_to_queue(element, queue):
    queue.append(element)
    return queue


def get_first_element_from_queue(queue):
    return queue[0] if not is_queue_empty(queue) else "none"


def remove_first_element_from_queue(queue):
    def by_first_element(element): return queue.index(element) != 0
    return list(filter(by_first_element, queue))
