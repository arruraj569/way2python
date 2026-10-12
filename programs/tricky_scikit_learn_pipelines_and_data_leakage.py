training = [0.0, 2.0]
held_out = [100.0]
training_mean = sum(training) / len(training)
combined = training + held_out
leaked_mean = sum(combined) / len(combined)
print(training_mean)
print(leaked_mean)
