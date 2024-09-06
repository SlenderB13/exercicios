yealy_earns = []

def calculate_stats(yearly_earns):
    min_value = min(yearly_earns)
    max_value = max(yearly_earns)
    avg = sum(yearly_earns)/len(yearly_earns)
    avg_superior = 0

    for value in yearly_earns:
        if value > avg:
            avg_superior = avg_superior + 1
