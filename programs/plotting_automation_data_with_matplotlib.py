import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
fig, axis = plt.subplots(figsize=(5, 3))
axis.bar(["login", "search", "profile"], [1.2, 0.8, 2.1])
axis.set_ylabel("Duration (seconds)")
axis.set_title("Local suite durations")
fig.tight_layout()
fig.savefig("durations.png", dpi=150)
plt.close(fig)
