def duplicate_count(text):
    # Your code goes here
    alfanum = 'abcdefghijklmnopqrstuvxwyz0123456789'
    count = 0
    for i in alfanum:
        if text.lower().count(i) > 1:
            count += 1
    return count

print(duplicate_count('qO8HMTAJQvY1TjXGsyTG2n48YVKJVMBxoHKn5ohTKx4N3lD682Bd7pt9NZKuXQ2Ct5mTP2o18'))